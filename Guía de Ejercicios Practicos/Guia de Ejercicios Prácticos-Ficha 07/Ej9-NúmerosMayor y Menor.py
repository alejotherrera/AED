#Cargar por teclado n números enteros positivos, uno a uno. Se deberá establecer qué número es el mayor de los números pares y el menor de los números impares.

#Por ejemplo, en una secuencia de números: 8, 15, 9, 2, 27, 18, 0; el mayor de los pares sería el número 18 y el menor de los impares el número 9.

def espar(n):
    determinacion = bool(False)
    if n % 2 == 0:
        determinacion = True
    else:
        determinacion = False
    return determinacion

#Programa principal

# Carga de datos
n = int(input("Ingrese numeros positivos a procesar:"))

# Inicializar variables
anteriorpar = siguientepar = siguienteimpar = anteriorimpar = mayorpar = mayorimpar = i = int(0)

# Repetitiva
for car in range(0,n):
    i = int(input("Ingrese el numero entero: "))
    if espar(i):
        siguientepar = i
        mayorpar = max(anteriorpar,siguientepar,mayorpar)
        anteriorpar = siguientepar
    else:
        siguienteimpar = i
        mayorimpar = max(anteriorimpar,siguienteimpar,mayorimpar)
        anteriorimpar = siguienteimpar

print("El mayor impar es: ",mayorimpar)
print("El mayor par es: ",mayorpar)