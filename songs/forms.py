from django import forms
from . import models


class SongForm(forms.ModelForm):
    class Meta:
        model = models.Song
        fields = ['title', 'artist', 'album', 'lyrics']
