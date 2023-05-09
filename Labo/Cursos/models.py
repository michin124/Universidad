from django.db import models

from xmlrpc.client import boolean
from Labo.Laboratorios.models import Laboratio
from Labo.Profesores.models import Profesor

# Create your models here.
class Curso(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    Laboratorios=models.ForeignKey(Laboratio,on_delete=models.CASCADE,null=False, blank=False)
    Profesor=models.ForeignKey(Profesor,on_delete=models.CASCADE,null=False, blank=False)