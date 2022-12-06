from django.urls import path
from . import views

app_name = 'songs'

urlpatterns = [
    path('', views.song_list, name="song_list"),
    path('<slug:slug>/', views.song_detail, name="detail"),
    path('my-songs', views.user_songs, name="user_songs"),
    path('add-song', views.add_song, name="add"),
]
