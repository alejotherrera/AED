__author__ = "Alejo Herrera/85969/1k04"

from modulos import *


# Menu de opciones

def principal():
    v = v2 = []
    x = ""
    fd = "planes.dat"
    op = -1
    while op != 9:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            v = carga(v, n, fd)
            print("Arreglo cargado con exito!!!!")
            sep()
        elif op == 2:
            if len(v) != 0:
                mostrar(v)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 3:
            if len(v) != 0:
                p = float(input("Ingrese valor a limitar: "))
                v2 = punto3(v, v2, p)
                print("Nuevo arreglo unidimensional creado!!!")
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 4:
            if len(v2) != 0:
                v2 = ordenamientodirecto(v2)
                mostrar(v2)
            else:
                print("Debe cargar los datos primero(opcion3)")
            sep()
        elif op == 5:
            if len(v) != 0:
                x = input("Ingrese nombre a buscar: ")
                res = busqueda_secuencial(v, x)
                if res != -1:
                    print("Nombre encontrado con exito...!!!")
                    print("Descripcion:", v[res].descripcion)
                    x = v[res].descripcion
                else:
                    print("No existe")
                    print("Cadena: ", x)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:
            if len(v2) != 0:
                k = int(input("Ingrese la clave de identificacion: "))
                res = busqueda_secuencial2(v2, k)
                if res != -1:
                    print("Clave encontrada...!!")
                    to_string(v[res])
                else:
                    print("Clave NO encontrada...!!")
            else:
                print("Debe cargar los datos primero(opcion3)")
            sep()
        elif op == 7:
            if len(v) != 0:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)
            else:
                print("Debe cargar los datos primero(opcion1)")

            sep()
        elif op == 8:
            if len(x) != 0:
                total = punto8(x)
                print("El total de palabras que cumple con los requisitos pedidos son: ", total)
            else:
                print("Debe utilizar el punto 5 del menu de opciones...!")
            sep()
        elif op == 9:
            print("Gracias por utilizar el programa!")
            sep()


# Script princial...
if __name__ == '__main__':
    principal()
