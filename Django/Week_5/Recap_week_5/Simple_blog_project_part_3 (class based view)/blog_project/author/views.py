from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm 
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from django.contrib.auth.decorators import login_required
from post.models import Post

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
#----------------------------------------------------------------------------------------------------------------------
def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect("register")
    else:
        form = forms.RegistrationForm()
    return render(request, 'register.html', {'form' : form, 'type' : 'Register'})
#----------------------------------------------------------------------------------------------------------------------
class UserLoginView(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return super().get_success_url()
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
#----------------------------------------------------------------------------------------------------------------------
@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data' : data})
#----------------------------------------------------------------------------------------------------------------------
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = forms.ChangeUserData(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect("profile")
    else:
        form = forms.ChangeUserData(instance = request.user)
    return render(request, 'update_profile.html', {'form' : form})
#----------------------------------------------------------------------------------------------------------------------
@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated successfully')
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {'form' : form})
#----------------------------------------------------------------------------------------------------------------------
def user_logout(request):
    logout(request)
    return redirect("login")
#----------------------------------------------------------------------------------------------------------------------