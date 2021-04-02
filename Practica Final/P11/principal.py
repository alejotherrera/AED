__author__ = "Alejo Herrera"

import random, os, pickle
from plan import *


# Utilidades graficas
def sep():
    print("=" * 50)


# Validaciones
def validar_entre(desde, hasta, mensaje):
    num = int(input(mensaje))
    while num < desde or num > hasta:
        print('Inválido! Debe ser un valor entre', desde, 'y', hasta)
        num = int(input(mensaje))
    return num


def validar_monto(mensaje):
    monto = float(input(mensaje))
    while monto < 0:
        print('Inválido! Debe ser un valor positivo.')
        monto = float(input(mensaje))
    return monto


def validar_pos(a):
    n = a
    while n <= a:
        n = int(input("Ingrese valor n a cargar en el arreglo(mayor a " + str(a) + "):"))
        if n <= a:
            print("Error ingrese un valor mayor a:", a)
    return n


def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while inf > n or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Error... opcion invalida, ingrese entre " + str(inf) + " y " + str(sup))
    return n


# Carga de datos
def carga(fd, n):
    m = open(fd, "a+b")
    nombres = ("julian", "camila", "carlos", "matias", "alejandra", "valerio")
    planes = (
        "plan progresar.", "plan amigos.", "plan tabaqueria.", "plan tabaco.", "plan trabajar.")
    for i in range(n):
        id = random.randint(1, 1000)
        nombre = random.choice(nombres)
        nombre = nombre.ljust(30, " ")
        descripcion = random.choice(planes)
        monto = random.randint(500, 10000)
        tipo = random.randint(1, 10)
        edades = random.randint(1, 5)
        reg = Plan(id, nombre, descripcion, monto, tipo, edades)
        pickle.dump(reg, m)
        m.flush()
    print("Planes grabados con exito...!")
    m.close()


# Mostrar archivo
def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo no existe, generelo con el punto 1")
        return

    m = open(fd, "rb")
    tmn = os.path.getsize(fd)

    print("Datos del archivo: ")
    while m.tell() < tmn:
        a = pickle.load(m)
        to_string(a)
    m.close()


# Generar arreglo
def generar_arreglo(fd, p, arreglo):
    if not os.path.exists(fd):
        print("El archivo no existe, generelo con el punto 1")
        return

    m = open(fd, "rb")
    tmn = os.path.getsize(fd)
    while m.tell() < tmn:
        reg = pickle.load(m)
        if reg.monto > p:
            arreglo.append(reg)
    print("Datos grabados con exito!!")
    m.close()
    return arreglo


# Ordenamientos
def ordenamientodirecto(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].id > v[j].id:
                v[i], v[j] = v[j], v[i]
    return v


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def busqueda_secuencial(v, nom):
    for i in range(len(v)):
        if v[i].nombre == nom:
            return i
    return -1


def busqueda_secuencial1(v, nom):
    for i in range(len(v)):
        if v[i].id == nom:
            return i
    return -1


def crear_matriz(fd):
    if not os.path.exists(fd):
        print("El archivo no existe, generelo con el punto 1")
        return

    matriz = [[0] * 5 for k in range(10)]

    m = open(fd, "rb")
    tmn = os.path.getsize(fd)

    while m.tell() < tmn:
        a = pickle.load(m)
        matriz[a.tipo - 1][a.edades - 1] += 1
    m.close()
    return matriz


def mostrar_matriz(matriz):
    print()
    for i in range(10):
        for j in range(5):
            if matriz[i][j] > 0:
                print("Plan " + str(i) + " por edad " + str(j) + " : ", matriz[i][j])
    print()


def analisis_cadena(cadena):
    hay_t = hay_tb = False
    cont = pal = 0
    for i in cadena:
        if i == " " or i == ".":
            if hay_tb and cont > 4:
                pal += 1
            # Reiniciar banderas
            cont = 0
            hay_tb = hay_t = False
        else:
            cont += 1
            if i == "t" and not hay_t:
                hay_t = True
            if hay_t and i == "b":
                hay_tb = True
    return pal


# Menu de opciones
def menu():
    print("1-Generar archivo binario con registros")
    print("2-Mostrar los datos del archivo generado")
    print("3-Generar arreglo cuyos montos a abonar sea mayor a un valor p")
    print("4-Mostrar los datos del punto 3 ordenados por identificacion")
    print("5-Buscar en el arreglo un plan que el nombre coincida con el valor nom")
    print("6-Buscar en el arreglo una identificacion")
    print("7-Plan por cada una de las posibles combinaciones entre tipo de planes y rango de edades")
    print("8-Analisis de cadena")
    print("9-Salir")
    sep()
    op = validar_rango(1, 9, "Ingrese opcion del menu: ")
    return op


# Menu principal
def principal():
    cadena = ""
    v = []
    fd = "planes.dat"
    op = -1
    while op != 9:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            carga(fd, n)
            sep()
        elif op == 2:
            mostrar_archivo(fd)
            sep()
        elif op == 3:
            p = int(input("Ingrese el valor del monto: "))
            v = generar_arreglo(fd, p, v)
            sep()
        elif op == 4:
            v = ordenamientodirecto(v)
            mostrar(v)
            sep()
        elif op == 5:
            if len(v) != 0:
                nom = input("Ingrese nombre a buscar en el arreglo: ")
                res = busqueda_secuencial(v, nom)
                if res != -1:
                    print(v[res].descripcion)
                    cadena = v[res].descripcion
                else:
                    print("No existe")
            else:
                print("Debe grabar datos en el vector!!")
            sep()
        elif op == 6:
            k = int(input("Ingrese id a buscar: "))
            res = busqueda_secuencial1(v, k)
            if res != -1:
                to_string(v[res])
            else:
                print("No se ha encontrado la identificacion ingresada...!")
            sep()
        elif op == 7:
            matriz = crear_matriz(fd)
            mostrar_matriz(matriz)
            sep()
        elif op == 8:
            if len(cadena) == 0:
                print("Debe generar la cadena en el punto 5")
            else:
                cant_pal = analisis_cadena(cadena)
                print("La cantidad de palabras que cumple con la condicion son: " + str(cant_pal))
            sep()
        elif op == 9:
            print("Gracias por utilizar el programa!")
            sep()


# Script princial...
if __name__ == '__main__':
    principal()
