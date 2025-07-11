from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Edificio, Departamento
from .serializers import EdificioSerializer, DepartamentoSerializer

# Create your views here.
class EdificioViewSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    permission_classes = [permissions.IsAuthenticated]

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
