from django.db import models
from post.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=75)
    email = models.EmailField()
    content = models.TextField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ['-created_date']
        indexes = [
            models.Index(fields=['-created_date'])
        ]


    def __str__(self):
        return f"Comment author-{self.name} for {self.post}"
    