class Precios:
    @staticmethod #Se usa un decorador staticmethod, este sirve para definir un método estático dentro de una clase
    #los métodos estáticos son aquellos que no dependen de una estancia particular de la clase
    #y no tienen acceso a los atributos o métodos de la estancia, es decir que no pueden acceder a 
    def calcular_precio_final(precio_base, impuesto, descuento):
        return precio_base+impuesto -descuento