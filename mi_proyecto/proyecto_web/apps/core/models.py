from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

class Ejemplo(models.Model):
    ej1 = models.CharField(max_length=100)
    ej2 = models.DecimalField(max_digits=6, decimal_places=2)
