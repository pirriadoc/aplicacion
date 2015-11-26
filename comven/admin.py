from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

from .models import Cliente, Juego, Stock

admin.site.register(Cliente)
admin.site.register(Juego)
admin.site.register(Stock)

# Define an inline admin descriptor for Cliente model
# which acts a bit like a singleton
class ClienteInline(admin.StackedInline):
    model = Cliente
    can_delete = False
    verbose_name_plural = 'clientes'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ClienteInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
