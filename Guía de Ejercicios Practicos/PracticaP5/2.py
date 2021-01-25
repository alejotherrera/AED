import random, os, pickle

#Centro de restauracion de arte

class Obrasdearte:
    def __init__(self, id, nombre, pais, precio):
        self.id = id
        self.nombre = nombre
        self.pais = pais
        self.precio = precio


def to_string(v):
    r = ""
    r += "{:<20}".format("Identificacion: " + str(v.id))
    r += "{:<20}".format("Nombre: " + str(v.nombre))
    r += "{:<25}".format("Pais: " + str(v.pais))
    r += "{:<25}".format("Precio: " + str(v.precio))
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
    for i in range(n):
        nombre = random.choice(nombres)
        id = random.randint(1,1000)
        pais = random.randint(0,49)
        precio = random.randint(100,10000)
        new = Obrasdearte(id, nombre, pais, precio)
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
        n = int(input("Ingrese valor(mayor a " + str(a) + "):"))
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
        if v[i].pais != 1:
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


def busqueda_secuencial(matriz, c,fila,col):
    for i in range(fila):
        for j in range(col):
            if matriz[i][j] == c:
                return
    return -1


def extra(cadena):
    letras = "abcdefghijkmñlopqrstuvwxyzaeiouáéíóú"
    vocales = "aeiouáéíóú"
    cadena = cadena.lower()
    rango = len(cadena)
    cont_vocales = 0
    cont_letras = 0
    for i in range(rango):
        if cadena[i] in letras:
            cont_letras += 1
            if cadena[i] in vocales:
                cont_vocales += 1
    porcentaje_vocales = cont_vocales * 100 / cont_letras
    return porcentaje_vocales

def menu():
    print("1-Carga de datos")
    print("2-Ordenar el arreglo")
    print("3-Crear un archivo")
    print("4-Mostrar el archivo")
    print("5-Buscar en el arreglo")
    print("6-Matriz")
    print("7-Ingresar cadena")
    print("8-Salir")
    print()
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
            v = carga(v,n)
            mostrar(v)
            sep()
        elif op == 2:
            if len(v) != 0:
                ordenamientodirecto(v)
                print("Obras de teatro: ")
                mostrar(v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 3:
            if len(v) != 0:
                x = 2
                crear_archivo(v,fd,x)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v) != 0:
                mostrar_archivo(fd)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 5:
            if len(v) != 0:
                nom = input("Ingrese busqueda nombre de la obra a buscar: ")
                res = busqueda_secuencial(v,nom)
                if res != -1:
                    to_string(v[res])
                else:
                    print("No se encontro una obra con tal nombre")
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:

                sep()
        elif op == 8:
            print("Gracias por utilizar el programa!")
            sep()
        elif op == 7:
            cadena = input("Ingrese una cadena para que sea analizada: ")
            porcentaje_vocales = extra(cadena)
            print("El porcentaje total de vocales es: ",porcentaje_vocales,"%")


if __name__ == '__main__':
    principal()