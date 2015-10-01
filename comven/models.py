from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre


class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    cantidad = models.IntegerField()
    def __str__(self):
        return self.titulo

