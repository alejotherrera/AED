from Utilidades.utilidades import *


def carga():
    n = int(input("Ingrese cantidad de transportes realizados en el mes: "))
    dia = monto = desc = [0] * n
    for i in range(n):
        separacion()
        dia[i] = int(input("Ingrese dia: "))
        separacion()
        desc[i] = int(input("Ingrese descripcion: "))
        separacion()
        monto[i] = int(input("Ingrese monto: "))
    return dia, desc, monto


def promedio(monto):
    suma = 0
    n = (len(monto))
    for i in range(n):
        suma += monto[i]
    promedio = suma / n
    print(promedio)


def list(monto):
    n = len(monto)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if monto[i].codigo > monto[j].codigo:
                monto[i], monto[j] = monto[j], monto[i]
    return monto


def menu():
    print("Menu!:")
    print("1 - Determinar el monto promedio obtenido en el mes")
    print("2 - Genere un listado de los envíos realizados, ordenado por importe en forma decreciente")
    print("3 - Salir")


def principal():
    dia, desc, monto = carga()
    op = 0
    print(monto)
    while op != 3:
        menu()
        op = int(input("Ingrese opcion: "))
        if op == 1:
            promedio(monto)

        elif op == 2:
            montoide = list(monto)
            print(montoide)
        elif op == 3:
            print("Gracias por utilizar el programa")
            break


if __name__ == '__main__':
    principal()
