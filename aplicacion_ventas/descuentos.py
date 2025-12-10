from .exceptions import DescuentoInvalidoError

class Descuentos: #Son los descuentos que va a tener una persona al comprar un producto
    def __init__(self, porcentaje): #Se crea un constructor con los respectivos atributos
        if not (0 <= porcentaje <= 1):
            raise DescuentoInvalidoError("El porcentaje de descuento debe estar entre 0 y 1.")
        self.porcentaje=porcentaje
    
    def aplicar_descuento(self, precio):
        return precio * self.porcentaje