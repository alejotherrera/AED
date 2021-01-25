__author__ = "Alejo Herrera"

# Declarar variables
num = 1
primero = 0
segundo = 0
mayor = "Par no ingresado"

#Estructura repetitiva
while num != 0:
    num = float(input("Ingrese numero: (0 para salir)"))
    if num % 2 == 0:
        primero = num
        mayor = max(primero, segundo)
        segundo = primero


#Imprimir numero
print("El mayor es: ",mayor)