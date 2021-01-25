import random
import pickle
import os


class pelicula:
    def __init__(self, id, titulo, tipo, importe, origen):
        self.id = id
        self.titulo = titulo
        self.importe = importe
        self.tipo = tipo
        self.origen = origen


def to_string(v):
    r = "{:<20}".format("ID: " + str(v.id))
    r += "{:<20}".format("Titulo: " + str(v.titulo))
    r += "{:<20}".format("Importe: " + str(v.importe))
    r += "{:<20}".format("tipo: " + str(v.tipo))
    r += "{:<20}".format("Codigo pais: " + str(v.origen))
    print()
    print(r)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def sep():
    print("-" * 30)


def menu():
    print("1- Carga de datos")
    print("2- Mostrar arreglo 1")
    print("3- Crear arreglo con condiciones")
    print("4- Mostrar archivo creado en punto 3")
    print("5- Buscar en el arreglo 1 id")
    print("6- Matriz")
    print("7- Salir")
    opc = validar_rango(1, 7, "Ingrese opcion del menu(entre 1 y 6): ")
    sep()
    return opc


def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while inf > n or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Error...opcion invalida,vuelva a cargar")
    return n


def carga_auto(v, n):
    titulos = ("Bruno", "Mariel", "Bianca", "Juan Cruz", "Jorge", "Antonela", "Josefina", "Lea",
               "Aylen", "Exequiel", "Lilith", "Lou", "Luz", "Lautaro", "Tomas", "Azul", "Cecilia",
               "Agustin", "Mairene", "Angelo", "Angela", "Celeste", "Karen", "Ludmila", "Francisca")
    for i in range(n):
        id = int(random.randint(10, 100))
        titulo = random.choice(titulos)
        importe = int(random.randint(1, 100))
        tipo = int(random.randint(0, 9))
        origen = int(random.randint(0, 19))
        new = pelicula(id, titulo, tipo, importe, origen)
        add_in_order_binary(v, new)


def add_in_order_binary(v, nuevo):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].titulo == nuevo.titulo:
            pos = c
        if nuevo.titulo < v[c].titulo:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [nuevo]


def crear_archivo(v, name):
    x = int(input("Ingrese monto para chequear: "))
    n = len(v)
    m = open(name, "wb")
    for i in range(n):
        if v[i].origen != 10 and v[i].importe < x:
            pickle.dump(v[i], m)
    m.close()


def mostrar_archivo(name):
    if not os.path.exists(name):
        print("El archivo no existe generalo con opcion 3")
        return

    m = open(name, "rb")
    tamaño = os.path.getsize(name)
    print("Datos del archivo:\n")
    while m.tell() < tamaño:
        a = pickle.load(m)
        to_string(a)
    m.close()


def busqueda(v, x):
    n = len(v)
    for i in range(n):
        if v[i].id == x:
            return i
    return -1


def crear_matriz(v):
    n = 10
    m = 20
    matriz = [[0] * m for i in range(n)]
    for i in range(len(v)):
        fil = v[i].tipo
        col = v[i].origen
        matriz[fil][col] += 1
    return matriz


def mostrar_matriz(matriz):
    n = len(matriz)
    m = len(matriz[0])
    for i in range(n):
        r = ""
        for j in range(m):
            if matriz[i][j] != 0:
                r += "{:<20}".format("\nTipo de pelicula: " + str(j) + " - origen:" + str(matriz[i][j]))
        if r != "":
            print("Tipo de pelicula: ", i, r)


def principal():
    op = -1
    v = []
    flag = True
    fd = "archivo.dat"
    while op != 7:
        op = menu()
        if op == 1:
            flag = True
            n = int(input("Ingrese cantidad de peliculas a registrar: "))
            carga_auto(v, n)
            print("Datos cargados!")
            sep()
        elif op == 7:
            print("Gracias por utilizar el programa")
        if flag:
            if op == 2:
                mostrar(v)
                sep()
            elif op == 3:
                crear_archivo(v, fd)
                print("Archivo guardado con exito!")
                sep()
            elif op == 4:
                mostrar_archivo(fd)
                sep()
            elif op == 5:
                x = int(input("Ingrese numero de identificacion a buscar: "))
                res = busqueda(v, x)
                if res != -1:
                    to_string(v[res])
                else:
                    print("Identificacion no encontrada")
                sep()
            elif op == 6:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)
                sep()
        else:
            print("Ingrese una opcion valida")


if __name__ == '__main__':
    principal()
