__author__ = "Alejo Herrera/85969/1k04"

from registros import *
import random, pickle


# MODULOS/PROCESOS


# Utilidades
def sep():
    print("-" * 50)


# Validaciones
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


# Carga de datos
def carga(v, n, fd):
    m = open(fd, "ab")
    nombres = ("alejo", "alejandra", "valerio", "jessica", "sofia", "julian", "camila", "jorge", "carlos", "dario")
    planes = (
        "plan progresar.", "plan amigos.", "plan estudiar.", "plan aed.", "plan trabajar.")
    for i in range(n):
        id = random.randint(10, 1000)
        nombre = random.choice(nombres)
        descripcion = random.choice(planes)
        monto = random.randint(1000, 100000)
        plan = random.randint(1, 10)
        rango = random.randint(1, 5)
        new = Plan(id, nombre, descripcion, monto, plan, rango)
        crear_archivo(new, m)
        v.append(new)
    return v
    m.close()


# Mostrar a razon de una linea por pantalla
def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


# Busquedas secuenciales
def busqueda_secuencial(v, x):
    for i in range(len(v)):
        if v[i].nombre == x:
            return i
    return -1


def busqueda_secuencial2(v, x):
    for i in range(len(v)):
        if v[i].id == x:
            return i
    return -1


# Ordenamiento
def ordenamientodirecto(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].id > v[j].id:
                v[i], v[j] = v[j], v[i]
    return v


# Punto 3(MAYOR A P)
def punto3(v, v2, p):
    n = len(v)
    for i in range(n):
        if v[i].monto > p:
            v2.append(v[i])
    return v2


# Manipulacion de archivos
def crear_archivo(v, m):
    pickle.dump(v, m)


# Punto7(Crear Matriz) PENDIENTE
def crear_matriz(v):
    n = len(v)
    matriz = [[0] * 10 for filas in range(5)]
    for i in v:
        filas = i.plan
        columnas = i.rango
        matriz[filas][columnas] += 1
    return matriz


def mostrar_matriz(matriz):
    n = len(matriz)
    m = len(matriz[0])
    for i in range(n):
        for j in range(m):
            if matriz[i][j] != 0:
                print("Combinacion en cada tipo de plan con cada tipo de edad: " + str(matriz[i][j]))


# Manipulacion de cadena de caracter
def punto8(cadena):
    letras = "abcdefghijkmñlopqrstuvwxyzaeiouáéíóú"
    cont = cant_pal4 = 0
    flag_t = hay_tb = False
    for i in cadena:
        if i in letras:
            cont += 1
            if i in "t":
                flag_t = True
            elif flag_t:
                if i in "b":
                    hay_tb = True
        else:
            if cont >= 4 and hay_tb:
                cant_pal4 += 1
            cont = 0
            flag_t = hay_tb = False
    return cant_pal4


# Menu print
def menu():
    print("                 MENU DE OPCIONES                 ")
    print("1-Carga de datos: ")
    print("2-Mostrar datos a razon de un registro por linea")
    print("3-Generar arreglo que contenga planes cuyo monto a abonar sea mayor a un valor p")
    print("4-Mostrar los datos del arreglo anterior unidimensional creado en el punto 3")
    print("5-Buscar un plan a partir de un valor nombre ingresado por parametro")
    print("6-Buscar identificacion a partir de un valor k ingresado por parametro")
    print("7-Matriz de conteo")
    print("8-Analisis de cadena")
    print("9-salir")
    sep()
    op = validar_rango(1, 9, "Ingrese opcion del menu: ")
    return op
