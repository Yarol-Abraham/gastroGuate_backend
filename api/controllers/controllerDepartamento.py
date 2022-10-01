import json
from django.views import View
from ..models.modelDepartamento import departamento
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class DepartamentoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, _id=0):
        _departamento={}
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }

        if _id > 0: 
            _departamento = list(departamento.objects.filter(id=_id).values())
            if len(_departamento) > 0:
                datos = { 'message': 'success', 'quantity': len(_departamento), 'data': _departamento[0] }
        else:
            _departamento = list(departamento.objects.values())
            if len(_departamento) > 0:
                datos = { 
                    'message': 'success',
                    'quantity': len(_departamento),
                    'data': _departamento 
                }
        return JsonResponse(datos)
                    
    def post(self, request):
        # RESPUESTA POR DEFECTO
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }
        # LEEMOS LOS DATOS ENVIADOS POR EL USUARIO
        jd = json.loads(request.body)
        _nombre=jd['nombre']
        _abreviatura=jd['abreviatura']
        print(_nombre == '')
        if _nombre == '' or _abreviatura == '':
            datos = { 'message': 'existen campos vacios', 'quantity': 0, 'data': [] }
            return JsonResponse(datos)
        departamento.objects.create(nombre=_nombre,abreviatura=_abreviatura)
        datos = {
                'message': 'success',
                'data': {
                    'nombre' : _nombre,
                    'abreviatura': _abreviatura
                }
            }
        return JsonResponse(datos)
    
    def put(self, request, _id=0):
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }
        _departamento = object()
        if _id>0:
            _departamento=list(departamento.objects.filter(id=_id).values())
            if len(_departamento)>0:
                __departamento = departamento.objects.get(id=_id)
                _departamentoj = json.loads(request.body)
                __departamento.nombre = _departamentoj['nombre']
                __departamento.abreviatura = _departamentoj['abreviatura']
                __departamento.save()
                datos = {
                    'message': 'success',
                    'quantity': 1,
                    'data': {
                        'id': _id,
                        'nombre': _departamentoj['nombre'],
                        'abreviatura': _departamentoj['abreviatura']
                    }
                }
        return JsonResponse(datos)
    
    def delete(self, request, _id=0):
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }
        
        if _id>0: 
            _departamento=list(departamento.objects.filter(id=_id).values())
            if len(_departamento)>0:
                __departamento = departamento.objects.get(id=_id)
                _departamentoj = json.loads(request.body)
                __departamento.estado = _departamentoj['estado']
                __departamento.save()
                datos = {
                    'message': 'success',
                    'quantity': 1,
                    'data': {
                        'id': _id,
                        'estado': _departamentoj['estado']
                    }
                }
        return JsonResponse(datos)