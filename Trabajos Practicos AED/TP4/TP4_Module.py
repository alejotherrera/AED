__author__ = "Herrera Alejo/Galanti Matias/Dellamas Agustin -   Grupo: TP4-G139"

import os.path
import time
import pickle
import random
from TP4_Clases import *


def separacion():
    print("-" * 40)


def show(vector):
    n = len(vector)
    p = "{:<18}".format("Confederacion")
    p += "{:<30}".format("Nombre")
    p += "{:<10}".format("Puntos")
    p += "{:<15}".format("Campeonatos")
    print(p)
    for i in range(n):
        write_first(vector[i])


def cargar_paises(v_a):
    confederacion = int(v_a[0])
    nombre = v_a[1]
    puntos = int(v_a[2])
    campeonatos = int(v_a[3])
    return paises(confederacion, nombre, puntos, campeonatos)



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




def add_in_orden_binary(vec, pais):
    n = len(vec)
    pos = 0
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].puntos == pais.puntos:
            pos = c
            break
        if pais.puntos < vec[c].puntos:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [pais]


def extraer_paises(nom):
    vector = []
    archive = open(nom, "rt")
    line = archive.readline()
    while line != "":
        v_a = line.split(",")
        pais = cargar_paises(v_a)
        add_in_orden_binary(vector, pais)
        line = archive.readline()
    archive.close()
    return vector


def op2(vector):
    max_campeonatos = 0
    for p in vector:
        if p.campeonatos > max_campeonatos:
            max_campeonatos = p.campeonatos
    print(end="El pais con mayor cantidad de campeonatos es"), time.sleep(0.5), print(end="."), time.sleep(0.5), print(
        end="."), time.sleep(0.5), print(".")
    for p in vector:
        if p.campeonatos == max_campeonatos:
            print(p.nombre, "con", p.campeonatos, "mundiales ganados en total")


def paises_conf_cpg(vector):
    cont = [0] * 6
    n = len(vector)
    for i in range(n):
        if vector[i].campeonatos > 0:
            if vector[i].confederacion == 0:
                cont[0] += 1
            elif vector[i].confederacion == 1:
                cont[1] += 1
            elif vector[i].confederacion == 2:
                cont[2] += 1
            elif vector[i].confederacion == 3:
                cont[3] += 1
            elif vector[i].confederacion == 4:
                cont[4] += 1
            else:
                cont[5] += 1
    print("Campeonatos por confederacion: ")
    print("UEFA:", cont[0])
    print("CONMEBOL:", cont[1])
    print("CONCACAF:", cont[2])
    print("CAF:", cont[3])
    print("AFC:", cont[4])
    print("OFC:", cont[5])


def create_conf(vector):
    nconf = validar_rango(0, 5, "Ingrese una condeferacion(entre 0 y 5): ")
    contregistros = 0
    newvector = []
    n = len(vector)
    for i in range(n):
        if nconf == vector[i].confederacion:
            nombre = vector[i].nombre
            puntos = vector[i].puntos
            campeonatos = vector[i].campeonatos
            newvector.append(newvectorC(nombre, puntos, campeonatos))
            contregistros += 1
    print("Cantidad de registros guardados: ", contregistros)
    return newvector, nconf


def binary_save(vector, conf):
    conf = str(conf)
    chearging = "clasificacion" + conf + ".dat"
    archive = open(chearging, "wb")
    for i in range(len(vector)):
        pickle.dump(vector[i], archive)
    print("Nombre del archivo: ", chearging)


def op5(vector):
    nconf = validar_rango(0, 5, "Ingrese una confederacion: ")
    narchive = "clasificacion" + str(nconf) + ".dat"
    if os.path.exists(narchive):
        print(10 * "-", "Archivo encontrado!", 10 * "-")
        a = open(narchive, 'rb')
        tam = os.path.getsize(narchive)
        while a.tell() < tam:
            binaryvector = pickle.load(a)
            to_stringdatos(binaryvector)
        a.close()
    else:
        separacion()
        print("Archivo no encontrado, generando...")
        newvector, nconf = create_conf(vector, nconf)
        binary_save(newvector, nconf)
        a = open(narchive, 'rb')
        tam = os.path.getsize(narchive)
        print("-" * 18, "Datos", "-" * 18)
        while a.tell() < tam:
            binaryvector = pickle.load(a)
            to_stringdatos(binaryvector)
        a.close()


def to_stringdatos(a):
    m = ""
    m += "{:<30}".format(str(a.nombre))
    m += "{:<10}".format(str(a.puntos))
    m += "{:<15}".format(str(a.campeonatos))
    print(m)


def menudeopciones():
    print("-" * 20, "MENU", "-" * 20)
    print("1. Mostrar el listado completo de países")
    print("2. Informar cuál es el país con mayor cantidad de campeonatos ganados")
    print("3. Determinar, para cada confederación, cuántos países ganaron algún campeonato.")
    print("4. Nuevo vector con los paises de un confederacion(ingresada por teclado la confederacion)")
    print("5. Ingresar una confederacion telcado y buscar su archivo de clasificacion")
    print("6. Prepara el fixture del proximo mundial")
    print("7. Buscar pais por nombre en el fixture del proximo mundial")
    print("8. Salir ")
    separacion()
    opcion = validar_rango(1,8,"Ingrese una opcion del menu: ")
    return opcion



def validate_name(vector, nombre):
    n = len(vector)
    for i in range(n):
        if vector[i].nombre == nombre.title():
            return nombre
    return -1


def preparar_proximofixture(vector):
    name = input("Ingrese nombre del pais a organizar: ")
    # --------------------
    pas = validate_name(vector, name)
    if pas == name:
        # CrearMatriz---------
        filas = 8
        columnas = 4
        fixture = [[None] * columnas for f in range(filas)]
        maspuntos = []
        menospuntos = []
        for i in range(36):
            if vector[i].nombre != name:
                if i < 8:
                    maspuntos.append(vector[i].nombre)
                else:
                    menospuntos.append(vector[i].nombre)
        cont = 0
        for i in range(filas):
            for j in range(columnas):
                if i == 0 and j == 0:
                    fixture[i][j] = [name]
                else:
                    if j == 0:
                        fixture[i][j] = [maspuntos[cont]]
                        cont += 1
                    else:
                        fixture[i][j] = nom = [random.choice(menospuntos)]
                        while validar_pais(fixture, filas, columnas, nom) == -1:
                            fixture[i][j] = nom = [random.choice(menospuntos)]
        mostrar_matriz(fixture)
        return fixture
    else:
        print("Pais no encontrado")


def validar_pais(matriz, filas, columnas, name):
    flag = False
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == name and not flag:
                flag = True
            elif matriz[i][j] and flag:
                return -1
    return name


def grup(i):
    if i == 0:
        grupo = "A"
    elif i == 1:
        grupo = "B"
    elif i == 2:
        grupo = "C"
    elif i == 3:
        grupo = "D"
    elif i == 4:
        grupo = "E"
    elif i == 5:
        grupo = "F"
    elif i == 6:
        grupo = "G"
    else:
        grupo = "H"
    return grupo


def mostrar_matriz(matriz):
    print("----------------Matriz hecha----------------")
    n = len(matriz)
    for i in range(n):
        grupo = grup(i)
        print("Grupo:" + grupo)
        print(matriz[i])


def buscar_nombre(fixture, nombre):
    for i in range(8):
        for j in range(4):
            if fixture[i][j] == [nombre]:
                return i
    return -1
