import random, os, pickle, io
from servicio import *


# Grafico
def sep():
    print("=" * 60)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def carga(v, n):
    clientes = ("Bruno", "Mariel", "Bianca", "Juan Cruz", "Jorge", "Antonela", "Josefina", "Lea",
                "Aylen", "Exequiel", "Lilith", "Lou", "Luz", "Lautaro", "Tomas", "Azul", "Cecilia",
                "Agustin", "Mairene", "Angelo", "Angela", "Celeste", "Karen", "Ludmila", "Francisca")
    descripciones = ("gas", "agua", "luz", "limpieza", "cloaca")
    for i in range(n):
        id = random.randint(1, 1000)
        descripcion = random.choice(descripciones)
        cliente = random.choice(clientes)
        monto = random.randint(100, 10000)
        tipo = random.randint(0, 24)
        mecanismo = random.randint(0, 4)
        nuevo = Servicio(id, descripcion, cliente, monto, tipo, mecanismo)
        v.append(nuevo)
    return v


# Ordenamientos
def ordenamientodirecto(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].id > v[j].id:
                v[i], v[j] = v[j], v[i]
    return v


def ordenamientodirecto2(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].descripcion > v[j].descripcion:
                v[i], v[j] = v[j], v[i]
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
        if a.importe > 0:
            to_string2(a)
    m.close()


# Busquedas--------------------
def busqueda_secuencial(v, id):
    for i in range(len(v)):
        if v[i].id == id:
            return i
    return -1


# Punto 3
def listado_punto3(v):
    print("Listado ordenado...!")
    v = ordenamientodirecto2(v)
    print("Mecanismos 1 y 4")
    for i in range(len(v)):
        if v[i].mecanismo == 1 or v[i].mecanismo == 4:
            to_string(v[i])


def crear_matriz(v):
    matriz = [[0] * 25 for i in range(5)]
    for i in v:
        fila = i.mecanismo
        columna = i.tipo
        matriz[fila][columna] += i.monto
    return matriz


def mostrar_matriz(matriz, servicios):
    print()
    for i in servicios:
        c = i.tipo
        f = i.mecanismo
        if matriz[f][c] > 0:
            print('El monto acomulado con tipo de servicio \t', c, ' \ty tipo de mecanismo de pago \t', f, ' es: ',
                  matriz[f][c])
            print()


def generar_archivofactura(matriz, v, fd):
    a = open(fd, "w+b")
    for i in v:
        tipo = i.tipo
        mecanismo = i.mecanismo
        importe = matriz[mecanismo][tipo]
        if matriz[mecanismo][tipo] > 0:
            m = Factura(tipo, mecanismo, importe)
            pickle.dump(m, a)
    print("archivo creado!!")


def analisis_cadena(cadena):
    hay_m = hay_mi = False
    n = len(cadena)
    condicion = 0
    for i in range(n):
        if cadena[i] == " " or cadena[i] == ".":
            if hay_mi:
                condicion += 1
            hay_mi = hay_m = False
        else:
            if cadena[i] == "m" or cadena[i] == "M":
                hay_m = True
            elif hay_m and (cadena[i] == "i" or cadena[i] == "I"):
                if cadena[i - 1] == "m" or cadena[i - 1] == "M":
                    hay_mi = True
    print("La cantidad de palabras que tienen mi son: ", condicion)


def menu():
    print("1-Carga de datos")
    print("2-Mostrar datos por id")
    print("3-Mostrar listado ordeando por descripción y mecanismo 1 y 4")
    print("4-Buscar clave c")
    print("5-Matriz de conteo")
    print("6-Generar archivo binario con Factura")
    print("7-Mostar archivo")
    print("8-Analisis de cadena")
    print("9-Salir")
    sep()
    op = validar_rango(1, 9, "Ingrese opcion del menu: ")
    return op


def principal():
    print("=================BIENVENIDO=================")
    v = []
    fd = "vector.dat"
    op = -1
    while op != 9:
        op = menu()
        if op == 1:
            n = int(input("Ingrese cantidad de servicios a cargar: "))
            v = carga(v, n)
            print("Servicios cargados...!")
            sep()
        elif op == 2:
            if len(v) != 0:
                v = ordenamientodirecto(v)
                print("arrgelo ordenado...!")
                mostrar(v)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 3:
            if len(v) != 0:
                listado_punto3(v)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 4:
            if len(v) != 0:
                c = int(input("Ingrese id a buscar: "))
                res = busqueda_secuencial(v, c)
                if res != -1:
                    to_string(v[res])
                else:
                    print("No existe la clave en el arreglo...!")
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 5:
            if len(v) != 0:
                matriz = crear_matriz(v)
                print("Matriz: ")
                mostrar_matriz(matriz, v)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 6:
            print("Generando archivo...!")
            generar_archivofactura(matriz, v, fd)
            sep()
        elif op == 7:
            mostrar_archivo(fd)
            sep()
        elif op == 8:
            cadena = input("Ingrese el reclamo: ")
            analisis_cadena(cadena)
            sep()
        elif op == 9:
            print("Gracias por utilizar el programa!")
            sep()


# Script princial...
if __name__ == '__main__':
    principal()
