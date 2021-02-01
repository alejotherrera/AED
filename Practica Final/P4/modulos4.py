# Modulos
import random, os, pickle, string
from registros4 import *


# Punto1(Carga del vector)
def carga(v, n):
    lugares = ("Autopista Carlos Paz.", "Cordoba acceso norte.", "Cordoba acceso sur.",
               "Cordoba acceso este.", "Cordoba acceso oeste.", "Cordoba centro.", "Villa Maria.",
               "Barrio Guemes.", "Nueva Cordoba.")

    for i in range(n):
        id = random.randint(100, 100000)
        nombre = random.choice(lugares)
        monto = random.randint(100, 100000)
        patente = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + random.choice(
            string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
        hora = random.randint(0, 23)
        new = Cobro(id, nombre, monto, patente, hora)
        v.append(new)
    return v


# ------------------------
# Separador grafico
def sep():
    print("-" * 30)


# ------------------------

# Mostrar vector segun COBRO
def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


# Mostrar vector segun Condicion
def mostrar_condicion(v, condicion):
    n = len(v)
    for i in range(n):
        if v[i].monto < condicion:
            to_string(v[i])


# ------------------------

# Ordenamiento del vector
def ordenamientodirecto(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].id > v[j].id:
                v[i], v[j] = v[j], v[i]
    return v


# ------------------------


# Validate pos and number
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


# ------------------------

# Punto4(Crear Matriz)
def crear_matriz(v):
    n = len(v)
    matriz = [[0] * 23 for i in range(2)]
    for i in v:
        c = i.hora
        matriz[c] += i.monto
    return matriz


def mostrar_matriz(matriz):
    print()
    for i in range(len(matriz)):
        if 0 < i < 6 or 20 < i < 23:
            print("En la hora: ", i, " se recaudo: ", matriz[i])


# ------------------------

# Crear y mostrar archivo
def crear_archivo(v, fd, x):
    m = open(fd, "wb")
    n = len(v)
    for i in range(n):
        if v[i].nombre == x:
            pickle.dump(v[i], m)
    print("Archivo generado!")
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo no existe, generelo con el punto anterior")
        return

    m = open(fd, "rb")
    tamaño = os.path.getsize(fd)
    print("Datos del archivo: ")
    while m.tell() < tamaño:
        a = pickle.load(m)
        to_string(a)
    m.close()


# Busqueda secuencial-----
def busqueda_secuencial(v, p, h):
    n = len(v)
    for i in range(n):
        if v[i].patente == p and v[i].hora == h:
            return i
    return -1


# ------------------------

# analisis de cadena
def cadena(cad):
    mayus = string.ascii_uppercase
    pal_mayus = 0
    flag_mayus = False
    for i in range(len(cad)):
        if cad[i] == " " or cad[i] == ".":
            if flag_mayus:
                print(cad[i])
                pal_mayus += 1
            flag_mayus = False
        else:
            if cad[i] in mayus:
                flag_mayus = True

    print()


# ------------------------

# Menu de opciones
def menu():
    print("1-Cargar vector")
    print("2-Mostrar arreglo generado")
    print("3-Mostrar listado ordenado por id segun menor ingresado")
    print("4-Generar matriz")
    print("5-Generar binario con cobros que se hicieron desde un puesto de cobro cuyo id es ingresado")
    print("6-Mostrar archivo binario generado")
    print("7-Ingresar patente y hora ingresados por parametro")
    print("8-Analisis de cadena")
    print("9-Salir")
    sep()
    op = validar_rango(1, 9, "Ingrese opcion del menu: ")
    return op
# ------------------------
