from django.contrib import admin
from .models import Edificio, Departamento

# Register your models here.
class EdificioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'direccion', 'ciudad', 'tipo')
    
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'costo_departamento', 'numero_cuartos', 'edificio')
    search_fields = ('nombre_completo', 'costo_departamento', 'numero_cuartos')
    list_filter = ('edificio',)
    
admin.site.register(Edificio, EdificioAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
