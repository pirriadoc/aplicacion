from django.contrib import admin

# Register your models here.

from .models import Cliente, Juego, Stock

admin.site.register(Cliente)
admin.site.register(Juego)
admin.site.register(Stock)
