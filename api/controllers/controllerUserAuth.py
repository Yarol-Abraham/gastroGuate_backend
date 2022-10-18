from ..models.modelUsuario import usuario
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# CRUD PARA AUTENTICACIONES DE USUARIOS.
class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        datos = {
            'message': 'fail',
            'quantity': 0,
            'data': []
        }

        if id > 0:
            _usuario = list(usuario.objects.filter(id=id,estado=1).values())
            if len(_usuario) > 0:
                datos = { 
                    'message': 'success',
                    'quantity': len(_usuario),
                    'data': _usuario[0] 
                }
        else:    
            _usuario = list(usuario.objects.filter(estado=1).values())
            if len(_usuario) > 0:
                datos = { 
                    'message': 'success',
                    'quantity': len(_usuario),
                    'data': _usuario 
                }
           
        return JsonResponse(datos)
        
   