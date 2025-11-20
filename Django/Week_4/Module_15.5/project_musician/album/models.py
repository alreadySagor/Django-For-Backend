from django.db import models
from musician . models import Musician
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_release_date = models.DateField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.album_name