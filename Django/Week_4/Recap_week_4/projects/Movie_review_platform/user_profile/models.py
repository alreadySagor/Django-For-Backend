from django.db import models
from user.models import User
# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"Name : {self.name} ~ for user : {self.user.name}"