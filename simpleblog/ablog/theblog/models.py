from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
# from .models import Post

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    # Create foreign key
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    # body = models.TextField()
    title_tag = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255,default='notarymama')
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail',args=(str(self.id)))
        return reverse('home')
