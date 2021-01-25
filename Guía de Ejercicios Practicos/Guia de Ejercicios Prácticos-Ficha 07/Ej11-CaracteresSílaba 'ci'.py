# Cargar por teclado una frase, cada palabra separada unicamente por espacio y el texto terminar cuando se ingrese un
# punto (el cual no forma parte de la frase a procesar). Se debe obtener la cantidad de palabras que poseen al menos
# una vez la sílaba “ci”. Por ejemplo, la frase “Este es un ejercicio moderado.” tiene 1 palabra que posee la sílaba
# “ci” (“ejercicio”).

__author__ = "Alejo Herrera"
ci = False
c = False
frasearmada = ""
frase = (input("Ingrese frase: "))
contci = 0
frase = frase.lower()

for i in frase:
    if i != " " and ".":
        if i == "C":
            c = True
        else:
            if i == "i":
                ci = True
            c = False
    else:
        if ci:
            contci += 1
        ci = False

print("La cantidad de palabras con ci son: ", contci)