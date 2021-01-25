
# Registros
class Envios:
    def __init__(self, codigo, descripcion, destino, tipo, precio, pagos):
        self.codigo = codigo
        self.descripcion = descripcion
        self.destino = destino
        self.tipo = tipo
        self.precio = precio
        self.pagos = pagos


def to_string(v):
    r = ""
    r += "{:<20}".format("codigo: " + str(v.codigo))
    r += "{:<30}".format("descripcion: " + str(v.descripcion))
    r += "{:<20}".format("destino: " + str(v.destino))
    r += "{:<20}".format("tipo: " + str(v.tipo))
    r += "{:<20}".format("precio: " + str(v.precio))
    r += "{:<20}".format("pago: " + str(v.pagos))
    print()
    print(r)