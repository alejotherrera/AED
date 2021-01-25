# mandar a un modulo aparte para import
'''En un pueblo alejado de las zonas urbanas de Cordoba, el Intendente, ordeno crear un programa
que permita ver o mostrar todos los productos que se encuentran activos en la plataforma de
Mercado Libre, con sus respectivas ubicaciones, precio, cantidad y estado, sin la posiblidad de compra (SOLO MUESTRA).
Este mismo pidio que se puedan ver los articulos y se puedan ordenar por codigo, precio o cantidad,
ademas de poder buscar alguna publicacion por su codigo.

Ultimamente con los precios relativos que estan existiendo por la inflacion, el intendente pidio
que se puedan ver ciertos productos en un rango de precio.
Ademas, para llevar de pequeña estadistica, tambien pidio que se puedan ver la cantidad de productos por estado.

El programa debera tener un menu de opciones.'''
#Si se desea cargar otro modulo a este modulo, deberiamos colocar:
#from prueba import *
#Ahi, estariamos agregando todo el codigo, funciones, etc, del archivo llamado prueba

import random


class Producto:
    def __init__(self, codigo, precio, est, cant, ubi):
        self.codigo = codigo
        self.precio = precio
        self.estado = est
        self.cantidad = cant
        self.ubicacion = ubi


def write(producto):
    r = ""
    r += "{:<15}".format("Codigo: " + str(producto.codigo))
    r += "{:<20}".format("Precio: $" + str(producto.precio))
    r += "{:<20}".format("Estado: " + str(producto.estado))
    r += "{:<15}".format("Cantidad: " + str(producto.cantidad))
    r += "{:<20}".format("Ubicacion: " + str(producto.ubicacion))
    print()
    print(r)


def separar():
    print("-" * 100)


def validar_mayor(x, mensaje):
    n = int(input(mensaje))

    # Si quisieramos en un rango, por ejemplo entre el 0 y el 10 ---> while n <= x or n > 10:
    # Si quisieramos que fuera en menor, por ejemplo menor que 10 ---> while n > 10 (Aca podrian poner negativos, no se recomienda):

    while n <= x:
        print(15 * "-", "ERROR", 15 * "-")
        print("Por favor, ingrese un valor mayor a", x, ":")
        n = int(input(mensaje))
    return n


def carga_automatica(v):
    n = len(v)
    est = ("Nuevo", "Usado")
    for i in range(n):
        codigo = random.randint(1, 100)
        precio = round(random.uniform(10, 1000), 2)
        estado = random.choice(est)
        cantidad = random.randint(1, 10)
        ubicacion = random.randint(1, 23)
        v[i] = Producto(codigo, precio, estado, cantidad, ubicacion)
    separar()
    print("Productos creados con exito!")
    separar()


def mostrar_vector(v):
    n = len(v)
    for i in range(n):
        write(v[i])


def ordenar_vector(v):
    print("1 - Codigo \n2 - Precio \n3 - Cantidad")
    eleccion = int(input("\nLo desea ordenar por: "))
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if eleccion == 1:
                if v[i].codigo > v[j].codigo:
                    v[i], v[j] = v[j], v[i]
            # Es de muestra, no es necesario HACERLO --------------------------------------------------------------
            if eleccion == 2:
                if v[i].precio > v[j].precio:
                    v[i], v[j] = v[j], v[i]
            if eleccion == 3:
                if v[i].cantidad > v[j].cantidad:
                    v[i], v[j] = v[j], v[i]
    print("\nProductos ordenados")


def buscar_publicacion(v, x):
    n = len(v)
    for i in range(n):
        if x == v[i].codigo:
            return i
    return -1


def publicaciones_precios(v, pre1, pre2):
    n = len(v)
    print("Publicaciones en el rango de precios: ")
    for i in range(n):
        if v[i].precio > pre1:
            if v[i].precio < pre2:
                write(v[i])


