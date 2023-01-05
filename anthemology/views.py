from django.shortcuts import render
from django.db.models import Q
from songs.models import Song


def about(request):
    return render(request, 'about.html')


def song_search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        songs = Song.objects.filter(title__contains=searched)
        return render(
            request, 'song_search.html', {
                'searched': searched,
                'songs': songs
                }
            )
    else:
        return render(request, 'song_search.html')
