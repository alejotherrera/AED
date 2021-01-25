import random, os, pickle


class Obra:
    def __init__(self, id, nombre, pais, precio):
        self.id = id
        self.nombre = nombre
        self.pais = pais
        self.precio = precio


def to_string(v):
    r = ""
    r += "{:<20}".format("Identificacion: " + str(v.id))
    r += "{:<20}".format("Nombre: " + str(v.nombre))
    r += "{:<25}".format("Pais: " + str(v.pais))
    r += "{:<25}".format("Precio: " + str(v.precio))
    print()
    print(r)


def sep():
    print("-" * 30)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def carga(v, n):
    nombres = ("cobre", "plomo", "zinc", "estaño", "hierro", "manganeso", "molibdeno", "cobalto",
               "tungsteno", "titanio", "cromo", "oro", "plata", "platino", "plutonio", "uranio", "radio",
               "torio", "mairene", "potasio ", "yodo  ", "carbonato ", "cloruro", "sulfato",
               "dolomita")
    for i in range(n):
        id = random.randint(1, 100)
        nombre = random.choice(nombres)
        pais = random.randint(1, 49)
        precio = random.randint(1000, 100000)
        new = Obra(id, nombre, pais, precio)
        v.append(new)
    return v


def ordenamientodirecto(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].id > v[j].id:
                v[i], v[j] = v[j], v[i]
    return v


def validar_pos(a):
    n = a
    while n <= a:
        n = int(input("Ingrese valor(mayor a " + str(a) + "):"))
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
        if v[i].precio > x:
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


def busqueda_secuencial(v, nom):
    for i in range(len(v)):
        if v[i].nombre == nom:
            return i
    return -1

from collections import Counter

def extra(cadena):
    letras = "abcdefghijkmñlopqrstuvwxyz"
    cadena = cadena.lower()
    rango = len(cadena)
    n = 1
    for i in range(rango):
        if cadena[i] in letras:
            n += 1
    return n

def menu():
    print("1-Carga de datos")
    print("2-Ordenar el arreglo")
    print("3-Crear archivo")
    print("4-Mostrar archivo")
    print("5-Buscar un nombre en el arreglo")
    print("6-Determinar la cantidad de inscriptos registrados por cada posible tipo de curso")
    print("7-Salir")
    sep()
    op = validar_rango(1, 7, "Ingrese opcion del menu: ")
    return op


def principal():
    v = []
    fd = "vector.dat"
    op = -1
    while op != 8:
        op = menu()
        if op == 1:
            print("Ingrese n cantidad de obras a registrar: ")
            n = validar_pos(0)
            v = carga(v, n)
            print("Datos cargados con exito!")
            mostrar(v)
            sep()
        elif op == 2:
            if len(v) != 0:
                v = ordenamientodirecto(v)
                mostrar(v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 3:
            if len(v) != 0:
                valor = float(input("Ingrese valor por mes inferior: "))
                crear_archivo(v, fd, valor)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v) != 0:
                mostrar_archivo(fd)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 5:
            if len(v) != 0:
                nom = input("Ingrese nombre a buscar en el vector: ")
                res = busqueda_secuencial(v, nom)
                if res != -1:
                    to_string(v[res])
                else:
                    print("El nombre a buscar no existe")
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:
                cadena = input("Ingrese cadena: ")
                n = extra(cadena)
                print("La cantidad de letras en la cadena ingresada son: ",n)
                sep()
        elif op == 7:
            print("Gracias por utilizar el programa!")
            sep()


if __name__ == '__main__':
    principal()
