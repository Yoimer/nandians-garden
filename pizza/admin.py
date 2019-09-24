from django.contrib import admin

# register your models here.

from .models import Pizza, Size

admin.site.register(Pizza)
admin.site.register(Size)