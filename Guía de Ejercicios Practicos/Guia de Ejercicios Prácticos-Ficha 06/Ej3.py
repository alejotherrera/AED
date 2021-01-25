__author__ ="Alejo Herrera"
import random
#Promedio de números aleatorios

#Realice un programa que permita calcular el promedio de 1000 números aleatorios generados en el rango de [0, 100000]

#Declarar variables auxiliares
cont = 1
promedio = 0
num = 0

#Estructura repetitiva
while cont < 10000:
    num = random.randint(0, 100000)
    promedio = num + promedio
    cont = cont + 1

#Imprimir y calcular promedio
promediototal = promedio / 100000
print(promedio)