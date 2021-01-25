import random
import pickle
import os


class Autos:
    def __init__(self, num, nombre, stock, pais, tipo):
        self.num = num
        self.nombre = nombre
        self.stock = stock
        self.pais = pais
        self.tipo = tipo


def to_string(autos):
    r = ""
    r += "{:<20}".format("Numero: " + str(autos.num))
    r += "{:<20}".format("Nombre: " + str(autos.nombre))
    r += "{:<25}".format("stock: " + str(autos.stock))
    r += "{:<25}".format("pais: " + str(autos.pais))
    r += "{:<20}".format("Tipo: " + str(autos.tipo))
    print(r)


def separacion():
    print(30 * "-")


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


def carga_datos(v, n):
    nombres = ("Bruno", "Mariel", "Bianca", "Juan Cruz", "Jorge", "Antonela", "Josefina", "Lea",
               "Aylen", "Exequiel", "Lilith", "Lou", "Luz", "Lautaro", "Tomas", "Azul", "Cecilia",
               "Agustin", "Mairene", "Angelo", "Angela", "Celeste", "Karen", "Ludmila", "Francisca")
    for i in range(n):
        num = random.randint(1, 100)
        nombre = random.choice(nombres)
        stock = random.randint(1, 100)
        pais = random.randint(0, 19)
        tipo = random.randint(0, 9)
        nuevo = Autos(num, nombre, stock, pais, tipo)
        add_in_order_binary(v, nuevo)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def crear_archivo(v, name):
    n = len(v)
    name = open(name, "wb")
    for i in range(n):
        if (v[i].pais != 6 or v[i].pais != 5) and v[i].stock > 0:
            pickle.dump(v[i], name)
    name.close()
#Readline

def mostar_archivo(name):
    m = open(name, "rb")
    tamaño = os.path.getsize(name)
    print("Datos del archivo:\n")
    while m.tell() < tamaño:
        a = pickle.load(m)
        to_string(a)
    m.close()


def menu():
    print("1- Cargar registros")
    print("2- Mostrar el arrgelo creado")
    print("3- Crear archivo")
    print("4- Mostar el archivo creado en el punto 3")
    print("5- Buscarn en el arrgelo 1 por identificacion")
    print("6- Determinar cantidad de vehiculos de cada pais")
    print("0- Salir")
    opcion = int(input("Ingrese opcion del menu: "))
    return opcion


def busqueda(v, x):
    n = len(v)
    for i in range(n):
        if v[i].num == x:
            return i
    return -1


def crear_matriz(v):
    mat = [[0] * 10 for f in range(20)]

    for reg in v:
        fil = reg.pais
        col = reg.tipo
        mat[fil][col] += 1
    return mat


def mostrar_matriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[f][c] != 0:
                print('Pais ', f, ' - Tipo ', c, ': ', mat[f][c], sep='')


def principal():
    opc = -1
    v = []
    name = "registros-parcial.dat"
    date_create = False
    archive = False
    while opc != 0:
        opc = menu()
        if opc == 1:
            n = int(input("Ingrese cantidad de vehiculos a registrar: "))
            carga_datos(v, n)
            date_create = True
            separacion()
        if date_create:
            if opc == 2:
                mostrar(v)
                separacion()
            elif opc == 3:
                crear_archivo(v, name)
                print("Archivo creado")
                archive = True
                separacion()
            elif archive and opc == 4:
                mostar_archivo(name)
                separacion()
            elif opc == 5:
                x = int(input("Ingrese valor a buscar: "))
                res = busqueda(v, x)
                if res != -1:
                    to_string(v[res])
                    separacion()
                else:
                    print("Numero de identificacion no encontrado")
            elif opc == 6:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)
                separacion()
            elif opc == 7:
                print("Gracias por utilizar el programa")
        else:
            print("Debe generar primero el vector")
            separacion()


if __name__ == '__main__':
    principal()
