#Diseñe un algoritmo que lea los datos necesarios y calcule la masa, según la formula siguiente:

presion = float(input("Ingrese la presion: "))
temperatura = float(input("Ingrese la temperatura: "))
volumen = float(input("Ingrese el volumen: "))

masa = (presion * volumen) / (0.37 * (temperatura + 460))

print(f"La masa es: {masa:.2f}")
