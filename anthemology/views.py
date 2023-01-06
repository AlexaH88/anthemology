from django.shortcuts import render
from django.db.models import Q
from songs.models import Song


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def song_search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        songs = Song.objects.filter(
            Q(title__icontains=searched) |
            Q(artist__icontains=searched) |
            Q(album__icontains=searched))
        return render(
            request, 'song_search.html', {
                'searched': searched,
                'songs': songs
                }
            )
    else:
        return render(request, 'song_search.html')
