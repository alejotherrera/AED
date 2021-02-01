# Principal
from modulos4 import *


def principal():
    v = []
    fd = "vector.dat"
    op = -1
    x = 0
    while op != 9:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            v = carga(v, n)
            print("Cobros cargados con exito!...")
            sep()
        elif op == 2:
            if len(v) != 0:
                print("Vector mostrado:")
                mostrar(v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 3:
            if len(v) != 0:
                v = ordenamientodirecto(v)
                cond = int(input("Ingrese numero a superar: "))
                print("Mostrando vector con monto menor a: ", cond)
                mostrar_condicion(v, cond)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v) != 0:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 5:
            if len(v) != 0:
                x = input("Ingrese nombre del puesto de cobro: ")
                crear_archivo(v, fd, x)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:
            if len(v) != 0:
                mostrar_archivo(fd)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 7:
            if len(v) != 0:
                p = input("Ingrese la patente del vehiculo: ")
                h = int(input("Ingrese hora registrada: "))
                res = busqueda_secuencial(v, p, h)
                if res != -1:
                    to_string(v[res])
                else:
                    print("No se han encontrado resultados")
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 8:
            if x != 0:
                cadena(x)
            else:
                print("Primero debe generar la cadena en el punto 5")
            sep()
        elif op == 9:
            print("Gracias por utilizar el programa!")
            sep()


if __name__ == '__main__':
    principal()
