from django.db import models
from categories.models import Category
# from author.models import Author
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) # Ekta post multiple categorir moddhe thakte pare abar ekta categorir moddhe multiple post thakte pare
    author = models.ForeignKey(User, on_delete = models.CASCADE) # many to one relationship deyar jonno amra Foreignkey field ta use kori
    # CASCADE use korar karone ami jodi ba kono athor jodi tar profile ta delete kore fele tahole oi author jotogula post koreche sob delete hoye jabe
    image = models.ImageField(upload_to='post/media/uploads/', blank=True, null=True)
    def __str__(self):
        return self.title