from django.http import HttpResponseRedirect
from django.shortcuts import render , get_object_or_404, redirect
from django.urls import reverse
from .models import Song , Artist , Album
from .forms import ArtistForm, AlbumForm, SongForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

def index(request):
    allSongs = Song.objects.all().order_by('-id')
    paginator = Paginator(allSongs, 7)

    page_number = request.GET.get('page')
    try:
        songs = paginator.page(page_number)
    except PageNotAnInteger:
        songs = paginator.page(1)
    except EmptyPage:
        songs = paginator.page(paginator.num_pages)

    total_artist = Artist.objects.count()
    total_album = Album.objects.count()
    total_song = Song.objects.count()
    latest_song = Song.objects.order_by('-created').first()

    return render(request, 'base_app/index.html', context={
        'songs': songs,
        'total_artist': total_artist,
        'total_album': total_album,
        'latest_song': latest_song,
        'total_song': total_song,
    })

def view_song(request, id):
    song = Song.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


@login_required
def create_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            new_artist = form.save(commit=False)
            new_artist.added_by = request.user
            new_artist.save()
            return redirect('/')
    else:
        form = ArtistForm()
    
    return render(request, 'base_app/add_artist.html', {'form': form})

@login_required
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            new_album = form.save(commit=False)
            new_album.added_by = request.user
            new_album.save()
            return redirect('/')
    else:
        form = AlbumForm()
    return render(request, 'base_app/add_album.html', {'form': form})

@login_required
def create_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            new_song = form.save(commit=False)
            new_song.added_by = request.user
            new_song.save()
            return redirect('/')
    else:
        form = SongForm()
    return render(request, 'base_app/add_song.html', {'form': form})

def edit_artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'base_app/edit_artist.html', {'form': form , 'artist' : artist})

def edit_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'base_app/edit_album.html', {'form': form,
    'album' : album})

def edit_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SongForm(instance=song)
    return render(request, 'base_app/edit_song.html', {'form': form ,
    'song' : song})

def delete_artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    if request.method == 'POST':
        artist.delete()
        return redirect('/')  
    form = ArtistForm(instance=artist)  
    return render(request, 'edit_artist.html', {'artist': artist, 'form': form})

def delete_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        album.delete()
        return redirect('/')  
    form = AlbumForm(instance=album)
    return render(request, 'edit_album.html', {'album': album, 'form': form})

def delete_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    if request.method == 'POST':
        song.delete()
        return redirect('/') 
    form = SongForm(instance=song) 
    return render(request, 'edit_song.html', {'song': song, 'form': form})


@login_required
def user_uploaded_songs(request):
    user_songs = Song.objects.filter(added_by=request.user)
    return render(request, 'base_app/user_songs.html', {'user_songs': user_songs})

@login_required
def user_uploaded_artists(request):
    user_artists = Artist.objects.filter(added_by=request.user)
    return render(request, 'base_app/user_artists.html', {'user_artists': user_artists})

@login_required
def user_uploaded_albums(request):
    user_albums = Album.objects.filter(added_by=request.user)
    return render(request, 'base_app/user_albums.html', {'user_albums': user_albums})