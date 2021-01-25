__author__ = "Alejo Herrera"

# Carga de variables
sueldomayor = float(1)
sueldomenor = float(1)
mes = 1
promedio = 0
cont = int(0)
# Estructura reptitiva
for i in range(0, 6):
    sueldo = float(input("Ingrese sueldo: "))
    # Calculo aguinaldo
    sueldomayor = float(max(sueldomayor, sueldo))
    aguinaldo = sueldomayor / 2

    # Calculo mes que recibio menos
    sueldomenor = float(min(sueldo, sueldomenor))
    cont+= 1
    if sueldomenor == sueldo:
        mes = cont

    #Promedio de sueldos
    promedio = promedio + sueldo

print("El aguinaldo es: ", aguinaldo)
print("El mes que recibio menos fue: ",mes)
promedio = promedio / 6
print("El promedio es: ",promedio)