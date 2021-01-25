# Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10
# dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.

__author__="Alejo Herrera"

#Ingreso de numeros
n1 = float(input("Ingrese n1"))
n2 = float(input("Ingrese n2"))
n3 = float(input("Ingrese n3"))

suma = n1+n2+n3

if suma>10:
    division = suma // 2
    print(division)
else:
    cubo = suma**3
    print(cubo)