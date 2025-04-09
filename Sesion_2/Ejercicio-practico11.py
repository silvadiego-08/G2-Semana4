#Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio
print("Calcula el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio")
edad = int(input("Ingrese su edad: "))

num_pulsaciones = (220 - edad) / 10

print("El número de pulsaciones que debe tener por cada 10 segundos de ejercicio es: ", num_pulsaciones)