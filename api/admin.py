from django.contrib import admin

from api.models.modelPlatillos import platillos

from .models.modelTipoUsuario import tipousuario
from .models.modelDepartamento import departamento
from .models.modelCategoria import categoria
from .models.modelMunicipio import municipio
from .models.modelUsuario import usuario
from .models.modelPedidos import pedidos

# Register your models here.
admin.site.register(tipousuario)
admin.site.register(departamento)
admin.site.register(categoria)
admin.site.register(municipio)
admin.site.register(usuario)
admin.site.register(platillos)
admin.site.register(pedidos)