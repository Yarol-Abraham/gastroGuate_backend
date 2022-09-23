import json
from django.shortcuts import render
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
                    datos = { 'message': 'success', 'quantity': len(_departamento), 'data': _departamento }
        return JsonResponse(datos)
                    
            