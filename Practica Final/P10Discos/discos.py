class Disco:
    def __init__(self, titulo, artista, anio, genero, reproducciones):
        self.titulo = titulo
        self.artista = artista
        self.anio = anio
        self.genero = genero
        self.reproducciones = reproducciones


def to_string(disco):
    r = ""
    r += "{:<30}".format("titulo: " + str(disco.titulo), end="  ")
    r += "{:<30}".format("  artista: " + str(disco.artista), end="  ")
    r += "{:<30}".format(" Año: " + str(disco.anio), end="  ")
    r += "{:<30}".format(" genero: " + str(disco.genero), end="  ")
    r += "{:<30}".format("reproducciones: " + str(disco.reproducciones))
    print()
    print(r)
