from planes import *
import random, os, pickle, io


def carga(n, fd):
    descripciones = (
        "Posible vacuna contbra el trabajar COVID-19.", "Posibte cura para el trabajar.", "Cura para tbdiscpacidad",
        "Medicamento tbpara el cancer", "Jatrabe para la ultrbatos")
    nombres1 = ("Bruno", "Mariel", "Bianca", "Juan Cruz", "Jorge", "Antonela", "Josefina", "Lea",
                "Aylen", "Exequiel", "Lilith", "Lou", "Luz", "Lautaro", "Tomas", "Azul", "Cecilia",
                "Agustin", "Mairene", "Angelo", "Angela", "Celeste", "Karen", "Ludmila", "Francisca")
    m = open(fd, "ab")
    for i in range(n):
        id = random.randint(10, 1000)
        nombre = random.choice(nombres1)
        descripcion = random.choice(descripciones)
        monto = random.randint(10, 1000)
        tipo = random.randint(1, 10)
        rango = random.randint(1, 5)
        new = Plan(id, nombre, descripcion, monto, tipo, rango)
        crear_archivo(new, fd, m)
    print("Archivo generado!")
    m.close()


def sep():
    print("=" * 60)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


# Manipulacion de archivos
def crear_archivo(v, fd, m):
    pickle.dump(v, m)


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo no existe, generelo con el punto 1")
        return

    m = open(fd, "rb")
    tamaño = os.path.getsize(fd)

    print("Datos del archivo: ")
    while m.tell() < tamaño:
        a = pickle.load(m)
        to_string(a)
    m.close()


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


def punto3(fd, v, p):
    if not os.path.exists(fd):
        print("El archivo no existe, generelo con el punto 1")
        return

    m = open(fd, "rb")
    tmn = os.path.getsize(fd)

    print("Recuperando datos...")
    while m.tell() < tmn:
        a = pickle.load(m)
        if a.tipo > p:
            v.append(a)
    m.close()
    return v


# Busquedas--------------------
def busqueda_secuencial(v, nom):
    for i in range(len(v)):
        if v[i].nombre == nom:
            return i
    return -1


def busqueda_secuencial1(v, k):
    for i in range(len(v)):
        if v[i].id == k:
            return i
    return -1


def crear_matriz(fd):
    if not os.path.exists(fd):
        print("El archivo no existe, generelo con el punto 1")
        return

    matriz = [[0] * 5 for k in range(10)]

    m = open(fd, "rb")
    tmn = os.path.getsize(fd)

    while m.tell() < tmn:
        a = pickle.load(m)
        matriz[a.tipo - 1][a.rango - 1] += 1
    m.close()
    return matriz


def mostrar_matriz(matriz):
    print()
    for i in range(10):
        for j in range(5):
            if matriz[i][j] > 0:
                print("Plan " + str(i) + " por edad " + str(j) + " : ", matriz[i][j])
    print()


def analisis_cadena(cadena):
    cont = condicion = 0
    hay_t = hay_tb = False
    print("La cadena es: ", cadena)
    for i in cadena:
        if i == " " or i == ".":
            if cont >= 4 and hay_tb:
                condicion += 1
            hay_tb = hay_t = False
            cont = 0
        else:
            if i == "t" or i == "T":
                hay_t = True
            if (i == "b" or i == "B") and hay_t:
                hay_tb = True
            cont += 1
    print("La cantidad de palabras que cumplen con la condicion son: ", condicion)


def menu():
    print("1-Carga de datos")
    print("2-Mostra datos")
    print("3-Generar un arreglo apartir del archivo")
    print("4-Mostrar datos del arreglo")
    print("5-Buscar un plan por nombre")
    print("6-Buscar un k ID")
    print("7-Matriz de conteo")
    print("8-Analizis de cadena")
    print("9-Salir")
    sep()
    op = validar_rango(1, 9, "Ingrese opcion del menu: ")
    return op


def principal():
    v = []
    fd = "vector.dat"
    op = -1
    while op != 9:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            carga(n, fd)
            sep()
        elif op == 2:
            mostrar_archivo(fd)
            sep()
        elif op == 3:
            p = int(input("Ingrese valor p a filtrar: "))
            v = punto3(fd, v, p)
            print("Arreglo Generado...!")
            sep()
        elif op == 4:
            mostrar(v)
            sep()
        elif op == 5:
            nom = input("Ingrese nombre a buscar: ")
            res = busqueda_secuencial(v, nom)
            if res != -1:
                print(v[res].descripcion)
                cadena = v[res].descripcion
            else:
                print("No existe")
            sep()
        elif op == 6:
            k = int(input("Ingrese id a buscar: "))
            res = busqueda_secuencial1(v, k)
            if res != -1:
                to_string(v[res])
            else:
                print("No existe")
            sep()
        elif op == 7:
            matriz = crear_matriz(fd)
            print()
            mostrar_matriz(matriz)
            sep()
        elif op == 8:
            analisis_cadena(cadena)
            sep()
        elif op == 9:
            print("Gracias por utilizar el programa!")
            sep()


# Script princial...
if __name__ == '__main__':
    principal()
