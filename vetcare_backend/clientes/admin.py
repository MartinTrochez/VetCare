from django.contrib import admin
from .models import Cliente, Animal, Visita


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "apellido", "email", "localidad", "provincia", "direccion", "telefono")


class AnimalAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "especie", "raza", "color", "edad", "cliente")


class VisitaAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha", "peso")


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Visita, VisitaAdmin)