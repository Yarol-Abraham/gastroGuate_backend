from django.db import models
from .modelUsuario import usuario
from .modelPlatillos import platillos

class pedidos(models.Model):
    descripcion=models.CharField(max_length=200)
    cantidad=models.IntegerField(max_length=11,default=1)
    total=models.FloatField(max_length=200)
    id_usuario=models.ForeignKey(usuario, on_delete=models.DO_NOTHING)
    id_platillo=models.ForeignKey(platillos, on_delete=models.DO_NOTHING)
    ubicacion=models.CharField(max_length=200)
    fecha=models.DateTimeField(auto_now_add=True)
    class ESTADOPEDIDO(models.TextChoices):
        PROCESO = 'p'
        ENVIADO = 'E'
        ENTREGADO = 'ET'
    estado_pedido = models.CharField(
        max_length=2,
        choices=ESTADOPEDIDO.choices,
        default=ESTADOPEDIDO.PROCESO,
    )
    estado=models.IntegerField(max_length=11,default=1)