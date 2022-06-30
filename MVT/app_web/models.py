from django.db import models

class Familiar(models.Model):

    nombre= models.CharField(max_length=12)
    apellido= models.CharField(max_length=12)
    telefono= models.IntegerField()
    nacimiento= models.DateField()