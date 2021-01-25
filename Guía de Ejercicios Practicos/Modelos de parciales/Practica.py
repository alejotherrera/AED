__author__ = "Alejo Herrera"


# Funcion
def tercepunto(letra,flag_top):
    if (letra == "p" or letra == "t") and letra != "a":
        flag_top = True
    if i == "a":
        flag_top = False
    return flag_top


# Carga de texto por teclado
frase = input("Ingrese frase(termina con punto): ")
frase = frase.lower()

# Carga de variables
vocales = "aeiouáéíóú"
flagdigitos = flagletra_e = flag_top = seg_vocales = False
cant_digitos_cons = vocales_pal = pal_mayor = letra_palabra = pos = contpal_e = cant_pal_cone = letras_palabra = \
    prome = cont_palcontop  = cont_seg = 0
digitos = "123456789"
i_anterior = " "
# Ciclo/Loop
for i in frase:
    if i != " " and i != ".":
        letras_palabra += 1
        # Primer Punto
        if i in vocales:
            vocales_pal += 1
        else:
            if i in digitos:
                flagdigitos = True
            cant_digitos_cons += 1

        # Segundo punto
        pos += 1
        if pos == 3 and (i == "e" or i == "é"):
            flagletra_e += True

        # Tercer punto
        flag_top = tercepunto(i,flag_top)

        # Cuarto punto
        if i_anterior in vocales and i in vocales:
            seg_vocales = True

    if i == " " or i == ".":
        # Primer Punto
        if vocales_pal < cant_digitos_cons and flagdigitos:
            pal_mayor += 1
        vocales_pal = 0
        cant_digitos_cons = 0
        flagdigitos = False

        # Segundo punto
        if flagletra_e:
            contpal_e += letras_palabra
            cant_pal_cone += 1
        pos = 0
        flagletra_e = False
        letras_palabra = 0

        # Tercer punto
        if flag_top:
            cont_palcontop += 1
        flag_top = False

        # Cuarto punto
        if seg_vocales:
            cont_seg += 1
            seg_vocales = False
    i_anterior = i


# Imprimo los resultados
# Primer punto
print("La cantidad de palabras cuya cantidad de digitos y consonantes es mayor que la cantidad de vocales es: ",
      pal_mayor)
if contpal_e != 0:
    prome = round(contpal_e / cant_pal_cone, 1)
# Segundo punto
print("El promedio de letras por palabra del texto que tienen la letra e en tercer posicion es: ", prome)
# Tercer punto
print("Las palabra sque tienen una p o una t pero no una a es: ",cont_palcontop)
# Cuarto punto
print("La cantidad de seguidilla doble con vocal: ",cont_seg)