
from modulo5 import *

def principal():
    v = []
    v2 = []
    fd = "productoservicio.dat"
    op = -1
    while op != 8:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            v = carga(v,n)
            print("Carga completa...")
            sep()
        elif op == 2:
            if len(v) != 0:
                print("Arreglo ordenado... mostrando...")
                v = ordenamiento_directo(v)
                mostrar(v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 3:
            if len(v) != 0:
                v2 = nuevo_arreglo(v,v2)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v2) != 0:
                mostrar(v2)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 5:
            if len(v2) != 0 and len(v) != 0:
                x = int(input("Ingrese precio a limitar"))
                mostar_segunp(v2,x)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:
            crear_archivo(v2,fd)
            sep()
        elif op == 7:
            mostrar_archivo(fd)
            sep()
        elif op == 8:
            print("Gracias por utilizar el programa!")
            sep()

#Script princial...
if __name__ == '__main__':
    principal()
