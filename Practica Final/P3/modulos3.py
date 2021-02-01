# Modulos

from registros3 import *
import os, pickle, random


# creando arreglo
def carga_vector(servicio, n):
    nom_servi = ('Gas', 'Agua', 'Alimentacion', 'Transporte Poblacional', 'Telecomunicaciones')
    cliente = ('ROBERTO', 'MARIO', 'JOSE', 'DARIO', 'LORENZO', 'JAVIER', 'CAMILO', 'JUAN', 'ALBERTO', 'DANIEL',
               'ALEJANDO', 'DAMIAN', 'EDUARDO')
    for i in range(n):
        id = random.randint(10000, 99999)
        descrip = random.choice(nom_servi)
        nom = random.choice(cliente)
        mon = random.randint(0, 10)
        tip = random.randint(0, 24)
        mec = random.randint(0, 4)
        new = Servicio(id, descrip, nom, mon, tip, mec)
        servicio.append(new)
    return servicio


def sep():
    print("-" * 30)


def mostrar(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def ordenamientodirecto(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].id > v[j].id:
                v[i], v[j] = v[j], v[i]
    return v


def ordenamientodirecto2(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].descripcion > v[j].descripcion:
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


def punto3(v):
    print("Datos: ")
    vector = ordenamientodirecto2(v)
    for i in range(len(vector)):
        if vector[i].mecanismo == 1 or vector[i].mecanismo == 4:
            to_string(vector[i])


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
        if a.monto > 0:
            to_string2(a)
    m.close()


def busqueda_secuencial(v, nom):
    for i in range(len(v)):
        if v[i].id == nom:
            return i
    return -1


def extra(cadena):
    hay_m = False
    hay_mi = False
    pal_con_mi = 0
    for i in range(len(cadena)):
        if cadena[i] != " " and cadena[i] != ".":
            if cadena[i] == "m" or cadena[i] == "M":
                hay_m = True
            else:
                if cadena[i] == "i" and hay_m:
                    hay_mi = True
                hay_m = False
        else:
            if hay_mi:
                pal_con_mi += 1
                hay_mi = False
    print("La cantidad de palabras con mi son: ", pal_con_mi)


def menu():
    print("1-Cargar servicios")
    print("2-Mostrar arreglo ordenado segun id")
    print("3-Mostrar un listado de los servicios cuyo mecanismo de pago sea 1 o 4 ordenado")
    print("4-Buscar un valor c por id")
    print("5-Matriz")
    print("6-Crear Factura y crear binario con factura")
    print("7-Mostrar archivo")
    print("8-Analizar cadena con ´mi´ ")
    print("9-Salir")
    sep()
    op = validar_rango(1, 9, "Ingrese opcion del menu: ")
    return op


def count(servicio):
    conteo = [[0] * 25 for f in range(5)]
    for i in servicio:
        c = i.tipo
        f = i.mecanismo
        conteo[f][c] += i.monto
    return conteo

def mostrar_matriz(servicio, conteo):
    print()
    for i in servicio:
        c = i.tipo
        f = i.mecanismo
        if conteo[f][c] > 0:
            print('\tEl monto acomulado con tipo de servicio ', c, ' y tipo de mecanismo de pago ', f, ' es: ', conteo[f][c])
    print()


#Opcion 6
# crear arreglo y generar archivo
def generar_automaticamente2(servicio, conteo):
    factura = []
    for i in range(len(conteo)):
        tip = servicio[i].tipo
        mec = servicio[i].mecanismo
        mon = conteo[mec][tip]
        if conteo[mec][tip] > 0:
            m = Factura(mon, tip, mec)
            factura.append(m)
    return factura

