import random, os, pickle


class inscriptos:
    def __init__(self, dni, nombre, titulo, curso, precio):
        self.dni = dni
        self.nombre = nombre
        self.titulo = titulo
        self.curso = curso
        self.precio = precio


def to_string(v):
    r = ""
    r += "{:<20}".format("dni: " + str(v.dni))
    r += "{:<20}".format("nombre: " + str(v.nombre))
    r += "{:<25}".format("titulo: " + str(v.titulo))
    r += "{:<25}".format("curso: " + str(v.curso))
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
    nombres = ("cobre", "plomo", "zinc", "estaño", "hierro", "manganeso", "molibdeno", "cobalto",
               "tungsteno", "titanio", "cromo", "oro", "plata", "platino", "plutonio", "uranio", "radio",
               "torio", "mairene", "potasio ", "yodo  ", "carbonato ", "cloruro", "sulfato",
               "dolomita")
    titulos = (
        "abogado", "metalero", "artista", "electronico", "sistemas", "contador", "quimico", "petrolero", "amadecasa",
        "medico", "kinesiologo", "criminologa", "profesor", "personaltrainer")
    for i in range(n):
        dni = random.randint(1, 500)
        nombre = random.choice(nombres)
        titulo = random.choice(titulos)
        curso = random.randint(0, 29)
        precio = random.randint(20, 100)
        new = inscriptos(dni, nombre, titulo, curso, precio)
        v.append(new)
    return v


def ordenamientodirecto(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].dni > v[j].dni:
                v[i], v[j] = v[j], v[i]
    return v


def validar_pos(a):
    n = a
    while n <= a:
        n = int(input("Ingrese cantidad de inscriptos(mayor a " + str(a) + ") :"))
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
        if v[i].precio < x:
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
    n = 0
    for i in range(rango):
        if cadena[i] not in letras:
            n += 1
    return n


def menu():
    print("1-Carga")
    print("2-Ordenar por dni y mostrar")
    print("3-Crear archivo con valor x")
    print("4-Mostrar archivo")
    print("5-Buscar en el arreglo")
    print("6-Matriz de conteo")
    print("7-Cadena a analizar")
    print("8-Salir")
    sep()
    op = validar_rango(1, 8, "Ingrese opcion del menu: ")
    return op


def principal():
    v = []
    fd = "vector.dat"
    op = -1
    while op != 8:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            v = carga(v, n)
            mostrar(v)
            sep()
        elif op == 2:
            if len(v) != 0:
                ordenamientodirecto(v)
                mostrar(v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 3:
            if len(v) != 0:
                x = int(input("Ingrese monto limite: "))
                crear_archivo(v, fd, x)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v) != 0:
                print("Mostrando datos...")
                mostrar_archivo(fd)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 5:
            if len(v) != 0:
                nom = input("Ingrese nombre a buscar: ")
                res = busqueda_secuencial(v, nom)
                if res != -1:
                    print("Nombre encontrado!")
                    to_string(v[res])
                else:
                    print("Error, nombre no encontrado")
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:
            if len(v) != 0:

                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
        elif op == 7:
            cadena = input("Ingrese cadena a analizar: ")
            n = extra(cadena)
            print("La cantidad de caracteres que no eran letras fueron: ", n)
        elif op == 8:
            print("Gracias por utilizar el programa!")
            sep()


if __name__ == '__main__':
    principal()
