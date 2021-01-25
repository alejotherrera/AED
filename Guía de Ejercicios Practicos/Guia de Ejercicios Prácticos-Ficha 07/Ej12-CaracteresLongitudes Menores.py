# Cargar por teclado una frase separada por espacios y termina con un punto (el cual no forma parte de la frase a
# procesar). Se debe establecer cuántas palabras de la frase están antecedidas por otra palabra de menor o igual
# longitud (la primer palabra de la frase nunca podrá ser contabilizada ya que no posee palabra antecesora).

# Por ejemplo, la frase “Este es un ejercicio un poco complicado.” tiene 4 palabras cuya antecesora es igual o más
# corta en longitud (“un”, “ejercicio”, “poco”, “complicado”).

__author__ = "Alejo Herrera"
# Ingreso de datos
frase = (input("Ingrese frase: "))
frase = frase.lower()

# Cargar variables
cantletras = 0
anterior = 0
siguiente = 0
cont = 0

for i in frase:
    if i != " " and i != ".":
        cantletras += 1
    else:
        siguiente = cantletras
        if siguiente >= anterior and anterior != 0:
            cont += 1
        anterior = siguiente
        cantletras = 0

print("Resultados")
print("-" * 30)
print("La cantidad de palabras antecedidas por na menor o igual longitud en el texto es: ", cont)
