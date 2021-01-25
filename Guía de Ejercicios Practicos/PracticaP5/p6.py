import random, os, pickle


class PaqueteTuristico:
    def __init__(self, codigo, descripcion, costo, ciudad, pais):
        self.codigo = codigo
        self.descripcion = descripcion
        self.costo = costo
        self.ciudad = ciudad
        self.pais = pais


def to_string(v):
    r = ""
    r += "{:<20}".format("codigo: " + str(v.codigo))
    r += "{:<20}".format("descripcion: " + str(v.descripcion))
    r += "{:<25}".format("costo : " + str(v.costo))
    r += "{:<25}".format("ciudad: " + str(v.ciudad))
    r += "{:<25}".format("pais: " + str(v.pais))
    print()
    print(r)


def add_in_order(v, nuevo):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].codigo == nuevo.codigo:
            pos = c
            break
        if nuevo.codigo < v[c].codigo:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [nuevo]


def sep():
    print("-" * 30)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def carga(v, n):
    nombres = ("Paeiou", "plomo", "zinc", "estaño", "hierro", "manganeso", "molibdeno", "cobalto",
               "tungsteno", "titanio", "cromo", "oro", "plata", "platino", "plutonio", "uranio", "radio",
               "torio", "mairene", "potasio ", "yodo  ", "carbonato ", "cloruro", "sulfato",
               "dolomita")
    for i in range(n):
        codigo = random.randint(1, 100)
        descripcion = random.choice(nombres)
        costo = random.randint(100, 1000)
        ciudad = random.randint(0, 24)
        pais = random.randint(0, 19)
        new = PaqueteTuristico(codigo, descripcion, costo, ciudad, pais)
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


def crear_archivo(v, fd):
    m = open(fd, "wb")
    n = len(v)
    for i in range(n):
        if v[i].pais != 15 and v[i].pais != 5:
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


def busqueda_secuencial(v, x):
    for i in range(len(v)):
        if v[i].codigo == x:
            return i
    return -1


def busqueda_rango(v, x):
    for i in range(len(v)):
        if v[i].costo > x:
            return i
    return -1


def extra(cadena):
    vocales = ('a', 'e', 'i', 'o', 'u')
    cons = 0
    vocal = 0
    if cadena[0] != "P":
        return False

    for i in cadena:
        if i in vocales:
            vocal += 1
        else:
            cons += 1

    if vocal > cons:
        return True
    else:
        return False


def NuevoVector(v):
    v2 = []
    for i in range(len(v)):
        if extra(v[i].descripcion) == True:
            v2.append(v[i])
    return v2


def menu():
    print("1-Carga de datos")
    print("2-Mostrar el arreglo generado")
    print("3-Generar un segundo arreglo con todos los paquetes turisticos")
    print("4-Mostrar el arreglo creado anteriormente")
    print("5-Matriz")
    print("6-Buscar codigo x")
    print("7-Buscar paquete cuyo costo por persona sea un valor mayor a X en el nuevo arreglo")
    print("8-Crear archivo cuyo destino no sea entre 5 y 15 ")
    print("9-Mostrar archivo generado en el punto anterior")
    print("10-salir")
    sep()
    op = validar_rango(1, 10, "Ingrese opcion del menu: ")
    return op


def principal():
    v = []
    fd = "vector.dat"
    op = -1
    while op != 10:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            v = carga(v, n)
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
                v2 = NuevoVector(v)
                print("Vector 2 creado")
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v) != 0 and len(v2) != 0:
                print("Datos del segundo vector")
                mostrar(v2)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1 y opcion2)")
                sep()
        elif op == 5:
            if len(v) != 0:
                pass
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:
            x = int(input("Ingrese nombre del paquete turistico: "))
            res = busqueda_secuencial(v, x)
            if res == -1:
                print("Paquete no encontrado")
            else:
                print("Paquete encontrado: ")
                to_string(v[res])
            sep()
        elif op == 7:
            x = int(input("Ingrese precio x a mayor:"))
            res1 = busqueda_rango(v, x)
            if res1 == -1:
                print("Paquete turistico no encontrado con el valor ingresado")
            else:
                print("Paquete encontrado: ")
                to_string(v[res1])
            sep()
        elif op == 8:
            crear_archivo(v, fd)
            sep()
        elif op == 9:
            print("Datos del archivo: ")
            mostrar_archivo(fd)
            sep()
        elif op == 10:
            print("Gracias por utilizar el programa!")
            sep()


if __name__ == '__main__':
    principal()
