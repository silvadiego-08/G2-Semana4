#En un hospital existen 3 áreas: Urgencias, Pediatría y Traumatología. El presupuesto anual del hospital se reparte de la siguiente manera:
#Urgencias: 37%, Pediatria: 42%, Traumatología: 21%.
#Obtener la cantidad de dinero que recibirá cada área para cualquier monto presupuestal

presupuesto = float(input("Ingrese el presupuesto anual del hospital: "))
urgencias = presupuesto * 0.37
pediatria = presupuesto * 0.42
traumatologia = presupuesto * 0.21

print(f"El presupuesto para Urgencias es: {urgencias:.2f}")
print(f"El presupuesto para Pediatría es: {pediatria:.2f}")
print(f"El presupuesto para Traumatología es: {traumatologia:.2f}")

