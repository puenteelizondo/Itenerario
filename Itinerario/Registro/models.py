from django.db import models


# Create your models here.
# creas las tablas
class Locales(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
