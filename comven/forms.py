from django import forms
from .models import Cliente

class Registro(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion']
