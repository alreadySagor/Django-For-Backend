from django.http import HttpResponse
from django.shortcuts import render, redirect
from . forms import RegistrationForm, ChangeUserData
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.

def home(request):
    return render(request, 'home.html')

def user_signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signup")
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form' : form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            pswd = form.cleaned_data['password']
            user = authenticate(username = name, password = pswd)
            if user is not None:
                login(request, user)
                return HttpResponse("Successfully logged in")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form})

def user_logout(request):
    logout(request)
    return HttpResponse("Logged Out")

def profile(request):
    if request.method == 'POST':
        form = ChangeUserData(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
    else:
        form = ChangeUserData(instance = request.user)
    return render(request, 'profile.html', {'form' : form})


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponse("Password change successfully")
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, 'pass_change.html', {'form' : form})



def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponse("Password change successfully")
    else:
        form = SetPasswordForm(user = request.user)
    return render(request, 'pass_change.html', {'form' : form})