__author__ = "Alejo Herrera"


class Automoviles:
    def __init__(self, patente, modelo):
        self.patente = patente
        self.estado = 1
        self.modelo = modelo


def to_string(automoviles):
    r = ""
    r += "{:<20}".format("Patente: " + str(automoviles.patente), end="  ")
    r += "{:<20}".format("  Estado: " + str(automoviles.estado), end="  ")
    r += "{:<15}".format(" Modelo: " + str(automoviles.modelo), end="  ")
    print()
    print(r)
