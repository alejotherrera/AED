from Cobro import *
import random, os, pickle, io, string


def sep():
    print("=" * 30)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def carga(v, n):
    lugares = ("Autopista Carlos Paz.", "Cordoba acceso norte.", "Cordoba acceso sur.",
               "Cordoba acceso este.", "Cordoba acceso oeste.", "Cordoba centro.", "Villa Maria.",
               "Barrio Guemes.", "Nueva Cordoba.")
    for i in range(n):
        id = random.randint(100, 100000)
        nombre = random.choice(lugares)
        monto = random.randint(100, 100000)
        patente = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + random.choice(
            string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
        hora = random.randint(0, 23)
        new = Cobro(id, nombre, monto, patente, hora)
        v.append(new)
    return v


# Ordenamientos
def punto3(v, m):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].id > v[j].id:
                v[i], v[j] = v[j], v[i]
    print("Arreglo ordenado... mostrando cobros...")
    for i in range(n):
        if v[i].monto < m:
            to_string(v[i])


def menu():
    print("1-Generar arreglo")
    print("2-Mostrar arreglo")
    print("3-Ordenado por id e import menor a m")
    print("4-Matriz de conteo")
    print("5-Generar archivo binario apartir de un puesto")
    print("6-Mostrar archivo")
    print("7-Buscar patente, a una determinada hora")
    print("8-Analisis de cadena")
    print("9-Salir")
    sep()
    op = validar_rango(1, 9, "Ingrese opcion del menu: ")
    return op


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


def crear_archivo(v, fd, x):
    m = open(fd, "wb")
    n = len(v)
    for i in range(n):
        if v[i].puesto == x:
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


def busqueda_secuencial(v, p, h):
    for i in range(len(v)):
        if v[i].domino == p and v[i].hora == h:
            return i
    return -1


def crear_matriz(v):
    matriz = [0] * 24
    for i in v:
        fil = i.hora
        matriz[fil] += i.monto
    return matriz
    print("Matriz generada!")


def mostrar_matriz(matriz, v):
    print()
    for i in v:
        fil = i.hora
        if matriz[fil] > 0:
            if 20 <= i.hora <= 23 or 0 <= i.hora <= 6:
                print("En la hora " + str(fil) + " se recaudo: " + str(matriz[fil]))

def analisis_cadena(cadena):
    letras = "abcdefghijkmñlopqrstuvwxyzaeiouáéíóú"
    mayus = letras.upper()
    cont = 0
    hay_mayus = False
    for i in cadena:
        if i == " " or i == ".":
            if hay_mayus:
                cont += 1
            hay_mayus = False
        else:
            if i in mayus:
                hay_mayus = True
    print("La cantidad de palabras ",cont)


def principal():
    v = []
    fd = "vector.dat"
    op = -1
    while op != 9:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            v = carga(v, n)
            print("Cobros cargados con exito!")
            sep()
        elif op == 2:
            if len(v) != 0:
                mostrar(v)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 3:
            if len(v) != 0:
                m = float(input("Ingrese valor m a filtrar: "))
                punto3(v, m)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 4:
            if len(v) != 0:
                matriz = crear_matriz(v)
                print("Datos de la matriz: ")
                mostrar_matriz(matriz, v)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 5:
            if len(v) != 0:
                puesto = input("Ingrese puesto a guardar en el archivo: ")
                crear_archivo(v, fd, puesto)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 6:
            mostrar_archivo(fd)
        elif op == 7:
            if len(v) != 0:
                p = input("Ingrese patente a buscar: ")
                h = int(input("Ingrese hora a buscar: "))
                res = busqueda_secuencial(v, p, h)
                if res != -1:
                    print("El puesto que se registro fue: ", v[res].puesto)
                    cadena = v[res].puesto
                else:
                    print("No se ha encontrado el cobro ingresado...!")
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 8:
            analisis_cadena(cadena)
            sep()
        elif op == 9:
            print("Gracias por utilizar el programa!")
            sep()


# Script princial...
if __name__ == '__main__':
    principal()
