from django.http import HttpResponseRedirect
from django.shortcuts import render , get_object_or_404, redirect
from django.urls import reverse
from .models import Song , Artist , Album
from .forms import ArtistForm, AlbumForm, SongForm

# Create your views here.
def index(request):
    allSongs = Song.objects.all().order_by('-id')
    total_artist = Artist.objects.count()
    total_album = Album.objects.count()
    total_song = Song.objects.count()
    latest_song = Song.objects.order_by('-created').first()
    # Calculate duration for each song
    return render(request , 'base_app/index.html', context={
        "allSongs" : allSongs,
        "total_artist" : total_artist,
        "total_album" : total_album,
        "latest_song": latest_song,
        "total_song": total_song,
    })

def view_song(request, id):
    song = Song.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def create_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or another view
            return redirect('/')
    else:
        form = ArtistForm()
    return render(request, 'base_app/add_artist.html', {'form': form})

def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AlbumForm()
    return render(request, 'base_app/add_album.html', {'form': form})

def create_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = SongForm()
    return render(request, 'base_app/add_song.html', {'form': form})
