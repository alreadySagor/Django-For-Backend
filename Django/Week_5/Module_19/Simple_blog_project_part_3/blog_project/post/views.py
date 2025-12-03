from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#----------------------------------------------------------------------------------------------------------------------
@login_required
def add_post(request):
    if request.method == 'POST': # user post request koreche
        post_form = forms.PostForm(request.POST) # user er post request data ekhane capture korlam
        if post_form.is_valid(): # post kora data gula valid kina seta check korlam/kortechi
            # post_form.cleaned_data['author'] = request.user # je user post ta korbe se nijei user (er line (ei line ta may be vul ache) er updated version hocche nicher line ta)
            post_form.instance.author = request.user # post_form ekti class, ei class er ekti object ba instance toiri hoiche, oi instance er moddhe author naamer ekta field to obossoi thakbe jehetu amra model form use kortechi, ei field tai amra bosiye dibo request.user ke
            post_form.save() # jodi data valid hoy tahole data gula databse e save korbo.
            return redirect("homepage") # sob thik thakle take add post ei url e pathiye dibo
    else: # user normally website e gele blank form pabe
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form' : post_form})
#--------------------------------------
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
#----------------------------------------------------------------------------------------------------------------------

@login_required
def edit_post(request, id):
    post = models.Post.objects.get(pk = id)
    post_form = forms.PostForm(instance = post) # post tite ja ja chilo segula soho open hobe. Edit korte chaile post er data gula show koranor jonno instance = post use korechi
    # print(post.title)
    if request.method == 'POST': # user post request koreche
        post_form = forms.PostForm(request.POST, instance = post) # user er post request data ekhane capture korlam
        if post_form.is_valid(): # post kora data gula valid kina seta check korlam/kortechi
            post_form.instance.author = request.user
            post_form.save() # jodi data valid hoy tahole data gula databse e save korbo.
            return redirect("homepage") # sob thik thakle take add post ei url e pathiye dibo
    return render(request, 'add_post.html', {'form' : post_form})
#--------------------------------------
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
#----------------------------------------------------------------------------------------------------------------------
@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk = id)
    post.delete()
    return redirect("homepage")
#--------------------------------------
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'
#----------------------------------------------------------------------------------------------------------------------