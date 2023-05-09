from django.db import models

# Create your models here.
from xmlrpc.client import boolean


class Profesor(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
   