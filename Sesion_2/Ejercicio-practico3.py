# Calcular el nuevo salario de un empleado si obtuvo un incremento del 8% sobre su salario actual y un descuento de 2,5% por servicios.

salario_actual = float(input("Ingrese el salario actual del empleado: "))
incremento = 0.08 * salario_actual
descuento = 0.025 * salario_actual
nuevo_salario = salario_actual + incremento - descuento

print(f"El nuevo salario del empleado es: {nuevo_salario:.2f}")