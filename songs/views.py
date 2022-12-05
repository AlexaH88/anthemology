from django.shortcuts import render
from .models import Song


def song_list(request):
    songs = Song.objects.all().order_by('artist')
    return render(request, 'songs/song_list.html', {'songs': songs})
