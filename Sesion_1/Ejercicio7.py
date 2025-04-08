#Diseña un algoritmo que intercambie el valor de dos variables numéricas. Usa una variable auxiliar para hacerlo.
# Definimos las dos variables
a = 5
b = 10

print("Antes del intercambio:")
print("a =", a)
print("b =", b)

auxiliar = a  
a = b        
b = auxiliar 

print("Después del intercambio:")
print("a =", a)
print("b =", b)

