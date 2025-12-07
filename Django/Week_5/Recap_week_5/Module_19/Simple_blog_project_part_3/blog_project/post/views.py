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

def edit_post(request, id):
    post = models.Post.objects.get(pk = id)
    form = forms.PostForm(instance = post)
    if request.method == 'POST':
        form = forms.PostForm(request.POST, instance = post)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Post updated successfully')
            return redirect("profile")
    return render(request, 'add_post.html', {'form' : form})

def delete_post(request, id):
    post = models.Post.objects.get(pk = id)
    post.delete()
    return redirect("profile")