# Registros

class Medicamento:
    def __init__(self, id, descripcion, director, monto, tipo, avales):
        self.id = id
        self.descripcion = descripcion
        self.director = director
        self.monto = monto
        self.tipo = tipo
        self.avales = avales

def to_string(medicamento):
    r = ""
    r += "{:<20}".format("id: " + str(medicamento.id), end="  ")
    r += "{:<30}".format("  descripcion: " + str(medicamento.descripcion), end="  ")
    r += "{:<30}".format(" director: " + str(medicamento.director), end="  ")
    r += "{:<30}".format("monto: $" + str(medicamento.monto), end="  ")
    r += "{:<30}".format("tipo: $" + str(medicamento.tipo), end="  ")
    r += "{:<30}".format("avales: $" + str(medicamento.avales))
    print()
    print(r)
