class Plan:
    def __init__(self, id, nombre, descripcion, monto, tipo, rango):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.monto = monto
        self.tipo = tipo
        self.rango = rango


def to_string(Plan):
    r = ""
    r += "{:<20}".format("ID: " + str(Plan.id), end="  ")
    r += "{:<30}".format(" NOMBRE: " + str(Plan.nombre), end="  ")
    r += "{:<40}".format("DESCR: " + str(Plan.descripcion), end="  ")
    r += "{:<40}".format("IMPORTE: $ " + str(Plan.monto), end="  ")
    r += "{:<40}".format("TIPO: " + str(Plan.tipo), end="")
    r += "{:<40}".format("RANGO: " + str(Plan.rango))
    print()
    print(r)
