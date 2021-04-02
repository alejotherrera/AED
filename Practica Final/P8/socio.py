__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

class Socio:

    def __init__(self,numero, nombre, plan, monto):
        self.numero = numero
        self.nombre = nombre
        self.plan = plan
        self.monto = monto
        self.activo = True


def to_string(socio):
    txt = '{:<10}'.format(socio.numero)
    txt += '{:<45}'.format(socio.nombre)
    txt += '{:<5}'.format(socio.plan)
    txt += '${:10,.2f}'.format(socio.monto)
    return txt