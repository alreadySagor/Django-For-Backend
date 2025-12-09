from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_musician")
    else:
        form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form' : form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            pswd = form.cleaned_data['password']
            user = authenticate(username = name, password = pswd)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successful')
                return redirect("view_data")
            else:
                messages.warning(request, 'Login information incorrect')
    else:
        form = AuthenticationForm()
    return render(request, 'login', {'form': form})
    