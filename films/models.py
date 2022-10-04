from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    date = models.DateTimeField()


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])