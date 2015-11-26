from django import forms
from .models import Cliente
from django.contrib.auth.models import User

#class Registro(forms.ModelForm):
#    class Meta:
#        model = Cliente
#        fields = ['nombre', 'direccion']


#formularios de login

class LoginForm(forms.Form):
    username = forms.CharField(label="User")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

