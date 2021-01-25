__author__ = "ALEJO HERRERA-85969"

# Modulos

# Ingreso de texto por teclado
texto = input("Ingrese frase(termina con punto): ")
texto = texto.lower()

# Carga de variables
# Banderas a utilizar
ult_letra = hay_d = hay_de = hay_r = hay_rr = hay_l2 = hay_la = hay_si = hay_s = hay_h_primerooultima \
    = hay_e = hay_en = False
primer_loop_palabra = primer_loop = True
# Contadores a utilizar
primer_letra = texto[0]
cont_primerletra = cont = cant_pal_primerletra = palabras = cant_pal_ultimaletra = cont_hayde = cont_hayrr = \
    pos_enpalabra = cont_hayla = cont_haysi = porc_primer_letra = cont_pal_conh = porc_haysi = cant_palabra_en = 0
ant = " "

# Ciclo / Loop

for i in texto:

    if i != " " and i != ".":
        pos_enpalabra += 1
        if primer_loop:
            primer_loop = False
        elif i == primer_letra and primer_loop_palabra:
            cont_primerletra += 1
            primer_loop_palabra = False

        if i == "d" and not hay_d:
            hay_d = True
        else:
            if (i == "e" or i == "é") and hay_d:
                hay_d = False
                hay_de = True
        if i == "r" and not hay_r:
            hay_r = True
        else:
            if i == "r" and hay_r:
                hay_rr = True
                hay_r = False
        if pos_enpalabra == 1 or pos_enpalabra == 2:
            if i == "l" and not hay_l2:
                hay_l2 = True
            else:
                if i == "a" and hay_l2:
                    hay_la = True
                    hay_l2 = False
        if i == "s" and not hay_s:
            hay_s = True
        else:
            if i == "i" and hay_s:
                hay_si = True
                hay_s = False
        if pos_enpalabra != 1 and i == "h" and not hay_h_primerooultima:
            hay_h_primerooultima = True
        if i == "e" and not hay_e:
            hay_e = True
        else:
            if i == "e" and hay_e:
                hay_e = False
                hay_en = True
                cont += 1

    if i == " " or i == ".":
        if not primer_loop_palabra:
            cant_pal_primerletra += 1
        primer_loop_palabra = True
        palabras += 1
        if ant == primer_letra:
            cant_pal_ultimaletra += 1
        if hay_de:
            cont_hayde += 1
        hay_de = False
        hay_d = False
        if hay_rr:
            cont_hayrr += 1
        hay_rr = False
        hay_r = False
        if hay_la:
            cont_hayla += 1
        hay_la = False
        hay_l2 = False
        if hay_si:
            cont_haysi += 1
        hay_s = False
        hay_si = False
        if hay_en and cont < 3:
            cant_palabra_en += 1
        hay_en = False
        hay_e = False
    ant = i

if palabras > 0:
    porc_primer_letra = round(cant_pal_primerletra * 100 / palabras, 2)
    porc_haysi = round(cont_haysi * 100 / palabras, 2)
# Mostrar por pantalla los resultados
print("1 - Determinar la cantidad de palabras que comienzan con la primera letra de todo el texto: ", cont_primerletra)
print("2 - Determinar la porcentaje de palabras que incluyeron la primera letra de todo el texto: ", porc_primer_letra,
      "%")
print("3 - Determinar la cantidad de palabras que terminan con la primera letra de todo el texto: ",
      cant_pal_ultimaletra)
print("4 - Determinar la cantidad de palabras que incluyeron la sílaba 'de':", cont_hayde)
print("5 - Determinar la cantidad de palabras que presentan la letra 'rr':", cont_hayrr)
print("6 - Determinar la cantidad de palanbras que comienzan con 'la':", cont_hayla)
print("7 - Determinar el porcentaje de palabras que contienen 'si' :", porc_haysi, " y contiene no:")
print("8 - Determinar la cantidad de palabras que contienen 'h' pero dentro de la palabra es decir no puede ser ni "
      "la primera ni la última letra de la palabra:", cont_pal_conh)
print("9 - Determinar la cantidad de palabras que incluyeron la sílaba 'en' 2 veces:", cant_palabra_en)
print("10 - Determinar la cantidad de palabras que comienzan con la letra 'll':", )
