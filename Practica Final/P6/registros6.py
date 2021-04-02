#Registros


class Trabajos:
    def __init__(self, id, nombre, importe, destino,pago):
        self.id = id
        self.nombre = nombre
        self.importe = importe
        self.destino = destino
        self.pago = pago


def to_string(inscripto):
    r = ""
    r += "{:<20}".format("NUMERO DE ID: " + str(inscripto.id), end="  ")
    r += "{:<20}".format("  NOMBRE: " + str(inscripto.nombre), end="  ")
    r += "{:<15}".format("IMPORTE: " + str(inscripto.importe), end="  ")
    r += "{:>15}".format(" destino: " + str(inscripto.destino), end="  ")
    r += "{:>15}".format("pago: $ " + str(inscripto.pago))
    print()
    print(r)
