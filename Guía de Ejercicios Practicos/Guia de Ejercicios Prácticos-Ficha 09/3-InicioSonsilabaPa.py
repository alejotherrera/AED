__author__ = "Alejo Herrera"

# 3-Inicio con sílaba "pa"
# Desarrollar un programa en Python que permita cargar por teclado un texto. Siempre se supone que usuario cargará un
# punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe determinar:
#
# a) La cantidad de palabras que comienzan con la expresión "pa" y termina con la letra "n"
#
# c) La cantidad de palabras que presentan mas de dos vocales a partir de la tercera letra de la palabra
#
# d) El porcentaje que representa la cantidad de palabras del punto anterior respecto de la cantidad de total de palabras del texto
#
# e) Cantidad de palabras de mas de 5 letras

texto = input("Ingrese texto(Termina con punto): ")
texto = texto.lower()

# Variables a usar
# Banderas
hay_pa = hay_p = hay1_vocal = hay2_vocal = True
vocales = "aeiouáéíóó"
anterior = " "
# Contadores
posicion_palabra = cont_pa = cont2_vocales = 0

for i in texto:
    if i != " " and i != ".":
        posicion_palabra += 1
        #Punto 1
        if posicion_palabra == 1:
            if i == "p" and not hay_pa:
                hay_p = True
        else:
            if i == "a" and hay_p:
                hay_pa = True
        #Punto2
        if i in vocales and posicion_palabra >= 3 and  not hay2_vocal:
            hay1_vocal = True
        else:
            if hay1_vocal:
                hay2_vocal = True
                hay1_vocal = False

        anterior = i

    if i == " " or i == ".":
        #Punto 1
        if anterior == "n" and hay_pa:
            cont_pa += 1
        #Punto2
        if hay2_vocal:
            cont2_vocales += 1
        hay_pa = False
        hay_p = False
        hay1_vocal = False
        hay2_vocal = False
        posicion_palabra = 0

print("La cantidad de palabaras que comienzan con a expresion p y terminan con la letra n: ",cont_pa)
print("Cantidad de palabras con mas de dos vocales mayor a la posicion 3:",cont2_vocales)