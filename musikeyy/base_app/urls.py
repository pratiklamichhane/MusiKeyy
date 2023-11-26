from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.view_song, name="viewsong"),
    path('add-artist/', views.create_artist, name="add_artist"),
    path('add-song/', views.create_song, name="add_song"),
    path('add-album/', views.create_album, name="add_album"),
]

