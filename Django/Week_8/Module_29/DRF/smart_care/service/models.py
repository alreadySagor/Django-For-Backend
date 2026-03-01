from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="service/images/")

    def __str__(self):
        return self.name

# Model er naam ki hobe seta bole dilam. Sadharonoto amra jei naam model er jonno rakhi, admin panel/model e setar sesh e ekta 's' jog hoy, ba onno kichu. Tai nijer mon moto jate sei naam ta thake tai ei kaj ta kora. 
    class Meta:
        verbose_name_plural = "Service"