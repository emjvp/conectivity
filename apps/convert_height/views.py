from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class ConvertHeight(APIView):
   
    renderer_classes = [JSONRenderer]

    def post(self, request):        
        data = request.data.copy()
        height_info = data['height'].split()
                
        if len(height_info) < 2:
            return Response("Las unidades no fueron especificadas")
        
        inches = int(height_info[0])
        units = height_info[1]
        
        if units != 'pulgadas':
            return Response("Sólo se pueden hacer una conversión de altura de pulgadas a metros")
        
        meters = str(inches/39.370)[0:4]        
        data['height'] = f"{meters} metros"        
        return Response(data)