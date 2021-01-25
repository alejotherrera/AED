# Ingresar por teclado las edades de 3 participantes de un concurso.

# Informar si todos cumplen con la edad mínima establecida para el mismo, también ingresada por teclado.

__author__ = "Alejo Herrera"

#Ingreso de edades
edad1 = int(input("Ingrese edad 1: "))
edad2 = int(input("Ingrese edad 2: "))
edad3 = int(input("Ingrese edad 3: "))

minima = int(input("Ingrese la edad minima: "))

#Condicion
if edad1 < minima or edad2 < minima or edad3 < minima:
    print("No todos cumplen con la edad minima")
else:
    print("Todos cumplen con la edad minima")