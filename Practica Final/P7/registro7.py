#Registros

class Paquetes:
    def __init__(self, codigo, descripcion, costo, ciudad, destino):
        self.codigo = codigo
        self.descripcion = descripcion
        self.costo = costo
        self.ciudad = ciudad
        self.destino = destino


def to_string(inscripto):
    r = ""
    r += "{:<20}".format("codigo: " + str(inscripto.codigo), end="  ")
    r += "{:<35}".format("descripcion: " + str(inscripto.descripcion), end="  ")
    r += "{:<15}".format("costo :$" + str(inscripto.costo), end="  ")
    r += "{:>15}".format("ciudad: " + str(inscripto.ciudad), end="  ")
    r += "{:>30}".format("destino: " + str(inscripto.destino))
    print()
    print(r)
