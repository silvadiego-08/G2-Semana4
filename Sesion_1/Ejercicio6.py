# Crea un algoritmo que, dado el año de nacimiento de una persona y el año actual, calcule su edad actual y su edad en 10 años.

año_actual = 2025
año_nacimiento = int(input("Introduce tu año de nacimiento: "))

edad_actual = año_actual - año_nacimiento
edad_futura = edad_actual + 10

print("Tu edad actual es:", edad_actual)
print("Tu edad en 10 años será:", edad_futura)
