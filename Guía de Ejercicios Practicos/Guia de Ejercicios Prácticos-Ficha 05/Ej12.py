# Se pide realizar un programa que ingresando el valor x e y de un punto determine a que cuadrante pertenece en el sistemas de coordenadas.

__author__ = "Alejo Herrera"

# Ingreso de datos

valorx = float(input("Ingrese valor x: "))
valory = float(input("Ingrese valor y: "))

# Proceso
if valorx > 0 and valory > 0:
    cuadrante = 1
elif valorx < 0 and valory > 0:
    cuadrante = 2
elif valorx < 0 and valory < 0:
    cuadrante = 3
elif valorx == 0 and valory == 0:
    cuadrante = "Esta en el medio"
else:
    cuadrante = 4

print("Se encuentra en el cuadrante: ", cuadrante)
