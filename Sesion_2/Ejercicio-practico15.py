# Algoritmo que calcule el salario de un trabajador de la manera siguiente. El trabajador cobra un precio fijo por hora y se le descuento el 5% en concepto de impuesto sobre la renta. 
# El programa debe pedir el nombre del trabajador, las horas trabajadas y el precio que cobra por hora. 
# Como salida debe imprimir el nombre del trabajador, el sueldo bruto, el descuento de renta y el salario a pagar.

nombre = input("Introduce el nombre del trabajador: ")
horas_trabajadas = float(input("Introduce las horas trabajadas: "))
precio_por_hora = float(input("Introduce el precio por hora: "))

sueldo_bruto = horas_trabajadas * precio_por_hora
descuento_renta = sueldo_bruto * 0.05
salario_a_pagar = sueldo_bruto - descuento_renta

print("\n--- Detalle del salario ---")
print(f"Nombre del trabajador: {nombre}")
print(f"Sueldo bruto: ${sueldo_bruto:.2f}")
print(f"Descuento por renta (5%): -${descuento_renta:.2f}")
print(f"Salario a pagar: ${salario_a_pagar:.2f}")

