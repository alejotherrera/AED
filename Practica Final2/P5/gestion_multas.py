import random, os, pickle, io, string
from multas import *


def sep():
    print("=" * 60)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


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
    for i in range(n):
        id = random.randint(1, 100)
        patente = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + random.choice(
            string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
        tipo = random.randint(0, 24)
        importe = random.randint(1, 10000)
        new = Multas(id, patente, tipo, importe)
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
    print("1-Carga de datos")
    print("2-Mostrar datos a razon de uno por linea")
    print("3-Crear otro arreglo cuyo monto a pagar es mayor al promedio")
    print("4-Mostrar arregnlo anterior")
    print("5-Buscar en el arreglo una multa por id e incrementar 10%")
    print("6-Matriz de conteo")
    print("7-Grabar archivo")
    print("8-Mostrar archivo")
    print("9-Salir")
    sep()
    op = validar_rango(1, 9, "Ingrese opcion del menu: ")
    return op


def punto3(v):
    n = len(v)
    prom = 0
    for i in range(n):
        prom += v[i].importe
    prom = prom / n
    v2 = []
    for i in range(len(v)):
        if v[i].importe > prom:
            v2.append(v[i])
    return v2


def buscar_id(v, x):
    for i in range(len(v)):
        if v[i].id == x:
            return i
    return -1


def crear_matriz(v):
    matriz = [0] * 25
    for i in v:
        f = i.tipo
        matriz[f] += i.importe
    return matriz


def mostrar_matriz(v, matriz):
    for i in v:
        f = i.tipo
        print("La cantidad de importe por tipo ", f, " son: ", matriz[f])


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


def principal():
    v = []
    fd = "vector.dat"
    op = -1
    while op != 9:
        op = menu()
        if op == 1:
            n = int(input("Ingrese cantidad de multas a cargar: "))
            v = carga(v, n)
            print("Multas cargadas con exito!")
            sep()
        elif op == 2:
            if len(v) != 0:
                mostrar(v)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 3:
            if len(v) != 0:
                v2 = punto3(v)
                print("Arreglo por promedio generado")
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 4:
            if len(v) != 0:
                mostrar(v2)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 5:
            if len(v) != 0:
                x = int(input("Ingrese id a buscar: "))
                res = buscar_id(v, x)
                if res != -1:
                    print("Importe anterior: ",v[res].importe)
                    v[res].importe = v[res].importe + v[res].importe * 10 / 100
                    print("Importe incrementado!")
                    to_string(v[res])
                else:
                    print("No existe el id ingresado")
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 6:
            if len(v) != 0:
                matriz = crear_matriz(v)
                print("Matriz generada!!!")
                print("Mostrando matriz...")
                mostrar_matriz(v, matriz)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 7:
            crear_archivo(v, fd)
            sep()
        elif op == 8:
            mostrar_archivo(fd)
            sep()
        elif op == 9:
            print("Gracias por utilizar el programa!")
            sep()


# Script princial...
if __name__ == '__main__':
    principal()
