from api.views import ClienteViewSet, AnimalViewSet, VisitaViewSet
from rest_framework import routers
from django.urls import path, include
from . import views


router = routers.SimpleRouter()

router.register('cliente', ClienteViewSet, basename="cliente")
router.register('animal', AnimalViewSet, basename="animal")
router.register('visita', VisitaViewSet, basename="visita")

urlpatterns = [
    path('', include(router.urls)),
    path('busqueda-cliente/', views.busqueda_cliente, name="busqueda"),
    path('todos-los-clientes/', views.get_clientes)
]