from django.contrib import admin
from django.urls import path, include
from . import views
from songs import views as song_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('songs/', include('songs.urls')),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('song-search/', views.song_search, name="song_search"),
]
