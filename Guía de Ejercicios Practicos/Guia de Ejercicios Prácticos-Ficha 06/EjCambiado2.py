__author__ = "Alejo Herrera"

# Variables auxiliares

cont: int = 0
aux = ""
pares = 0
impares = 0
suma = 0
cero = bool
serie = bool
#Ciclo

while cont>=0:
    num = float(input("Ingrese numero: "))
    if 50<num<100:
        suma = suma + num

    if num % 2 == 0:
        pares= pares + 1
    else:
        impares = impares + 1

    if num == 0:
        cero = True
    anterior = num
    if anterior % 2 == 0 and num % 2 != 0:
        serie == True
    cont = num

print("La suma de los numeros entre 50 y 100 es: ",suma)
print("La cantidad de pares ingresados fue: ",pares)
print("La cantidad de impares ingresados fue: ",impares)
if cero == True:
    print("Se ingreso al menos un numero 0")
if serie == True:
    print("La serie esta alterada por numeros pares e impares")