from django.db import models

# Create your models here.
class StudentModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    date_time_field = models.DateTimeField()
    duration_field = models.DurationField()
    generic_ip_address_field = models.GenericIPAddressField()
    json_field = models.JSONField()
    positive_integer_field = models.PositiveIntegerField()
    slug_field = models.SlugField()
    url_field = models.URLField()
