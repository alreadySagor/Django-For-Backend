from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_user_profile(request):
    if request.method == 'POST':
        user_profile_form = forms.UserProfileForm(request.POST)
        if user_profile_form.is_valid():
            user_profile_form.save()
            return redirect("add_user_profile")
    else:
        user_profile_form = forms.UserProfileForm()
    return render(request, 'add_user_profile.html', {'form' : user_profile_form})