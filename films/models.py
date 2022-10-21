from enum import auto
from operator import mod
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from FilmsCorp import settings


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    photo = models.ImageField(upload_to='media/', blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])