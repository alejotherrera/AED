import random, os, pickle


class Traslado:
    def __init__(self, id, nombre, importe, destino, pago):
        self.id = id
        self.nombre = nombre
        self.importe = importe
        self.destino = destino
        self.pago = pago


def add_in_order(v, nuevo):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].id == nuevo.id:
            pos = c
            break
        if nuevo.id < v[c].id:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [nuevo]


def to_string(v):
    r = ""
    r += "{:<20}".format("id: " + str(v.id))
    r += "{:<20}".format("nombre: " + str(v.nombre))
    r += "{:<25}".format("importe: " + str(v.importe))
    r += "{:<25}".format("destino: " + str(v.destino))
    r += "{:<25}".format("pago: " + str(v.pago))
    print()
    print(r)


def sep():
    print("-" * 30)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def carga(v, n):
    nombres = ("c'obre", "pl¿omo", "zin7c", "es|taño", "hierro", "manganeso", "molibdeno", "cobalto",
               "tungsteno", "titanio", "cromo", "oro", "plata", "platino", "plutonio", "uranio", "radio",
               "torio", "mairene", "potasio ", "yodo  ", "carbonato ", "cloruro", "sulfato",
               "dolomita")
    for i in range(n):
        id = random.randint(1, 1000)
        nombre = random.choice(nombres)
        importe = random.randint(100, 50000)
        destino = random.randint(0, 22)
        pago = random.randint(0, 4)
        new = Traslado(id, nombre, importe, destino, pago)
        add_in_order(v, new)
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


def crear_archivo(v, fd, x, inf, sup):
    m = open(fd, "wb")
    n = len(v)
    for i in range(n):
        if v[i].pago == x:
            if inf < v[i].importe < sup:
                pickle.dump(v[i], m)
    print("Archivo generado!")
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo no existe, generelo con el punto anterior")
        return

    m = open(fd, "rb")
    tamaño = os.path.getsize(fd)
    if tamaño == 0:
        return print("El archivo esta vacio")

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
    letras = "abcdefghijkmñlopqrstuvwxyzaeiouáéíóú "
    cadena = cadena.lower()
    rango = len(cadena)
    for i in range(rango):
        if cadena[i] not in letras:
            nom = cadena + "*"
            extraño = cadena[i]
            return nom, extraño
    return cadena


def es_letra(car):
    if car >= 'a' and car <= 'z':
        return True
    if car >= 'A' and car <= 'Z':
        return True
    return False


def validar_nombre(nombre):
    validas = 0
    for car in nombre:
        if es_letra(car) or car == ' ':
            validas += 1
    validas == len(nombre)
    return validas


def menu():
    print("1-Cargar n traslados")
    print("2-Mostrar el arreglo creado en el punto 1")
    print("3-Buscar en el arreglo creado en el punto 1 un nombre")
    print("4-Crear archivo con forma de pago 0 e importe entre dos numero n y m")
    print("5-Mostar el archivo creado")
    print("6-Salir")
    sep()
    op = validar_rango(1, 6, "Ingrese opcion del menu: ")
    return op


def principal():
    v = []
    fd = "vector.dat"
    op = -1
    while op != 6:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            v = carga(v, n)
            print("Datos cargados con exito!!!!!!")
            sep()
        elif op == 2:
            if len(v) != 0:
                print("Datos del arreglo: ")
                mostrar(v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 3:
            if len(v) != 0:
                nom = input("Ingrese nombre a buscar: ")
                res = busqueda_secuencial(v, nom)
                if res != -1:
                    to_string(v[res])
                else:
                    print("El nombre no existe en el arreglo")
                sep()
                nom, extraño = extra(nom)
                if nom[-1] == "*":
                    print("El nombre contiene caracteres que no son espacios y letras")
                    print("Tiene un: ", extraño)
                else:
                    print("El nombre contiene solo letras y espacios")
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v) != 0:
                inf = int(input("Ingrese importe inferior: "))
                sup = int(input("Ingrese importe superior: "))
                crear_archivo(v, fd, 0, inf, sup)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 5:
            if len(v) != 0:
                mostrar_archivo(fd)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:
            print("Gracias por utilizar el programa!")
            sep()


if __name__ == '__main__':
    principal()
