import os, pickle, io
from auto import *


# Utilidad
def sep():
    print("-" * 30)


# Funcion Buscar
def buscar(fd, m, patente):
    t = os.path.getsize(fd)

    fp_inicial = m.tell()
    m.seek(0, io.SEEK_SET)

    posicion = -1
    while m.tell() < t:
        fp = m.tell()
        print(fp)
        auto = pickle.load(m)
        if auto.patente == patente:
            posicion = fp
            break

    m.seek(fp_inicial, io.SEEK_SET)
    return posicion


# Validaciones
def validar_entre(desde, hasta, mensaje):
    num = int(input(mensaje))
    while num < desde or num > hasta:
        print('Inválido! Debe ser un valor entre', desde, 'y', hasta)
        num = int(input(mensaje))
    return num


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


def alta(fd):
    m = open(fd, "a+b")
    patente = input("Patente del auto a regsitrar: ")
    pos = buscar(fd, m, patente)
    if pos == -1:
        modelo = int(input("Modelo: "))
        aut = Automoviles(patente, modelo)
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


def listado_filtrado(fd):
    if not os.path.exists:
        print("El archivo no existe, debe generarlo en el punto 1")
        return

    tbm = os.path.getsize(fd)
    m = open(fd, "rb")

    modelo = int(input("Modelo de atomovil para filtrar: "))
    print("Listado de automoviles disponibles conmodelo mayor a " + str(modelo))
    while m.tell() < tbm:
        aut = pickle.load(m)
        if aut.estado == 1 and aut.modelo > modelo:
            to_string(aut)

    m.close()

    print()
    input("Presione para continuar...")


def menu():
    op = -1
    print('Opciones del archivo de automoviles')
    print('   1. Alta de automoviles')
    print('   2. Modificación de estado de un automovil')
    print('   3. Listado completo de automoviles')
    print('   4. Listado de automoviles disponibles con modelo mayor a m')
    print('   5. Salir')
    sep()
    op = validar_rango(0, 5, "Ingrese opcion del menu de opciones: ")
    return op


def principal():
    fd = "automoviles.dat"
    op = 0
    while op != 5:
        op = menu()
        if op == 1:
            alta(fd)
            sep()
        elif op == 2:
            modificacion(fd)
            sep()
        elif op == 3:
            listado_completo(fd)
            sep()
        elif op == 4:
            listado_filtrado(fd)
            sep()
        elif op == 5:
            print("Gracias por utilizar el programa")
            sep()


# Script princial...
if __name__ == '__main__':
    principal()
