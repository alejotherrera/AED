__author__= "Alejo Herrera"

# Ingreso de datos

# Ingreso barco 1
print("Datos del primer barco")
nombre1 = str(input("Ingrese nombre del barco 1: "))
tiempo1 = float(input("Ingrese tiempo del barco 1: "))

# Ingreso barco 2
print("Datos del segundo barco")
nombre2 = str(input("Ingrese nombre del barco 2: "))
tiempo2 = float(input("Ingrese tiempo del barco 2: "))

# Ingreso barco 3
print("Datos del segundo barco")
nombre3 = str(input("Ingrese nombre del barco 3: "))
tiempo3 = float(input("Ingrese tiempo del barco 3: "))

# Proceso
if tiempo1>tiempo2 and tiempo1>tiempo3:
    mayor = tiempo1
    barcomayor=nombre1
elif tiempo2>tiempo1 and tiempo2>tiempo3:
    mayor = tiempo2
    barcomayor=nombre2
else:
    mayor = tiempo3
    barcomayor=nombre3
promedio = ((tiempo1+tiempo2+tiempo3) / 3)*2

if promedio< mayor:
    print ("El barco:",barcomayor, "debe ser bajado de categoria")
