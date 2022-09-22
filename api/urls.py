from django.urls import path
from .views import TipoUsuariosView

urlpatterns = [
    path('tipo/usuarios', TipoUsuariosView.as_view()),
    path('tipo/usuarios/<int:id>', TipoUsuariosView.as_view())

]

