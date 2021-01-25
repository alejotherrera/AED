__author__ = "Alejo Herrera"

# Programa principal

# Carga por teclado de un texto
texto = input("Ingrese texto(El texto finaliza con punto): ")
texto = texto.lower()
# Variables a usar
vocales = "aeiouáéíóú"
letras = palabra = palabras_digito = digito = cont = palabra_l = long_palabra = posicion = palabra_anterior = menor_palabra = 0
numeros = "123456789"
letra_anterior = " "

# Loop / Repetitiva
for i in texto:
    # Contador de digitos
    if i == " " or i == ".":
        digito = 0
    else:
        if i in numeros:
            digito += 1
            if digito == 2:
                palabras_digito += 1
    # Determinar cuantas palabras tienen l
    if i == " " and i == ".":
        if letra_anterior == "l":
            palabra_l -= 1
        cont = 0
    else:
        if i == "l" and cont == 0:
            cont += 1
            continue
        else:
            if i == "l" and cont == 1:
                palabra_l += 1
            cont += 1
        letra_anterior = i
    # Palabra mas corta
    if i == " " or i == ".":
        if palabra_anterior == 0 or menor_palabra == 0:
            menor_palabra = 1
            continue
        else:
            menor_palabra = min(long_palabra, palabra_anterior,menor_palabra)
        long_palabra = 0
    else:
        long_palabra += 1
    palabra_anterior = long_palabra
    # Determinar el porcentaje de palabras que incluyeron la silaba "en"


print("La cantidad de palabras que superan los dos digitos: ", palabras_digito)
print("La cantidad de palabras que contienen la letra l: ", palabra_l)
print("La menor palabra es: ", menor_palabra)
