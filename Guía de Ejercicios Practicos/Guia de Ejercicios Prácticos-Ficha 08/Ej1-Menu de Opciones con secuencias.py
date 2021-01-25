__author__ = "Alejo Herrera"


# Modulos

def menu():
    print("1-Generar una serie de n numeros")
    print("-" * 30)
    print("2-Ingresar un texto finalizado por un punto y determinar la cantidad de palabrasa que finalizan con vocales")
    print("-" * 30)
    print("3-Ingresar una serie de numeros y determinar si hay mayor cantidad de valores pares o de impares")
    print("-" * 30)
    print("4-Salir")
    print("-" * 30)


def opcion1():
    n = 0
    suma = 0
    while n <= 0:
        n = int(input("Ingrese numero: "))
        if n <= 0:
            print("Error, ingrese numero valido")
        for i in range (1, n+1):
            suma += i ** 2
    print("La suma de los cuadrados es: ", suma)
    return


def opcion2():
    texto = input("Ingrese texto: ")
    anterior = " "
    contvocales = 0
    vocales = "aeiouAEIOU"
    for i in texto:
        if i == " " or i == ".":
            if anterior in vocales:
                contvocales += 1
        anterior = i
    print("La cantidad de palabras que terminan con vocales son ", contvocales)
    return


def opcion3():
    n = int
    contpares = 0
    contimpares = 0
    while n != 0:
        n = int(input("Ingrese numero: "))
        if n == 0:
            break
        if n % 2 == 0:
            contpares += 1
        else:
            contimpares += 1
    print("La cantidad de pares es: ", contpares)
    print("La cantidad de impares son: ", contimpares)
    return


def opcion4(salida):
    print("Gracias por usar nuestro programa")
    salida = True
    return salida


# Programa principal
salida = False
menu()
while salida != True:

    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
        opcion1()
    elif opcion == 2:
        opcion2()
    elif opcion == 3:
        opcion3()
    elif opcion == 4:
        opcion4(salida)
