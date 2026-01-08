from django.db import models
from user.models import User
# Create your models here.
class Review(models.Model):
    rating = models.CharField(max_length=3)
    review = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name : {self.user.name} ~ Rating : {self.rating}"