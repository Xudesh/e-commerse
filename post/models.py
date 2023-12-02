from django.db import models
from django.urls import reverse




class Category(models.Model):
    category_name = models.CharField(max_length=100, null=True, blank=True)
        
    def __str__(self):
        return self.category_name




class Post(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    image = models.ImageField(upload_to='food-images/', null=True, blank=True)
    slug = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey(to=Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    


    def get_absolute_url(self):
        return reverse(
            'post_detail',
            args=[
                self.slug,              
            ]
        )