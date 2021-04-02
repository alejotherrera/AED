# Modulos

from registros3 import *
import os, pickle, random


# Visual
def sep():
    print("=" * 30)


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


# Creando Arreglo
def carga(v, n):
    descripciones = ("gas", "agua", "luz", "limpieza", "cloaca")
    nombres = ("julian", "camila", "carlos", "matias", "alejandra", "valerio")
    for i in range(n):
        id = random.randint(10, 1000)
        descripcion = random.choice(descripciones)
        nombre = random.choice(nombres)
        monto = random.randint(100, 1000)
        tipo = random.randint(0, 24)
        mecanismo = random.randint(0, 4)
        new = Servicio(id, descripcion, nombre, monto, tipo, mecanismo)
        v.append(new)
    return v


# Mostrar por pantalla a razon de una linea
def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def mostra2r(v):
    n = len(v)
    for i in range(n):
        to_string2(v[i])


# Ordenamientos
def ordenamientodirecto(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].nombre > v[j].nombre:
                v[i], v[j] = v[j], v[i]
    return v


def punto3(v):
    print()
    print("Listado de mecanismo 1 y 4")
    v = ordenamientodirecto(v)
    for i in range(len(v)):
        if v[i].mecanismo == 1 or v[i].mecanismo == 4:
            to_string(v[i])


# Busquedas
def busqueda_secuencial(v, nom):
    for i in range(len(v)):
        if v[i].id == nom:
            return i
    return -1


def crear_matriz(servicio):
    conteo = [[0] * 25 for f in range(5)]
    for i in servicio:
        c = i.tipo
        f = i.mecanismo
        conteo[f][c] += i.monto
    return conteo


def mostrar_matriz(conteo, servicio):
    print()
    for i in servicio:
        c = i.tipo
        f = i.mecanismo
        if conteo[f][c] > 0:
            print('El monto acomulado con tipo de servicio \t', c, ' \ty tipo de mecanismo de pago \t', f, ' es: ',
                  conteo[f][c])
    print()


def generar_archivofactura(conteo, servicio, fd):
    a = open(fd, "wb")
    for i in range(len(conteo)):
        tip = servicio[i].tipo
        mec = servicio[i].mecanismo
        mon = conteo[mec][tip]
        if conteo[mec][tip] > 0:
            m = Factura(mon, tip, mec)
            pickle.dump(m, a)
    print("Archivo creado!!")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo no existe, generelo...!")
        return

    m = open(fd, "rb")
    tamaño = os.path.getsize(fd)

    print("Datos del archivo: ")
    while m.tell() < tamaño:
        a = pickle.load(m)
        to_string2(a)
    m.close()


def analisis_cadena(cadena):
    hay_m = hay_mi = False
    pal_mi = 0
    for i in cadena:
        if i == " " or i == ".":
            if hay_mi:
                pal_mi += 1
            hay_mi = hay_m = False
        else:
            if i == "m" or i == "M":
                hay_m = True
            elif hay_m and i == "i":
                hay_mi = True
            else:
                hay_m = False
    return pal_mi


# Menu
def menu():
    print("1-Generar el arreglo de servicios")
    print("2-Mostrar arreglo generado")
    print("3-Mostrar listado cuyo mecanismo sea 1 o 4")
    print("4-Buscar un id ingresado por teclado")
    print("5-Cada posible combinacion de los posibles tipos por mecanismo de pago")
    print("6-Generar archivo binario a partir de FACTURA")
    print("7-Mostrar el archivo generado a razon de un registro por linea")
    print("8-Analisis de cadena")
    print("9-Salir")
    sep()
    op = validar_rango(1, 9, "Ingrese opcion del menu: ")
    return op
