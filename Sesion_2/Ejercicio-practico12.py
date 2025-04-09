#El dueño de una tienda compra un artículo a un precio determinado. Obtener el precio en que lo debe vender para obtener una ganancia del 30%
print("Calcula una ganancia del 30%")

precio = float(input("Introduce el precio de compra del artículo: "))
ganancia = precio * 0.30
precio_venta = precio + ganancia
print("El precio de venta del artículo es: ", precio_venta)