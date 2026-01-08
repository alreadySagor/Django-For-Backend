from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_genre(request):
    if request.method == 'POST':
        genre_form = forms.GenreForm(request.POST)
        if genre_form.is_valid():
            genre_form.save()
            return redirect("add_genre")
    else:
        genre_form = forms.GenreForm()
    return render(request, 'add_genre.html', {'form' : genre_form})