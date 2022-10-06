import json
from django.views import View
from ..models.modelCategoria import categoria
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# CRUD PARA TIPO DE USUARIOS.
class CategoriaView(View):

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
            _categoria = list(categoria.objects.filter(id=id,estado=1).values())
            if len(_categoria) > 0:
                datos = { 
                    'message': 'success',
                    'quantity': len(_categoria),
                    'data': _categoria[0] 
                }
        else:    
            _categoria = list(categoria.objects.filter(estado=1).values())
            if len(_categoria) > 0:
                datos = { 
                    'message': 'success',
                    'quantity': len(_categoria),
                    'data': _categoria 
                }
           
        return JsonResponse(datos)

    def post(self, request):
        
        jd = json.loads(request.body)
        _tipo=jd['tipo']
        categoria.objects.create(tipo=_tipo)
        datos = {
                'message': 'success',
                'data': {
                    'tipo' : _tipo
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
            _categoria = list(categoria.objects.filter(id=id,estado=1).values())
            if len(_categoria) > 0:
                __categoria = categoria.objects.get(id=id)
                jd = json.loads(request.body)
                __categoria.tipo = jd['tipo']
                __categoria.save()
                datos = {
                    'message': 'success',
                    'quantity': 1,
                    'data': {
                        'id': id,
                        'tipo': jd['tipo']
                    }
                }

        return JsonResponse(datos)

    def delete(self, request, id=0):
        
        datos = {
            'message': 'fail',
            'quantity': 0,
            'data': {}
        }

        if id > 0:
            _categoria = list(categoria.objects.filter(id=id,estado=1).values())
            if len(_categoria) > 0:
                __categoria = categoria.objects.get(id=id)
                jd = json.loads(request.body)
                __categoria.estado = jd['estado']
                __categoria.save()
                datos = {
                    'message': 'success',
                    'quantity': 1,
                    'data': {
                        'id': id,
                        'estado': jd['estado']
                    }
                }

        return JsonResponse(datos)

        