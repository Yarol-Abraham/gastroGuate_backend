import json
from django.views import View
from ..models.modelMunicipio import municipio
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# CRUD PARA MUNICIPIO.
class MunicipiosView(View):
    
    #permite que el controlador sea interpetado por un metodo http
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        datos = {
            'message': 'fail',
            'quantity': 0,
            'data':[]
        }
        if id>0:
            _municipio = list(municipio.objects.filter(id=id,estado=1))
            if len(_municipio) > 0 :
                datos = {
                    'message': 'success',
                    'quantity': len(_municipio),
                    'data': _municipio[0] 
                }
        else:
            _municipio = list(municipio.objects.filter(estado=1).values())
            if len(_municipio) > 0:
                datos = {
                    'message': 'success',
                    'quantity': len(_municipio),
                    'data': _municipio
                }
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        _nombre = jd['nombre']
        _abreviatura = jd['abreviatura']
        _idDepartamento = jd['id_departamento']
        municipio.objects.create(nombre=_nombre,abreviatura=_abreviatura,id_departamento_id=_idDepartamento)
        
        datos = {
                'message': 'success',
                'data': {
                    'nombre': _nombre,
                    'abreviatura' : _abreviatura,
                    'id_departamento': _idDepartamento
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
            _municipio = list(municipio.objects.filter(id=id).values())
            if len(_municipio) > 0:
                muni = municipio.objects.get(id=id)
                jd = json.loads(request.body)
                muni.nombre = jd['nombre']
                muni.abreviatura = jd['abreviatura']
                muni.id_departamento_id = jd['id_departamento']
                muni.save()
                
                datos = {
                    'message': 'success',
                    'quantity': 1,
                    'data': {
                        'nombre': jd['nombre'],
                        'abreviatura': jd['abreviatura'],
                        'id_departamento': jd['id_departamento']
                    }
                }
        return JsonResponse(datos)
    
    def delete(self,request, id=0):
        datos = {
            'message': 'fail',
            'quantity': 0,
            'data': {}
        }
        if id>0:  
            _municipio = list(municipio.objects.filter(id=id,estado=1).values())
            if len(_municipio)>0:
                __municipio = municipio.objects.get(id=id)
                _municipioj = json.loads(request.body)
                __municipio.estado = _municipioj['estado']
                __municipio.save()
                datos = {
                        'message': 'success',
                        'quantity': 1,
                        'data': {
                            'id': id,
                            'estado': _municipioj['estado']
                        }
                    }
        return JsonResponse(datos)