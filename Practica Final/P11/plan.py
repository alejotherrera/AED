__author = "Alejo Herrera"


class Plan:
    def __init__(self, id, nombre, descripcion, monto, tipo, edades):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.monto = monto
        self.tipo = tipo
        self.edades = edades


def to_string(plan):
    r = ""
    r += "{:<10}".format("Id: " + str(plan.id), end="  ")
    r += "{:<20}".format(" Nombre: " + str(plan.nombre), end="  ")
    r += "{:<30}".format(" Descripcion: " + str(plan.descripcion), end="  ")
    r += "{:>15}".format(" Monto: $" + str(plan.monto), end="  ")
    r += "{:>30}".format(" Tipo: " + str(plan.tipo), end="  ")
    r += "{:>30}".format(" Edades: " + str(plan.edades))
    print()
    print(r)
