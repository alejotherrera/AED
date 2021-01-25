# Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente. Permitir que un jugador apueste a cara o
# cruz y luego informar si acertó o no con su apuesta.

__author__ = "Alejo Herrera"

import random

# Ingreso de datos
opcionusuario = str(input("Ingrese cara o cruz: "))

caras = "cara","cruz"

# Determinacion de random
opcionpc = random.choice(caras)

# Condicion
if opcionusuario == opcionpc:
    print("Acerto con su apuesta")
else:
    print("No acerto con su apuesta")
