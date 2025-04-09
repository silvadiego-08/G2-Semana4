#Dado un total de cuenta y un porcentaje de propina (por ejemplo, 10%), calcula cuánto dejar de propina
total_cuenta = float(input("Introduce el total de la cuenta: "))
porcentaje_propina = float(input("Introduce el porcentaje de propina: "))

propina = (total_cuenta * porcentaje_propina) / 100
total_con_propina = total_cuenta + propina

print("Su total de cuenta es: ", total_cuenta)
print(f"Su propina es: {propina:.2f}")
print(f"Su total con propina es: {total_con_propina:.2f}")