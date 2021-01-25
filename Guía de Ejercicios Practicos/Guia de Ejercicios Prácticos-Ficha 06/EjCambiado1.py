__author__ = "Alejo Herrera"

#ESTE EJERCICIO LO HICE PERO A LOS DIAS LO CAMBIARON

import random

# Mostrar por pantalla el menu y elegir la opcion

print("Opción 1: Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000].")
print("Opción 2: Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000].")
print(
    "Opción 3: Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000] y calcular el valor promedio de los números menores a 10.000.")
opcion = int(input("Ingrese opcion: "))

# Funciones def
def primeropcion():
    cont = 1
    num = 0

    while cont < 1000:
        numrandom = random.randrange(0, 100.001)
        num = num + numrandom
        cont = cont + 1
    promedio = float(num / 1000)
    print("El promedio es:", promedio)


def segundaopcion():
    cont = 1
    num = 0
    while cont < 10000:
        num = random.randrange(0, 100.001)
        primero = num
        segundo = primero
        mayor = max(primero, segundo)
        cont = cont + 1
    print(mayor)


def terceraopcion():
    cont = 1
    num = 0
    while cont < 5000:
        num = random.randrange(0, 100.001)
        primero = num
        segundo = primero
        menor = min(primero, segundo)
        cont = cont + 1
    print(menor)


# Condicion con funciones def
if opcion == 1:
    primeropcion()
elif opcion == 2:
    segundaopcion()
elif opcion == 3:
    terceraopcion()
else:
    print("Ingrese una opcion valida")
