class Profesionales:
    def __init__(self, dni, nombre, importe, tipo_afiliacion, tipo_trabajo):
        self.dni = dni
        self.nombre = nombre
        self.importe = importe
        self.tipo_afiliacion = tipo_afiliacion
        self.tipo_trabajo = tipo_trabajo


def to_string(profesional):
    r = ""
    r += "{:<20}".format("DNI: " + str(profesional.dni))
    r += "{:<20}".format("Nombre: " + str(profesional.nombre))
    r += "{:<25}".format("Importe: $ " + str(profesional.importe))
    r += "{:<25}".format("Tipo de afiliacion: " + str(profesional.tipo_afiliacion))
    r += "{:<20}".format("Tipo de trabajo: " + str(profesional.tipo_trabajo))
    print(r)
