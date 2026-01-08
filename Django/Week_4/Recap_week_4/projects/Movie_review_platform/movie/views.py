from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_movie(request):
    if request.method == 'POST':    
        movie_form = forms.MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("add_movie")
    else:
        movie_form = forms.MovieForm()
    return render(request, 'add_movie.html', {'form' : movie_form})