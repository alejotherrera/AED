import random, os, pickle, io

class Obra:
    def __init__(self, id, servicio, pais, precio):
        self.id = id
        self.servicio = servicio
        self.pais = pais
        self.precio = precio

def to_string(inscripto):
    r = ""
    r += "{:<20}".format("NUMERO DE DNI: " + str(inscripto.dni), end="  ")
    r += "{:<30}".format("  descripciones: " + str(inscripto.nombre), end="  ")
    r += "{:<30}".format("CURSO: " + str(inscripto.curso), end="  ")
    r += "{:<30}".format(" TIPO: " + str(inscripto.tipo), end="  ")
    r += "{:<30}".format("IMPORTE: $ " + str(inscripto.importe))
    print()
    print(r)


# Ordenamientos agregado
def add_in_order(v, nuevo):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].descripcion == nuevo.descripcion:
            pos = c
            break
        if nuevo.descripcion < v[c].descripcion:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [nuevo]


def sep():
    print("=" * 30)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def carga(v, n):
    for i in range(n):
        new = new
        v.append(new)

    return v


# Ordenamientos
def ordenamientodirecto(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].id > v[j].id:
                v[i], v[j] = v[j], v[i]
    return v


def bubble_sort(v):
    n = len(v)
    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            if v[j] > v[j + 1]:
                ordenado = False
                v[j], v[j + 1] = v[j + 1], v[j]
        if ordenado:
            break
    return v

def insertion_sort(v):
    n = len(v)
    for j in range(1, n):
        y = v[j]
        k = j - 1
        while k >= 0 and y < v[k]:
            v[k + 1] = v[k]
            k -= 1
        v[k + 1] = y
    return v

def shell_sort(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1
    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and y < v[k]:
                v[k + h] = v[k]
                k -= h
            v[k + h] = y
        h //= 3
    return v


def heap_sort(v):
    # ordenamiento Heap Sort
    n = len(v)
    # Primera fase: crear el grupo inicial...
    for i in range(n):
        e = v[i]
        s = i
        f = (s - 1) // 2
        while s > 0 and v[f] < e:
            v[s] = v[f]
            s = f
            f = (s - 1) // 2
        v[s] = e
    # Segunda fase: Extraer la raiz, y reordenar el vector y el grupo...
    for i in range(n - 1, 0, -1):
        valori = v[i]
        v[i] = v[0]
        f = 0
        if i == 1:
            s = -1
        else:
            s = 1
        if i > 2 and v[2] > v[1]:
            s = 2
        while s >= 0 and valori < v[s]:
            v[f] = v[s]
            f = s
            s = 2 * f + 1
            if s + 1 <= i - 1 and v[s] < v[s + 1]:
                s += 1
                if s > i - 1:
                    s = -1
        v[f] = valori


# ------------------

# Validaciones
def validar_monto(mensaje):
    monto = float(input(mensaje))
    while monto < 0:
        print('Inválido! Debe ser un valor positivo.')
        monto = float(input(mensaje))
    return monto


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

# Manipulacion de archivos
def crear_archivo(v, fd, x):
    m = open(fd, "wb")
    n = len(v)
    for i in range(n):
        if v[i].precio > x:
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


# Busquedas----------------

def busqueda_secuencial(v, nom):
    for i in range(len(v)):
        if v[i].nombre == nom:
            return i
    return -1


def binary_search(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1
    return -1
# ------------------------

# ------------------------
# Fusion de vectores
def merge(a, b):
    n, m = len(a), len(b)
    t = n + m
    c = t * [0]
    i = k = j = 0
    while i < n and j < m:
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[i]
            j += 1
        k += 1
    v, pos = b, j
    if i < n:
        v, pos = a, i
    while pos < len(v):
        c[k] = v[pos]
        pos += 1
        k += 1
    return c


# -----------------------

def extra(cadena):
    letras = "abcdefghijkmñlopqrstuvwxyzaeiouáéíóú"
    mayus = letras.upper()
    cadena = cadena.lower()
    rango = len(cadena)
    n = 1
    for i in range(rango):
        if cadena[i] in letras:
            n += 1
    return n


def menu():
    print("1-")
    print("2-")
    print("3-")
    print("4-")
    print("5-")
    print("6-")
    print("7-")
    print("8-Salir")
    sep()
    op = validar_rango(1, 8, "Ingrese opcion del menu: ")
    return op


# Manipulacion de archivos

# Funcion Buscar
def buscar(fd, m, patente):
    t = os.path.getsize(fd)

    fp_inicial = m.tell()
    m.seek(0, io.SEEK_SET)

    posicion = -1
    while m.tell() < t:
        fp = m.tell()
        auto = pickle.load(m)
        if auto.patente == patente:
            posicion = fp
            break
    m.seek(fp_inicial, io.SEEK_SET)
    return posicion


def alta(fd):
    m = open(fd, "a+b")
    patente = input(": ")
    pos = buscar(fd, m, patente)
    if pos == -1:
        modelo = int(input("Modelo: "))
        aut = ClaseParaCrearElObjeto()
        pickle.dump(aut, m)
        m.flush()
        print("Registros grabado en el archivo...")
    else:
        print("Patente repetida... alta rechazada")


def modificacion(fd):
    if not os.path.exists(fd):
        print("El archivo", fd, "no existe... use la opcion 1 para crearlo y grabarle registros...")
        print()
        return
    m = open(fd, "r+b")

    patente = input("Patente del automovil a modificar su estado(carge 0 para salir): ")
    while patente != "0":
        pos = buscar(fd, m, patente)
        if pos != -1:
            m.seek(pos, io.SEEK_SET)
            aut = pickle.load(m)

            print()
            print("El registro actualmente grabado es: ")
            to_string(aut)

            if aut.estado == 0:
                print("El automovil ya fue vendido")
            else:
                aut.estado = 0
                m.seek(pos, io.SEEK_SET)
                pickle.dump(aut, m)
                print()
                print("EL automovil cambio su estado a vendido...")
        else:
            print("Ese registro no existe en el archivo...")
        input("Presione para seguir")
        patente = input("Otra patente a modificar su estado(cargue 0 para salir): ")

    m.close()


def listado_completo(fd):
    if not os.path.exists(fd):
        print("El archivo", fd, "no existe... use la opcion 1 para crearlo y grabarle registros...")
        print()
        return
    tbm = os.path.getsize(fd)
    m = open(fd, "rb")
    print("Listado general de automoviles registrados: ")
    while m.tell() < tbm:
        aut = pickle.load(m)
        to_string(aut)

    m.close()

    print()
    input("Presione para seguir...")


def principal():
    v = []
    fd = "vector.dat"
    op = -1
    while op != 8:
        op = menu()
        if op == 1:

            sep()
        elif op == 2:
            if len(v) != 0:
                pass
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 3:
            if len(v) != 0:
                pass
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 4:
            if len(v) != 0:
                pass
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 5:
            if len(v) != 0:
                pass
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 6:
            sep()
        elif op == 7:
            sep()
        elif op == 8:
            print("Gracias por utilizar el programa!")
            sep()


# Script princial...
if __name__ == '__main__':
    principal()
