import random
from Registros1 import *


# Modulos

def validar_pos(a):
    n = a
    while n <= a:
        n = int(input("Ingrese valor n a cargar en el arreglo(mayor a " + str(a) + "):"))
        if n <= a:
            print("Error ingrese un valor mayor a:", a)
    return n


def carga(v, n):
    nombres = ("cobre", "plomo", "zinc", "estaño", "hierro", "manganeso", "molibdeno", "cobalto",
               "tungsteno", "titanio", "cromo", "oro", "plata", "platino", "plutonio", "uranio", "radio",
               "torio", "mairene", "potasio ", "yodo  ", "carbonato ", "cloruro", "sulfato",
               "dolomita")
    for i in range(n):
        id = random.randint(1, 10000)
        nombre = random.choice(nombres)
        tipo = random.randint(1, 19)
        precio = random.randint(1, 10000)
        new = Producto(id, nombre, tipo, precio)
        v.append(new)
    return v


def ordenamientodirecto(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].id > v[j].id:
                v[i], v[j] = v[j], v[i]
    return v


def sep():
    print("-" * 30)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def promedio_precio(v):
    n = len(v)
    suma = 0
    preciomayor = 0
    for i in range(n):
        suma += v[i].precio
        if preciomayor < v[i].precio:
            preciomayor = v[i].precio
    promedio = suma / n
    print("El precio con mayor costo es: ", preciomayor)
    print("El precio promedio es: ", promedio)
    print("La diferencia entre el costo mayor y el promedio es: ", (preciomayor - promedio))


def busqueda_secuencial(v, nom):
    for i in range(len(v)):
        if v[i].nombre == nom:
            return i
    return -1


def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while inf > n or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Error... opcion invalida, ingrese entre " + str(inf) + " y " + str(sup))
    return n


def menu():
    print("1-Cargar vector")
    print("2-Ordenar vector por id")
    print("3-Matriz")
    print("4-Mostrar precio mayor y diferencia con el promedio")
    print("5-Ingresar X producto")
    print("6-Salir")
    sep()
    op = validar_rango(1, 6, "Ingrese opcion del menu: ")
    return op
