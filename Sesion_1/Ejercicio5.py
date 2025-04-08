#Algoritmo que calcule el porcentaje de un número dado. Ejemplo: ¿qué es el 15% de 200?

print("¿Qué porcentaje quieres calcular?")
porcentaje = float(input("Introduce el porcentaje: "))
print("¿De qué número quieres calcular el porcentaje?")
numero = float(input("Introduce el número: "))
resultado = (porcentaje * numero) / 100
print("El", porcentaje, "% de", numero, "es:", resultado)


