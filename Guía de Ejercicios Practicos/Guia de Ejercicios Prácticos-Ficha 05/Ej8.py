__author__ = "Alejo Herrera"

import random

# Juego de Dados: Pares e Impares

# Ingreso de datos
record = int(input("Ingrese record del campeon: "))
print("Ronda 1")
print("Dados del retador 1: ")
print("Tira!!!!!")
dado11j1 = random.randint(1, 6)
dado12j1 = random.randint(1, 6)
print("Dados del retador 2: ")
print("Tira!!!!!")
dado11j2 = random.randint(1, 6)
dado12j2 = random.randint(1, 6)

print("Ronda 2")
print("Dados del retador 1: ")
print("Tira!!!!!")
dado21j1 = random.randint(1, 6)
dado22j1 = random.randint(1, 6)
print("Dados del retador 2: ")
print("Tira!!!!!")
dado21j2 = random.randint(1, 6)
dado22j2 = random.randint(1, 6)

totalretador1 = dado11j1 + dado12j1 + dado21j1 + dado22j1
totalretador2 = dado11j2 + dado12j2 + dado21j2 + dado22j2

if totalretador1 % 2 == 0:
    print("Gana el retador 2!!!!")
    print("Ronda final! puntos de campeon:", record)
    if totalretador2 < record:
        print("Gana el campeon")
    else:
        print("Retador 2, se convierte en el nuevo campeon!")
else:
    print("Gana el retador 1!!!!")
    print("Ronda final! puntos de campeon:", record)
    if record > totalretador1:
        print("Gana el campeon")
    else:
        print("Retador 1, se convierte en el nuevo campeon!!!")
