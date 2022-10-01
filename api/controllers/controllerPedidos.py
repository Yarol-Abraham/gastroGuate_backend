import json
from django.views import View
from ..models.modelPedidos import pedidos
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class PedidosView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, _id=0):
        _pedidos={}
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }

        if _id > 0: 
            _pedidos = list(pedidos.objects.filter(id=_id).values())
            if len(_pedidos) > 0:
                datos = { 'message': 'success', 'quantity': len(_pedidos), 'data': _pedidos[0] }
        else:
            _pedidos = list(pedidos.objects.values())
            if len(_pedidos) > 0:
                datos = { 
                    'message': 'success',
                    'quantity': len(_pedidos),
                    'data': _pedidos 
                }
        return JsonResponse(datos)
                    
    def delete(self, request, _id=0):
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }
        
        if _id>0: 
            _pedido=list(pedidos.objects.filter(id=_id).values())
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