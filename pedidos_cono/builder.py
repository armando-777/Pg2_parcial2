class ConoPersonalizadoBuilder:
    def __init__(self, base):
        self.base = base
        self.precio = base.precio_base()
        self.toppings = list(base.obtener_toppings_base())

    def agregar_topping(self, topping):
        precios = {
            "queso_extra": 2,
            "papas_al_hilo": 1.5,
            "salchicha_extra": 3,
            "palta": 2.5,
            "champiñones": 2,
        }
        if topping not in precios:
            raise ValueError(f"Topping '{topping}' no válido o no disponible.")
        self.toppings.append(topping)
        self.precio += precios[topping]

    def ajustar_tamanio(self, tamanio):
        if tamanio == "mediano":
            self.precio *= 1.2
        elif tamanio == "grande":
            self.precio *= 1.5

    def obtener_precio(self):
        return round(self.precio, 2)

    def obtener_toppings_finales(self):
        return self.toppings


class ConoDirector:
    def __init__(self, builder):
        self.builder = builder

    def construir(self, toppings, tamanio):
        for t in toppings:
            self.builder.agregar_topping(t)
        self.builder.ajustar_tamanio(tamanio)