def vector_acumulacion(v):
    n = len(v)
    v_ubi = [0] * 23
    for i in range(n):
        v_ubi[v[i].ubicacion - 1] += 1
    return v_ubi


def mostrar_v_ubi(v):
    n = len(v)
    print("Cantidad de publicaciones por ubicacion")
    for i in range(n):
        if v[i] != 0:
            print("\nUbicacion: ", i + 1)
            print("--->Total: ", v[i])

def mostrar_v_est(v):
    n = len(v)
    estado = ("Nuevo", "Usado")
    for i in range(n):
        print("\nTipo: ", estado[i])
        print("Cantidad: ", v[i])


def vector_conteo(v):
    n = len(v)
    v_est = [0] * 2
    for i in range(n):
        #Si fuera con numeros, int, se usaria practicamente la misma forma que en el punto 5.
        #Pondriamos v_est[v[i].estado] += 1
        #Teniendo en cuenta de que en estado hubieramos colocado 0 o 1
        if v[i].estado == "Nuevo":
            v_est[0] += 1
        else:
            v_est[1] += 1
    return v_est

def principal():
    # opc en -1 es para que inicie el menu
    opc = -1

    # Aca validamos que el usuario cargue un numero mayor que 0, le pasamos 2 parametro a la funcion validar_mayor
    n = validar_mayor(0, "Ingrese la cantidad de productos a crear: ")

    # Aca creamos el vector con una cantidad de n espacios que nos asigno el usuario
    v = n * [0]

    # Aca cargamos en todos los espacios informacion random para poder utilizar el programa
    carga_automatica(v)

    # Menu de opciones inicializado por opc = -1
    while opc != 0:
        print("1 - Mostrar los articulos ")
        # Mostrar la forma original o simple que van a pedir, solamente ordenar por Codigo (Ejemplo)
        print("2 - Ordenar los productos por categoria ")
        print("3 - Buscar publicacion por codigo")
        print("4 - Mostrar publicaciones en un rango de precio")
        print("5 - Mostrar la cantidad de productos que hay por Ubicacion")
        print("6 - Mostrar la cantidad de productos por estado")
        print("0 - Salir")
        opc = int(input("\nIngrese a donde desee ir:"))
        separar()

        if opc == 1:
            print("Publicaciones: ")
            mostrar_vector(v)
            separar()

        elif opc == 2:
            ordenar_vector(v)
            separar()

        elif opc == 3:
            x = int(input("Ingrese el codigo: "))
            busqueda = buscar_publicacion(v, x)
            if busqueda == -1:
                separar()
                print("\nNo se ha encontrado ninguna publicacion con el codigo", x, " :(\n")
                separar()
            else:
                write(v[busqueda])
                separar()

        elif opc == 4:
            pre1 = int(input("Ingrese el rango minimo (DESDE): "))
            pre2 = int(input("Ingrese el rango maximo (HASTA): "))
            separar()
            publicaciones_precios(v, pre1, pre2)
            separar()

        elif opc == 5:
            v_ubi = vector_acumulacion(v)
            mostrar_v_ubi(v_ubi)
            separar()

        elif opc == 6:
            v_est = vector_conteo(v)
            mostrar_v_est(v_est)
            separar()
        elif opc == 0:
            print("Fin del programa")

        else:
            print("\nError\n")


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    principal()
# Se utiliza este condicional medio "Raro" para inicializar el menu de manera automatica.
# Ya que si no pusieramos este condicional, practicamente o probablemente no iniciaria nuestro querido menu.
# En resumen, estamos preguntando si el nombre de nuestro archivo es igual a nuestro nombre de archivo, si es asi
# este mismo iniciara la funcion "principal()", que es nuestra funcion donde guardamos el MENU.
# Por ende, este condicional es muy importante. Ademas, que siempre va a devolver True ya que...
# nuestro archivo se llama como nuestro archivo ;) (Filosofia en programacion)
