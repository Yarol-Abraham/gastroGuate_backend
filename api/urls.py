from django.urls import path

from api.controllers.controllerMunicipio import MunicipiosView
from .controllers.controllerTipoUsuario import TipoUsuariosView
from .controllers.controllerDepartamento import DepartamentoView
from .controllers.controllerCategoria import CategoriaView

urlpatterns = [
    path('tipo/usuarios', TipoUsuariosView.as_view()),
    path('tipo/usuarios/<int:id>', TipoUsuariosView.as_view()),
    path('departamentos', DepartamentoView.as_view()),
    path('categorias', CategoriaView.as_view()),
    path('categorias/<int:id>', CategoriaView.as_view()),
    path('departamentos/<int:_id>', DepartamentoView.as_view()),
    path('municipio/<int:id>', MunicipiosView.as_view()),
    path('municipio', MunicipiosView.as_view())
]

