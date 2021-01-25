__author__ = "Grupo: TP3-G233 (Herrera Alejo Tomas 85969, Dellamas Agustin 87360)"

import random


# Trabajo Practico N°3

# Modulos

# Definir clases---------------------------------
class participantes:
    def __init__(self, nombre, continente, ranking):
        self.nombre = nombre
        self.continente = continente
        self.ranking = ranking


class carga_cruces:
    def __init__(self, nombre1, nombre2, punto1, punto2, ranking1, ranking2, continente1, continente2):
        self.nombre1 = nombre1
        self.ranking1 = ranking1
        self.continente1 = continente1
        self.punto1 = punto1

        self.nombre2 = nombre2
        self.continente2 = continente2
        self.ranking2 = ranking2
        self.punto2 = punto2


# -------------------------------------------------
def random_name(vector):
    nombres = ["AED", "MAD", "ALG", "SOR", "ACO", "AM1", "ASI", "AM2", "SSL", "PPR", "SOP", "DSI", "COM", "GDA", "SIM",
               "ECO"]
    pas = True
    for i in range(len(vector)):
        for j in range(len(nombres)):
            if vector[i].nombre == nombres[j] and pas:
                pas = False
            elif vector[i].nombre == nombres[j]:
                nombres = random.choice(nombres)


# Carga del vector---------------------------------
def carga_vector():
    print("-" * 10, "Generacion de datos aleatorios", "-" * 10)
    precarga = ["AED", "MAD", "ALG", "SOR", "ACO", "AM1", "ASI", "AM2", "SSL", "PPR", "SOP", "DSI", "COM", "GDA", "SIM",
                "ECO"]
    v_participantes = [0] * 16
    for i in range(len(v_participantes)):
        nombre = precarga[i]
        continente = random.randint(0, 4)
        ranking = random.randint(1, 30)
        v_participantes[i] = participantes(nombre, continente, ranking)
    print("\t\tGenerando datos, porfavor espere")
    print("\t", "-" * 5, "¡Generacion de datos completa!", "-" * 5)
    separacion()
    return v_participantes


# -------------------------------------------------
# Determinar Item1---------------------------------
def cant_continente(vector_participantes):
    part_porlugar = [0] * 5
    for i in range(len(vector_participantes)):
        if vector_participantes[i].continente == 0:
            part_porlugar[0] += 1
        elif vector_participantes[i].continente == 1:
            part_porlugar[1] += 1
        elif vector_participantes[i].continente == 2:
            part_porlugar[2] += 1
        elif vector_participantes[i].continente == 3:
            part_porlugar[3] += 1
        else:
            part_porlugar[4] += 1
    print("Verificando cantidad de participantes por continentes")
    print("Participantes de America: ", part_porlugar[0])
    print("Participantes de Europa: ", part_porlugar[1])
    print("Participantes de Asia: ", part_porlugar[2])
    print("Participantes de África: ", part_porlugar[3])
    print("Participantes de Oceanía: ", part_porlugar[4])


# -------------------------------------------------
# Ordenamiento del vector a partir del ranking-----
def ordenamiento_ranking(vec):
    n = len(vec)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vec[i].ranking < vec[j].ranking:
                vec[i].ranking, vec[j].ranking = vec[j].ranking, vec[i].ranking
                vec[i].nombre, vec[j].nombre = vec[j].nombre, vec[i].nombre
                vec[i].continente, vec[j].continente = vec[j].continente, vec[i].continente
    return vec


# -------------------------------------------------
# -------------------------------------------------
def separacion():
    print("-" * 70)


# -------------------------------------------------

# Mostrar vector completo-------------------------
def escribir(participantes):
    p = ""
    p += "{:<20}".format("Nombre: " + str(participantes.nombre))
    p += "{:<20}".format("Continente: " + str(participantes.continente))
    p += "{:<20}".format("Ranking: " + str(participantes.ranking))
    print()
    print(p)


def mostrar(vector_participantes):
    for i in range(len(vector_participantes)):
        escribir(vector_participantes[i])


# -------------------------------------------------
# Generar Cruces-----------------------------------
def cruce(vector_datos):
    n = int(len(vector_datos))
    rango = int(n / 2)
    v_cruces = [0] * rango
    for i in range(rango):
        nombre1 = vector_datos[i].nombre
        continente1 = vector_datos[i].continente
        ranking1 = vector_datos[i].ranking
        punto1 = random.randint(10, 100)
        # --------------------------------------
        nombre2 = vector_datos[n - 1 - i].nombre
        continente2 = vector_datos[n - 1 - i].continente
        ranking2 = vector_datos[n - 1 - i].ranking
        punto2 = random.randint(10, 100)
        while punto1 == punto2:
            print("Empate, generando desempate")
            print("Entre:", nombre1, "y", nombre2)
            punto1 = random.randint(1, 100)
            punto2 = random.randint(1, 100)
        v_cruces[i] = carga_cruces(nombre1, nombre2, punto1, punto2, ranking1, ranking2, continente1, continente2)
    return v_cruces


# -------------------------------------------------
# Itempromedio---------------------------------------------
def promediopuntos(v_conpuntos):
    totalpuntos = 0
    n = len(v_conpuntos)
    for i in range(n):
        totalpuntos += v_conpuntos[i].punto1 + v_conpuntos[i].punto2
    totalpuntos = round((totalpuntos / (n * 2)), 2)
    return totalpuntos


# ---------------------------------------------------
# Verificar ganadores-------------------------------
def verify1(vector_cruce, tercerpuesto, segundopuesto):
    rango = int(len(vector_cruce))
    v_segundopuesto = [0] * 1
    v_tercerpuesto = [0] * rango
    v_participantes = [0] * rango
    i: int
    for i in range(rango):
        if vector_cruce[i].punto1 > vector_cruce[i].punto2:
            nombre = vector_cruce[i].nombre1
            continente = vector_cruce[i].continente1
            ranking = vector_cruce[i].ranking1
        else:
            nombre = vector_cruce[i].nombre2
            ranking = vector_cruce[i].ranking2
            continente = vector_cruce[i].continente2
        v_participantes[i] = participantes(nombre, continente, ranking)

        if segundopuesto:
            if vector_cruce[i].punto1 > vector_cruce[i].punto2:
                nombress = vector_cruce[i].nombre2
                rankings = vector_cruce[i].ranking2
                continentes = vector_cruce[i].continente2
            else:
                nombress = vector_cruce[i].nombre1
                continentes = vector_cruce[i].continente1
                rankings = vector_cruce[i].ranking1
            v_segundopuesto[i] = participantes(nombress, continentes, rankings)

        if tercerpuesto:
            if vector_cruce[i].punto1 < vector_cruce[i].punto2:
                nombret = vector_cruce[i].nombre1
                rankingt = vector_cruce[i].ranking1
                continentet = vector_cruce[i].continente1
            else:
                nombret = vector_cruce[i].nombre2
                rankingt = vector_cruce[i].ranking2
                continentet = vector_cruce[i].continente2
            v_tercerpuesto[i] = participantes(nombret, continentet, rankingt)
    if segundopuesto:
        return v_participantes, v_segundopuesto
    if tercerpuesto:
        return v_participantes, v_tercerpuesto
    return v_participantes


# -------------------------------------------------


# Muestra de datos---------------------------------
def escribir_cruce(vector_cruce):
    p = ""
    p += "{:<12}".format("Participante: " + str(vector_cruce.nombre1))
    b = "{:<12}".format("\tPuntos: " + str(vector_cruce.punto1))
    v = ""
    v += "{:<12}".format("Participante: " + str(vector_cruce.nombre2))
    c = "{:<12}".format("Puntos: " + str(vector_cruce.punto2))
    print()
    print(p, b, "VS\t", v, "\t ", c)


def escribir_seccion(vector_cruce):
    p = ""
    p += format(str(vector_cruce.nombre1))
    v = ""
    v += "{:<20}".format(str(vector_cruce.nombre2))
    print()
    print(p, "VS", v)


def escribir_podio(v, v1, v2):
    p = ""
    p += "{:<20}".format("Primer Puesto: " + str(v.nombre))
    m = ""
    m += "{:<20}".format("Segundo Puesto: " + str(v1.nombre))
    c = ""
    c += "{:<20}".format("Tercer Puesto: " + str(v2.nombre))
    print()
    print(p, m, c)


def mostrar_cruce(vector_cruce):
    for i in range(len(vector_cruce)):
        escribir_cruce(vector_cruce[i])


def mostrar_onlycruce(vector_cruce):
    for i in range(len(vector_cruce)):
        escribir_seccion(vector_cruce[i])


def mostrar_podio(v, v1, v2):
    for i in range(len(v)):
        escribir_podio(v[i], v1[i], v2[i])


def new_rank(v_primer, v_segundo, v_tercero, v_aux):
    for i in range(len(v_aux)):
        if v_aux[i].nombre == v_primer[0].nombre:
            v_aux[i].ranking += 25
        if v_aux[i].nombre == v_segundo[0].nombre:
            v_aux[i].ranking += 15
        if v_aux[i].nombre == v_tercero[0].nombre:
            v_aux[i].ranking += 5
    return v_aux
