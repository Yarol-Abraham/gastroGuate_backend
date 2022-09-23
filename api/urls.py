from django.urls import path
from .controllers.controllerTipoUsuario import TipoUsuariosView
from .controllers.controllerDepartamento import DepartamentoView

urlpatterns = [
    path('tipo/usuarios', TipoUsuariosView.as_view()),
    path('tipo/usuarios/<int:id>', TipoUsuariosView.as_view()),
    path('departamentos', DepartamentoView.as_view())
]

