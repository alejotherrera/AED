__author__ = "Alejo Herrera"

# Números pares e impares

# Se pide desarrollar un programa que permita leer una serie de números. La finalización de carga de datos se presenta cuando el usuario ingrese un número negativo.
# Los requerimientos funcionales del programa son:
# a) La sumatoria de solo los números que estén comprendidos entre 50 y 100.
# b) Cantidad de valores pares ingresados.
# c) Cantidad de valores impares ingresados.
# d) Informar si en la carga de números se ingreso al menos un número 0.
# e) Informar si la serie contiene solo números pares e impares alternados

# Variables auxiliares

cont = 0
aux = ""
num = 1

pares = 0
impares = 0

suma = 0
cero = bool

serie = bool
primero = 0
anterior = 0
# Ciclo
while num >= 0:
    num = float(input("Ingrese numero: "))
    if 50 < num < 100:
        suma = suma + num

    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

    if num == 0:
        cero = True

    primero = num
    if anterior == 0:
        anterior= primero
    else:
        anterior = anterior
    if (primero % 2 == 0 and anterior % 2 != 0) or (anterior % 2 == 0 and primero % 2 != 0):
      serie = True

    anterior = primero

print("La suma de los numeros entre 50 y 100 es: ", suma)
print("La cantidad de pares ingresados fue: ", pares)
print("La cantidad de impares ingresados fue: ", impares)
if cero == True:
    print("Se ingreso al menos un numero 0")
if serie == True:
    print("La serie esta alterada por numeros pares e impares")
