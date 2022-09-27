import json
from django.shortcuts import render
from django.views import View
from ..models.modelUsuario import usuario
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# CRUD PARA TIPO DE USUARIOS.
class UsuarioView(View):

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
            _usuario = list(usuario.objects.filter(id=id).values())
            if len(_usuario) > 0:
                datos = { 
                    'message': 'success',
                    'quantity': len(_usuario),
                    'data': _usuario[0] 
                }
        else:    
            _usuario = list(usuario.objects.values())
            if len(_usuario) > 0:
                datos = { 
                    'message': 'success',
                    'quantity': len(_usuario),
                    'data': _usuario 
                }
           
        return JsonResponse(datos)

    def post(self, request):
        # RESPUESTA POR DEFECTO
        datos = { 'message': 'fail', 'quantity': 0, 'data': [] }
        # LEEMOS LOS DATOS ENVIADOS POR EL USUARIO
        jd = json.loads(request.body)
        _nombre=jd['nombre']
        _apellido=jd['apellido']
        _usuario=jd['usuario']
        _password=jd['password']
        _passwordConfirmar=jd['passwordConfirmar']
        _identificacion=jd['identificacion']
        _idTipoUsuario=jd['idTipoUsuario']
        _idMunicipio=jd['idMunicipio']
        print(int(_idTipoUsuario) != _idTipoUsuario )
        if _nombre == '' or _apellido == '' or _usuario == '' or _password == '' or _passwordConfirmar == '' or _identificacion == '':
            datos = { 'message': 'existen campos vacios', 'quantity': 0, 'data': [] }
            return JsonResponse(datos)
        if _password != _passwordConfirmar:
            datos = { 'message': 'las contraseñas no conciden', 'quantity': 0, 'data': [] }
            return JsonResponse(datos)

        usuario.objects.create(nombre=_nombre,apellido=_apellido, usuario=_usuario,password=_password, identificacion=_identificacion, id_municipio_id=_idMunicipio, id_tipousuario_id=_idTipoUsuario)
      
        datos = {
                'message': 'success',
                'data': {
                    'nombre' : _nombre,
                    'apellido': _apellido,
                    'usuario': _usuario,
                    'identificacion': _identificacion,
                    'idTipoUsuario': _idTipoUsuario,
                    'idMunicipio': _idMunicipio 
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
                    __usuario = list(usuario.objects.filter(id=id).values())
                    _usuario = usuario.objects.get(id=id)
                    jd = json.loads(request.body)
                    _usuario.nombre = jd['nombre']
                    _usuario.apellido = jd['apellido']
                    _usuario.usuario = jd['usuario']
                    _usuario.identificacion = jd['identificacion']
                    _usuario.id_tipousuario_id = jd['idTipoUsuario']
                    _usuario.id_municipio_id = jd['idMunicipio']

                    _usuario.save()
                    datos = {
                        'message': 'success',
                        'quantity': 1,
                        'data': {
                            'id': id,
                            'nombre': jd['nombre'],
                            'apellido': jd['apellido'],
                            'usuario': jd['usuario'],
                            'identificacion': jd['identificacion'],
                            'idTipoUsuario': jd['idTipoUsuario'],
                            'idMunicipio': jd['idMunicipio']
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
                _usuario = list(usuario.objects.filter(id=id).values())
                if len(_usuario)>0:
                    _usuario = usuario.objects.get(id=id)
                    __usuario = json.loads(request.body)
                    _usuario.estado = __usuario['estado']
                    _usuario.save()
                    datos = {
                            'message': 'success',
                            'quantity': 1,
                            'data': {
                                'id': id,
                                'estado': __usuario['estado']
                            }
                        }
            return JsonResponse(datos)        

        