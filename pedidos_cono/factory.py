from pedidos_cono.base import Carnivoro, Vegetariano, Saludable

class ConoFactory:
    @staticmethod
    def obtener_base(variante):
        if variante == "carnivoro":
            base = Carnivoro()
        elif variante == "vegetariano":
            base = Vegetariano()
        elif variante == "saludable":
            base = Saludable()
        else:
            raise ValueError("Variante no válida")
        
        base.inicializar()
        return base
