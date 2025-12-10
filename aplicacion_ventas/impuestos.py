from .exceptions import ImpuestoInvalidoError

class Impuestos: #Se crea una clase de los impuestos que se deben de pagar por producto
    def __init__(self, porcentaje): #Se crea una clase con los respectivos atributos
        if not(0 <= porcentaje <= 1):
            raise ImpuestoInvalidoError("La tasa de impuesto debe de estar entre 0 y 1.")
        self.porcentaje=porcentaje
    
    def aplicar_impuesto(self, precio):
        return precio * self.porcentaje