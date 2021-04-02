__author__ = "Alejo Herrera/85969/1k04"


# Clase constructora

class Plan:
    def __init__(self, id, nombre, descripcion, monto, plan, rango):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.monto = monto
        self.plan = plan
        self.rango = rango


# To String de la clase

def to_string(printer):
    r = ""
    r += "{:<30}".format("id: " + str(printer.id), end="  ")
    r += "{:<30}".format("nombre: " + str(printer.nombre), end="  ")
    r += "{:<35}".format("descripcion: " + str(printer.descripcion), end="  ")
    r += "{:<30}".format("monto: $" + str(printer.monto), end="  ")
    r += "{:<30}".format("plan: " + str(printer.plan), end="  ")
    r += "{:<30}".format("rango: " + str(printer.rango), end="  ")
    print()
    print(r)
