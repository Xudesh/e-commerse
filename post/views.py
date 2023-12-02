from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import generic



class FastFoodView(generic.ListView):
    queryset = Post.objects.filter(categories_id = 1)
    context_object_name = 'fastfoods'
    template_name = 'post/fast_food.html'


class CocktailView(generic.ListView):
    queryset = Post.objects.filter(categories_id = 2)
    context_object_name = 'cocktails'
    template_name = 'post/cocktail.html'


class HomeView(generic.ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'post/home.html'


def Post_detail(request, slug):
    post = get_object_or_404(
        Post, 
        slug=slug,        
        )

    context = {
        'post': post
    }

    return render(request, 'post/post_detail.html', context)


def Free_Arrive(request):
    return render(request, 'post/free_arrive.html')