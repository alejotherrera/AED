__author__ = "Alejo Herrera"

#Ingreso de datos
lluvia1=float(input("Ingrese mililitros de la primer lluvia: "))
lluvia2=float(input("Ingrese mililitros de la segunda lluvia: "))
lluvia3=float(input("Ingrese mililitros de la tercer lluvia: "))

#Promedio de milímetros caídos
promedio = (lluvia1+lluvia2+lluvia3)/3
print("El promedio de milimetros caido trimestral es:",promedio)
cantmayor=0
#Cantidad de meses con más o igual lluvia que el promedio
if lluvia1>=promedio:
    cantmayor += 1
if lluvia2>=promedio:
    cantmayor += 1
if lluvia3>=promedio:
    cantmayor += 1

print("La cantidad de meses con mas lluvias o igual que el promedio es:",cantmayor)

minimo = min(lluvia1,lluvia2,lluvia3)
if minimo == 0:
    print("La lluvia minima fue de 0 milimetros, hay un problema")
else:
    print("La lluvia menor fue:",minimo)

