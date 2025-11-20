from django.shortcuts import render, redirect
from musician.models import Musician
from album.models import Album
from musician.forms import MusicianForm
from album.forms import AlbumForm

def view_data(request):
    # musician_data = Musician.objects.all()
    # album_data = Album.objects.all()
    # return render(request, 'view_data.html', {'musician_data' : musician_data, 'album_data' : album_data})
    album_data = Album.objects.all()
    return render(request, 'view_data.html', {'album_data' : album_data})

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