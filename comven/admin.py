from django.contrib import admin

# Register your models here.

from .models import Cliente, Juego

admin.site.register(Cliente)
admin.site.register(Juego)
