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
    r += "{:<20}".format("ID: " + str(Medicamento.id), end="  ")
    r += "{:<30}".format("  Descripcion: " + str(Medicamento.descripcion), end="  ")
    r += "{:<30}".format(" Nombre: " + str(Medicamento.nombre), end="  ")
    r += "{:>15}".format(" Monto: $" + str(Medicamento.monto), end="  ")
    r += "{:>30}".format(" Tipo:  " + str(Medicamento.tipo), end="  ")
    r += "{:>30}".format(" Avales:  " + str(Medicamento.avales))
    print()
    print(r)

