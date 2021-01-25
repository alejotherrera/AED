# Modulos

import random, os, pickle
from Parcial5.registros import *


def add_in_order(v, nuevo):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].codigo == nuevo.codigo:
            pos = c
            break
        if nuevo.codigo < v[c].codigo:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [nuevo]


def sep():
    print("-" * 68)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def carga(v, n):
    descripciones = ("muebles", "sillas", "cama", "lavarropas", "computadoras", "escritorio", "ventilador", "puerta",
                     "paquetes", "teclado", "mouse", "sillones", "monitor", "vajillas", "televisor", "cocina",
                     "inodoro",
                     "lavamanos", "espejo", "cepillos", "cepillos", "metales", "minerales",
                     "mesita de luz", "biblioteca")
    for i in range(n):
        codigo = random.randint(1, 100)
        descripcion = random.choice(descripciones)
        destino = random.randint(1, 25)
        tipo = random.randint(0, 9)
        precio = round(random.uniform(100, 10000), 2)
        pagos = random.randint(1, 5)
        new = Envios(codigo, descripcion, destino, tipo, precio, pagos)
        v.append(new)
    return v


def ordenamientodirecto(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]
    return v


def validar_pos(a):
    n = a
    while n <= a:
        n = int(input("Ingrese valor n a cargar en el arreglo(mayor a " + str(a) + "): "))
        if n <= a:
            print("Error ingrese un valor mayor a: ", a)
    return n


def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while inf > n or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Error... opcion invalida, ingrese entre" + str(inf) + " y " + str(sup))
    return n


def crear_archivo(v, fd, x):
    m = open(fd, "wb")
    n = len(v)
    contador = 0
    for i in range(n):
        if v[i].pagos == 1 or v[i].pagos == 3 or v[i].pagos == 5:
            pickle.dump(v[i], m)
            contador += 1
    print("Archivo generado!")
    m.close()
    return contador


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


def punto3(v):
    vector_ordenado = []
    cont_precios = 0
    acumulador_precio = 0
    for i in range(len(v)):
        cont_precios += 1
        acumulador_precio += v[i].precio
    promedio_precios = round((acumulador_precio / cont_precios), 2)
    print("Datos segun el precio: ", promedio_precios)

    for i in range(len(v)):
        if v[i].precio > promedio_precios:
            vector_ordenado.append(v[i])

    vector_ordenado = ordenamientodirecto(vector_ordenado)
    mostrar(vector_ordenado)



def menu():
    print("--------------------------------MENU--------------------------------")
    print("1-Carga de datos")
    print("2-Mostrar vector anterior")
    print("3-Mostrar segun promedio de precios y ordenado por codigo")
    print("4-Crear matriz")
    print("5-Manipular matriz")
    print("6-Crear archivo")
    print("7-Mostrar archivo")
    print("8-Salir")
    sep()
    op = validar_rango(1, 8, "Ingrese opcion del menu: ")
    return op



