import json
from django.views import View
from ..models.modelPlatillos import platillos
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class PlatilloswView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, _id=0):
            _platillos={}
            datos = { 'message': 'fail', 'quantity': 0, 'data': [] }

            if _id > 0: 
                _platillos = list(platillos.objects.filter(id=_id,estado=1).values())
                if len(_platillos) > 0:
                    datos = { 'message': 'success', 'quantity': len(_platillos), 'data': _platillos[0] }
            else:
                _platillos = list(platillos.objects.filter(estado=1).values())
                if len(_platillos) > 0:
                    datos = { 
                        'message': 'success',
                        'quantity': len(_platillos),
                        'data': _platillos 
                    }
            return JsonResponse(datos)
                    
    def post(self, request):
        # RESPUESTA POR DEFECTO
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }
        # LEEMOS LOS DATOS ENVIADOS POR EL USUARIO
        jd = json.loads(request.body)
        _descripcion=jd['descripcion']
        _precio=jd['precio']
        id_usuario=jd['id_usuario']
        id_categoria=jd['id_categoria']
        _stock=jd['stock']
        if _descripcion == '' or _precio == '' or id_usuario == '' or id_categoria == '' or _stock == '':
            datos = { 'message': 'existen campos vacios', 'quantity': 0, 'data': [] }
            return JsonResponse(datos)
        platillos.objects.create(descripcion=_descripcion,precio=_precio,id_usuario_id=id_usuario,id_categoria_id=id_categoria,stock=_stock)
        datos = {
                'message': 'success',
                'data': {
                    'descripcion' : _descripcion,
                    'precio': _precio,
                    'id_usuario': id_usuario,
                    'id_categoria': id_categoria,
                    'stock' : _stock
                }
            }
        return JsonResponse(datos)        

    def put(self, request, _id=0):
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }
        _platillos = object()
        if _id>0:
            _platillos=list(platillos.objects.filter(id=_id).values())
            if len(_platillos)>0:
                __platillos = platillos.objects.get(id=_id)
                _platillosj = json.loads(request.body)
                __platillos.descripcion = _platillosj['descripcion']
                __platillos.precio = _platillosj['precio']
                __platillos.id_usuario_id = _platillosj['id_usuario']
                __platillos.id_categoria_id = _platillosj['id_categoria']
                __platillos.stock = _platillosj['stock']
                __platillos.save()
                datos = {
                    'message': 'success',
                    'quantity': 1,
                    'data': {
                        'id': _id,
                        'descripcion': _platillosj['descripcion'],
                        'precio': _platillosj['precio'],
                        'id_usuario': _platillosj['id_usuario'],
                        'id_categoria': _platillosj['id_categoria'],
                        'stock': _platillosj['stock']
                    }
                }
        return JsonResponse(datos)
    
    def delete(self, request, _id=0):
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }
        
        if _id>0: 
            _platillos=list(platillos.objects.filter(id=_id).values())
            if len(_platillos)>0:
                __platillos = platillos.objects.get(id=_id)
                _platillosj = json.loads(request.body)
                __platillos.estado = _platillosj['estado']
                __platillos.save()
                datos = {
                    'message': 'success',
                    'quantity': 1,
                    'data': {
                        'id': _id,
                        'estado': _platillosj['estado']
                    }
                }
        return JsonResponse(datos)