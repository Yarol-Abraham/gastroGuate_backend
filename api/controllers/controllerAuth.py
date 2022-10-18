import json 
from rest_framework.authtoken.models import Token
from django.views import View
from ..models.modelUsuario import usuario
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

# CRUD PARA LOGIN DE USUARIOS.
class LoginView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        _usuarioj = json.loads(request.body)
        datos = { 'message': 'usuario o contraseña son incorrectas', 'quantity': 0, 'data': [] }
        # BUSCAR SI EXISTE EL USUARIO
        usuarios = list(usuario.objects.filter(usuario=_usuarioj['usuario']).values())
        if len(usuarios) > 0:
            #OBTENER EL USUARIO DEL ARREGLO
            _user = User.objects.get(username=_usuarioj['usuario'])
            # VALIDAR LA CONTRASEÑA
            if check_password(_usuarioj['password'], _user.password):
                token, created = Token.objects.get_or_create(user=_user)
                datos = { 'message': 'success', 'quantity': 1, 'data': token.key }
                return JsonResponse(datos)
            else:
                return JsonResponse(datos)
        return JsonResponse(datos)
        