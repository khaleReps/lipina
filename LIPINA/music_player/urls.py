from django.urls import path
from . import views

urlpatterns = [
    path('', views.music_player, name="music_player"),
    path('upload/', views.upload_music, name='upload_music'),
  path('create_playlist/', views.create_playlist, name='create_playlist'),
    path('playlist/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
]
