from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(unique=True, max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    lyrics = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug
        self.title = self.title.title()
        self.artist = self.artist.title()
        self.album = self.album.title()
        self.lyrics = self.lyrics.title()
        self.date = self.date
        self.author = self.author
        super(Song, self).save(*args, **kwargs)
