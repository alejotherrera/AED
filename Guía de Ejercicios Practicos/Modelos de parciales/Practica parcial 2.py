# Un coto de caza ha solicitado un programa para procesar los datos de los clientes
# que han asistido al predio para practicar la caza en ambientes controlados y permitidos.
# Por cada Cliente se conoce su nombre, cantidad de acompañantes, tipo de trofeo de caza
# (un valor del 0 al 14) que obtuvo y el precio total que debe abonar. Se desea almacenar
# la información referida a los n clientes en un arreglo de registros de tipo Cliente
# (definir el tipo Cliente y cargar n por teclado).

# Se pide desarrollar un programa en Python controlado por un menú de opciones,  que permita
# gestionar las siguientes tareas:

# 1-Cargar el arreglo con los datos de los n clientes. Valide que el precio total a abonar sea
#  mayor a cero y que el tipo de trofeo de caza esté en el rango especificado. Puede hacer la
#  carga en forma manual, o puede generar los datos en forma automática (con valores aleatorios)
#  o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

# 2-Mostrar todos los datos de todos los clientes, en un listado ordenado de menor a mayor, según
#  el precio a pagar.

# 3-Determinar el total que se ganó por cada tipo de pieza de trofeo, 15 acumuladores en total con
#  un vector de acumulacion.

# 4-Determinar y mostrar los datos del cliente con mayor cantidad de acompañantes. Si ese cliente
#  pagó un precio inferior al valor p que se carga por teclado, cargar un nuevo precio, asignarlo
#  en el registro del cliente, y volver a mostrar sus datos.

# 5-Determinar si existe un cliente cuyo nombre sea igual x, siendo x un valor que se carga por teclado.
#  Si existe, mostrar sus datos. Si no existe, informar con un mensaje. Si existe más de un registro
#  que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.

import random


def separacion():
    print("-" * 100)


class Cliente:
    def __init__(self, nombre, acompañante, trofeo, precio):
        self.nombre = nombre
        self.acompañante = acompañante
        self.trofeo = trofeo
        self.precio = precio


def mostrar(Cliente):
    m = ""
    m += "{:<20}".format("Nombre: " + str(Cliente.nombre))
    m += "{:<20}".format("acompañante: " + str(Cliente.acompañante))
    m += "{:<20}".format("trofeo: " + str(Cliente.trofeo))
    m += "{:<20}".format("precio: " + str(Cliente.precio))
    print(m)


def carga_auto():
    n = int(input("Ingrese cantidad de clientes: "))
    vector = [0] * n
    nombres = ("Jorge", "Mario", "Alejo", "Gustavo", "Valerio")
    for i in range(len(vector)):
        nombre = random.choice(nombres)
        acompañante = random.randint(1, 10)
        trofeo = random.randint(0, 14)
        precio = random.randint(1000, 10000)
        vector[i] = Cliente(nombre, acompañante, trofeo, precio)
    separacion()
    print("Clientela generada con exito!")
    separacion()
    return vector


def ordenamiento(vector):
    n = len(vector)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vector[i].precio > vector[j].precio:
                vector[i], vector[j] = vector[j], vector[i]
    print("Productos ordenados por precio")

def totaltrofy(vector):
    n = len(vector)



def main():
    vector = carga_auto()
    ordenamiento(vector)
    for i in range(len(vector)):
        print(mostrar(vector[i]))


if __name__ == "__main__":
    main()
