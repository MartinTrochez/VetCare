from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    localidad = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellido}"


class Animal(models.Model):
    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    edad = models.IntegerField(null="true")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="mascota")

    def __str__(self) -> str:
        return f"{self.nombre} ({self.especie})"


class Visita(models.Model):
    diagnostico = models.TextField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE, related_name="visita")
    peso = models.FloatField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.fecha}, {self.peso} kg"