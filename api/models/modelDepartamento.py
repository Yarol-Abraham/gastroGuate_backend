from django.db import models

class departamento(models.Model): 
    nombre=models.CharField(max_length=200)
    abreviatura=models.CharField(max_length=20)