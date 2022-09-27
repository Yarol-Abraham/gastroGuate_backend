from django.db import models
from .modelTipoUsuario import tipousuario
from .modelMunicipio import municipio

class usuario(models.Model):
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    usuario=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    identificacion=models.CharField(max_length=100)
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    id_tipousuario=models.ForeignKey(tipousuario, on_delete=models.DO_NOTHING)
    id_municipio=models.ForeignKey(municipio, on_delete=models.DO_NOTHING)
    estado=models.IntegerField(max_length=11,default=1)