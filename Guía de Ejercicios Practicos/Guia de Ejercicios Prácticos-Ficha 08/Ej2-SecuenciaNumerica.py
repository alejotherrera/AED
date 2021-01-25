__author__ = "Alejo Herrera"

# Carga de variables
n = -1
contn = 0
cont3 = 0
anterior = 0
cuadant = 0
mayorimpar = 0

# Ciclo
while n != 0:
    n = int(input("Ingrese numero: "))
    if n == 0:
        break
    contn += 1
    # PuntoA
    if n % 3 == 0:
        cont3 += 1
    # PuntoB
    if contn == 1:
        continue
    else:
        if anterior ** 2 == n:
            cuadant += 1
    anterior = n
    # PuntoC
    if n % 2 != 0:
        mayorimpar = max(mayorimpar, n)

# PuntoAPorcentaje
porc3 = cont3 * 100 / contn

# Imprimir resultados
print("A) El procentaje de los numeros divisibles por 3 sobre el total de la secuencia es: ", porc3)
print("-" * 30)
print("B) La cantidad de numeros que son el cuadrado del numero anterior es: ", cuadant)
print("-" * 30)
print("C) La posicion mayor del elemento impar de la secuencia es: ",mayorimpar )
