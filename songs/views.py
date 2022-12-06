from django.shortcuts import render, redirect
from .models import Song
from django.contrib.auth.decorators import login_required
from . import forms


def song_list(request):
    songs = Song.objects.all().order_by('artist')
    return render(request, 'songs/song_list.html', {'songs': songs})


def song_detail(request, slug):
    song = Song.objects.get(slug=slug)
    return render(request, 'songs/song_detail.html', {'song': song})


def user_songs(request):
    user_songs = Song.objects.all().filter(author=request.user)
    return render(request, 'songs/user_songs.html', {'user_songs': user_songs})


@login_required(login_url="/accounts/login/")
def add_song(request):
    if request.method == 'POST':
        form = forms.AddSong(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('songs:song_list')
    else:
        form = forms.AddSong()
    return render(request, 'songs/add_song.html', {'form': form})
