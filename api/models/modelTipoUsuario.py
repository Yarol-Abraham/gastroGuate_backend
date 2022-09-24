from django.db import models

# Create your models here.
class tipousuario(models.Model):
    rol=models.CharField(max_length=200)
    abreviatura=models.CharField(max_length=200)
    estado=models.IntegerField(max_length=11,default=1)
