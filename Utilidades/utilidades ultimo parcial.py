import random, os, pickle


class Inscripto:
    def __init__(self, dni, nombre, curso, tipo, importe):
        self.dni = dni
        self.nombre = nombre
        self.curso = curso
        self.tipo = tipo
        self.importe = importe


def write(inscripto):
    r = ""
    r += "{:<20}".format("NUMERO DE DNI: " + str(inscripto.dni), end="  ")
    r += "{:<20}".format("  NOMBRE: " + str(inscripto.nombre), end="  ")
    r += "{:<15}".format("CURSO: " + str(inscripto.curso), end="  ")
    r += "{:>15}".format(" TIPO: " + str(inscripto.tipo), end="  ")
    r += "{:>30}".format("IMPORTE: $ " + str(inscripto.importe))
    print(r)


# 1
def load_registry(v, n):
    nombres = ("Bruno", "Mariel", "Bianca", "Juan Cruz", "Jorge", "Antonela", "Josefina", "Lea",
               "Aylen", "Exequiel", "Lilith", "Lou", "Luz", "Lautaro", "Tomas", "Azul", "Cecilia",
               "Agustin", "Mairene", "Angelo", "Angela", "Celeste", "Karen", "Ludmila", "Francisca")
    cursos = ("Pasteleria", "Mecanica", "Chef", "Idiomas", "Electricista", "Plomeria")
    for i in range(n):
        dni = random.randint(30000000, 40000000)
        nombre = random.choice(nombres)
        curso = random.choice(cursos)
        tipo_curso = random.randint(0, 29)
        importe = round(random.uniform(10, 10000), 2)
        inscripto = Inscripto(dni, nombre, curso, tipo_curso, importe)
        v.append(inscripto)
    return v


# 2
def order_v(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].dni > v[j].dni:
                v[i], v[j] = v[j], v[i]
    return v


def display_v(v):
    n = len(v)
    for i in range(n):
        write(v[i])


# 3
def load_file(fd, v, importe_max):
    n = len(v)
    m = open(fd, "wb")
    for i in range(n):
        if v[i].importe < importe_max:
            pickle.dump(v[i], m)
    print("\nArchivo generado con exito!")
    m.close()


# 4
def display_file(fd):
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    print("\nDatos del archivo:\n")
    while m.tell() < size:
        inscripto = pickle.load(m)
        write(inscripto)
    m.close()


# 5
def search_nom(v, nom):
    for i in range(len(v)):
        if v[i].nombre == nom:
            print("\nEl Incripto fue encontrado:")
            write(v[i])
            return
        print('\nEl inscripto que busca no fue encontrado.')


# 6
def cont(vec):
    cant = [0] * 30
    for i in range(len(vec)):
        cant[vec[i].tipo] += 1

    for i in range(len(cant)):
        if cant[i] != 0:
            print('Cantidad de inscriptos en el curso tipo[' + str(i) + ']:', cant[i])


# 7
def analisis_cadena(cad):
    cont = 0
    carac = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM0123456789'
    for i in cad:
        if i not in carac:
            cont += 1
    print('\nLa cantidad de caracteres que no eran letras son:', str(cont))


def main():
    opc = -1
    v = []
    fd = "inscriptos.dat"

    while opc != 0:
        print()
        print("1 - Cargar registro")
        print("2 - Ordenar y Mostrar arreglo")
        print("3 - Crear un archivo a partir de un monto base ")
        print("4 - Mostrar datos del archivo 'inscriptos.dat' ")
        print("5 - Buscar un inscripto por su nombre y mostrar sus datos")
        print("6 - Vector de conteo por tipo de curso")
        print("7 - Analisis de cadena")
        print("0 - Salir")
        print()
        opc = int(input("Ingrese a donde desee ir: "))
        print()

        if opc == 1:
            n = int(input("Ingrese la cantidad de inscriptos a cargar: "))
            load_registry(v, n)
        elif opc == 2:
            if not v:
                print("Primero debe cargar el arreglo")
            else:
                v = order_v(v)
                display_v(v)
        elif opc == 3:
            if not v:
                print("Primero debe cargar el arreglo")
            else:
                importe_max = int(input("Ingrese el importe maximo: "))
                load_file(fd, v, importe_max)
        elif opc == 4:
            if os.path.exists(fd):
                display_file(fd)
            else:
                print("Primero debe cargar el archivo")
        elif opc == 5:
            if not v:
                print("Primero debe cargar el arreglo")
            else:
                nom = input("Ingrese el nombre a buscar: ")
                search_nom(v, nom)
        elif opc == 6:
            if not v:
                print("Primero debe cargar el arreglo")
            else:
                print()
                cont(v)
        elif opc == 7:
            cad = input('Ingrese la cadena de caracteres a analizar:')
            analisis_cadena(cad)
        else:
            print("Error")


if __name__ == '__main__':
    main()