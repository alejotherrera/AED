__author__ = "Alejo Herrera"

#Ingrese de datos
print("Datos del mantenimiento 1")
ident1 = int(input("numero de identificacion: "))
tiempo1=int(input("Minutos de mantenimiento: "))
causa1 = str(input("Causa de mantenimiento software/hardware: "))

print("Datos del mantenimiento 2")
ident2 = int(input("numero de identificacion: "))
tiempo2=int(input("Minutos de mantenimiento: "))
causa2 = str(input("Causa de mantenimiento software/hardware: "))

print("Datos del mantenimiento 3")
ident3 = int(input("numero de identificacion: "))
tiempo3=int(input("Minutos de mantenimiento: "))
causa3 = str(input("Causa de mantenimiento software/hardware: "))

#calculos de total de mantenimiento
totalminutos = tiempo1+tiempo2+tiempo3

#Calculo de mayor tiempo de mantenimiento
maximo = max(tiempo1,tiempo2,tiempo2)
if maximo == tiempo1:
    print("El mantenimiento ",ident1, "tuvo mayor tiempo en tareas de mantenimiento")
elif maximo == tiempo2:
    print("El mantenimiento ",ident2, "tuvo mayor tiempo en tareas de mantenimiento")
elif maximo == tiempo3:
    print("El mantenimiento ",ident3, "tuvo mayor tiempo en tareas de mantenimiento")

#Tiempo promedio de tareas de mantenimiento
promedio = (tiempo1+tiempo2+tiempo3)/3
print("El promedio de mantenimiento es: ",promedio)

if causa1 == "hardware" and causa2 == "hardware" and causa3 == "hardware":
    print("Todas las pc tuvieron problemas de hardware")