#Registros

class Producto:
    def __init__(self, id, nombre, tipo, precio):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio


def to_string(producto):
    r = ""
    r += "{:<20}".format("NUMERO DE ID: " + str(producto.id), end="  ")
    r += "{:<20}".format("  NOMBRE: " + str(producto.nombre), end="  ")
    r += "{:<15}".format("TIPO: " + str(producto.tipo), end="  ")
    r += "{:>15}".format(" PRECIO: " + str(producto.precio), end="  ")
    print(r)