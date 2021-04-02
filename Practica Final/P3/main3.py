# Principal

from modulos3 import *


# Menu de opciones


def principal():
    v = []
    fd = "servicios.dat"
    op = -1
    while op != 9:
        op = menu()
        if op == 1:
            n = int(input("Ingrese cantidad de servicios a cargar: "))
            v = carga(v, n)
            sep()
        elif op == 2:
            if len(v) != 0:
                mostrar(v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 3:
            if len(v) != 0:
                punto3(v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v) != 0:
                c = int(input("Ingrese id a buscar: "))
                res = busqueda_secuencial(v, c)
                if res != 0:
                    to_string(v[res])
                else:
                    print("No existe el id buscado...")
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 5:
            if len(v) != 0:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz, v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:
            if len(matriz) != 0:
                generar_archivofactura(matriz, v, fd)
            else:
                print("Debe generar la matriz en el punto 5")
            sep()
        elif op == 7:
            mostrar_archivo(fd)
            sep()
        elif op == 8:
            cadena = input("Ingrese la cadena a analizar: ")
            cant_pal = analisis_cadena(cadena)
            print("La cantidad de palabras en la cadena con mi es: ", cant_pal)
            sep()
        elif op == 9:
            print("Gracias por utilizar el programa!")
            sep()


# Script princial...
if __name__ == '__main__':
    principal()
