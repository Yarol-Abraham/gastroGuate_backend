from django.contrib import admin

from .models.modelTipoUsuario import tipousuario
from .models.modelDepartamento import departamento
from .models.modelCategoria import categoria

# Register your models here.
admin.site.register(tipousuario)
admin.site.register(departamento)
admin.site.register(categoria)