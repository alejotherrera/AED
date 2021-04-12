class Medicamento:
    def __init__(self, id, descripcion, director, monto, tipo, avales):
        self.id = id
        self.descripcion = descripcion
        self.director = director
        self.monto = monto
        self.tipo = tipo
        self.avales = avales


def to_string(Medicamento):
    r = ""
    r += "{:<10}".format("ID: " + str(Medicamento.id), end="  ")
    r += "{:<60}".format("  Descripcion: " + str(Medicamento.descripcion), end="  ")
    r += "{:<30}".format(" Director: " + str(Medicamento.director), end="  ")
    r += "{:<20}".format(" Monto: $" + str(Medicamento.monto), end="  ")
    r += "{:<20}".format(" Tipo: " + str(Medicamento.tipo), end="  ")
    r += "{:<20}".format(" Avales:  " + str(Medicamento.avales))
    print()
    print(r)