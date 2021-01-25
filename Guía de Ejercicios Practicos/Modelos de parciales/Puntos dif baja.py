__author__ = "Alejo Herrera"

# Puntos de dificultad baja:
# 1 - Determinar la cantidad de palabras del texto.
# 2 - Determinar el promedio de letras por palabra.
# 3 - Determinar el promedio de vocales por palabra.
# 4 - Determinar el promedio de consonantes por palabra.
# 5 - Determinar la cantidad de palabras que incluyeron alguna letra e.
# 6 - Determinar el porcentaje de palabras que incluyeron alguna consonante.
# 7 - Determinar la cantidad de palabras que tuvieron exactamente 3 vocales.
# 8 - Determinar el porcentaje de palabras que tuvieron algún dígito ('0' al '9').
# 9 - Determinar la cantidad de palabras que tuvieron más de 3 caracteres.
# 10- Determinar la cantidad total dígitos del texto.

# Carga por teclado
frase = input("Ingrese frase(termina con punto): ")
frase = frase.lower()

# Carga de variables
palabras = letras_totales = letras_palabra = promedio_letras_palabra = letras_vocales = promedio_vocales = \
    cant_palabrase = cant_consonante = porc_consonantes = pal_3vocales = cont_dig = cont_pal_3 = cant_digitos = 0
vocales = "aeiouáéíóú"
flage = pal_consonante = dig_flag = mayor_3 = False
digitos = "123456789"
# Ciclo / Loop
for i in frase:
    if i != " " and i != ".":
        letras_palabra += 1
        letras_totales += 1
        # Punto 3
        if i in vocales:
            letras_vocales += 1
        #Punto 5
        if i == "e" or i == "é":
            flage = True
        # Punto 6
        if i not in vocales:
            pal_consonante = True
        # Punto 8
        if i in digitos:
            cant_digitos += 1
            dig_flag = True
        if letras_palabra > 3 and not mayor_3:
            mayor_3 = True

    if i == " " or i == ".":
        palabras += 1
        letras_palabra = 0
        #Punto 4
        if flage:
            cant_palabrase += 1
        flage = False
        # Punto 6
        if pal_consonante:
            cant_consonante += 1
        pal_consonante = False
        if letras_vocales == 3:
            pal_3vocales += 1
        if dig_flag:
            cont_dig += 1
        if mayor_3:
            cont_pal_3 += 1
            mayor_3 = False
        letras_palabra = 0

print("1-Determinar la cantidad de palabras del texto: ", palabras)
if palabras > 0:
    promedio_letras_palabra = round(letras_totales / palabras, 2)
print("2-Determinar el promedio de letras por palabra: ", promedio_letras_palabra)
if letras_vocales > 0:
    promedio_vocales = round(letras_totales / letras_vocales, 2)
print("3-Determinar el promedio de vocales por palabra: ", promedio_vocales)
print("4-Determinar el promedio de consonantes por palabra: ",cant_palabrase )

print("5-Determinar la cantidad de palabras que incluyeron alguna letra e: ", cant_palabrase)
if palabras > 0:
    porc_consonantes = round(cant_consonante*100/palabras)
print("6-Determinar el porcentaje de palabras que incluyeron alguna consonante: ",porc_consonantes,"%")
print("7-Determinar la cantidad de palabras que tuvieron exactamente 3 vocales: ",pal_3vocales)
print("8-Determinar el porcentaje de palabras que tuvieron algun digito(0 al 9): ",cont_dig)
print("9-Determinar la cantidad de palabras que tuvieron más de 3 caracteres",cont_pal_3)
print("10-Determinar la cantidad total dígitos del texto.",cant_digitos)
