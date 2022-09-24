from django.db import models

class categoria(models.Model):
    tipo=models.CharField(max_length=100)
    estado=models.IntegerField(max_length=1,default=1)