from Parcial4Modulos import *
from Parcial4Principal import *

import pickle
import os
import random


class Mineral:
    def __init__(self, codigo, peso, descripcion, volumen):
        self.codigo = codigo
        self.peso = peso
        self.descripcion = descripcion
        self.volumen = volumen


def to_string(v):
    r = ""
    r += "{:<20}".format("Codigo: " + str(v.codigo))
    r += "{:<20}".format("peso: " + str(v.peso))
    r += "{:<25}".format("descripcion: " + str(v.descripcion))
    r += "{:<25}".format("volumen: " + str(v.volumen))
    print()
    print(r)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def sep():
    print("-" * 30)


def validar_pos(a):
    n = a
    while n <= a:
        n = int(input("Ingrese valor(mayor a " + str(a) + "):"))
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
    print("1-Carga de datos")
    print("2-Mostrar datos anteriores cargados")
    print("3-Mostrar registros en un rango de peso")
    print("4-Generar matriz")
    print("5-Generar archivo con volumen mayor a x")
    print("6-Mostrar archivo")
    print("7-Salir")
    op = validar_rango(1, 7, "Ingrese opcion del menu(entre 1 y 7): ")
    return op


def add_in_order(v, nuevo):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].descripcion == nuevo.descripcion:
            pos = c
        if nuevo.descripcion < v[c].descripcion:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [nuevo]


def crear_archivo(v, fd, x):
    m = open(fd, "wb")
    n = len(v)
    for i in range(n):
        if v[i].volumen > x:
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


def carga_datos(v, n):
    descripciones = ("cobre", "plomo", "zinc", "estaño", "hierro", "manganeso", "molibdeno", "cobalto",
                     "tungsteno", "titanio", "cromo", "oro", "plata", "platino", "plutonio", "uranio", "radio",
                     "torio", "mairene", "potasio ", "yodo  ", "carbonato ", "cloruro", "sulfato",
                     "dolomita")
    for i in range(n):
        codigo = random.randint(1, 1000)
        peso = random.randint(1, 10)
        descripcion = random.choice(descripciones)
        volumen = random.randint(1, 20)
        new = Mineral(codigo, peso, descripcion, volumen)
        add_in_order(v, new)
    return v


def rango3(v, inf, sup):
    n = len(v)
    for i in range(n):
        if (inf <= v[i].peso and v[i].peso <= sup):
            to_string(v[i])
    return


def matriz(v):
    n = 10
    m = 20
    matriz = [[0] * m for f in range(n)]
    for i in v:
        fila = i.peso
        col = i.volumen
        matriz[fila][col] += 1
    return matriz


def escribir_matriz(matriz):
    print("Datos de la matriz")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                print("Cantidad de peso:", i, " volumen:", j, "Cantidad total:", matriz[i][j])
