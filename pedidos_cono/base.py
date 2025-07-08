class ConoBase:
    def __init__(self):
        self.toppings = []
        self.precio = 0

    def inicializar(self):
        raise NotImplementedError()

    def obtener_toppings_base(self):
        return self.toppings

    def precio_base(self):
        return self.precio

class Carnivoro(ConoBase):
    def inicializar(self):
        self.toppings = ["carne", "queso"]
        self.precio = 20

class Vegetariano(ConoBase):
    def inicializar(self):
        self.toppings = ["verduras", "palta"]
        self.precio = 18

class Saludable(ConoBase):
    def inicializar(self):
        self.toppings = ["pollo", "ensalada"]
        self.precio = 19
