from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_user(request):
    if request.method == 'POST':
        user_form = forms.UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("add_user")
    else:
        user_form = forms.UserForm()
    return render(request, 'add_user.html', {'form' : user_form})