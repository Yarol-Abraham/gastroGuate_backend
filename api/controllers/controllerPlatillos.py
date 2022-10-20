import json
from rest_framework.views import APIView
from api.serializer import PlatillosSerializer
from ..models.modelPlatillos import platillos
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class PlatilloswView(APIView):
    
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
        jd = request.data
        _descripcion=jd['descripcion']
        _precio=jd['precio']
        id_usuario=jd['id_usuario']
        id_categoria=jd['id_categoria']
        _stock=jd['stock']
        _oferta=jd['oferta']
        _precio_oferta=jd['precio_oferta']
        if _descripcion == '' or _precio == '' or id_usuario == '' or id_categoria == '' or _stock == '':
            datos = { 'message': 'existen campos vacios', 'quantity': 0, 'data': [] }
            return JsonResponse(datos)
        serializer=PlatillosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        datos = {
                'message': 'success',
                'data': {
                    'descripcion' : _descripcion,
                    'precio': _precio,
                    'id_usuario': id_usuario,
                    'id_categoria': id_categoria,
                    'stock' : _stock,
                    'oferta': _oferta,
                    'precio_oferta': _precio_oferta
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
                _platillosj = request.data
                __platillos.descripcion = _platillosj['descripcion']
                __platillos.precio = _platillosj['precio']
                __platillos.id_usuario_id = _platillosj['id_usuario']
                __platillos.id_categoria_id = _platillosj['id_categoria']
                __platillos.stock = _platillosj['stock']
                if 'image_url' in _platillosj : __platillos.image_url = _platillosj['image_url']
                __platillos.oferta = _platillosj['oferta']
                __platillos.precio_oferta = _platillosj['precio_oferta']
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
                        'stock': _platillosj['stock'],
                        'oferta': _platillosj['oferta'],
                        'precio_oferta': _platillosj['precio_oferta']
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