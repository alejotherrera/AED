# Modulos5

import random, os, pickle
from registros5 import *


def sep():
    print("-" * 30)


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


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


# Carga del vector--------------
def carga(v, n):
    nombres = ("cobre", "plomo", "zinc", "estaño", "hierro", "manganeso", "molibdeno", "cobalto",
               "tungsteno", "titanio", "cromo", "oro", "plata", "platino", "plutonio", "uranio", "radio",
               "torio", "mairene", "potasio ", "yodo  ", "carbonato ", "cloruro", "sulfato",
               "dolomita")
    for i in range(n):
        id = random.randint(10, 10000)
        descripcion = random.choice(nombres)
        tipo = random.randint(0, 14)
        calidad = random.randint(0, 4)
        precio = random.randint(10, 99999)
        new = ProductoServicio(id, descripcion, tipo, calidad, precio)
        v.append(new)
    return v


# ----------------------------

def ordenamiento_directo(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].id > v[j].id:
                v[i], v[j] = v[j], v[i]
    return v


# Archivo--------------
def crear_archivo(v, fd):
    m = open(fd, "wb")
    n = len(v)
    for i in range(n):
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


# --------------------

#Punto 4
def nuevo_arreglo(v,v2):
    n = len(v)
    for i in range(n):
        if v[i].tipo < 10:
            id = v[i].id
            descripcion = v[i].descripcion
            tipo = v[i].tipo
            calidad = v[i].calidad
            precio = v[i].precio
            new = ProductoServicio(id, descripcion, tipo, calidad, precio)
            v2.append(new)
    print("Vector creado!")
    return v2


def mostar_segunp(v2,x):
    n = len(v2)
    for i in range(n):
        if v2[i].precio <= x:
            to_string(v2[i])

def menu():
    print("-------------------MENU-------------------")
    print("1-Cargar producto/servicios")
    print("2-Mostrar vector a partir de id")
    print("3-Generar otro arreglo tipo mejor a 10")
    print("4-Mostrar nuevo arreglo")
    print("5-Mostrar los datos cuyo precio sea menor o igual a un valor p")
    print("6-Grabar archivo del segundo arreglo")
    print("7-Mostrar archivo")
    print("8-Salir")
    sep()
    op = validar_rango(1, 8, "Ingrese opcion del menu: ")
    return op
