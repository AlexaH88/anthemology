from django.contrib import admin
from .models import Song


class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Song, SongAdmin)
