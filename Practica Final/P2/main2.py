from modulos2 import *


def principal():
    cadena = ""
    v = []
    fd = "vector.dat"
    op = -1
    while op != 9:
        op = menu()
        if op == 1:
            n = validar_pos(0)
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
                nom = input("Ingrese nombre del director a buscar: ")
                cadena = busqueda_secuencial(v, nom)
                if cadena != "No existe":
                    print("Nombre encontrado con exito...")
                    print(cadena)
                else:
                    print("No existe")
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v) != 0:
                nom = (input("Ingrese id a buscar: "))
                res = busqueda_secuencial2(v, nom)
                if res != -1:
                    to_string(v[res])
                else:
                    agregar_medicamento(v, nom)
                    print("Identificacion agregada con exito!!")
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
                crear_archivo(v, fd)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 7:
            if len(v) != 0:
                mostrar_archivo(fd)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 8:
            if len(cadena) != 0:
                print("Cadena analizada!")
                analisis_cadena(cadena)
            else:
                print("Debe generar la cadena en el punto 3")
            sep()
        elif op == 9:
            print("Gracias por utilizar el programa!")


if __name__ == '__main__':
    principal()
