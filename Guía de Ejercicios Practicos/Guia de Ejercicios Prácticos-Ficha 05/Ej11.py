__author__ = "Alejo Herrera"

#Ingreso de datos
parcial1= float(input("Ingrese nota del primer parcial: "))
parcial2= float(input("Ingrese nota del segundo parcial: "))
tps= float(input("Ingrese nota de los trabajos practicos: "))

#determinacion de promedio
promedio = (parcial1+parcial2+tps)/3

#Determinacion de estado de la materia
if promedio<4:
    condicion="Alumno libre"
elif 4<promedio<8:
    condicion="Alumno regularizado"
else:
    condicion="Alumno promociono"

print("El alumno se encuentra en condicion: ", condicion)
