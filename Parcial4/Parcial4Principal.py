from Parcial4Modulos import *
from Parcial4Principal import *


# Una compañía minera dedicada a la explotación de áridos desea un programa para gestionar los
# datos de las extracciones de minerales. Por cada extracción realizada se tienen los siguientes
# datos: CODIGO (un número entero que se asigna como identificador), PESO (un número entero que
# indica las toneladas extraídas y que va de 1 al 10 ambos valores inclusive), DESCRIPCION
# (un string que contiene una breve descripción de la extracción), VOLUMEN (un número entero que
# indica la cantidad de metros cúbicos removidos y que va del 1 al 20 ambos valores inclusive).
# Se pide definir el tipo registro Extraccion con los campos pedidos, y desarrollar un programa
# en Python controlado por un menú de opciones que permita gestionar las siguientes tareas:

# 1- Cargar un arreglo de registros con los datos de n extracciones de manera que en
# todo momento se mantenga ordenado por descripción, para esto debe utilizar el algoritmo de
#  inserción ordenada con búsqueda binaria (Se considerará directamente incorrecta la solución
#  basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de
#  inserción ordenada pero con búsqueda secuencial). Valide que el peso y el volumen estén
#  dentro de los valores descriptos y recuerde que estos son números enteros. Puede hacer la
#  carga en forma manual, o puede generar los datos en forma automática (con valores aleatorios)
#  (pero si hace carga manual, TODA la carga debe ser manual, y si la hace automática entonces
#  TODA debe ser automática).

# 2- Mostrar el contenido del vector a razón de un registro por línea.

# 3- A partir del vector, mostrar los datos de todos los registros cuyo peso se encuentre dentro
# de un rango de dos valores cargados desde teclado. Es decir, se cargan dos valores desde
# teclado y debe mostrar todos los registros que tengan un peso dentro de esos dos valores.

# 4- A partir del vector, generar un matriz para contar la cantidad de extracciones realizadas
# (matriz de conteo de 10 * 20 contadores) de manera que cada fila represente un peso posible
# y cada columna un volumen. Al finalizar la generación de la matriz, muestre sus datos, pero
# solo en aquellos casos en los que se encuentren valores mayores a cero.

# 5- Generar un archivo con todas las extracciones que tengan un volumen mayor a un valor
# cargado desde teclado.

# 6- Mostrar el contenido del archivo generado en el punto anterior a razón de un registro
# por línea.


def principal():
    v = []
    fd = "minerales.dat"
    op = -1
    while op != 7:
        op = menu()
        if op == 1:
            print("Ingrese n cantidad de materiales a registrar: ")
            n = validar_pos(0)
            v = carga_datos(v, n)
            print("Datos cargados con exito!")
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
                inf = int(input("Ingrese peso inferior: "))
                sup = int(input("Ingrese peso superior: "))
                rango3(v, inf, sup)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v) != 0:
                mat = matriz(v)
                escribir_matriz(mat)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 5:
            if len(v) != 0:
                x = int(input("Ingrese condicion de volumen a cargar en el archivo: "))
                crear_archivo(v, fd, x)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:
            if len(v) != 0:
                mostrar_archivo(fd)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 7:
            print("Gracias por utilizar el programa!")
            sep()


if __name__ == '__main__':
    principal()
