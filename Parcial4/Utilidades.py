import random
import pickle
import os


class --------:
    def __init__(self, ---, -----, ------, ------, -----):
        self. - ---- = ----
        self. - ---- = ------
        self. - ------ = -----
        self. - ---- = ------
        self. - -------- = -------


def to_string(--------):
    r = ""
    r += "{:<25}".format("---------: " + str(------. - ----))
    r += "{:<29}".format(" --------: " + str(-------. - ------))
    r += "{:<33}".format(" --------: " + str(round(-------. - -----, 0)))
    r += "{:<15}".format(" ---------: " + str(------. - -----))
    r += "{:<20}".format(" --------: " + str(-----.))
    print("-" * 100)
    print(r)


def validar_positivo(reques):  # valida que sea mayor a cero el numero cargado
    n = reques
    while n <= reques:
        n = int(input('Valor (mayor a ' + str(reques) + '): '))
        if n <= reques:
            print('Error: se pidio mayor a', reques, '... cargue de nuevo...')
    return n  # cantidad de datos a cargar


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def sep():
    print("-" * 40)


def menu():
    print("--------MENU DE OPCIONES--------")
    print("1-Carga de datos")
    print("2-Mostrar datos anteriores cargados")
    print("3-Mostrar registros en un rango de peso")
    print("4-Generar matriz")
    print("5-Generar archivo con volumen mayor a x")
    print("6-Mostrar archivo")
    print("7-Salir")
    opc = validar_rango(1,7,"Ingrese opcion del menu: ")
    sep()
    return opc

def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while inf > n or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Error...opcion invalida,ingrese entre",inf ,"y",sup)
    return n


def carga_datos(v, n):

   for i in range(n):
        new = "class"
        add_in_order_binary(v,new)

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


def mostrar_vector(v):
    for i in range(len(v)):
        to_string(v[i])j


def grabar_archivo(v, direccion, x):
    m = direccion
    for i in range(len(v)):
        if v[i]. - ----- != -- and v[i]. - ---- < ------:  e
            pickle.dump(v[i], m)

    print("Archivo generado con exito!")
    m.close()


def mostrar_archivo(direccion, fd):
    m = direccion
    size = os.path.getsize(fd)
    print("Datos del archivo:\n")
    existe = False
    while m.tell() < size:
        a = pickle.load(m)
        to_string(a)
        existe = True
    if existe == False:
        print("El archivo no contiene datos")
    m.close()


def busqueda(v):
    --- = int(input('---------------- a buscar: '))
    n = len(v)
    for i in range(n):
        if v[i]. - --- == ----:
            to_string(v[i])
            return  #
    return -1


def busqueda_b(v):
    x = int(input("ingrese la opcion a buscar:"))
    n = len(v)
    izq = 0
    der = n - 1
    pos = n
    while izq <= der:
        c = (izq + der) // 2
        if v[c]. - ---- == x:
            return c
        if x < v[c]. - ----:
            der = c - 1
        else:
            izq = c + 1


def matriz(v):
    mat = [0] * ---
    for i in range(len(mat)):
        mat[i] = [0] * ----

    for i in range(len(v)):
        fila = v[i]. - ---
        col = v[i]. - ----
        mat[fila][col] += 1

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != 0:
                print("Cantidad de ----------:", i, "-------:", j, "Cant:", mat[i][j])  # mostramos


def principal():
    v = []
    fd = "---------"
    op = 1
    while op != 8:
        op = menu()
        if op == 1:
            print("Ingrese n cantidad a cargar:  -----------: ")
            n = validar_positivo(0)
            v = cargar_vector(n,v)

        elif op == 2:
            if len(v) != 0:
                print("-" * 100)
                print("{:>55}".format('REGISTRO DE ----------:'))
                print("-" * 100)
                mostrar_vector(v)
            else:
                print("Error, debe generar el vector anteriormente")


        elif op == 3:
            if len(v) != 0:
                print("ingrese el------- tope ------- que desea consultar...")
                x = validar_positivo(0)
                m = open(fd, "wb")
                grabar_archivo(v, m, x)
            else:
                print("Error, debe generar el vector anteriormente")


        elif op == 4:
            if os.path.exists(fd):
                m = open(fd, "rb")
                mostrar_archivo(m, fd)
            else:
                print("Error, debe generar el vector anteriormente")


        elif op == 5:
            if len(v) != 0:
                busqueda(v)
            else:
                print("Error, debe generar el vector anteriormente")
        elif op == 6:
            if len(v) != 0:
                busqueda_b(v)
            else:
                print("Error, debe generar el vector anteriormente")


        elif op == 7:
            if len(v) != 0:
                matriz(v)
            else:
                print("")

        elif op == 8:
            print("Gracias por utilizar el programa")
        else:
            print("Ingrese una opcion valida")


if __name__ == "__main__":
    principal()
