#Pide nombre y apellido y muestra un posible correo: nombre.apellido@miuniversidad.edu.ni

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

correo = nombre.lower() + "." + apellido.lower() + "@miuniversidad.edu.ni"
print("Su correo es:", correo)
