from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import *
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from post.models import *


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()

        context = {
            'form': form
        }

        return render(request, 'users/register.html', context)
    
     
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)

            user.username = user.username
            user.save()
            messages.success(request, 'You have singed up successfully.')
           
            return redirect('login')
        else:

            context = {
                'form': form
            }

            return render(request, 'users/register.html', context)
        

def sign_in(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request,'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('home')
        
        # either form not valid or user is not authenticated
        messages.error(request,f'Имя пользователя или пароль не правильны')
        return render(request,'users/login.html',{'form': form})
    


def sign_out(request):
    logout(request)
    messages.success(request,f'Вы вышли с аккаунта!')
    return redirect('home')  


def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    comment = None

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)

        comment.post = post

        comment.save()

    context = {
        'post': post,
        'comment': comment,
        'form': form
    }

    return render(request, 'users/comment.html', context)