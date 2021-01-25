# Programa Principal


from Parcial5.modulos import *


def principal():
    v = []
    fd = "enviós.dat"
    op = -1
    while op != 8:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            v = carga(v, n)
            print("Datos cargados con exito!")
            sep()
        elif op == 2:
            if len(v) != 0:
                print("Datos del vector cargado: ")
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

                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 5:
            if len(v) != 0:

                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:
            if len(v) != 0:

                contador = crear_archivo(v, fd,1)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 7:
            if len(v) != 0 and contador != 0:
                mostrar_archivo(fd)
                print("La cantidad de envios mostrados fueron: ",contador)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 8:
            print("Gracias por utilizar el programa!!!!")
            sep()


if __name__ == "__main__":
    principal()
