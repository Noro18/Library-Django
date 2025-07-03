from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Empresta)
admin.site.register(Empresta_Detail)
