from django.db import models

# Create your models here.
class Distributer(models.Model):
    name = models.CharField(max_length=50)
    production_company = models.CharField(max_length=50)

    def __str__(self):
        return f"Name : {self.name} ~ Production Company : {self.production_company}"