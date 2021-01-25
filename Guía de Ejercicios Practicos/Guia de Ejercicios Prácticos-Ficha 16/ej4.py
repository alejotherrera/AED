import random


def validate_rango(inf, sup, mensaje):
    numero = inf - 1
    while numero <= inf or numero >= sup:
        numero = int(input(mensaje))
        if numero <= inf or numero >= sup:
            print("Error carge de nuevo valores de ", inf, " hasta ", sup)
    return numero


def carga_matriz(matriz, n, m):
    for i in range(n):
        for j in range(m):
            n = random.randint(1, 24)
            matriz[i][j] = n
    return matriz


def find_rol(matriz, n):
    rol = int(input("Ingrese rol: "))
    suma = 0
    for i in range(n):
        suma += matriz[i][rol]
    return suma


def proyecto_hora(matriz, m):
    x = int(input("Ingrese proyecto: "))
    suma = 0
    for i in range(m):
        suma += matriz[x][i]
    return suma


def rango_proyectos(matriz, inf, sup):
    total = 0
    for i in range(inf, sup + 1):
        for c in range(len(matriz[inf])):
            total += matriz[i][c]
    return total


def sep():
    print("-" * 30)


def menu():
    sep()
    print("MENU: ")
    print("1- Buscar rol: ")
    print("2- Saber cantidad de horas que un proyecto ocupo: ")
    print("3- Las horas promedios para un rango de proyectos: ")
    print("4- Calcular dinero: ")
    print("5- Salir")
    sep()
    opcion = int(input("Ingrese opcion del menu: "))
    sep()
    return opcion


def calculo_por_proyecto(matriz, cont, m):
    for i in range(len(cont)):
        for j in range(m):
            cont[i] += matriz[i][j]
    return cont


def principal():
    n = int(input("Ingrese cantidad de proyectos: "))
    m = int(input("Ingrese cantidad de roles involucrados: "))
    matriz = [[0] * m for i in range(n)]
    matriz = carga_matriz(matriz, n, m)
    print(matriz)
    opcion = -1
    while opcion != 5:
        opcion = menu()
        if opcion == 1:
            suma = find_rol(matriz, n)
            print("El total de horas que ocupo el rol fue de: ", suma)
        elif opcion == 2:
            horas_proyecto = proyecto_hora(matriz, m)
            print("El total de horas que un proyecto llevo fue de: ", horas_proyecto)
        elif opcion == 3:
            inf = validate_rango(0, n, "Ingrese rango inferior: ")
            sup = validate_rango(inf, n, "Ingrese rango superior: ")
            total = rango_proyectos(matriz, inf, sup)
            print("Las horas promedio es:", round(total / (sup - inf)))
        elif opcion == 4:
            x = int(input("Ingrese cantidad de proyectos cotizados: "))
            cont = [0] * x
            et = calculo_por_proyecto(matriz, cont, m)
            for i in range(len(cont)):
                print("El proyecto", (i + 1), " tuvo un costo de: $", et[i] * 157)
        elif opcion == 5:
            print("Gracias por utilizar el programa")
        else:
            print("Opcion Invalida")


if __name__ == '__main__':
    principal()
