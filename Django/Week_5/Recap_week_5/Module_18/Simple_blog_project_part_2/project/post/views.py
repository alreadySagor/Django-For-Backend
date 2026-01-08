from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Post added successfully')
            return redirect("profile")
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form' : form})

@login_required
def edit_post(request, id):
    post = Post.objects.get(pk = id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Post updated successfully')
            return redirect("profile")
    return render(request, 'add_post.html', {'form' : form})


@login_required
def delete_post(request, id):
    post = Post.objects.get(pk = id)
    post.delete()
    return redirect("profile")