class Servicio:
    def __init__(self, id, descripcion, cliente, monto,tipo,mecanismo):
        self.id = id
        self.descripcion = descripcion
        self.cliente = cliente
        self.monto = monto
        self.tipo = tipo
        self.mecanismo = mecanismo


def to_string(servicio):
    r = ""
    r += "{:<20}".format(" ID: " + str(servicio.id), end="  ")
    r += "{:<30}".format("  Descripciones: " + str(servicio.descripcion), end="  ")
    r += "{:<30}".format(" CLIENTE: " + str(servicio.cliente), end="  ")
    r += "{:<20}".format(" MONTO: " + str(servicio.monto), end="  ")
    r += "{:<20}".format(" TIPO: " + str(servicio.tipo), end="  ")
    r += "{:<30}".format(" MECANISMO: " + str(servicio.mecanismo))
    print()
    print(r)


class Factura:
    def __init__(self,servicio,mecanismo,importe):
        self.servicio = servicio
        self.mecanismo = mecanismo
        self.importe = importe

def to_string2(factura):
    r = ""
    r += "{:<20}".format("SERIVICO: " + str(factura.servicio), end="  ")
    r += "{:<30}".format("MECANISMO: " + str(factura.mecanismo), end="  ")
    r += "{:<30}".format("importe: $" + str(factura.importe))
    print()
    print(r)