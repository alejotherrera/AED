import random
from Parcial_4_CET_Archivo_Profesionales import *


def separar():
    print(60 * "-")

def add_in_order_bin(v,nuevo):
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


def cargar_registro(v,n):
    nombres = ("Bruno", "Mariel", "Bianca", "Juan Cruz", "Jorge", "Antonela", "Josefina", "Lea",
               "Aylen", "Exequiel", "Lilith", "Lou", "Luz", "Lautaro", "Tomas", "Azul", "Cecilia",
               "Agustin", "Mairene", "Angelo", "Angela", "Celeste", "Karen", "Ludmila", "Francisca")
    for i in range(n):
        dni = random.randint(30000000, 40000000)
        nombre = random.choice(nombres)
        importe = round(random.uniform(10,100000), 2)
        tipo_afiliacion = random.randint(0,4)
        tipo_trabajo = random.randint(0,14)
        nuevo = Profesionales(dni,nombre,importe,tipo_afiliacion,tipo_trabajo)
        add_in_order_bin(v,nuevo)

def mostrar_registro(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])

def buscar_arreglo(nom,v):
    n = len(v)
    for i in range(n):
        if v[i].nombre == nom:
            return i
    return -1

def crear_matriz(v):
    n = 5
    m = 15
    matriz = [[0] * m for filas in range(n)]
    for i in range(len(v)):
        fil = v[i].tipo_afiliacion
        col = v[i].tipo_trabajo
        matriz[fil][col] += 1
    return matriz


def mostrar_matriz(matriz):
    n = len(matriz)
    m = len(matriz[0])
    for i in range(n):
        r = ""
        for j in range(m):
            if matriz[i][j] != 0:
                r += "{:40}".format("\nTipo de trabajo: " + str(j) + " Cantidad: "+ str(matriz[i][j]))
        if r != "":
            print("\n>>> Tipo de afiliacion: ", i , r)

def principal():
    opc = -1
    v = []
    fd = "profesionales.dat"
    while opc != 0:
        print("1 - Cargar registro")
        print("2 - Mostrar arreglo")
        print("3 - Cargar un archivo con profesionales de tipo_trabajo 3,4, o 5 a partir de un importe base")
        print("4 - Mostrar datos del archivo 'profesionales.dat' ")
        print("5 - Buscar un profesional por su nombre y mostrar sus datos")
        print("6 - Crear y Mostrar matriz")
        print("0 - Salir")
        opc = int(input("Ingrese a donde desee ir: "))
        separar()
        if opc == 1:
            n = int(input("Ingrese la cantidad de Profesionales a cargar: "))
            cargar_registro(v,n)
            separar()
        elif opc == 2:
            if not v:
                print("Primero debe cargar el arreglo")
                separar()
            else:
                mostrar_registro(v)
                separar()
        elif opc == 3:
            if not v:
                print("Primero debe cargar el arreglo")
                separar()
            else:
                importe_base = int(input("Ingrese el importe base: "))
                cargar_archivo(fd,v,importe_base)
                separar()
        elif opc == 4:
            if os.path.exists(fd):
                mostrar_archivo(fd)
                separar()
            else:
                print("Primero debe cargar el archivo")
                separar()
        elif opc == 5:
            if not v:
                print("Primero debe cargar el arreglo")
                separar()
            else:
                nom = input("Ingrese el nombre a buscar: ")
                busqueda = buscar_arreglo(nom, v)
                if busqueda != -1:
                    print("Resultado de la busqueda: \n")
                    to_string(v[busqueda])
                    separar()
                else:
                    print("No se ha encontrado ningun profesional con el nombre: ", nom)
                    separar()
        elif opc == 6:
            if not v:
                print("Primero debe cargar el arreglo")
                separar()
            else:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)
                separar()
        else:
            print("Error")


if __name__ == '__main__':
    principal()
