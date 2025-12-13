from django.shortcuts import render, redirect

from musician.forms import MusicianForm
from album.forms import AlbumForm
from album.models import Album
# Create your views here.

def delete_album_musician(request, id):
    details = Album.objects.get(pk = id)
    details.delete()
    return redirect("view_data")

def edit(request, id):
    album = Album.objects.get(pk = id)
    musician = album.musician
    musicianForm = MusicianForm(instance=musician)
    albumForm = AlbumForm(instance=album)

    if request.method == 'POST':
        musicianForm = MusicianForm(request.POST, instance=musician)
        albumForm = AlbumForm(request.POST, instance=album)
        if musicianForm.is_valid and albumForm.is_valid():
            musicianForm.save()
            albumForm.save()
            return redirect("view_data")
    return render(request, 'edit.html', {'musicianForm' : musicianForm, 'albumForm' : albumForm})