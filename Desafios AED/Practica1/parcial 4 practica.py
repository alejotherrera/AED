"Ejercicio Tipo Parcial 4"
import random
import pickle
import os


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
    print("2- Buscar x alumno")
    print("3- Generar matriz ")
    print("4- Generar archivo con los alumnos de un año x")
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


def buscar_alumno(v, nom):
    n = len(v)
    for i in range(n):
        if v[i].nombre == nom:
            return i
    return -1


def carga_matriz(v):
    matriz = [[0] * 7 for i in range(10)]
    for i in v:
        fil = i.codigo
        col = i.año
        matriz[fil][col] += 1
    sep()
    print("datos de la matriz:")
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c] != 0:
                print("Deporte: ", f, "- Año: ", c, ":", matriz[f][c], sep="")


def archivo_x(v, x, fd):
    m = open(fd, "wb")
    for i in range(len(v)):
        if v[i].año == x:
            pickle.dump(v[i], m)
    m.close()
    print("Se creo el archivo", fd, "con los registros del año", x)


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo no existe, crearlo para imprimirlo")
        print()
        return

    print("Contenido actual del archivo: ", fd)
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        alumno = pickle.load(m)
        to_string(alumno)


def principal():
    opcion = -1
    v = []
    fd = "archivoparcialherrera.dat"
    flag1 = False
    while opcion != 6:
        opcion = menu()
        if opcion == 1:
            flag1 = True
            n = int(input("Ingrese cantidad de alumnos a registrar: "))
            carga_auto(v, n)
            print("Datos creados")
            mostrar(v)
            sep()
        elif opcion == 6:
            print("Gracias por utilizar el programa")
        if flag1:
            if opcion == 2:
                nombre_x = input("Ingrese nombre del alumno a buscar: ")
                res = buscar_alumno(v, nombre_x)
                if res != -1:
                    print("Alumno encontrado!")
                    to_string(v[res])
                else:
                    print("Alumno no encontrado")
                sep()
            elif opcion == 3:
                carga_matriz(v)
            elif opcion == 4:
                x = validar_rango(1, 7, "Ingrese año(entre 1 y 7): ")
                archivo_x(v, x, fd)
                sep()
            elif opcion == 5:
                mostrar_archivo(fd)
                sep()
        else:
            print("Primero debe crear el vector con alumnos")


if __name__ == '__main__':
    principal()
