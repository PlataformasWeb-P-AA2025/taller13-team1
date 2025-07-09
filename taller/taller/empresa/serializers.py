from django.contrib.auth.models import User, Group
from .models import Edificio, Departamento
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edificio
        fields = ['url', 'nombre', 'direccion', 'ciudad', 'tipo']
        
class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    edificio = serializers.HyperlinkedRelatedField(
        view_name='edificio-detail',
        queryset=Edificio.objects.all()
    )
    
    class Meta:
        model = Departamento
        fields = ['url', 'nombre_completo', 'costo_departamento', 'numero_cuartos', 'edificio']
