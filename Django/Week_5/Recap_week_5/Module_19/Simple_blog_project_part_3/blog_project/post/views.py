from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def add_post(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Post added successfully')
            return redirect("homepage")
    else:
        form = forms.PostForm()
    return render(request, 'add_post.html', {'form' : form})
            