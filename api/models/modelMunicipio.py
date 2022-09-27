from django.db import models
from .modelDepartamento import departamento

class municipio(models.Model):
    nombre=models.CharField(max_length=200)
    abreviatura=models.CharField(max_length=20)
    id_departamento=models.ForeignKey(departamento, on_delete=models.DO_NOTHING)
    estado=models.IntegerField(max_length=11,default=1)