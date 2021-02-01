#Registros
#Clases y to string
class Cobro:
    def __init__(self, id, nombre, monto, patente,hora):
        self.id = id
        self.nombre = nombre
        self.monto = monto
        self.patente = patente
        self.hora = hora

def to_string(inscripto):
    r = ""
    r += "{:<20}".format("NUMERO DE ID: " + str(inscripto.id), end="  ")
    r += "{:<35}".format("  PUESTO: " + str(inscripto.nombre), end="  ")
    r += "{:<15}".format("MONTO: " + str(inscripto.monto), end="  ")
    r += "{:>15}".format(" PATENTE: " + str(inscripto.patente), end="  ")
    r += "{:>30}".format("HORA: " + str(inscripto.hora))
    print(r)
    print(r)
