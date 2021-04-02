from registro7 import *
import random, pickle, os


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
    print("-" * 30)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def carga(v, n):
    nombres = ("Ploae", "cobre", "plomo", "zinc", "estaño", "hierro", "manganeso", "molibdeno", "cobalto",
               "tungsteno", "titanio", "cromo", "oro", "Plata", "Platino", "Plutonio", "uranio", "radio",
               "torio", "Poaeou", "potasio ", "yodo  ", "carbonato ", "cloruro", "sulfato",
               "dolomita")
    for i in range(n):
        codigo = random.randint(10, 1000)
        descripcion = random.choice(nombres)
        costo = random.randint(100, 10000)
        ciudad = random.randint(0, 24)
        destino = random.randint(0, 19)
        new = Paquetes(codigo, descripcion, costo, ciudad, destino)
        add_in_order(v, new)
    return v


def punto3(v, v2):
    voc = cons = 0
    flag = False
    n = len(v)
    for i in range(n):
        cadena = str(v[i].descripcion)
        for j in cadena:
            if j in "aeiouAEIOU":
                voc += 1
            else:
                cons += 1
        if voc > cons and cadena[0] == "P":
            codigo = v[i].codigo
            descripcion = v[i].descripcion
            costo = v[i].costo
            ciudad = v[i].ciudad
            destino = v[i].destino
            new = Paquetes(codigo, descripcion, costo, ciudad, destino)
            v2.append(new)
        voc = cons = 0
    return v2


def binary_search(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c].codigo:
            return c
        if x < v[c].codigo:
            der = c - 1
        else:
            izq = c + 1
    return -1


def busqueda_secuencial(v, nom):
    for i in range(len(v)):
        if v[i].costo > nom:
            return i
    return -1


def crear_archivo(v, fd):
    m = open(fd, "wb")
    n = len(v)
    for i in range(n):
        if v[i].destino != 5 and v[i].destino != 15:
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
    print("1-Carga de datos")
    print("2-Mostrar arreglo creado")
    print("3-Generar segundo arreglo segun cadena")
    print("4-Mostrar ese nuevo arreglo")
    print("5-Matriz")
    print("6-Buscar paquete por codigo x")
    print("7-Buscar paquete segun mayor a x ingreso por parametro del punto 3")
    print("8-Crear archivo sin destino 5 y 15")
    print("9-Mostrar archivo")
    print("10-Salir")
    sep()
    op = validar_rango(1, 10, "Ingrese opcion del menu: ")
    return op
