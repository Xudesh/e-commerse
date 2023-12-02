from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.sign_up, name='register'),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('<int:post_id>/comment/', views.post_comment, name='comment')
]