from django.shortcuts import render
from movie.models import Movie
def home(request):
    return render(request, 'home.html')

def movie_details(request):
    data = Movie.objects.all()
    return render(request, 'movie_details.html', {'data' : data})