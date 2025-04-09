#Calcula la calificación final de un estudiante con ponderaciones:
#Tareas: 30%, Examen parcial: 30%, Examen final: 40%

calificacion_tareas = float(input("Ingrese la calificación de tareas: "))
calificacion_examen_parcial = float(input("Ingrese la calificación del examen parcial: "))
calificacion_examen_final = float(input("Ingrese la calificación del examen final: "))

#Ponderaciones
ponderacion_tareas = 0.30
ponderacion_examen_parcial = 0.30
ponderacion_examen_final = 0.40

#Cálculo de la calificación final
calificacion_final = (calificacion_tareas * ponderacion_tareas) + (calificacion_examen_parcial * ponderacion_examen_parcial) + (calificacion_examen_final * ponderacion_examen_final)

print(f"La calificación final del estudiante es: {calificacion_final:.2f}")