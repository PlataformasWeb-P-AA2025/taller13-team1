from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Edificio, Departamento
from .serializers import EdificioSerializer, DepartamentoSerializer
from rest_framework import permissions

# Create your views here.
class EdificioViewSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    # permission_classes = [permissions.IsAuthenticated]

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    # permission_classes = [permissions.IsAuthenticated]
