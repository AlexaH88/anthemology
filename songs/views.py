from django.shortcuts import render, HttpResponse


def song_list(request):
    return render(request, 'songs/song_list.html')
