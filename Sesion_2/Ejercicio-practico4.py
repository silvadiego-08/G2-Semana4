#Solicita el nombre, precio de un producto y un porcentaje de descuento. Muestra el nombre del producto y precio final luego de aplicar el descuento.

nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

print("Nombre del producto:", nombre)
precio_final = precio - (precio * (descuento / 100))
print(f"El precio final con descuento aplicado es: {precio_final:.2f}")