from django.db import models

from .modelUsuario import usuario
from .modelCategoria import categoria

class platillos(models.Model):
    descripcion=models.CharField(max_length=200)
    precio=models.FloatField(max_length=200)
    id_usuario=models.ForeignKey(usuario, on_delete=models.DO_NOTHING)
    id_categoria=models.ForeignKey(categoria, on_delete=models.DO_NOTHING)
    stock=models.IntegerField(max_length=11)
    estado=models.IntegerField(max_length=11,default=1)
    oferta=models.IntegerField(max_length=11,default=0)
