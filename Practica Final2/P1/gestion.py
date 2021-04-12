import random, os, pickle, io
from medicamento import *


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


def sep():
    print("=" * 55)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def carga(v, n):
    descripciones = (
        "Posible vacuna contra el MALDITO1 COVID-19", "Posibe cura para el cancer", "Cura para discpacidad",
        "Medicamento para el cancer", "Jarabe para la ultratos")
    directores = ("jorge", "alejo", "alejandra", "valerio", "carlos", "martin", "julian", "camila")
    for i in range(n):
        id = random.randint(1, 1000)
        descripcion = random.choice(descripciones)
        director = random.choice(directores)
        monto = random.randint(100, 10000)
        tipo = random.randint(1, 30)
        avales = random.randint(0, 9)
        nuevo = Medicamento(id, descripcion, director, monto, tipo, avales)
        add_in_order(v, nuevo)
    return v


# Validaciones
def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while inf > n or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Error... opcion invalida, ingrese entre " + str(inf) + " y " + str(sup))
    return n


def validar_pos(a):
    n = a
    while n <= a:
        n = int(input("Ingrese valor n a cargar en el arreglo(mayor a " + str(a) + "):"))
        if n <= a:
            print("Error ingrese un valor mayor a:", a)
    return n


# archivos
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


# Busquedas--------------------

def busqueda_secuencial(v, director):
    for i in range(len(v)):
        if v[i].director == director:
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


# matriz
def crear_matriz(vector):
    matriz = [[0] * 30 for i in range(10)]
    n = len(vector)
    for i in vector:
        col = i.tipo
        fil = i.avales
        matriz[fil][col] += i.monto
    return matriz


def mostrar_matriz(matriz, v, m):
    print()
    for i in v:
        c = i.tipo
        f = i.avales
        if matriz[f][c] > m:
            print("El monto acumulado con tipo ", c, " y avales ", f, " es: $", matriz[f][c])
        print()


# Cadena
def analisis_cadena(cadena):
    tam = len(cadena)
    contm = 0
    contd = 0
    mayus = "ÁÉÍÓÚ"
    for i in range(tam):
        if cadena[i] != " " or cadena[i] != ".":
            if cadena[i].isdigit():
                contd += 1
            elif "A" <= cadena[i] <= "Z" or cadena[i] in mayus:
                contm += 1
    print("Cantidad de digitos: ", contd)
    print("Cantidad de mayusculas: ", contm)


def analisis_cadena(cadena):
    cont_mayus = cont_digitos = 0
    mayus = "ÁÉÍÓÚ"
    for i in cadena:
        if i != " " or i != ".":
            if i.isdigit():
                cont_digitos += 1
            elif "A" <= i <= "Z" or i in mayus:
                cont_mayus += 1
    print("Cantidad de digitos: ",cont_digitos)
    print("Cantidad de mayusculas: ",cont_mayus)


def agregar_medicamento(v, id):
    descripciones = (
        "Posible vacuna contra el MALDITO1 COVID-19", "Posibe cura para el cancer", "Cura para discpacidad",
        "Medicamento para el cancer", "Jarabe para la ultratos")
    directores = ("jorge", "alejo", "alejandra", "valerio", "carlos", "martin", "julian", "camila")
    for i in range(1):
        id = id
        descripcion = random.choice(descripciones)
        director = random.choice(directores)
        monto = random.randint(100, 10000)
        tipo = random.randint(1, 30)
        avales = random.randint(0, 9)
        nuevo = Medicamento(id, descripcion, director, monto, tipo, avales)
        add_in_order(v, nuevo)
    return v


# Menu de opciones
def menu():
    print("=========Bienvendios a la gestion de medicamento========")
    print("1-Carga de datos")
    print("2-Mostrar arreglo creado")
    print("3-Buscar un director cargado por teclado")
    print("4-Buscar por id")
    print("5-Matriz de conteo")
    print("6-Crear archivo binario")
    print("7-Mostrar archivo binario")
    print("8-Analizar cadena")
    print("9-Salir")
    sep()
    op = validar_rango(1, 9, "Ingrese opcion del menu: ")
    return op


# Opciones
def principal():
    v = []
    fd = "vector.dat"
    cadena = ""
    op = -1
    while op != 9:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            v = carga(v, n)
            print("Arreglo cargado con exito...!")
            sep()
        elif op == 2:
            if len(v) != 0:
                mostrar(v)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 3:
            if len(v) != 0:
                dir = input("Ingrese director a buscar: ")
                res = busqueda_secuencial(v, dir)
                if res != -1:
                    print("Descripcion: ", v[res].descripcion)
                    cadena = v[res].descripcion
                else:
                    print("No existe")
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 4:
            if len(v) != 0:
                id = int(input("Ingrese id a buscar: "))
                res = binary_search(v, id)
                if res != -1:
                    to_string(v[res])
                    print()
                else:
                    v = agregar_medicamento(v, id)
                    print("Medicamento no encontrado, el mismo fue cargado con exito...!")
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 5:
            if len(v) != 0:
                matriz = crear_matriz(v)
                print("matriz: ")
                filtro = int(input("Ingrese valor m a filtrar: "))
                mostrar_matriz(matriz, v, filtro)
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
            if len(cadena) != 0:
                analisis_cadena(cadena)
            else:
                print("Debe consultar un director primero(opcion 3)")
            sep()
        elif op == 9:
            print("Gracias por utilizar el programa!")
            sep()


# Script princial...
if __name__ == '__main__':
    principal()
