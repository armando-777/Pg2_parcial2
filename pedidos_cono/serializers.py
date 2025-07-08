from rest_framework import serializers
from pedidos_cono.models import PedidoCono
from pedidos_cono.factory import ConoFactory
from pedidos_cono.builder import ConoPersonalizadoBuilder, ConoDirector
from api_patrones.logger import Logger

class PedidoConoSerializer(serializers.ModelSerializer):
    precio_total = serializers.SerializerMethodField()
    toppings_finales = serializers.SerializerMethodField()

    class Meta:
        model = PedidoCono
        fields = [
            "id",
            "cliente",
            "variante",
            "toppings",
            "tamanio_cono",
            "fecha_pedido",
            "precio_total",
            "toppings_finales",
        ]

    def get_precio_total(self, obj):
        base = ConoFactory.obtener_base(obj.variante)
        builder = ConoPersonalizadoBuilder(base)
        director = ConoDirector(builder)
        director.construir(obj.toppings, obj.tamanio_cono)
        Logger().registrar(f"Se calculó el precio del pedido {obj.id}")
        return builder.obtener_precio()

    def get_toppings_finales(self, obj):
        base = ConoFactory.obtener_base(obj.variante)
        builder = ConoPersonalizadoBuilder(base)
        director = ConoDirector(builder)
        director.construir(obj.toppings, obj.tamanio_cono)
        Logger().registrar(f"Toppings finales calculados para el pedido {obj.id}")
        return builder.obtener_toppings_finales()

    def validate_toppings(self, value):
        toppings_validos = {
            "queso_extra": 2,
            "papas_al_hilo": 1.5,
            "salchicha_extra": 3,
            "palta": 2.5,
            "champiñones": 2,
        }
        invalidos = [t for t in value if t not in toppings_validos]
        if invalidos:
            raise serializers.ValidationError(
                f"Toppings inválidos: {invalidos}. Permitidos: {list(toppings_validos.keys())}"
            )
        return value
