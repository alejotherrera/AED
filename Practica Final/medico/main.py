import random, os, pickle
from registros import *


def carga(v, n):
    medicamentos = ("COBRÉ1.", "PLOMO1234.", "zinc4.", "ÉSTAÑO5.", "HIERRO51.", "manganeso5", "1m2olibdeno5", "cobalto",
                    "Posible VACUNA1 contra el maldito COVID-19.", "titan4567io", "cromo", "oro", "plata", "platino", "plutonio", "uranio", "radio",
                    "torio", "mairene", "potasio ", "yodo  ", "carbonato ", "cloruro", "sulfato",
                    "dolomita")
    directores = ("Bruno", "Mariel", "Bianca", "Juan Cruz", "Jorge", "Antonela", "Josefina", "Lea",
                  "Aylen", "Exequiel", "Lilith", "Lou", "Luz", "Lautaro", "Tomas", "Azul", "Cecilia",
                  "Agustin", "Mairene", "Angelo", "Angela", "Celeste", "Karen", "Ludmila", "Francisca")
    idstr = ("A", "B", "C", "D", "E")
    for i in range(n):
        id = str(random.randint(1, 10)) + random.choice(idstr)
        descripcion = random.choice(medicamentos)
        director = random.choice(directores)
        monto = random.randint(100, 100000)
        tipo = random.randint(1, 30)
        avales = random.randint(0, 9)
        new = Medicamento(id, descripcion, director, monto, tipo, avales)
        add_in_order(v, new)
    return v


# Ordenamientos agregado
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


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def menu():
    print("1-Carga de datos")
    print("2-Mostrar arreglo a razon de una linea")
    print("3-Buscar en el arreglo un director")
    print("4-Buscar clave por id K")
    print("5-Matriz acumulacion")
    print("6-Generar archivo")
    print("7-Mostrar archivo")
    print("8-Analizar cadena")
    print("9-Salir")
    sep()
    op = validar_rango(1, 9, "Ingrese opcion del menu: ")
    return op


def sep():
    print("=" * 30)


# Validaciones
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


def busqueda_secuencial(v, nom):
    for i in range(len(v)):
        if v[i].director == nom:
            return i
    return -1


def binary_search(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c].id:
            return c
        if x < v[c].id:
            der = c - 1
        else:
            izq = c + 1
    return -1


def crear_matriz(v):
    conteo = [[0] * 30 for i in range(10)]
    for i in v:
        c = i.tipo
        f = i.avales
        conteo[f][c] += i.monto
    return conteo


def mostrar_matriz(conteo, v, m):
    print()
    for i in range(len(conteo)):
        for j in range(len(conteo[i])):
            if conteo[i][j] != 0:
                print("El monto acumulado con tipo ", i, " y avales ", j, " es: $", conteo[i][j])


# Manipulacion de archivos
def crear_archivo(v, fd):
    m = open(fd, "wb")
    n = len(v)
    for i in range(n):
        if v[i].descripcion >= 25 and v[i].tipo != 15 and v[i].tipo != 10:
            pickle.dump(v[i], m)
    print("Archivo generado!")
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo no existe, generelo con el punto anterior")
        return

    m = open(fd, "rb")
    tamano = os.path.getsize(fd)

    print("Datos del archivo: ")
    while m.tell() < tamano:
        a = pickle.load(m)
        if a.monto > 100000:
            to_string(a)
    m.close()


def extra(cadena):
    if len(cadena) <= 0:
        print("Primero debe generar la cadena en el punto 3")
        return

    letras = "abcdefghijkmñlopqrstuvwxyzaeiouáéíóú"
    mayus = letras.upper()
    rango = len(cadena)
    cumple_condicion = 0
    hay_min = hay_mayus = False
    hay_digito = 0
    for i in cadena:
        print(i)
        if i != " " and i != ".":
            if i in letras:
                hay_min = True
                print("mins", hay_min)
            if i in mayus:
                hay_mayus = True
                print("mayus", hay_mayus)
            if i.isdigit():
                hay_digito += 1
                print("digito", hay_digito)
        else:
            if (hay_min == False) and (hay_mayus == True) and (hay_digito >= 1):
                cumple_condicion += 1
                print("entra")

            hay_min = hay_mayus = False
            hay_digito = 0
    print("La cantidad de palabras que cumple de la cadena es: ", cumple_condicion)

def principal():
    v = []
    fd = "vector.dat"
    op = -1
    cadena = ""
    while op != 9:
        op = menu()
        if op == 1:
            n = int(input("Ingrese cantidad de medicamentos a cargar: "))
            v = carga(v, n)
            print("Vector cargado con exito!")
            sep()
        elif op == 2:
            if len(v) != 0:
                mostrar(v)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 3:
            if len(v) != 0:
                nom = input("Ingrese el directo: ")
                res = busqueda_secuencial(v, nom)
                if res != -1:
                    print(v[res].descripcion)
                    cadena = v[res].descripcion
                else:
                    print("No existe dicho director...")
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 4:
            if len(v) != 0:
                k = input("Ingrese el directo: ")
                res = binary_search(v, k)
                if res != -1:
                    to_string(v[res])
                else:
                    print("No existe dicho id...")
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 5:
            if len(v) != 0:
                matriz = crear_matriz(v)
                print("Matriz creada con exito!")
                m = int(input("Ingrese valor a filtrar: "))
                mostrar_matriz(matriz, v, m)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 6:
            crear_archivo(v, fd)
            sep()
        elif op == 7:
            mostrar_archivo(fd)
            sep()
        elif op == 8:
            extra(cadena)
            sep()
        elif op == 9:
            print("Gracias por utilizar el programa!")
            sep()


# Script princial...
if __name__ == '__main__':
    principal()
