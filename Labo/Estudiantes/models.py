from django.db import models

# Create your models here.
from Labo.Cursos.models import Curso

class Esudiante(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    Cursos=models.ForeignKey(Curso,on_delete=models.CASCADE,null=False, blank=False)