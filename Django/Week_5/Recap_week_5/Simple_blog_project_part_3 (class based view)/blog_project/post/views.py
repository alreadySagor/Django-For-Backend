from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

#----------------------------------------------------------------------------------------------------------------------
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
#----------------------------------------------------------------------------------------------------------------------
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("profile")
#----------------------------------------------------------------------------------------------------------------------
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy("profile")
    pk_url_kwarg = 'id'
#----------------------------------------------------------------------------------------------------------------------
class DetailsPostView(DetailView):
    model = models.Post
    template_name = 'post_details.html'
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comment = post.comment.all()
        comment_form = forms.CommentForm()

        context['comment'] = comment
        context['comment_form'] = comment_form
        return context
#----------------------------------------------------------------------------------------------------------------------