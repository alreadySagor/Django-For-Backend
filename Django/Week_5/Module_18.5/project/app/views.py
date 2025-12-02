from django.shortcuts import render, redirect
from .forms import Registration
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate

# Create your views here.

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = Registration(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created Successfully')
                return redirect("login")
        else:
            form = Registration()
        return render(request, 'register.html', {'form' : form})
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
                    messages.warning(request, 'Login Information Incorrect')
                    return redirect("register")
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form})
    else:
        return redirect("profile")

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect("homepage")

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Updated Successfully')
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'pass_change.html', {'form' : form})
    else:
        return redirect("register")

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Updated Successfully')
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = SetPasswordForm(request.user)
        return render(request, 'pass_change.html', {'form' : form})
    else:
        return redirect("register")

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect("register")