from django.db import models
from brand.models import Brand
from car.models import Car
from django.contrib.auth.models import User

# Create your models here.
class Buy(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50)
    features = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/uploads/', blank=True, null=True)
    buy_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} -- {self.model_name}"