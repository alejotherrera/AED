##Operaciones de orden con 3 nros.##
##Realizar un programa que tome tres números, los ordene de mayor a menor, ##
##y diga si el tercero es el resto de la división de los dos primeros. ##

__author__ = "Alejo Herrera"
##Carga de numeros##
n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
n3 = float(input("Ingrese el tercer numero: "))

##Ordenar de mayor a menor##
valores = [n1, n2, n3]
valores.sort(reverse=True)
print(valores)

##determinas si el tercero es el resto de la divsion de los dos primeros##
if valores[0] / valores[1] == valores[2]:

    print(valores[2], "Es resto de la division de los dos primeros")

else:

    print(valores[2], "No es resto de la division de los dos primeros")



