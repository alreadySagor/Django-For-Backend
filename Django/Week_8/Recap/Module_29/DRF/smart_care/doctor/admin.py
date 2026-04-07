from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.AvailableTime)

class specializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', ), }

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', ), }

admin.site.register(models.Designation, DesignationAdmin)
admin.site.register(models.Specialization, specializationAdmin)
admin.site.register(models.Doctor)
admin.site.register(models.Review)