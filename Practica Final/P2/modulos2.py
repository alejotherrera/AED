import random, os, pickle

from registros2 import *


# Modulos

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


def carga(v, n):
    nombres = ("COBRÉ1", "PLOMO1234", "zinc4", "ÉSTAÑO5", "HIERRO51", "manganeso5", "1m2olibdeno5", "cobalto",
               "tungste3no", "titan4567io", "cromo", "oro", "plata", "platino", "plutonio", "uranio", "radio",
               "torio", "mairene", "potasio ", "yodo  ", "carbonato ", "cloruro", "sulfato",
               "dolomita")
    letras = "abcdefghijkmñlopqrstuvwxyzaeiou"
    numeros = "1234567890"
    nombres1 = ("Bruno", "Mariel", "Bianca", "Juan Cruz", "Jorge", "Antonela", "Josefina", "Lea",
                "Aylen", "Exequiel", "Lilith", "Lou", "Luz", "Lautaro", "Tomas", "Azul", "Cecilia",
                "Agustin", "Mairene", "Angelo", "Angela", "Celeste", "Karen", "Ludmila", "Francisca")
    for i in range(n):
        id = random.choice(letras) + random.choice(letras) + random.choice(numeros) + random.choice(numeros)
        descripcion = random.choice(nombres)
        nombre = random.choice(nombres1)
        monto = random.randint(100, 9999999)
        tipo = random.randint(1, 30)
        avales = random.randint(0, 9)
        new = Medicamento(id, descripcion, nombre, monto, tipo, avales)
        add_in_order(v, new)
    return v


def agregar_medicamento(v, k):
    nombres = ("cobre1", "plomo3", "zinc4", "estaño5", "hierro5", "manganeso5", "1m2olibdeno5", "cobalto",
               "tungsteno", "titanio", "cromo", "oro", "plata", "platino", "plutonio", "uranio", "radio",
               "torio", "mairene", "potasio ", "yodo  ", "carbonato ", "cloruro", "sulfato",
               "dolomita")
    nombres1 = ("Bruno", "Mariel", "Bianca", "Juan Cruz", "Jorge", "Antonela", "Josefina", "Lea",
                "Aylen", "Exequiel", "Lilith", "Lou", "Luz", "Lautaro", "Tomas", "Azul", "Cecilia",
                "Agustin", "Mairene", "Angelo", "Angela", "Celeste", "Karen", "Ludmila", "Francisca")
    for i in range(1):
        id = k
        descripcion = random.choice(nombres)
        nombre = random.choice(nombres1)
        monto = random.randint(100, 9999999)
        tipo = random.randint(1, 30)
        avales = random.randint(0, 9)
        new = Medicamento(id, descripcion, nombre, monto, tipo, avales)
        add_in_order(v, new)
    return v


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


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


def sep():
    print("-" * 30)


def busqueda_secuencial(v, nom):
    for i in range(len(v)):
        if v[i].nombre == nom:
            return v[i].descripcion
    return "No existe"


def busqueda_secuencial2(v, nom):
    for i in range(len(v)):
        if v[i].id == nom:
            return i
    return -1


def crear_archivo(v, fd):
    m = open(fd, "wb")
    n = len(v)
    for i in range(n):

        a = len(v[i].descripcion)
        if a <= 25 and v[i].tipo != 10 and v[i].tipo != 15:
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


def analisis_cadena(cadena):
    tam = len(cadena)
    contm = 0
    contd = 0
    mayus = "ÁÉÍÓÚ"
    for i in range(tam):
        if cadena[i] != " " or cadena[i] != ".":
            if cadena[i].isdigit():
                contd += 1
            elif cadena[i] >= "A" and cadena[i] <= "Z" or cadena[i] in mayus:
                contm += 1
    print("Cantidad de digitos: ", contd)
    print("Cantidad de mayusculas: ", contm)


def menu():
    print("1-Cargar vector")
    print("2-Mostrar vector generado")
    print("3-Buscar nombre del director")
    print("4-Buscar por clave de id")
    print("5-Matriz")
    print("6-Crear archivo binario")
    print("7-Mostrar archivo binario")
    print("8-Analizar cadena del punto 3")
    print("9-Salir")
    sep()
    op = validar_rango(1, 9, "Ingrese opcion del menu: ")
    return op
