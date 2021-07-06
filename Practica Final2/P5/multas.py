class Multas:
    def __init__(self, id, patente, tipo, importe):
        self.id = id
        self.patente = patente
        self.tipo = tipo
        self.importe = importe


def to_string(multa):
    r = ""
    r += "{:<20}".format("ID: " + str(multa.id), end="  ")
    r += "{:<30}".format("Patente: " + str(multa.patente), end="  ")
    r += "{:<30}".format("tipo: " + str(multa.tipo), end="  ")
    r += "{:<30}".format(" importe: " + str(multa.importe))
    print()
    print(r)