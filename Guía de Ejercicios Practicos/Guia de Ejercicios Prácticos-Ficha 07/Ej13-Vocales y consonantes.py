__author__ = "Alejo Herrera"

# Cargar por teclado una frase, pero a razón de un caracter por vez en una variable. La frase debe terminar con un
# punto (al aparecer el punto, la carga debe finalizar). El programa debe informar

# a) Cuántas vocales existen en la frase

# b) Cuántas letras en total existen en la frase (no contar símbolos como comas, puntos y comas, números, etc).

# c) El porcentaje de vocales respecto al total de letras.


# Modulos
def puntoa(letra):
    contvocal = 0
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contvocal = 1
    return contvocal

def puntob(letra):
    contletra = 0
    if letra.isalpha():
        contletra = 1
    return contletra


# Programa principal

# Carga de variables
letra = ""
palabra = ""
contvocal = 0
contletra = 0

# Ciclo
while letra != ".":
    # Ingreso por teclado
    letra = input("Ingrese letra (Punto para finalizar): ")
    letra = letra.lower()
    palabra += letra
    # Punto a
    contvocal += puntoa(letra)
    # Punto b
    contletra += puntob(letra)

porcentajevocal = round((contvocal * 100 / contletra), 2)

# Imprimir resultados

print("Resultados")
print("-"*30)
print("La cantidad de vocales son: ", contvocal)
print("La cantidad de letras ingresadas fueron ", contletra)
print("El porcentaje es: %", porcentajevocal)