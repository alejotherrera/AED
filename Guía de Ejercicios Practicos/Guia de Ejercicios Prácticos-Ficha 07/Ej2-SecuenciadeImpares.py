__author__ = "Alejo Herrera"

#Ingreso de datos
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

a = max(a,b)
b = min(a,b)

#Generar variables
lim = a + 1
num = b

#Estructura repetitiva
    #Impresion descendente
for i in range (1,lim):
    if i % 2 != 0:
        print(i)

    #Impresion ascendente
num = a
print("\n")
for i in range (1,lim):
    if i % 2 != 0:
        print(num)
    num-= 1
