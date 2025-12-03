from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.Category)

class CategoryAdmin(admin.ModelAdmin):
    # slug field er je value ta ache seta name diye jate fillup hoye jay
    prepopulated_fields = {'slug' : ('name', )} # 'name', name er por comma karon jate tuple hisebe input ney arki.
    # ki ki jinish amra ei category er jonno dekhte chai. 
    list_display = ['name', 'slug'] # category'r name ar slug tau dekhte chais

admin.site.register(models.Category, CategoryAdmin)