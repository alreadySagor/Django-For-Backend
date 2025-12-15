from django.db import models
from brand . models import Brand
# Create your models here.
class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50)
    features = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='media/uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.brand} -- {self.model_name}"
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.name}"