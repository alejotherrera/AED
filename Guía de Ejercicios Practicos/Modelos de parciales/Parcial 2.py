'''
1 - Determinar la cantidad de palabras del texto.
2 - Determinar el promedio de letras por palabra.
3 - Determinar el promedio de vocales por palabra.
'''


def promedio(a, b):
    operacion = a / b
    return operacion


texto = input("Ingrese su texto con punto al finalizar:")

vocales = "aeiou"
palabra = 0
letras = 0
palabra_primer_letra = False
palabras_con_e = 0
palabras_con_primer_letra = 0
vocales_total = 0
e_en_palabra = False
pos = 0
anterior = ""
sa_en_palabra = False
palabras_con_sa = 0
for letra in texto:
    if letra != " " and letra != ".":
        letras += 1
        if letra in vocales:
            vocales_total += 1
        if letra == "e":
            e_en_palabra = True
        if pos == 0 and letra == texto[0]:
            palabra_primer_letra = True
        pos += 1
        if letra == "a" and anterior == "s":
            sa_en_palabra = True

    else:
        if letras > 0:
            palabra += 1
            if e_en_palabra == True:
                palabras_con_e += 1
                e_en_palabra = False
            if palabra_primer_letra == True:
                palabras_con_primer_letra += 1
                palabra_primer_letra = False
            if sa_en_palabra == True:
                palabras_con_sa += 1
                sa_en_palabra = False
            pos = 0
    anterior = letra

if palabra != 0:
    promedio_letras = promedio(letras, palabra)
    print("Promedio de letras por palabra:", round(promedio_letras, 2))
    promedio_vocales = promedio(vocales_total, palabra)
    print("Promedio de vocales por palabra:", round(promedio_vocales, 2))
    print("Cantidad de palabras que contienen la silaba sa:", palabras_con_sa)

print("Cantidad de palabras:", palabra)
print("Cantidad de letras:", letras)

print("Cantidad de palabras con la letra e:", palabras_con_e)

print("Cantidad de palabras que empiezan con la primer letra del texto: ", palabras_con_primer_letra)
print("Porcentaje de palabras que tienen la ultima letra:", )
