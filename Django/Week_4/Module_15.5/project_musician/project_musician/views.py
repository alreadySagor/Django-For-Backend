from django.shortcuts import render, redirect
from musician.models import Musician
from album.models import Album


def view_data(request):
    # musician_data = Musician.objects.all()
    # album_data = Album.objects.all()
    # return render(request, 'view_data.html', {'musician_data' : musician_data, 'album_data' : album_data})
    album_data = Album.objects.all()
    return render(request, 'view_data.html', {'album_data' : album_data})
