#Herrera Alejo

class Servicio:
    def __init__(self, id, descrip, nombre, monto, tipo, mecanismo):
        self.id = id
        self.descripcion = descrip
        self.nombre = nombre
        self.monto = monto
        self.tipo = tipo
        self.mecanismo = mecanismo

def to_string(servicio):
    r = ''
    r += '{:<40}'.format('- Clave de identificación: ' + str(servicio.id))
    r += '{:<60}'.format('Nombre del servicio: ' + servicio.descripcion)
    r += '{:<40}'.format('Nombre del cliente: ' + servicio.nombre)
    r += '{:<40}'.format('Monto facturado: ' + str(servicio.monto))
    r += '{:<40}'.format('Tipo de servicio: ' + str(servicio.tipo))
    r += '{:<40}'.format('Mecanismo de pago: ' + str(servicio.mecanismo))
    print()
    print(r)

class Factura:
    def __init__(self, mon, tip, mec):
        self.monto = mon
        self.tipo = tip
        self.mecanismo = mec

def to_string2(factura):
    r = ''
    r += '{:<40}'.format('Monto facturado: ' + str(factura.monto))
    r += '{:<40}'.format('Tipo de servicio: ' + str(factura.tipo))
    r += '{:<40}'.format('Mecanismo de pago: ' + str(factura.mecanismo))
    print()
    print(r)
