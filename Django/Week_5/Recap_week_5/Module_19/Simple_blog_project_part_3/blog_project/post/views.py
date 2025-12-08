from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
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

@login_required
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

@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk = id)
    post.delete()
    return redirect("profile")

@login_required
def post_details(request, id):
    post = models.Post.objects.get(pk = id)
    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = forms.CommentForm()
    comment = post.comment.all()

    return render(request, 'post_details.html', {'post' : post, 'comment' : comment, 'comment_form' : comment_form})
