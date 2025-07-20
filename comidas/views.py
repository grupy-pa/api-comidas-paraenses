from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response 
from rest_framework import status
from comidas.serializers import ComidaParaenseSerializer
from comidas.models import Comida

class ViewSetStatus(ViewSet):
    def list(self, request):
        return Response({"message": "API funcionando!"}, status=status.HTTP_200_OK)

class ComidasViewSet(ModelViewSet):
    serializer_class = ComidaParaenseSerializer
    queryset = Comida.objects.all()
# Create your views here.
