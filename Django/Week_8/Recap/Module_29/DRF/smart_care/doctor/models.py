from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
# Create your models here.

class Specialization(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)

    def __str__(self):
        return self.name