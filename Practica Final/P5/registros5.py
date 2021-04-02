# Clases

class ProductoServicio:
    def __init__(self, id, descripcion, tipo, calidad, precio):
        self.id = id
        self.descripcion = descripcion
        self.tipo = tipo
        self.calidad = calidad
        self.precio = precio


def to_string(inscripto):
    r = ""
    r += "{:<20}".format("NUMERO DE ID: " + str(inscripto.id), end="  ")
    r += "{:<30}".format("  descripcion: " + str(inscripto.descripcion), end="  ")
    r += "{:<15}".format("tipo: " + str(inscripto.tipo), end="  ")
    r += "{:>15}".format(" calidad: " + str(inscripto.calidad), end="  ")
    r += "{:>30}".format("precio: $ " + str(inscripto.precio))
    print()
    print(r)
