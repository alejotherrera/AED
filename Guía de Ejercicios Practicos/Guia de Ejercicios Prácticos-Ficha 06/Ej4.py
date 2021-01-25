__author__ = "Alejo Herrera"
import random
# Busqueda de mayor

# Realizar un programa que permita buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000].

#Declarar variables
num = 0
primero = 0
segundo = 0
cont = 1

#Estructura repetitiva
while cont <= 10000:
    num =  random.randint(0, 100.000)
    primero = num
    mayor = max(primero,segundo)
    segundo = primero
    cont += 1

print("El mayor de los numeros tomados es: ",mayor)