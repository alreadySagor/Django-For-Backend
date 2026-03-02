from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.AvailableTime)

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', ), }

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', ), }

admin.site.register(models.Designation)

admin.site.register(models.Specialization)
admin.site.register(models.Doctor)