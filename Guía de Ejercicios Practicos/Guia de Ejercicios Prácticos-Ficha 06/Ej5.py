__author__ = "Alejo Herrera"
import random

#Variables auxiliares
cont = 1
primero = 0
anterior = 0
suma = 0
#Estructura repetitiva
while cont < 5000:
    num = random.randint(1, 100000)
    suma = num + suma
    primero = num
    minimo = min(primero, anterior)
    anterior = primero
    cont += 1

#Calcular promedio
promedio = suma/5000

#Mostrar resultados
print("El menor es: ", minimo)
print("El promedio es: ",promedio)