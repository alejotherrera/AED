"""Puntos de dificultad mayor:
1 - Determinar la cantidad de palabras que contienen 'll' más de una vez.
2 - Determinar la cantidad de palabras que comienzan con 'le' y terminan en 'to'.
3 - Determinar la cantidad de palabras que terminan con 'io' y tienen más de 3 letras.
4 - Determinar la cantidad de palabras que comienzan con la misma letra que terminó la palabra anterior.
5 - Determinar la cantidad de palabras que incluyen 'll' y tienen cantidad de letras par.
6 - Determinar cuantas palabras incluyeron '10' después de la mitad.
7 - Determinar cuantas palabras tuvieron 'u' y terminaron en 'lo'.
8 - Determinar la cantidad de palabras que comienzan con la última letra de la primera palabra del texto y tienen más de 2 vocales.
9- Determinar la cantidad de palabras que contienen 'de' en la primera mitad de la palabra."""



def es_vocal(c):
    return c.lower() in 'aeiouáéíóú'


def analisis(text):
    cl = cp = cant_ll = hay_ll = cant_le_to = cant_io = cant_iguales = \
        cant_ll_par = cant_10 = pos = cant_lo_u = cant_ultprimera = vocales = \
        cant_de = posde = 0
    ant = ultima = ult_de_pri = ''
    triple_l = hay_le = hay_to = hay_u = hay_lo = hay_de = False
    hay_io = empiezan_igual = False

    for ctr in text:
        if ctr == ' ' or ctr == '.':
            # a ver si cl es mayor a 0, asi no cargaron un espacio
            if cl > 0:
                cp += 1
                # ANALIZO TODO
                # defino la ultima letra de la primera palabra
                if cp == 1:
                    ult_de_pri = ant

                if hay_ll > 1:
                    cant_ll += 1
                    # Aprovecho el contador ya hecho y analizo si es par la LL
                if hay_ll and cl % 2 == 0:
                    cant_ll_par += 1

                if hay_le and hay_to:
                    cant_le_to += 1

                if hay_io and cl > 3:
                    cant_io += 1

                if pos > (cl / 2):
                    cant_10 += 1

                if hay_u and hay_lo:
                    cant_lo_u += 1
                if empiezan_igual and vocales > 2:
                    cant_ultprimera += 1

                if hay_de and posde < (cl / 2):
                    cant_de += 1

            # REINICIO TODO
            ultima = ant
            cl = hay_ll = pos = posde = 0
            triple_l = hay_le = hay_to = hay_u = hay_lo = hay_de = empiezan_igual = False


        else:
            cl += 1
            # 1. Contador y analisis de "LL", banderas para evitar "lll"
            if ctr in 'lL' and ant in 'lL' and not triple_l:
                hay_ll += 1
                triple_l = True
            else:
                triple_l = False

            # 2. Analisis de si empieza con "le" y si termina con "TO", banderas para definir final.
            if cl == 2:
                if ant in 'lL' and ctr in 'EÉeé':
                    hay_le = True

            if ant in 'tT' and ctr in 'oÓOó':
                hay_to = True
            else:
                hay_to = False

            # 3. Analisis de si termina con io
            if ant in 'iÍIí' and ctr in 'oÓOó':
                hay_io = True
            else:
                hay_io = False
            ant = ctr

            # 4. Si la palabra empieza con la que termino la anterior.
            if cl == 1:
                if ctr==ultima:
                    cant_iguales += 1

            # 8. Si es igual a la ult letra de la primera
                if ctr == ult_de_pri:
                    empiezan_igual = True
            if es_vocal(ctr):
                vocales += 1

            # 6. analizo si aparece el 10 y guardo su pos
            if ant == '1' and ctr == '0':
                pos = cl

            # 7. Palabras que tienen u y terminaron en 'LO'
            if ctr in 'uUÚú':
                hay_u = True
            if ant in 'lL' and ctr in 'oÓOó':
                hay_lo = True

            # 9. Me fijo si existe la silaba DE
            if ant in 'dD' and ctr in 'EÉeé' and not hay_de:
                hay_de = True
                posde = cl

    return cant_ll, cant_le_to, cant_io, cant_iguales, cant_ll_par, cant_10, cant_lo_u, cant_ultprimera, cant_de


def principal():
    print('\t\t\033[1;7;36m====BIENVENIDO AL PROGRAMA=====\033[0m\n')
    texto = input('>>Ingrese el texto a analizar: ')
    cant_ll, cant_le_to, cant_io, cant_iguales, cant_ll_par, cant_10, cant_lo_u, cant_ultprimera, cant_de = analisis(
        texto)
    print('='*70)
    print('Resultados...')
    print('='*70)
    print('1. -->Cantidad de palabras que contienen "ll" más de una vez:',
          cant_ll)
    print(
        '2. -->Cantidad de palabras que comienzan con "le" y terminan en "to":',
        cant_le_to)
    print(
        '3. -->Cantidad de palabras que terminan con "IO" y tienen más de 3 letras:',
        cant_io)
    print(
        '4. -->Cantidad de palabras que comienzan con la letra que terminó la '
        'anterior.', cant_iguales)
    print(
        '5. -->Cantidad de palabras que incluyen "ll" y tienen cantidad de letras par',
        cant_ll_par)
    print(
        '6. -->Cantidad de palabras que incluyeron "10" después de la mitad.',
        cant_10)
    print('7. -->Cantidad de palabras que tuvieron 'u' y terminaron en "LO"',
          cant_lo_u)
    print(
        '8. -->Cantidad de palabras que comienzan con la última letra de la '
        'primera palabra del texto y tienen más de 2 vocales',
        cant_ultprimera)
    print(
        '9. -->Cantidad de palabras que contienen "DE" en la primera mitad de la palabra:',
        cant_de)


if __name__ == '__main__':
    principal()
