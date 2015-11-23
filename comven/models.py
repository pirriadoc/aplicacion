#-*- enconding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('cliente', kwargs={'pk': self.pk})

class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    def __str__(self):
        return self.titulo

class Stock(models.Model):
    nombre = models.ForeignKey(Juego)
    cantidad = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre






