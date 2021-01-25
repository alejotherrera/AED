__author__ = "Alejo Herrera"

import random


def carga_datos_aleatorios(cant):
    tupla_col = "Blanco", "Negro", "Azul"
    tupla_tipo = "Cuero", "Tela"
    n = list()
    c = list()
    e = list()
    t = list()
    for i in range(0, cant):
        n.append(random.randint(35, 40))
        c.append(random.choice(tupla_col))
        e.append(random.randint(10, 25))
        t.append(random.choice(tupla_tipo))
    return n, c, e, t


# Funcion que muestra las opciones  del menu
def menu():
    print("\n ESTADISTICAS ")
    print("1) Número de zapatillas promedio")
    print("2) Color de Preferencia entre 10 y 18 años")
    print("3) Material de  preferencia de los jóvenes entre 19 y 25 años")
    print("4) Demanda de cada número de calzado")
    print("5) El número de mayor y menor demanda")
    print("0) Salir del menu")



