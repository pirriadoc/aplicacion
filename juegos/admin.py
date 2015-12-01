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
