__author__ = "Alejo Herrera"

import random


# Modulos
def punto1():
    suma = cont = promedio = n = 0
    while n != -1:
        n = int(input("Ingrese un numero(-1 para salir): "))
        if n == -1:
            break
        suma += n
        cont += 1
    if cont != 0:
        promedio = round(suma / cont,2)
    else:
        promedio = 0
    print("El promedio es: ", promedio)
    return


def punto2():
    contpos = contneg = 0
    n = int(input("Ingrese cantidad de valores a generar: "))
    for i in range(0, n):
        nrandom = random.randint(-100, 100)
        if nrandom > 0:
            contpos += 1
        elif nrandom == 0:
            pass
        else:
            contneg += 1
    print("La cantidad de positivos es: ", contpos)
    print("La cantidad de negativos es: ", contneg)
    return


def punto3():
    nota = int(input("Ingrese nota del alumno: "))
    if 0 <= nota <= 10:
        if nota >= 4:
            print("El alumno esta aprobado")
        else:
            print("El alumno no esta aprobado")
    else:
        print("El alumno no esta aprobado")
    return


# Script principal
opcion = 0

# Ciclo / Loop
while opcion != 4:
    opcion = int(input("Ingrese opcion: "))
    if opcion == 1:
        punto1()
    elif opcion == 2:
        punto2()
    elif opcion == 3:
        punto3()
    elif opcion == 4:
        print("Gracias por usar el menu de opciones")
