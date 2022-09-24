from django.db import models

class departamento(models.Model): 
    nombre=models.CharField(max_length=200)
    abreviatura=models.CharField(max_length=20)
    estado=models.IntegerField(max_length=11,default=1)