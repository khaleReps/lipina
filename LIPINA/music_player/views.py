from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Song, Playlist

def upload_music(request):
    if request.method == 'POST' and request.FILES['music_file']:
        music_file = request.FILES['music_file']
        # Handle the uploaded file, save it to a designated directory
        # You may want to store metadata about the file in a database
    return render(request, 'music_player/index.html')

def music_player(request):
    if request.method == 'POST' and request.FILES['music_file']:
        music_file = request.FILES['music_file']

    context = {

    }
    return render(request, 'music_player/index.html', context)



def create_playlist(request):
    if request.method == 'POST':
        playlist_title = request.POST.get('playlist_title')
        selected_songs = request.POST.getlist('selected_songs')

        # Create a new playlist
        playlist = Playlist(title=playlist_title)
        playlist.save()

        # Add selected songs to the playlist
        for song_id in selected_songs:
            song = Song.objects.get(id=song_id)
            playlist.songs.add(song)

        return redirect('playlist_detail', playlist_id=playlist.id)

    songs = Song.objects.all()
    return render(request, 'music_player/create_playlist.html', {'songs': songs})

def playlist_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    return render(request, 'music_player/playlist_detail.html', {'playlist': playlist})
