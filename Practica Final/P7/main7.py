from modulo7 import *


def principal():
    v = []
    v2 = []
    fd = "vector.dat"
    op = -1
    while op != 10:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            v = carga(v, n)
            print("Datos generados con exito!!!")
            sep()
        elif op == 2:
            if len(v) != 0:
                print("Mostrando archivo...")
                mostrar(v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 3:
            if len(v) != 0:
                v2 = punto3(v, v2)
                print("Arreglo nuevo creado con exito!!")
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v) != 0:
                mostrar(v2)
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
                x = int(input("Ingrese codigo de paquete: "))
                res = binary_search(v, x)
                if res != -1:
                    to_string(v[res])
                else:
                    print("El codigo de paquete no fue encontrado!...")
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 7:
            if len(v2) != 0:
                costo = int(input("Ingrese costo de paquete a buscar: "))
                res = busqueda_secuencial(v2, costo)
                if res != -1:
                    to_string(v2[res])
                else:
                    print("Paquete segun costo mayor no encontrado...")
            else:
                print("Debe generar el vector en el punto 3")
            sep()
        elif op == 8:
            if len(v) != 0:
                crear_archivo(v,fd)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 9:
            if len(v) != 0:
                mostrar_archivo(fd)
            else:
                print("Debe cargar los datos primero(opcion1)")
            sep()
        elif op == 10:
            print("Gracias por utilizar el programa!")
            sep()



# Script princial...
if __name__ == '__main__':
    principal()
