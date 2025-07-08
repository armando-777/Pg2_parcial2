from django.db import models
from django.core.exceptions import ValidationError
from pedidos_cono.factory import ConoFactory
from pedidos_cono.builder import ConoPersonalizadoBuilder

class PedidoCono(models.Model):
    cliente = models.CharField(max_length=100)
    variante = models.CharField(
        max_length=20,
        choices=[
            ("carnivoro", "Carnívoro"),
            ("vegetariano", "Vegetariano"),
            ("saludable", "Saludable"),
        ],
    )
    toppings = models.JSONField(default=list)
    tamanio_cono = models.CharField(
        max_length=10,
        choices=[
            ("pequeño", "Pequeño"),
            ("mediano", "Mediano"),
            ("grande", "Grande"),
        ],
    )
    fecha_pedido = models.DateField(auto_now_add=True)

    def clean(self):
        cono = ConoFactory.obtener_base("carnivoro")
        builder = ConoPersonalizadoBuilder(cono)

        toppings_invalidos = []

        for topping in self.toppings:
            try:
                builder.agregar_topping(topping)
            except ValueError:
                toppings_invalidos.append(topping)

        if toppings_invalidos:
            raise ValidationError({
                'toppings': (
                    f"Toppings no válidos: {toppings_invalidos}. "
                    f"Los permitidos son: ['queso_extra', 'papas_al_hilo', 'salchicha_extra', 'palta', 'champiñones']"
                )
            })
