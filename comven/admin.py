from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

from .models import Cliente, Juego, Stock

admin.site.register(Cliente)
admin.site.register(Juego)
admin.site.register(Stock)


