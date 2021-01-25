from Registros import *
from Parcial4Modulos import *
from Parcial4Principal import *

class Mineral:
    def __init__(self, codigo, peso, descripcion, volumen):
        self.codigo = codigo
        self.peso = peso
        self.descripcion = descripcion
        self.volumen = volumen


def to_string(v):
    r = ""
    r += "{:<20}".format("Codigo: " + str(v.codigo))
    r += "{:<20}".format("peso: " + str(v.peso))
    r += "{:<25}".format("descripcion: " + str(v.descripcion))
    r += "{:<25}".format("volumen: " + str(v.volumen))
    print()
    print(r)