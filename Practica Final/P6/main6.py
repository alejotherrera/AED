from modulo6 import *

# Modulo principal

def principal():
    v = []
    fd = "vector.dat"
    op = -1
    while op != 6:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            v = carga(v,n)
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
                nom = input("Ingrese el nombre a buscar")
                res = busqueda_secuencial(v,nom)
                if res != -1:
                    to_string(v[res])
                else:
                    print("Nombre no encontrado")
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v) != 0:
                a = int(input("Limite inferior de factura: "))
                b = int(input("Limite superior de factura: "))
                crear_archivo(v,fd,a,b)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 5:
            if len(v) != 0:
                mostrar_archivo(fd)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:
            print("Gracias por utilizar el programa!!")
            sep()

#Script princial...
if __name__ == '__main__':
    principal()
