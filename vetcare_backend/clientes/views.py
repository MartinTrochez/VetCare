from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Cliente, Animal, Visita
from api.serializers import ClienteSerializer, AnimalSerializer, VisitaSerializer

# Create your views here.
def get_clientes(APIView):
    def get(self, request, format=None):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def busqueda_cliente(request):
    query = request.data.get('query', '')
    if query:
        clientes = Cliente.objects.filter(Q(name_icontains=query) | Q(description_icontains=query))
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)
    else:
        return Response({'cliente': []})