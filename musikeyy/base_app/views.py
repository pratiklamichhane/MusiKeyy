from django.http import HttpResponseRedirect
from django.shortcuts import render , get_object_or_404, redirect
from django.urls import reverse
from .models import Song , Artist , Album
# Create your views here.
def index(request):
    allSongs = Song.objects.all()
    # Calculate duration for each song
    return render(request , 'base_app/index.html', context={
        "allSongs" : allSongs
    })

def view_song(request, id):
    song = Song.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
