import random


def mostrar_matriz(matriz):
    print("Matriz hecha: ")
    n = len(matriz)
    for i in range(n):
        print("Linea" + str(i + 1))
        print(matriz[i])


def main():
    n = int(input("Ingrese cantidad de lineas de colectivo: "))
    m = int(input("Ingrese numero de paradas a procesar: "))
    matriz = [[0] * m for f in range(n)]
    for i in range(n):
        for j in range(m):
            cant = random.randint(1, 30)
            matriz[i][j] = cant
    print("Info:")
    opcion1 = op1(matriz, n, m)
    print("Total de pasajeros transportados: ")
    for i in range(len(opcion1)):
        print("Linea " + str(i + 1) + " total transportados: " + str(opcion1[i]))
    print(n)
    opcion2 = op2(matriz, n)
    print("El promedio es: ", opcion2)

    opcion3 = parada_menor(matriz)
    print("La menor cantidad de pasajeros fue: " + str(opcion3))

    opcion4 = op4(matriz, n, m)
    print("EL total recaudado es de: " + str(opcion4) + "$")


def op1(matriz, n, m):
    cont = [0] * n
    for i in range(n):
        for j in range(m):
            cont[i] += matriz[i][j]
    return cont


def op2(matriz, lineas):
    parada = int(input("Ingrese parada a buscar promedio: "))
    suma = 0
    lineas = lineas
    for i in range(lineas):
        suma += matriz[i][parada]
    return suma / lineas


def parada_menor(matriz):
    linea_menor = int(input("Ingrese linea menor: "))
    par_menor = 0
    men = matriz[linea_menor][0]
    for j in range(1, len(matriz[linea_menor])):  # j toma cada valor parada de la linea_menor
        if matriz[linea_menor][j] < men:
            par_menor = j
            men = matriz[linea_menor][j]

    return par_menor


def op4(matriz, n, m):
    suma = 0
    for i in range(n):
        for j in range(m):
            suma += matriz[i][j]
    suma = (suma * 8.5)
    return suma


if __name__ == '__main__':
    main()
