from django.shortcuts import render


def song_list(request):
    return render(request, 'songs/song_list.html')
