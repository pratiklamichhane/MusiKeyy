from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.view_song, name="viewsong"),
    path('add-artist/', views.create_artist, name="add_artist"),
    path('add-song/', views.create_song, name="add_song"),
    path('add-album/', views.create_album, name="add_album"),
    path('edit-artist/<int:artist_id>/', views.edit_artist, name='edit_artist'),
    path('edit-album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('edit-song/<int:song_id>/', views.edit_song, name='edit_song'),
    path('delete/artist/<int:artist_id>/', views.delete_artist, name='delete_artist'),
    path('delete/album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('delete/song/<int:song_id>/', views.delete_song, name='delete_song'),
]

