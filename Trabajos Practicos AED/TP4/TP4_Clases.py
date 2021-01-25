__author__ = "Herrera Alejo/Galanti Matias/Dellamas Agustin -  Grupo: TP4-G139"


class paises:
    def __init__(self, confederacion, nombre, puntos, campeonatos):
        self.confederacion = confederacion
        self.nombre = nombre
        self.puntos = puntos
        self.campeonatos = campeonatos


def write_first(vector):
    m = ""
    if vector.confederacion == 0:
        m += "{:<18}".format(str("UEFA"))
    elif vector.confederacion == 1:
        m += "{:<18}".format(str("CONMEBOL"))
    elif vector.confederacion == 2:
        m += "{:<18}".format(str("CONCACAF"))
    elif vector.confederacion == 3:
        m += "{:<18}".format(str("CAF"))
    elif vector.confederacion == 4:
        m += "{:<18}".format(str("AFC"))
    else:
        m += "{:<18}".format(str("OFC"))
    m += "{:<30}".format(str(vector.nombre))
    m += "{:<10}".format(str(vector.puntos))
    m += "{:<15}".format(str(vector.campeonatos))
    print(m)


class newvectorC:
    def __init__(self, nombre, puntos, campeonatos):
        self.nombre = nombre
        self.puntos = puntos
        self.campeonatos = campeonatos