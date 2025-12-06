from django.shortcuts import render, redirect
from .forms import RegistrationForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form' : form, 'type' : 'Registration'})

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
                # return redirect("profile")
                return redirect("login")
            else:
                messages.warning(request, 'Login information incorrect')
    else:
        form = AuthenticationForm()
        return render(request, 'register.html', {'form' : form, 'type' : 'Login'})

def profile(request):
    return render(request, 'profile.html')

def edit_profile(request):
    if request.method == 'POST':
        form = ChangeUserData(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully')
            # return redirect("profile")
            return redirect("edit_profile")
    else:
        form = ChangeUserData(instance = request.user)
    return render(request, 'update_profile.html', {'form' : form})

def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            # return render("profile")
            return render("login")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {'form' : form})