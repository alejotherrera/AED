from discos import *
import random, os, pickle, io


# Visual
def sep():
    print("=" * 30)


# Validaciones
def validar_pos(a):
    n = a
    while n <= a:
        n = int(input("Ingrese valor n a cargar en el arreglo(mayor a " + str(a) + "):"))
        if n <= a:
            print("Error ingrese un valor mayor a:", a)
    return n


def extrar_musica(fd):
    archivo = open(fd, "rt")
    n = int(archivo.readline())
    v = [None] * n
    for i in range(n):
        titulo = archivo.readline().strip()
        artista = archivo.readline().strip()
        anio = int(archivo.readline())
        genero = int(archivo.readline())
        reproducciones = int(archivo.readline())
        v[i] = Disco(titulo, artista, anio, genero, reproducciones)
    archivo.close()
    return v


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def punto1(v):
    mayor = None
    for i in range(len(v)):
        if i == 0 or v[i].reproducciones > mayor.reproducciones:
            mayor = v[i]
    return mayor


def punto2(v):
    generos = [0] * 21
    for i in range(len(v)):
        generos[v[i].genero] += 1
    return generos


def punto3(v, x):
    for i in range(len(v)):
        if v[i].titulo == x:
            return i
    return -1


def punto4(v):
    titulo = input("Ingrese titulo: ")
    artista = input("Ingrese artista: ")
    anio = input("Ingrese año: ")
    genero = input("Ingrese genero: ")
    reproducciones = input("Ingrese reproducciones: ")
    new = Disco(titulo, artista, anio, genero, reproducciones)
    v.append(new)
    return v


def punto5(v, x, y):
    for i in range(len(v)):
        if v[i].titulo == x and v[i].titulo == y:
            del v[i]
    return v


def grabar_discos(v, fd):
    file = open(fd, "wt")
    n = len(v)
    file.write(str(n) + "\n")
    for disco in v:
        file.write(disco.titulo + "\n")
        file.write(disco.artista + "\n")
        file.write(str(disco.anio) + "\n")
        file.write(str(disco.genero) + "\n")
        file.write(str(disco.reproducciones) + "\n")
    file.flush()
    file.close()


def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while inf > n or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Error... opcion invalida, ingrese entre " + str(inf) + " y " + str(sup))
    return n


def menu():
    print("1-Determinar cual fue el disco con mas reproducciones")
    print("2-Determinar la cantidad de discos de cada genero")
    print("3-Actualizar la cantidad de reproducciones de un disco con titulo x")
    print("4-Agregar un nuevo disco")
    print("5-Eliminar un disco con titulo x y artista y")
    print("6-Al salir actualizar el archivo con los datos del vector")
    print("7-Mostrar listado de discos")
    sep()
    op = validar_rango(1, 7, "Ingrese opcion del menu: ")
    return op


def principal():
    fd = "discos.txt"
    op = -1
    v = extrar_musica(fd)
    while op != 6:
        op = menu()
        if op == 1:
            mayor = punto1(v)
            print("El disco con mayor reporudcciones es: ")
            to_string(mayor)
            sep()
        elif op == 2:
            generos = punto2(v)
            for i in range(len(generos)):
                if generos[i] != 0:
                    print("En el genero ", i, " hay: ", generos[i], " cantidad de discos")
            sep()
        elif op == 3:
            x = input("Ingrese titulo: ")
            res = punto3(v, x)
            if res != -1:
                v[res].reproducciones = int(input("Ingrese cantidad de reproducciones: "))
                print("Reproducciones grabadas con exito...!")
            else:
                print("No se ha encontrado el disco...!")
            sep()
        elif op == 4:
            v = punto4(v)
            print("Disco agregado!!!")
            sep()
        elif op == 5:
            x = input("Ingrese titulo: ")
            y = input("Ingrese artista: ")
            v = punto5(v, x, y)
            print("Disco eliminado con exito...!")
            sep()
        elif op == 6:
            grabar_discos(v, fd)
            print("Gracias por utilizar el programa!!")
            sep()
        elif op == 7:
            mostrar(v)

# Script princial...
if __name__ == '__main__':
    principal()
