__author__ = "Alejo Herrera"
import random
#Ingreso datos de jugador
jugador = str(input("piedra, papel o tijera: "))

#opcion de la computadora
elementos = ("piedra","papel","tijera")
computadora = random.choice(elementos)
print(computadora)

#procesos
if jugador == computadora:
    print("Empataron")
if (jugador == "piedra" and computadora == "tijera") or (jugador == "papel" and computadora == "piedra") or (jugador == "tijera" and computadora== "papel"):
        print("Gana el jugador")
else:
        print("Gana la computadora")
