#Adivina un numero
import random

numero_secreto = random.randint(1, 100)
print (numero_secreto)
numero_usuario = int(input("Dime un numero dl 1 al 10: "))

while True:
    if(numero_secreto == numero_usuario):
        print("Felicidades, adivinaste el numero secreto")
        break
    else:
        print ("Sigue intentando")
        numero_usuario = int(input("Dime un numero dl 1 al 100: "))

    if (numero_usuario > numero_secreto):
        print("El numero es menor")
    else:
        print("El numero es mayor")