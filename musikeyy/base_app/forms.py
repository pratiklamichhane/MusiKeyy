from django import forms
from .models import Artist, Album, Song
from django.utils.translation import gettext_lazy as _

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['artistName']
        labels = {
            'artistName': _('Artist Name')
        }
        widgets = {
            'artistName' : forms.TextInput(attrs={
                'class' : 'form-control'
            })
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['artist', 'albumName']
        labels = {
            'artist': _('Artist'),
            'albumName': _('Album Name')
        }
        widgets = {
            'artist' : forms.Select(attrs={
                'class' : 'form-control'
            }),
            'albumName' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
        }

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['album', 'songThumbnail', 'song', 'songName']
        labels = {
            'album': _('Song Album'),
            'songThumbnail': _('Song Thumbnail'),
            'song': _('Song'),
            'songName': _('Song Name')
        }
        widgets = {
            'album': forms.Select(attrs={'class': 'form-control'}),
            'songThumbnail': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'song': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'songName': forms.TextInput(attrs={'class': 'form-control'})
        }

