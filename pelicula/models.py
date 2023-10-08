from django.db import models
from .validators import validar_only_text, validar_calificacion
from django.core.validators import EmailValidator

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=80, unique=True, validators=[validar_only_text])
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre

class Director(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    apellido = models.CharField(max_length=50 )
    edad = models.IntegerField()
    def __str__(self):
        return self.nombre

class Actor(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    apellido = models.CharField(max_length=50 )
    edad = models.IntegerField()
    def __str__(self):
        return self.nombre
# class ProductUnits(models.TextChoices):
#     UNITS = 'u', 'Unidades'
#     KG = 'kg', 'Kilogramos'

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actor_principal = models.ForeignKey(Actor, on_delete=models.CASCADE)
    resumen = models.TextField()
    calificacion = models.DecimalField(max_digits=4, decimal_places=2)
    # unidades = models.CharField(
    #     max_length=2,
    #     choices=ProductUnits.choices,
    #     default=ProductUnits.UNITS
    # )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo