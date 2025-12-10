from aplicacion_ventas.gestor_ventas import GestorVentas

def main():
    precio_base=100.0
    impuesto_porcentaje=0.05 #Equivale al 5%
    descuento_porcentaje=0.10 #Equivale al 10%
    
    gestor=GestorVentas(precio_base,impuesto_porcentaje,descuento_porcentaje)
    precio_final=gestor.calcular_precio_final()
    
    print(f"Precio Base: {precio_base}")
    print(f"Impuesto: {impuesto_porcentaje*100}")
    print(f"Descuento: {descuento_porcentaje*100}")
    print(f"El Precio Final es: {precio_final}")

if __name__=="__main__":
    main()