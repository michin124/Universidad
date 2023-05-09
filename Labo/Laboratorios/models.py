from django.db import models


# Create your models here.


class Laboratio(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    Link=models.CharField(max_length=30)
    Disponibilidad=models.BooleanField()
    FechaEntrega=models.DateTimeField()
    Descripcion=models.CharField(max_length=200)
