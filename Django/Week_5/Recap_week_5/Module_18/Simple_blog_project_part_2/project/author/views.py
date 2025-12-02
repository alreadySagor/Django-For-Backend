from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import Registration, ChangeUserData
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from post.models import Post
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect("login")
    else:
        form = Registration()
    return render(request, 'register.html', {'form' : form, 'type' : 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            pswd = form.cleaned_data['password']
            user = authenticate(username = name, password = pswd)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect("profile")
            else:
                messages.warning(request, 'Login Information Incorrect')
                return redirect("register")
    else:
        form = AuthenticationForm()
        return render(request, 'register.html', {'form' : form, 'type' : 'Login'})

@login_required
def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data' : data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ChangeUserData(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect("profile")
    else:
        form = ChangeUserData(instance = request.user)
    return render(request, 'update_profile.html', {'form' : form})

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated successfully')
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {'form' : form})