"""anthemology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import profile_view
from songs.views import song_list
from songs import views as song_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile', profile_view, name="profile_view"),
    path('songs/', song_list, name="song_list"),
    path('', song_views.song_list, name="home"),
]
