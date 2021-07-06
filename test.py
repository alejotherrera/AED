def sep():
    print("=" * 30)


def test():
    cont_apr = suma = cont_desr = 0
    n = input("Desea ingresar un alumno? s/n: ")
    print("=" * 30)
    if n == "s":
        repeat = True
    else:
        repeat = False
    while repeat == True:
        suma = 0
        for i in range(5):
            nota = int(input("Ingrese nota del ejercicio: "))
            suma += nota
        if suma >= 60:
            cont_apr += 1
        else:
            cont_desr += 1
        print("=" * 30)
        n = input("Desea ingresar otra alumno? s/n: ")
        if n == "s":
            repeat = True
        else:
            repeat = False
    print("Gracias por utilizar el programa")
    print("Alumnos aprobados: ", cont_apr)
    print("Alumnos desaprobados: ", cont_desr)


if __name__ == '__main__':
    test()
