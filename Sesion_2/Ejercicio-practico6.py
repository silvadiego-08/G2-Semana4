#Solicita el precio de 3 productos y muestra: Subtotal, IVA (15%), Total a pagar

precio1 = float(input("Introduce el precio del primer producto: "))
precio2 = float(input("Introduce el precio del segundo producto: "))
precio3 = float(input("Introduce el precio del tercer producto: "))

subtotal = precio1 + precio2 + precio3
print(f"Tu subtotal es: {subtotal:.2f}")

precio_con_iva = subtotal * 0.15
print(f"IVA: {precio_con_iva:.2f}")

gran_total = subtotal + precio_con_iva
print(f"El total a pagar es: {gran_total:.2f}")

