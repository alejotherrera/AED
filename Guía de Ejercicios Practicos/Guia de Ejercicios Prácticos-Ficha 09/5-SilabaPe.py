__author__ = "alejo herrera"

texto = input("Ingrese texto: ")

#Variables a usar
posicion_palabra = cont_pal357 = cont_vocen3 = cont_vocales = cont_palabras_convocales = palabras = 0
vocales = "aeiou"
voc_palabra = False

#Loop / Repetitiva
for i in texto:
    if i != "." and i != " ":
        posicion_palabra += 1
        if posicion_palabra == 3 and i in vocales:
            voc_palabra = True
        if i in vocales:
            cont_vocales += 1

    if i == " " or i == ".":
        #PuntoA
        if posicion_palabra == 3 or posicion_palabra == 5 or posicion_palabra == 7:
            cont_pal357 += 1
        posicion_palabra = 0

        #PuntoB
        if voc_palabra == True:
            cont_vocen3 += 1
        voc_palabra = False

        #PuntoC
        if cont_vocales <= 2:
            cont_palabras_convocales += 1
        palabras += 1
        cont_vocales = 0

promedio = cont_palabras_convocales * 100 / palabras

print("La cantidad de palabras que contienen 3, 5 o 7 letras es:",cont_pal357)
print("Determinar la cantidad de palabras con más de tres letras, que tienen una vocal en la tercera letra:",cont_vocen3)
print("Determinar el porcentaje de palabras que tienen sólo una o dos vocales sobre el total de palabras del texto:",promedio,"%")
print("Determinar el porcentaje de palabras que tienen sólo una o dos vocales sobre el total de palabras del texto:",)