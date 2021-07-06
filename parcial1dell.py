def sep():
    print("=" * 30)


def menu():
    print("1-Carga de datos y determinacion por edades")
    print("2-Analisis de cadena")
    print("3-Salir")
    sep()
    op = validar_rango(1, 3, "Ingrese opcion del menu: ")
    return op


def validar_pos(a):
    n = a
    while n <= a:
        n = int(input("Ingrese valor n a cargar en el arreglo(mayor a " + str(a) + "):"))
        if n <= a:
            print("Error ingrese un valor mayor a:", a)
    return n


def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while inf > n or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Error... opcion invalida, ingrese entre " + str(inf) + " y " + str(sup))
    return n


def opcion1():
    # Carga de datos
    nombre1 = input("Ingrese nombre 1: ")
    edad1 = int(input("Ingrese edad 1: "))
    nombre2 = input("Ingrese nombre 2: ")
    edad2 = int(input("Ingrese edad 1: "))
    nombre3 = input("Ingrese nombre 3: ")
    edad3 = int(input("Ingrese edad 1: "))
    sep()
    # Pacientes mayores de 60(Grupo de riesgo)
    print("Listado de pacientes de riesgo: ")
    if edad1 > 60:
        print(nombre1)
    if edad2 > 60:
        print(nombre2)
    if edad3 > 60:
        print(nombre3)
    sep()
    #Pacientes menores a 21
    print("Menores a 21 años:")
    if edad1 < 21:
        print(nombre1)
    if edad2 < 21:
        print(nombre2)
    if edad3 < 21:
        print(nombre3)

def analisis_cadena(cadena):
    cant_x = cont_letras = 0
    for i in cadena:
        if i == "x" or i == "X":
            cant_x += 1
        cont_letras += 1
    promedio = cant_x * 100 / cont_letras
    promedio = 100 - promedio

    return promedio

def principal():
    op = -1
    while op != 3:
        op = menu()
        if op == 1:
            opcion1()
            sep()
        elif op == 2:
            cadena = input("Ingrese cadena a analizar: ")
            promedio = analisis_cadena(cadena)
            print(promedio)
            sep()
        elif op == 3:
           print("Gracias por utilizar el programa")


# Script princial...
if __name__ == '__main__':
    principal()