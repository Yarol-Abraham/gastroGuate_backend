import json
from django.shortcuts import render
from django.views import View
from ..models.modelPlatillos import platillos
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class PlatilloswView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def put(self, request, _id=0):
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }
        _platillos = object()
        if _id>0:
            _platillos=list(platillos.objects.filter(id=_id).values())
            if len(_platillos)>0:
                __platillos = platillos.objects.get(id=_id)
                _platillosj = json.loads(request.body)
                __platillos.nombre = _platillosj['nombre']
                __platillos.descripcion = _platillosj['descripcion']
                __platillos.precio = _platillosj['precio']
                __platillos.idUsuario = _platillosj['id_usuario']
                __platillos.stock = _platillosj['stock']
                __platillos.save()
                datos = {
                    'message': 'success',
                    'quantity': 1,
                    'data': {
                        'id': _id,
                        'nombre': _platillosj['nombre'],
                        'descripcion': _platillosj['descripcion'],
                        'precio': _platillosj['precio'],
                        'id_usuario': _platillosj['id_usuario'],
                        'id_categoria': _platillosj['id_categoria']
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