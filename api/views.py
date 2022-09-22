import json
from django.shortcuts import render
from django.views import View
from .models import tipousuario
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class TipoUsuariosView(View):

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
            _tipousuario = list(tipousuario.objects.filter(id=id).values())
            if len(_tipousuario) > 0:
                datos = { 
                    'message': 'success',
                    'quantity': len(_tipousuario),
                    'data': _tipousuario[0] 
                }
        else:    
            _tipousuario = list(tipousuario.objects.values())
            if len(_tipousuario) > 0:
                datos = { 
                    'message': 'success',
                    'quantity': len(_tipousuario),
                    'data': _tipousuario 
                }
           
        return JsonResponse(datos)

    def post(self, request):
        
        jd = json.loads(request.body)
        _rol=jd['rol']
        _abreviatura=jd['abreviatura']
        tipousuario.objects.create(rol=_rol,abreviatura=_abreviatura)
        datos = {
                'message': 'success',
                'data': {
                    'rol' : _rol,
                    'abreviatura': _abreviatura
                }
            }
        return JsonResponse(datos)

    def put(self, request, id=0):
        
        datos = {
            'message': 'fail',
            'quantity': 0,
            'data': {}
        }

        if id > 0:
            _tipousuario = list(tipousuario.objects.filter(id=id).values())
            if len(_tipousuario) > 0:
                tipo = tipousuario.objects.get(id=id)
                jd = json.loads(request.body)
                tipo.rol = jd['rol']
                tipo.abreviatura = jd['abreviatura']
                tipo.save()
                datos = {
                    'message': 'success',
                    'quantity': 1,
                    'data': {
                        'id': id,
                        'rol': jd['rol'],
                        'abreviatura': jd['abreviatura']
                    }
                }

        return JsonResponse(datos)

        