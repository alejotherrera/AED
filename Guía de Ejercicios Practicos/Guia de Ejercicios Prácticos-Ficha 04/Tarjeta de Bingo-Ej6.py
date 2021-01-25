__author__ = "Alejo Herrera"

import random

# ingreso de numeros

num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))
num3 = int(input("Ingrese numero 3: "))

# determinamos random
billete = random.randint(1, 100)
if billete == num1 or billete == num2 or billete == num3:
    print("El jugador marcó algún numero de la tarjeta")
else:
    print("El jugador tiene mala suerte, no marcó ninguna casilla")
