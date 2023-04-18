from clientes.models import Cliente, Animal, Visita
from rest_framework import serializers


class VisitaSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = [-1]
        model = Visita
        fields = [
            'animal',
            'peso',
            'diagnostico',
            'fecha'
        ]
        
    def create(self, data_validada):
        try:
            animal = Animal.objects.get(id=data_validada['animal'].id)
        except Animal.DoesNotExist:
            raise serializers.ValidationError('Animal no existe')
        
        visita = Visita.objects.create(**data_validada)
        return visita


class AnimalSerializer(serializers.ModelSerializer):
    visita = VisitaSerializer(many=True)
    class Meta:
        model = Animal
        fields = [
            'id',
            'nombre',
            'especie',
            'raza',
            'color',
            'edad',
            'cliente',
            'visita'
        ]
    
    def create(self, data_validada):
        try:
            cliente = Cliente.objects.get(id=data_validada['cliente'].id)
        except Cliente.DoesNotExist:
            raise serializers.ValidationError('Cliente no existe')
        
        visita_data = data_validada.pop('visita', [])
        animal = Animal.objects.create(**data_validada)
        for visita_data in visita_data:
            Visita.objects.create(animal=animal, **visita_data)

        return animal
    
    
class ClienteSerializer(serializers.ModelSerializer):
    mascota = AnimalSerializer(many=True)

    class Meta:
        ordering = ['apellido']
        model = Cliente
        depth = 1
        fields = [
            'id',
            'nombre',
            'apellido',
            'email',
            'localidad',
            'provincia',
            'direccion',
            'telefono',
            'mascota'
        ]
    
    def create(self, data_validada):
        nombre = data_validada.get('nombre')
        apellido = data_validada.get('apellido')
        if Cliente.objects.filter(nombre=nombre, apellido=apellido).exists():
            raise serializers.ValidationError('El cliente ya esta resgistrado en la base de datos')
        mascota_data = data_validada.pop('mascota', [])
        cliente = Cliente.objects.create(**data_validada)

        for animal_data in mascota_data:
            visita_data = animal_data.pop('visita', [])
            animal = Animal.objects.create(cliente=cliente, **animal_data)

            for visita_data in visita_data:
                Visita.objects.create(animal=animal, **visita_data)

        return cliente