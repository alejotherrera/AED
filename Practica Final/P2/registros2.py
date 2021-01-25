# Registros

class Medicamento:
    def __init__(self, id, descripcion, nombre, monto, tipo, avales):
        self.id = id
        self.descripcion = descripcion
        self.nombre = nombre
        self.monto = monto
        self.tipo = tipo
        self.avales = avales


def to_string(Medicamento):
    r = ""
    r += "{:<20}".format("NUMERO DE ID: " + str(Medicamento.id), end="  ")
    r += "{:<30}".format("  descripcion: " + str(Medicamento.descripcion), end="  ")
    r += "{:<30}".format("nombre: " + str(Medicamento.nombre), end="  ")
    r += "{:>15}".format(" monto: $" + str(Medicamento.monto), end="  ")
    r += "{:>30}".format("tipo:  " + str(Medicamento.tipo), end="  ")
    r += "{:>30}".format("avales:  " + str(Medicamento.avales))
    print(r)
