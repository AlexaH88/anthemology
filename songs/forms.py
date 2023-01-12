from django import forms
from . import models


class SongForm(forms.ModelForm):
    class Meta:
        model = models.Song
        fields = ['slug', 'title', 'artist', 'album', 'lyrics']
