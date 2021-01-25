#3- major league baseball
import random
def sep():
    print("-"*30)

class Jugador:
    def __init__(self,nombre,pos,hits):
        self.nombre = nombre
        self.posicion = pos
        self.hits = hits

def to_string(jugador):
    return 'Jugador ' + jugador.nombre + \
           ' juega en la posicion ' + str(jugador.posicion) + \
           ' y ha llegado a primera base ' + str(jugador.hits) + ' veces'


def cargar_nombre(vector):
    nombres = ['pra', 'con', 'lis', 'cam', 'man', 'are', 'atro', 'pac', 'ino']
    existe = 1
    nombre = ''
    while existe == 1:
        nombre = random.choice(nombres) + random.choice(nombres) + random.choice(nombres) + ' ' + \
                 random.choice(nombres) + random.choice(nombres) + random.choice(nombres)
        existe = validar_si_existe_jugador(vector, nombre)
        if existe == 1:
            print('Error!!! Ese jugador ya se encuentra cargado, se va a generar uno nuevo')
    return nombre

def validar_si_existe_jugador(vector, nombre):
    for elemento in vector:
        if elemento.nombre == nombre:
            return 1
    return 0

def carga_vector(vector,n):
    for i in range(n):
        nombre = cargar_nombre(vector)
        posicion = random.randint(1,9)
        hits = random.randint(0,20)
        jugador = Jugador(nombre,posicion,hits)
        vector.append(jugador)

def display(vector):
    print("Listado de jugadores: ")
    sep()
    for elemento in vector:
        print(to_string(elemento))


def crear_martiz(vector):
    matriz = [[0] * 20 for i in range(9)]
    for  elemento in vector:
        fila = elemento.posicion - 1
        columna = elemento.hits - 1
        matriz[fila][columna] += 1
    return matriz


def validate_rango(inf,sup,mensaje):
    numero = inf -1
    while numero <= inf or numero >= sup:
        numero = int(input(mensaje))
        if numero<= inf or numero>= sup:
            print("Error,carge de nuevo valores de ",inf," hasta ",sup)
    return numero

def cantidad_total(matriz,pos):
    total = 0
    fila = pos - 1
    for j in range(len(matriz[fila])):
        total += matriz[fila][j]
    return total

def menu():
    menu = 'Menu de Opciones \n' + \
           '=' * 60 + '\n' + \
           '1  ---------- Cargar Jugadores\n' + \
           '2  ---------- Generar hits por posiciones (matriz)\n' + \
           '3  ---------- Mostrar Hits por posiciones\n' + \
           '4  ---------- Acumular porcentajes de efectividad por posicion\n' + \
           '5  ---------- Nombre del jugador con mejor porcentaje de bateo\n' + \
           '0  ---------- Salir\n' + \
           'Ingrese su opcion: '
    return int(input(menu))

def acumular_por_posicion(vector):
    bat = [0] * 9
    for elemento in vector:
        pos = elemento.posicion - 1
        bat[pos] += (elemento.hits/100) * 100
    return bat

def buscar_masbateadores(vector):
    mayor = vector[0]
    for i in range(1,len(vector)):
        if vector[i].hits > mayor.hits:
            mayor = vector[i]
    return mayor.nombre


def principal():
    n = int(input("Ingrese n jugadores a cargar: "))
    vector = []
    matriz_flag = False
    opcion = -1
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            carga_vector(vector,n)
            display(vector)
            matriz = crear_martiz(vector)
        else:
            if len(vector) > 0:
                if opcion == 2:
                    matriz_flag = True
                    matriz = crear_martiz(vector)
                    for i in range(len(matriz)):
                        for j in range(len(matriz[i])):
                            print('m[' + str(i) + '][' + str(j) + '] = ' + str(matriz[i][j]))
                elif opcion == 3:
                    if matriz_flag:
                        pos = validate_rango(1,9,"Ingrese la posicion a ver: ")
                        total = cantidad_total(matriz,pos)
                        print("La cantidad total de hits para la posicion",pos,"fue de",total)
                    else:
                        print("Primero debe contar que posicion y cantidad de hits(opcion 2)")
                elif opcion== 4:
                    bat = acumular_por_posicion(vector)
                    for i in range(len(bat)):
                        print("El porcentaje de bateo para la posicion",i+1,"fue de",bat[i],"%")
                elif opcion == 5:
                    nom = buscar_masbateadores(vector)
                    print("EL nombre del jugador que mas palos pego es",nom)
            else:
                print("Debe cargar perimo la opcion 1")

    print("Gracias por utilizar el programa")




if __name__ == '__main__':
    principal()