from django.db import models

# Create your models here.

from django.db import models
# Create your views here.

class familia(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apePaterno =  models.CharField(max_length=70)
    fechaNacimiento = models.CharField(max_length=70)
    telefono = models.IntegerField()
    email = models.EmailField()