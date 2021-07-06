class Cobro:
    def __init__(self, id, puesto, monto, domino,hora):
        self.id = id
        self.puesto = puesto
        self.monto = monto
        self.domino = domino
        self.hora = hora

def to_string(obra):
    r = ""
    r += "{:<20}".format("ID: " + str(obra.id), end="  ")
    r += "{:<30}".format(" puesto: " + str(obra.puesto), end="  ")
    r += "{:<30}".format(" monto: " + str(obra.monto), end="  ")
    r += "{:<30}".format(" domino: " + str(obra.domino), end="  ")
    r += "{:<30}".format(" hora: " + str(obra.hora))
    print()
    print(r)
