from Utilidades.utilidades import *


def carga(n):
    print("Equipo: ", n)
    n = int(n)
    equipo = [0] * n
    puntos = [0] * n
    goles = [0] * n
    for i in range(n):
        separacion()
        equipo[i] = input("ingrese nombre del equipo: ")
        puntos[i] = int(input("puntos total obtenido en el torneo (maximo 20): "))
        goles[i] = int(input("ingrese total de goles anotados: "))
    return equipo, puntos, goles


def tabla(equipo, puntos, goles, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if puntos[i] < puntos[j]:
                puntos[i], puntos[j] = puntos[j], puntos[i]
                equipo[i], equipo[j] = equipo[j], equipo[i]
                goles[i], goles[j] = goles[j], goles[i]
    return equipo, puntos, goles


def write(equipo, puntos, goles):
    m = ""
    m += "{:<15}".format(str(equipo))
    m += "{:<15}".format(str(puntos))
    m += "{:<15}".format(str(goles))


def show(equipo, puntos, goles, n):
    for i in range(n):
        write(equipo[i], puntos[i], goles[i])


def main():
    n = int(input("Ingrese cantidad de equipos: "))
    equipo, puntos, goles = carga(n)
    equipo, puntos, goles = tabla(equipo, puntos, goles, n)
    separacion()
    #First requirement
    print("Tabla:")
    print("Equipo", "    ", "Puntos", "    ", "Goles")
    for i in range(n):
        m = ""
        m += "{:<15}".format(equipo[i])
        m += "{:<15}".format(puntos[i])
        m += "{:<15}".format(goles[i])
        print(m)
    separacion()
    #Second requirement
    print("Punteros de la liga: ")
    print("Equipo", "    ", "Puntos", "    ", "Goles")
    for i in range(3):
        m = ""
        m += "{:<15}".format(equipo[i])
        m += "{:<15}".format(puntos[i])
        m += "{:<15}".format(goles[i])
    #Third requirement
    

if __name__ == '__main__':
    main()
