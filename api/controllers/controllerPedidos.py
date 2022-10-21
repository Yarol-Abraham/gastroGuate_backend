import json
from ..models.modelPedidos import pedidos
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class PedidosView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # LOS PEDIDOS INDIVIDUALES SOLO SE PUEDEN OBTENER POR EL ID DEL USUARIO
    def get(self, request, _id=0):
        _pedidos={}
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }

        if _id > 0: 
            _pedidos = list(pedidos.objects.filter(id_usuario_id=_id,estado=1).values())
            if len(_pedidos) > 0:
                datos = { 'message': 'success', 'quantity': len(_pedidos), 'data': _pedidos[0] }
        else:
            _pedidos = list(pedidos.objects.filter(estado=1).values())
            if len(_pedidos) > 0:
                datos = { 
                    'message': 'success',
                    'quantity': len(_pedidos),
                    'data': _pedidos 
                }
        return JsonResponse(datos)

    def post(self, request):
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }
        # LEEMOS LOS DATOS ENVIADOS POR EL USUARIO
        jd = json.loads(request.body)
        _descripcion=jd['descripcion']
        _cantidad=jd['cantidad']
        _total=jd['total']
        _ubicacion=jd['ubicacion']
        _id_usuario=jd['id_usuario']
        _id_platillo=jd['id_platillo']
        if _descripcion == '' or _cantidad == '' or _total == '' or _id_usuario == '' or _id_platillo == '' or _ubicacion == '':
            datos = { 'message': 'existen campos vacios', 'quantity': 0, 'data': [] }
            return JsonResponse(datos)
        pedidos.objects.create(descripcion=_descripcion,cantidad=_cantidad,total=_total,ubicacion=_ubicacion,
        estado_pedido='p',id_platillo_id=_id_platillo,id_usuario_id=_id_usuario)
        datos = {
                'message': 'success',
                'data': {
                    'descripcion' : _descripcion,
                    'cantidad': _cantidad,
                    'total': _total,
                    'ubicacion': _ubicacion,
                    'id_usuario': _id_usuario,
                    '_id_platillo': _id_platillo 
                }
            }
        return JsonResponse(datos)

    def put(self, request, _id=0):
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }
        _pedido = object()
        if _id > 0:
            _pedido=list(pedidos.objects.filter(id=_id,estado=1).values())
            if len(_pedido)>0:
                __pedido = pedidos.objects.get(id=_id)
                _pedidoj = json.loads(request.body)
                __pedido.descripcion=_pedidoj['descripcion']
                __pedido.cantidad=_pedidoj['cantidad']
                __pedido.total=_pedidoj['total']
                __pedido.ubicacion=_pedidoj['ubicacion']
                __pedido.id_usuario_id =_pedidoj['id_usuario']
                __pedido.id_platillo_id=_pedidoj['id_platillo']
                __pedido.save()
                datos = {
                    'message': 'success',
                    'quantity': 1,
                    'data': {
                        'id': _id,
                        'descripcion': _pedidoj['descripcion'],
                        'cantidad': _pedidoj['cantidad'],
                        'total': _pedidoj['total'],
                        'ubicacion': _pedidoj['ubicacion'],
                        'id_usuario': _pedidoj['id_usuario'],
                        'id_platillo': _pedidoj['id_platillo']
                    }
                }
        return JsonResponse(datos)

    def delete(self, request, _id=0):
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }
        
        if _id>0: 
            _pedido=list(pedidos.objects.filter(id=_id,estado=1).values())
            if len(_pedido)>0:
                __pedido = pedidos.objects.get(id=_id)
                _pedidoj = json.loads(request.body)
                __pedido.estado = _pedidoj['estado']
                __pedido.save()
                datos = {
                    'message': 'success',
                    'quantity': 1,
                    'data': {
                        'id': _id,
                        'estado': _pedidoj['estado']
                    }
                }
        return JsonResponse(datos)