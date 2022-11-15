from django.shortcuts import render, HttpResponse


def songs_test(request):
    # return HttpResponse("Songs Working!")
    return render(request, 'songs/song_list.html')
