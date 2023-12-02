from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_date']
    list_display_links = ['name', 'email', 'created_date']

admin.site.register(Comment, CommentAdmin)