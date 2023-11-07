from django.contrib import admin

# Register your models here.

from service1 import models
admin.site.register(models.book)