#Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometralos tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en recorrerla ruta en una semana cualquiera

tiempo_segundos = float(input("Ingrese el tiempo que corre en segundos: "))
tiempo_lunes = tiempo_segundos
tiempo_miercoles = tiempo_segundos
tiempo_viernes = tiempo_segundos
tiempo_total = tiempo_lunes + tiempo_miercoles + tiempo_viernes
tiempo_promedio = tiempo_total / 3
tiempo_promedio_minutos = tiempo_promedio / 60

print("El tiempo promedio que tarda en recorrer la ruta es de: ", tiempo_promedio_minutos, "minutos")


