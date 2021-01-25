__author__ = "Alejo Herrera"

import random


# Modulos
def separacion():
    print("-----------------------------------------------")


def validardado(n):
    print("Tiro de dados")
    dado1 = [0] * n
    dado2 = [0] * n
    for i in range(n):
        dado1[i] = random.randint(1, 6)
        dado2[i] = random.randint(1, 6)
        print("Tiro del dado 1 numero", i + 1, ":", dado1[i])
        print("Tiro del dado 2 numero", i + 1, ":", dado2[i])
    separacion()
    return (dado1, dado2)


def validacion():
    n = int(input("Ingrese cantidad de lanzamientos: "))
    while n <= 0:
        print("Error, ingrese un numero mayor a 0")
    separacion()
    return n


def menu():
    print("2 _ Mismo valor y que porcentaje representa sobre los lanzamientos")
    print("3 _ En qué lanzamiento se dio por primera vez una suma impar entre ambos dados")
    print("4 _ Cuál fue el mayor valor que apareció en cada dado y cuántas veces se presentó")
    print("5 _ Cuántas veces apareció cada una de las sumas posibles entre ambos dados")
    print(
        "6 - Determinar la cantidad de tiradas en las que la suma de ambos dados fue mayor que la suma promedio de todas las tiradas")
    print("7 _ Salir")


def repeticion(dado1, dado2):
    iguales = 0
    for i in range(len(dado1)):
        if dado1[i] == dado2[i]:
            iguales += 1
    porcentaje = iguales * 100 / (len(dado1) + len(dado2))
    return iguales, porcentaje


def suma_impar(dado1, dado2):
    sumaimpar = 0
    for i in range(len(dado1)):
        if (dado1[i] + dado2[i]) % 2 == 0:
            sumaimpar += 1
            return i+1
    return -1


def mayorvalor(dado):
    pase = False
    mayor = dado[0]
    repeticiones = 0
    for i in range(len(dado)):
        if mayor < dado[i]:
            mayor = dado[i]
        elif dado[i] == mayor and pase:
            repeticiones += 1
        pase = True
    return mayor


def sumadedadospares(dado1, dado2):
    conteo = [0] * 13
    for i in range(len(dado1)):
        suma = dado1[i] + dado2[i]
        conteo[suma] += 1
    return conteo


def mostrar(conteo):
    for i in range(len(conteo)):
        print("suma", i, "->", conteo[i], "veces")


def promedio(dado1, dado2):
    ac = 0
    for i in range(len(dado1)):
        ac += dado1[i]
        ac += dado2[i]

    promedio = ac / len(dado1)
    cant_mayores = 0

    for i in range(len(dado1)):
        s = dado1[i] + dado2[i]
        if s > promedio:
            cant_mayores += 1
    return cant_mayores


def main():
    print("Bienvenido a los dados")
    sumaimpar = 0
    contar_sumas = 0
    opcion = 0
    n = validacion()
    dado1, dado2 = validardado(n)
    while opcion != 7:
        menu()
        separacion()
        opcion = int(input("Ingrese opcion: "))
        separacion()
        if opcion == 1:
            iguales, porcentaje = repeticion(dado1, dado2)
            print("Mismo valor en ambos dados: ", iguales)
            print("Porcentaje: ", porcentaje)
        elif opcion == 2:
            total = suma_impar(dado1,dado2)
            if total == -1:
                print("Nunca hubo una suma impar")
            else:
                print("La primer suma impar aparecio en el lanzamiento",total)
        elif opcion == 3:
            eleccion = input("Ingrese 1 o 2 por dado")
            if eleccion == 1:
                print("El mayor valor del dado 1 es: ", mayorvalor(dado2))
            else:
                print("El mayor valor del dado 2 es: ", mayorvalor(dado2))
        elif opcion == 4:
            conteo = sumadedadospares(dado1, dado2)
            print("El conteo: ")
            mostrar(conteo)
        elif opcion == 5:
            cantidad_mayores = promedio(dado1, dado2)
            print('En', cantidad_mayores, 'tiradas la suma fue mayor al promedio')
        else:
            print("Error,numero invalido")
        separacion()


if __name__ == "__main__":
    main()
