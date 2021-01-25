__author__="Alejo Herrera"

#Ingreso de datos
opcion = int(input("1- representa Diurno y 2- representa Nocturno"))
horas = int(input("Ingrese horas: "))

#Condicion
if opcion == 1:
    sueldo = 40.60 * horas
else:
    sueldo = 35.50 * horas

print(sueldo)