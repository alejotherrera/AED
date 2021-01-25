#Cargar por teclado una frase (de a un caracter por vez). La carga solo debe terminar cuando se ingrese un punto
#(el cual no forma parte de la frase a procesar). Se debe informar la cantidad de palabras de la frase y cantidad promedio de letras por palabra.
#Por ejemplo, la frase “Este es un ejercicio muy sencillo.” tiene 6 palabras y la cantidad promedio de letras por palabra es de 4,66 ([4+2+2+9+3+8]/6).

print('Tratamiento de Caracteres, lectura caracter por caracter')
print('-' * 90)

cant_letras = 0
cant_palabras = 0
total_letras = 0
termino = False

print('Se procesara un texto caracter a carater, termina con punto')
caracter = input('Ingrese una letra: ')
while caracter != '.':
    if caracter.isalpha():
        cant_letras += 1
    else:
         cant_palabras += 1
         total_letras += cant_letras
         cant_letras = 0

    if termino:
        break

    caracter = input('Ingrese una letra: ')
    if caracter == '.':
        caracter = ' '
        termino = True

print('Resultado del proceso')
print('-' * 90)
print('Cantidad de palabras del texto:', cant_palabras)
promedio = 0
if cant_palabras > 0:
    promedio = total_letras / cant_palabras
print('El promedio de letras por palabra fue de', round(promedio, 2))
