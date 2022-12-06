from django.shortcuts import render
from .models import Song


def song_list(request):
    songs = Song.objects.all().order_by('artist')
    return render(request, 'songs/song_list.html', {'songs': songs})


def song_detail(request, slug):
    song = Song.objects.get(slug=slug)
    return render(request, 'songs/song_detail.html', {'song': song})


def user_songs(request):
    user_songs = Song.objects.all().filter(author=request.user)
    return render(request, 'songs/user_songs.html', {'user_songs': user_songs})
