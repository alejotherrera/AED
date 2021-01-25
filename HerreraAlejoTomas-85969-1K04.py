__author__ = "ALEJO HERRERA-85969"


# Consigna

# Consigna Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable
# de tipo cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el
# final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa
# debe incluir al menos una función simple con parámetros y retorno de resultado, debe procesar el texto caracter a
# caracter (a razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:

# 1-Determinar cuántas palabras del texto tienen más de cuatro letras, y contienen la letra 't'. Por ejemplo,
# el texto:  "Estamos listos para adelantar la fase tres." tiene 3 palabras que cumplen la condición: "Estamos",
# "listos" y "adelantar".

# 2-Determinar el promedio de letras por palabras entre las palabras que comienzan con la letra ‘p’. Por ejemplo,
# en el texto:  "La puerta del parque necesita pintura." hay 3 palabras que comienzan con 'p' ("puerta", "parque" y
# "pintura"). La cantidad de letras entre las tres es 18, y por lo tanto el promedio pedido es de 6 letras por
# palabra.

# 3-Determinar cuántas palabras tienen el primer caracter de la primera palabra, pero ingresado a partir del
# tercer carecter en adelante. Por ejemplo, en el texto: "ahora estamos alejados del puesto de peaje." el primer
# caracter de la primera palabra es "a", y hay 4 palabras que contienen al menos una "a" a partir del tercer
# caracter: "ahora",  "estamos", "alejados" y "peaje". Note que en este ejemplo, la propia primera palabra ("ahora")
# contiene una segunda "a" en la quinta posición, por lo que esta palabra también cumple y debe contarse.

# 4-Determinar cuántas palabras tienen la expresión "ti" una sóla vez. Por ejemplo, en el texto: "tienes que ver a un
# titiritero de ese tiempo." hay 2 palabras que tienen una sóla vez la expresión "ti":  "tienes" y "tiempo".

# Funciones
def promedio(a, b):
    promedio = round(a / b, 2)
    return promedio


# PROGRAMA / SCRIPT PRINCIPAL
print("-----------------------Parcial 2-----------------------")
# Ingreso de texto por teclado
texto = input("Ingrese texto(finaliza con punto): ")
texto = texto.lower()

# Carga de variables
# Banderas a utilizar
hay_t = primer_loop = hay_primercaracter = hay_ti = hay_ti1 = False
# Contadores a utilizar
letras = cant_palabras_mayor3yt = cont_letras_conp = cont_palabras_conp = promp = pos_palabra = \
    cont_palabras_cont = cont_palabras_ti = cont_ti = 0

# Tercer punto (Guardo el primer caracter)
primer_caracter = texto[0]

# Ciclo / Loop
for i in texto:
    if i != " " and i != ".":

        # Primer Punto
        pos_palabra += 1
        letras += 1
        if i == "t":
            hay_t = True

        # Segundo punto
        if pos_palabra == 1 and i == "p":
            primer_loop = True

        # Tercer punto
        if pos_palabra >= 3 and i == primer_caracter:
            hay_primercaracter = True

        # Cuarto punto
        if not hay_ti and i == "t":
            hay_ti = True
        else:
            if hay_ti and (i == "i" or i == "í"):
                hay_ti1 = True
                cont_ti += 1

    if i == " " or i == ".":

        # Primer punto
        if letras > 4 and hay_t:
            cant_palabras_mayor3yt += 1

        # Segundo punto
        if primer_loop:
            cont_letras_conp += letras
            cont_palabras_conp += 1

        # Tercer punto
        if hay_primercaracter:
            cont_palabras_cont += 1

        # Cuarto punto
        if hay_ti1 and cont_ti == 1:
            cont_palabras_ti += 1

        # Reseteo de variables
        hay_ti1 = hay_ti = hay_primercaracter = primer_loop = hay_t = False
        cont_ti = letras = pos_palabra = 0


# Mostrar por pantalla los resultados
print("=" * 80)
print("1-Las palabras del texto que tienen mas de cuatro letras y contienen la letra t es: ", cant_palabras_mayor3yt)
print("=" * 80)
if cont_palabras_conp > 0:
    promp = promedio(cont_letras_conp, cont_palabras_conp)
print("2-El promedio de letras por palabras entre las palabras que comienzan con la letra p es: ", promp)
print("=" * 80)
print("3-Las palabras que tienen el primer caracter en la tercera posicion ", cont_palabras_cont)
print("=" * 80)
print("4-Palabras que tienen la expresion 'ti' una sola vez: ", cont_palabras_ti)
print("=" * 80)
print("Gracias por utilizar el programa")
