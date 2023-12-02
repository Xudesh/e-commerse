from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']

admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'categories', 'price']
    list_display_links = ['name', 'categories', 'price']

    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Post, PostAdmin)