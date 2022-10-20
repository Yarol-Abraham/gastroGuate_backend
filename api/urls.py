from django.urls import path

from api.controllers.controllerMunicipio import MunicipiosView
from .controllers.controllerTipoUsuario import TipoUsuariosView
from .controllers.controllerDepartamento import DepartamentoView
from .controllers.controllerCategoria import CategoriaView
from .controllers.controllerUsuario import UsuarioView
from .controllers.controllerPlatillos import PlatilloswView
from .controllers.controllerPedidos import PedidosView
from .controllers.controllerAuth import LoginView
from .controllers.controllerUserAuth import UserView
urlpatterns = [
    path('tipo/usuarios', TipoUsuariosView.as_view()),
    path('tipo/usuarios/<int:id>', TipoUsuariosView.as_view()),
    path('departamentos', DepartamentoView.as_view()),
    path('categorias', CategoriaView.as_view()),
    path('categorias/<int:id>', CategoriaView.as_view()),
    path('departamentos/<int:_id>', DepartamentoView.as_view()),
    path('usuarios', UsuarioView.as_view()),
    path('usuarios/<int:id>', UsuarioView.as_view()),
    path('municipio/<int:id>', MunicipiosView.as_view()),
    path('municipio', MunicipiosView.as_view()),
    path('platillos', PlatilloswView.as_view()),
    path('platillos/<int:_id>/<int:id_categoria>', PlatilloswView.as_view()),
    path('pedidos', PedidosView.as_view()),
    path('pedidos/<int:_id>', PedidosView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('user/<int:id>', UserView.as_view())
]

