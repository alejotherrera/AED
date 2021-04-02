import random, os, pickle
from registros6 import *


def add_in_order(v, nuevo):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].id == nuevo.id:
            pos = c
            break
        if nuevo.id < v[c].id:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [nuevo]


def sep():
    print("-" * 30)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def carga(v, n):
    nombres = ("cobre", "plomo", "zinc", "estaño", "hierro", "manganeso", "molibdeno", "cobalto",
               "tungsteno", "titanio", "cromo", "oro", "plata", "platino", "plutonio", "uranio", "radio",
               "torio", "mairene", "potasio ", "yodo  ", "carbonato ", "cloruro", "sulfato",
               "dolomita")
    for i in range(n):
        id = random.randint(10, 1000)
        nombre = random.choice(nombres)
        importe = random.randint(1000, 100000)
        destino = random.randint(0, 22)
        pago = random.randint(0, 4)
        new = Trabajos(id, nombre, importe, destino, pago)
        add_in_order(v, new)
    return v


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


def menu():
    print("1-Cargar n registros ordenado por ")
    print("2-Mostrar el arreglo creado")
    print("3-Buscar en el arreglo un nombre")
    print("4-Crear archivo pago 0 e importe entre a y b")
    print("5-Mostrar el archivo creado")
    print("6-Salir")
    sep()
    op = validar_rango(1, 6, "Ingrese opcion del menu: ")
    return op


def busqueda_secuencial(v, nom):
    for i in range(len(v)):
        if v[i].nombre == nom:
            return i
    return -1


def crear_archivo(v, fd, a, b):
    m = open(fd, "wb")
    n = len(v)
    for i in range(n):
        if a < v[i].importe < b and v[i].pago == 0:
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
