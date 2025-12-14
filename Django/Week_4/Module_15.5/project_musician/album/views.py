from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_album(request):
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            # form.instance.musician = request.user
            form.save()
            return redirect("homepage")
    else:
        form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form' : form})