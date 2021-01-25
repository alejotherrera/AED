__author__ = "Alejo Herrera"

#Ingreso de datos
n = (input("Ingrese competidores: "))

#Cargar variables
nombreganador = ""
tiempoganador = 0
contador = int

#Estructura repetitiva
for i in (0,n):
    nombre = str(input("Ingrese nombre del competidor: "))
    tiempo = float(input("Ingrese tiempo: "))

    if tiempo>tiempoganador:
        nombreganador = nombre
        tiempoganador = tiempo

    tiempo = 0

print("El ganador es: ", nombreganador,"con un tiempo de: ", tiempoganador)