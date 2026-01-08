from django.db import models
from distributer.models import Distributer
from genre.models import Genre
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    producer = models.CharField(max_length=30)
    production_company = models.CharField(max_length=30)
    cast = models.CharField(max_length=100)
    story = models.TextField()
    runtime = models.CharField(max_length=30)
    genre = models.ManyToManyField(Genre)
    distributer = models.ForeignKey(Distributer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Movie Title : {self.title} ~ Director : {self.director}"