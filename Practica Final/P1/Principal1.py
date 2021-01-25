from Modulos1 import *

def principal():
    print("---------Bienvenidos al sistema de gestion de productos----------")
    v = []
    op = -1
    while op != 8:
        op = menu()
        if op == 1:
            n = int(input("Ingrese la cantidad de productos a cargar: "))
            v = carga(v,n)
            print("Vector generado!!")
            sep()
        elif op == 2:
            if len(v) != 0:
                v = ordenamientodirecto(v)
                mostrar(v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 3:
            if len(v) != 0:
                pass
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v) != 0:
                promedio_precio(v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 5:
            if len(v) != 0:
                nom = input("Ingrese nombre del producto a buscar: ")
                res = busqueda_secuencial(v,nom)
                if res != -1:
                    print("Datos encontrados")
                    to_string(v[res])
                    nuevo_precio = validar_pos(0)
                    v[res].precio = nuevo_precio
                    sep()
                    print("Precio actualizado: ")
                    to_string(v[res])
                else:
                    print("Error, producto no encontrado")
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:
            print("Gracias por utilizar el programa!")
            sep()


if __name__ == '__main__':
    principal()