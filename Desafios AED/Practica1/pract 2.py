"Ejercicio Tipo Parcial 4"
import random
import pickle
import os
import os.path
import io

class Alumno:
    def __init__(self, legajo, nombre, año, codigo):
        self.legajo = legajo
        self.nombre = nombre
        self.año = año
        self.codigo = codigo


def to_string(v):
    r = "{:<20}".format("Legajo: " + str(v.legajo))
    r += "{:<20}".format("nombre: " + str(v.nombre))
    r += "{:<20}".format("año: " + str(v.año))
    r += "{:<20}".format("codigo: " + str(v.codigo))
    print()
    print(r)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def carga_auto(v, n):
    nombres = ("Bruno", "Mariel", "Bianca", "Juan Cruz", "Jorge", "Antonela", "Josefina", "Lea",
               "Aylen", "Exequiel", "Lilith", "Lou", "Luz", "Lautaro", "Tomas", "Azul", "Cecilia",
               "Agustin", "Mairene", "Angelo", "Angela", "Celeste", "Karen", "Ludmila", "Francisca")
    for i in range(n):
        legajo = random.randint(10, 1000)
        nombre = random.choice(nombres)
        año = random.randint(1, 7)
        codigo = random.randint(0, 9)
        nuevo = Alumno(legajo, nombre, año, codigo)
        add_in_order_binary(v, nuevo)


def add_in_order_binary(v, nuevo):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].nombre == nuevo.nombre:
            pos = c
        if nuevo.nombre < v[c].nombre:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [nuevo]


def menu():
    print("1- Carga de datos")
    print("2- Buscar alumno por legajo")
    print("3- Generar matriz ")
    print("4- Generar archivo con los alumnos")
    print("5- Mostar contenido creado en el 4")
    print("6- Salir")
    opc = validar_rango(1, 6, "Ingrese opcion del menu(entre 1 y 6): ")
    sep()
    return opc


def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while inf > n or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Error...opcion invalida,vuelva a cargar")
    return n


def sep():
    print("-" * 30)


def buscar_alumno(v, leg):
    n = len(v)
    for i in range(n):
        if v[i].legajo == leg:
            return i
    return -1


def crear_archivo(v):
    fd = input("Ingrese nombre del archivo a crear: ")
    while os.path.exists(fd):
        print("El archivo existe, eliga otro nombre...")
        fd = input("Ingrese nombre del archivo a crear: ")

    m = open(fd, "wb")
    for i in range(len(v)):
        pickle.dump(v[i], m)
    m.close
    print("Datos creados en el archivo:",fd)
    return fd


def mostrar_archivo(fd):
    if not os.path.exists:
        print("El archivo no existe, generelo(punto4)")
        return
    m = open(fd, "rb")
    tamaño = os.path.getsize(fd)
    print("Datos del archivo:\n")
    while m.tell() < tamaño:
        a = pickle.load(m)
        to_string(a)
    m.close()


def principal():
    op = -1
    flag1 = False
    v = []
    while op != 6:
        op = menu()
        if op == 1:
            n = int(input("Ingrese cantidad de alumnos a cargar: "))
            flag1 = True
            carga_auto(v, n)
            mostrar(v)
            sep()
        elif op == 6:
            print("Gracias por utilizar el programa")
        if flag1:
            if op == 2:
                leg = int(input("Ingrese legajo del alumno: "))
                res = buscar_alumno(v, leg)
                if res != -1:
                    to_string(v[res])
                else:
                    print("Alumno no encontrado")
                sep()
            elif op == 3:
                pass
                sep()
            elif op == 4:
                fd = crear_archivo(v)
                sep()
            elif op == 5:
                mostrar_archivo(fd)
                sep()
        else:
            print("Debe cargar el vector primero(opcion 1)")
            sep()


if __name__ == '__main__':
    principal()
