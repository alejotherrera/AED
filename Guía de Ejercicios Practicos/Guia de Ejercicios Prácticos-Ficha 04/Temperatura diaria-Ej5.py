__author__ = "Alejo Herrera"

# Ingreso de datos
temp1 = float(input("Temperatura 1: "))
temp2 = float(input("Temperatura 2: "))
temp3 = float(input("Temperatura 3: "))

# Determinamos promedio de temperaturas
promedio = (temp1 + temp2 + temp3) / 3

# Determinamos si hay alguna temperatura mayor al promedio
tempmax = max(temp1, temp2, temp3)

if promedio < tempmax:
    print("La temperatura: ", tempmax, "Es mayor al promedio")
