from django.db import models
from distributer.models import Distributer
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    distributer = models.OneToOneField(Distributer, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"Name : {self.name} ~ for distributer : {self.distributer.name}"