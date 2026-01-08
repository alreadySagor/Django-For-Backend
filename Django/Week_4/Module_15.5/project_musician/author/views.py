from django.shortcuts import render, redirect

from .forms import RegistrationForm, ChangeUserData
from album.forms import AlbumForm
from album.models import Album
from django.contrib import messages
from musician.forms import MusicianForm

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
# Create your views here.

def registration(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Created Successfully')
                return redirect("login")
        else:
            form = RegistrationForm()
        return render(request, 'regi_login.html', {'form' : form, 'type' : 'Registration'})
    else:
        return redirect("homepage")

def user_login(request):
    if not request.user.is_authenticated:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            pswd = form.cleaned_data['password']
            user = authenticate(username = name, password = pswd)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully')
                # return redirect("profile")
                return redirect("homepage")
        else:
            form = AuthenticationForm(request)
        return render(request, 'regi_login.html', {'form' : form, 'type' : 'Login'})
    else:
        return redirect("homepage")
    

def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def delete_album_musician(request, id):
    details = Album.objects.get(pk = id)
    details.delete()
    return redirect("homepage")

@login_required
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
            return redirect("homepage")
    return render(request, 'edit.html', {'musicianForm' : musicianForm, 'albumForm' : albumForm})