__author__ = "Alejo Herrera"

import random

#Carga de datos
n = int(input("Ingrese cantidad a convertir: "))

#Carga de variables
c = False
hexadecimal = ""
q = int
r = int
for i in range (1,n):
    num = random.randrange(5000,450000)
    while c == False:
        q = num // 16
        r = num % 16

        if r == 10 or q == 10:
            asignacion = str("A")
        elif r == 11 or q == 11:
            asignacion = str("B")
        elif r == 12 or q == 12:
            asignacion = str("C")
        elif r == 13 or q == 13:
            asignacion = str("D")
        elif r == 14 or q == 14:
            asignacion = str("E")
        elif r == 15 or q == 15:
            asignacion = str("F")
        elif r == 16 or q == 16:
            asignacion = str("G")
        elif 1 <= r <= 15:
            asignacion = str(r)
        elif 1 <= q <= 15:
            asignacion = str(q)

        hexadecimal = hexadecimal + asignacion
        if q < 15:
            c = True
            print(hexadecimal)
