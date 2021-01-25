__author__ = "Alejo Herrera"

# Se ingresan las medidas de frente y fondo de un terreno.

# Determinar si es cuadrado o rectangular y calcular su superficie.

#Ingreso de datos

altura = float(input("Ingrese altura:  "))
base = float(input("Ingrese base: "))
superficie = altura * base

#Condicion
if altura == base:
    print("Es un cuadrado")
else:
    print("Es un rectangulo")

print("La superficie es: ",superficie)