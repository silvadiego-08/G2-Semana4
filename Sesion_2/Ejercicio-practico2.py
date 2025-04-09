#Algoritmo para calcular el porcentaje de mujeres y varones en un aula.
print("Ingrese el número de alumnos varones:")
varones = int(input())
print("Ingrese el número de alumnos mujeres:")
mujeres = int(input())
#Calculo del total de alumnos
total = varones + mujeres
#Calculo del porcentaje de varones y mujeres
porcentaje_varones = (varones / total) * 100
porcentaje_mujeres = (mujeres / total) * 100

print("El porcentaje de varones es: {:.2f} %".format(porcentaje_varones))
print("El porcentaje de mujeres es: {:.2f} %".format(porcentaje_mujeres))
print("El total de alumnos es: ", total)