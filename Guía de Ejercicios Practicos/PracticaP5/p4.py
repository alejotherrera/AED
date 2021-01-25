import random, os, pickle


class  ProductoServicio:
    def __init__(self, id, titulo, tipo, calidad ,precio):
        self.id = id
        self.titulo = titulo
        self.tipo = tipo
        self.calidad = calidad
        self.precio = precio


def to_string(v):
    r = ""
    r += "{:<20}".format("id: " + str(v.id))
    r += "{:<20}".format("titulo: " + str(v.titulo))
    r += "{:<25}".format("tipo: " + str(v.tipo))
    r += "{:<25}".format("calidad: " + str(v.calidad))
    r += "{:<25}".format("precio: " + str(v.precio))
    print()
    print(r)


def sep():
    print("-" * 30)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def carga(v, n):
    titulos = (
        "abogado", "metalero", "artista", "electronico", "sistemas", "contador", "quimico", "petrolero", "amadecasa",
        "medico", "kinesiologo", "criminologa", "profesor", "personaltrainer")
    for i in range(n):
        id = random.randint(1,1000)
        titulo = random.choice(titulos)
        tipo = random.randint(0,14)
        calidad = random.randint(0,4)
        precio = random.randint(100,10000)
        new = ProductoServicio(id, titulo, tipo, calidad ,precio)
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
        n = int(input("Ingrese n cantidad de producto/servicio a cargar(mayor a " + str(a) + "):"))
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


def crear_archivo(v, fd):
    m = open(fd, "wb")
    n = len(v)
    for i in range(n):
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


def extra(cadena):
    letras = "abcdefghijkmñlopqrstuvwxyzaeiouáéíóú"
    cadena = cadena.lower()
    rango = len(cadena)
    n = 1
    for i in range(rango):
        if cadena[i] in letras:
            n += 1
    return n


def extra3(v,v2):
    for i in range(len(v)):
        if v[i].tipo < 10:
            add_in_order(v2,v[i])
    return v2


def add_in_order(v, nuevo):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].precio == nuevo.precio:
            pos = c
        if nuevo.precio < v[c].precio:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [nuevo]


def menu():
    print("1-Carga de datos")
    print("2-Mostrar los datos ordenados por numero de identificacion")
    print("3-Generar otro arreglo con solo menor a 10 de tipo")
    print("4-Mostrar el nuevo arreglo")
    print("5-Mostrar datos de los productos precio menor a x")
    print("6-Matriz de conteo")
    print("7-Grabar archivo con todos los datos del segundo arreglo")
    print("8-Mostrar el archivo")
    print("9-Salir")
    sep()
    op = validar_rango(1, 9, "Ingrese opcion del menu: ")
    return op


def punto5(v2,p):
    New = []
    for i in range(len(v2)):
        if v2[i].precio <= p:
            New.append(v2[i])
    return New

def principal():
    v = []
    v2 = []
    fd = "vector.dat"
    op = -1
    while op != 9:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            v = carga(v,n)
            print("Datos cargados con exito!")
            sep()
        elif op == 2:
            if len(v) != 0:
                print("Datos del segundo arreglo ordenados:  ")
                v = ordenamientodirecto(v)
                mostrar(v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 3:
            if len(v) != 0:
                v2 = extra3(v,v2)
                print("Datos generados en el segundo arreglo!")
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v2) != 0 and len(v) != 0:
                print("Datos del segundo arreglo")
                mostrar(v2)
                sep()
            else:
                print("Debe cargar los datos primero")
                sep()
        elif op == 5:
            if len(v) != 0:
                p = int(input("Ingrese valor para mostrar menor igual: "))
                NewVector = punto5(v2,p)
                mostrar(NewVector)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:
            pass
            sep()
        elif op == 7:
            crear_archivo(v2,fd)
            sep()
        elif op == 8:
            mostrar_archivo(fd)
            sep()
        elif op == 9:
            print("Gracias por utilizar el programa!")
            sep()


if __name__ == '__main__':
    principal()
