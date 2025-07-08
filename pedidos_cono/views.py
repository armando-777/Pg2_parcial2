from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from pedidos_cono.models import PedidoCono
from pedidos_cono.serializers import PedidoConoSerializer

class PedidoConoViewSet(viewsets.ModelViewSet):
    queryset = PedidoCono.objects.all().order_by("-fecha_pedido")
    serializer_class = PedidoConoSerializer
