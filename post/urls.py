from django.urls import path
from .views import *


urlpatterns = [
    path('fast_foods/', view=FastFoodView.as_view(), name='fast_foods'),
    path('cocktails/', view=CocktailView.as_view(), name='cocktails'),
    path('', view=HomeView.as_view(), name='home'),
    path('posts/<slug:slug>/', view=Post_detail, name='post_detail'),
    path('delivery/', view=Free_Arrive, name='delivery')
]