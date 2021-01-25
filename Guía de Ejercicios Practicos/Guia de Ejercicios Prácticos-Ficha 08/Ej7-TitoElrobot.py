__author__ = "Alejo Herrera"

import random


# Fuciones
# Menu
def menuopcion():
    print("A) Girar al norte y avanzar 10 pasos")
    print("B) Girar al sur y avanzar 20 pasos")
    print("C) Girar al este y avanzar 10 pasos")
    print("D) Girar al oeste y avanzar 20 pasos")
    print("E) Salir")


# Punto A
def norte(x, y):
    y += 10
    print("Posicion x,y: ",x, y)
    return


# Punto B
def sur(x, y):
    x += -20
    print("Posicion x,y: ",x, y)
    return


# Punto C
def este(x, y):
    x += 10
    print("Posicion x,y: ", x, y)
    return


# Punto D
def oeste(x, y):
    x += -20
    print("Posicion x,y: ", x, y)
    return


# Script principal
opcion = " "
x = random.randint(-100, 100)
y = random.randint(-100, 100)
print("Posicion incial (x,y): ", x, y)

while opcion != "E":
    menuopcion()
    print("-" * 30)
    opcion = input("Ingrese opcion: ")
    opcion = opcion.upper()
    print("-" * 30)
    if opcion == "A":
        norte(x, y)
    elif opcion == "B":
        sur(x,y)
    elif opcion == "C":
        este(x,y)
    elif opcion == "D":
        oeste(x,y)
    elif opcion == "E":
        print("Gracias por usar el programa")
