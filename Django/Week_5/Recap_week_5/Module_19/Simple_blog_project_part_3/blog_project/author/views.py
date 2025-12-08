from django.shortcuts import render, redirect
from .forms import RegistrationForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from post.models import Post, Comment
from django.contrib.auth.decorators import login_required

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully')
                return redirect("login")
        else:
            form = RegistrationForm()
        return render(request, 'register.html', {'form' : form, 'type' : 'Registration'})
    else:
        return redirect("profile")
    
def user_login(request):
    if not request.user.is_authenticated:
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
                    messages.warning(request, 'Login information incorrect')
        else:
            form = AuthenticationForm()
            return render(request, 'register.html', {'form' : form, 'type' : 'Login'})
    else:
        return redirect("profile")
    
    
@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data': data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ChangeUserData(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully')
            return redirect("profile")
    else:
        form = ChangeUserData(instance = request.user)
    return render(request, 'update_profile.html', {'form' : form})

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return render("profile")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {'form' : form})

def user_logout(request):
    logout(request)
    return redirect("login")