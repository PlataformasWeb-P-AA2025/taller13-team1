from django.db import models

# Create your models here.
class Edificio(models.Model):
    """
    Modelo que representa un edificio de una empresa.
    """
    
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} - {self.ciudad} ({self.tipo})"
    

class Departamento(models.Model):
    """
    Modelo que representa un departamento dentro de un edificio.
    """
    
    nombre_completo = models.CharField(max_length=100)
    costo_departamento = models.DecimalField(max_digits=10, decimal_places=2)
    numero_cuartos = models.CharField(max_length=10)
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, related_name='departamentos')
    
    def __str__(self):
        return f"{self.nombre_completo} - {self.edificio.nombre}"
    