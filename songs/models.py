from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    lyrics = models.TextField()
    artwork = models.ImageField(upload_to='', default='default.jpg', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
