from django.contrib import admin

from .models.modelTipoUsuario import tipousuario
from .models.modelDepartamento import departamento

# Register your models here.
admin.site.register(tipousuario)
admin.site.register(departamento)