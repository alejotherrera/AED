__author__ = "Alejo Herrera"


# Modulos
# Modulo de ingreso de datos por teclado
def ingresodatos():
    nombre = input("Ingrese nombre del barco: ")
    tipo = input("Ingrese tipo (1 si es velero, 2 si es lancha): ")
    monto = input("Ingrese monto por mes: ")

    return nombre, tipo, monto


def primerpunto(tipo, monto):
    montoveleros = 0
    montolanchas = 0
    if tipo == 1:
        montoveleros += monto
    else:
        montolanchas += monto
    return montolanchas, montoveleros


# Programa principal
# Carga de datos
n = int(input("Ingrese cantidad de barcos a cargar: "))

# Carga de variables
montoveleros = 0
montolanchas = 0
anterior = 0
montomaxveleros = 0
montototal = 0
veleros = 0
lanchas = 0

# Estructura
for i in range(1, n+1):
    # Punto 1
    tipo,monto = ingresodatos()[1][2]
    if tipo == 1:
        montoveleros += monto
        veleros += 1
        # Punto 2
        montomaxveleros += max(monto, anterior)

        anterior = monto

    else:
        montolanchas += monto
        lanchas += 1

    # Punto 3
    montototal += monto

# Punto 3 termino
montototal = montototal * 100 / n

# Punto 4
totalveleros = montoveleros * 100 / montototal
totallanchas = montolanchas * 100 / montototal

# Mostrar por pantallas resultados
# Punto 1
print("El total aportado por los veleros es: ", montoveleros)
print("El total aportado por las lanchas es: ", montolanchas)
print("-" * 30)
# Punto 2
print("")
print("-" * 30)
# Punto 3
print("El valor promedio de la couta de las embarcaciones: ", montototal)
print("-" * 30)
# Punto 4
print("El porcentaje de los veleros es :", totalveleros)
print("El procentaje de las lanchas es :", totallanchas)
