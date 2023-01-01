from django.contrib import admin

# Register your models here.
from .models import Car , employee
from . import models

class CarAdmin(admin.ModelAdmin):
    list_display=['name' , 'description' , 'price' , 'color']
    list_display_links=['name','description']
    list_editable=['price' , 'color']
    search_fields=['name' , 'price']
admin.site.register(models.Car,CarAdmin)
admin.site.register(models.employee)