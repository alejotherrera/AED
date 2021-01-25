# Simular un juego en el que se lanzan dos dados.

# Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario. En caso contrario, gana la máquina.

__author__ = "Alejo Herrera"

import random
# Determinacion de dados
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
print(dado1, dado2)
suma = dado1+dado2

# Condicion
if  suma % 2 != 0 or dado1 == dado2:
    print("Gana el usuario")
else:
    print("Gana la maquina")
