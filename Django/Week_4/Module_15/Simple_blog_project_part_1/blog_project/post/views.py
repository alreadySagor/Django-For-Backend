from django.shortcuts import render, redirect
from . import forms
from . import models
def add_post(request):
    if request.method == 'POST': # user post request koreche
        post_form = forms.PostForm(request.POST) # user er post request data ekhane capture korlam
        if post_form.is_valid(): # post kora data gula valid kina seta check korlam/kortechi
            post_form.save() # jodi data valid hoy tahole data gula databse e save korbo.
            return redirect("homepage") # sob thik thakle take add post ei url e pathiye dibo
    else: # user normally website e gele blank form pabe
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form' : post_form})


def edit_post(request, id):
    post = models.Post.objects.get(pk = id)
    post_form = forms.PostForm(instance = post) # post tite ja ja chilo segula soho open hobe. Edit korte chaile post er data gula show koranor jonno instance = post use korechi
    # print(post.title)
    if request.method == 'POST': # user post request koreche
        post_form = forms.PostForm(request.POST, instance = post) # user er post request data ekhane capture korlam
        if post_form.is_valid(): # post kora data gula valid kina seta check korlam/kortechi
            post_form.save() # jodi data valid hoy tahole data gula databse e save korbo.
            return redirect("homepage") # sob thik thakle take add post ei url e pathiye dibo
    return render(request, 'add_post.html', {'form' : post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk = id)
    post.delete()
    return redirect("homepage")