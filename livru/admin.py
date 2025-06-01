from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Livru)
admin.site.register(LivruKopia)
admin.site.register(Kategoria)