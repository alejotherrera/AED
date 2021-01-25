__author__ = "Grupo: TP2-G245 (Herrera Alejo Tomas 85969, Dellamas Agustin 87360)"

import random


# Modulos
# Modulo para verificar cadenas
def validacion(cadena):
    cont, cont_ = 1, 0
    error, salida = False, False

    # Verificar @ y . en primera y ultima posicion
    if "@" == cadena[0] or "@" == cadena[-1] or "." == cadena[0] or "." == cadena[-1]:
        error = True

    # Verificar dos puntos seguidos
    if ".." in cadena:
        error = True

    # Verificar un solo @
    for i in cadena:
        if i == "@":
            cont_ += 1
    if cont_ >= 2 or cont_ == 0:
        error = True

    # Verificar volver a intentar o no
    if error is True:
        cont += 1
        print("Usuario mal ingresado")
    else:
        salida = True

    return salida


# Modulo para imprimir el menu
def menuopciones():
    print("1-Cantidad de casos confirmados (test positivo) y porcentaje sobre el total de casos.")
    print("2-Edad promedio de los pacientes que pertenecen a grupo de riesgo")
    print("3-Cantidad y porcentaje que el personal de salud representa sobre el total de casos.")
    print("4-Edad promedio entre los casos confirmados.")
    print("5-Menor edad entre los casos autóctonos.")
    print("6-Cantidad de casos confirmados por región y porcentaje que representa cada uno sobre el total de casos.")
    print("7-Cantidad de casos confirmados con viaje al exterior.")
    print("8-Cantidad de casos sospechosos en contacto con casos confirmados.")
    print("9-Las regiones sin casos confirmados.")
    print("10-Porcentaje de casos positivos autóctonos sobre el total de positivos.")


# Programa principal
print("Programa para Programa para Generación de Estadísticas de COVID-19 (Coronavirus)")

# Variables a usar
validar, cont = False, 1

# Verificar los 3 intentos
while validar is False and cont <= 3:
    # Ingreso de cadena
    if cont == 1:
        cadena = input("Ingrese cuenta con formato nombre@dominio: ")
    else:
        cadena = input("Ingrese cuenta con formato nombre@dominio nuevamente porfavor: ")

    validar = validacion(cadena)
    cont += 1

# Generar estadisticas
if validar:

    # Carga de pacientes por teclado
    pacientes = int(input("Ingrese cantidad de pacientes a procesar: "))
    print(30 * "-")

    # Carga de variables a usar en for
    siguiente, menor, anterior, positivos, gruporiesgo, respdesalud, totaledades, contcapital, contgrancordoba, \
    contnorte, contsur, contviaje, contcontacto, edadriesgo, contentra, promedioautoctonopositivo \
        = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    capitalunconfirmed, grancordobaunconfirmed, norteunconfirmed, surunconfirmed = bool(False), bool(False), bool(
        False), bool(False)

    # Cargar variables con contenido
    test = "positivo", "negativo"
    region = "gran cordoba"
    opcionsino = "si", "no"

    # Repetitiva segun la cantidad de pacientes
    for i in range(0, pacientes):
        # Generar randoms
        edad = int(random.randint(1, 100))
        resultadodeltest = random.choice(test)
        resultadoregion = "gran cordoba"
        resultadocontacto = random.choice(opcionsino)
        resultadopersonaldesalud = random.choice(opcionsino)
        resultadoviajealexterior = random.choice(opcionsino)

        # Datos para el menu de opciones
        # Resultado de positivos
        if resultadodeltest == "positivo":
            positivos += 1
            totaledades += edad

        # Grupo de riesgo
        if resultadodeltest == "negativo" and edad >= 60:
            gruporiesgo += 1
            edadriesgo += edad

        # Caso personal de salud
        if resultadopersonaldesalud == "si" and resultadodeltest == "positivo":
            respdesalud += 1

        # Menor edad y caso autoctono
        if resultadoregion == "gran cordoba" and resultadodeltest == "positivo":
            contentra += 1
        if contentra == 1:
            anterior, menor = edad, edad
            contentra = 2
        if resultadoregion == "gran cordoba" and resultadodeltest == "positivo":
            siguiente = edad
            menor = min(anterior, siguiente, menor)
        anterior = siguiente

        # Determinar casos por regiones
        if resultadoregion == "capital" and resultadodeltest == "positivo":
            contcapital += 1
        if resultadoregion == "gran cordoba" and resultadodeltest == "positivo":
            contgrancordoba += 1
        if resultadoregion == "norte" and resultadodeltest == "positivo":
            contnorte += 1
        if resultadoregion == "sur" and resultadodeltest == "positivo":
            contsur += 1

        if resultadoviajealexterior == "si" and resultadodeltest == "positivo":
            contviaje += 1

        if resultadocontacto == "si" and resultadodeltest == "negativo":
            contcontacto += 1

    # 1)Porcentaje total sobre los casos
    if positivos == 0 or pacientes == 0:
        porctotal = 0
    else:
        porctotal = round(positivos * 100 / pacientes)

    # 2)Edad promedio de los pacientes que pertenecen a grupo de riesgo
    if gruporiesgo == 0:
        promedioedadriesgo = 0
    else:
        promedioedadriesgo = round(edadriesgo / gruporiesgo)

    # 3)Porcentaje que el personal de salud representa sobre el total de casos
    if positivos == 0:
        porcpsalud = 0
    else:
        porcpsalud = round(respdesalud * 100 / positivos)
    # 4)Edad promedio entre los casos confirmados
    if pacientes == 0:
        promedioedad = 0
    else:
        promedioedad = round(totaledades / pacientes)

    # 6) Porcentaje sobre los infectados
    if positivos == 0:
        promediocapital = 0
        promediograncordoba = 0
        promedionorte = 0
        promediosur = 0
    else:
        promediocapital = round(contcapital * 100 / positivos)
        promediograncordoba = round(contgrancordoba * 100 / positivos)
        promedionorte = round(contnorte * 100 / positivos)
        promediosur = round(contsur * 100 / positivos)

    # 9) Determinar regiones sin casos confirmados
    if contcapital == 0:
        capitalunconfirmed = True
    if contgrancordoba == 0:
        grancordobaunconfirmed = True
    if contnorte == 0:
        norteunconfirmed = True
    if contsur == 0:
        surunconfirmed = True

    # 10) Determinar porcentaje de casos positivos autoctonos sobre el total de positivos
    if positivos == 0:
        promedioautoctonopositivo = 0
    else:
        promedioautoctonopositivo = round(contgrancordoba * 100 / positivos)

    # Generacion de menu
    menuopciones()
    print(30 * "-")

    #Eleccion del menu
    eleccion = int(11)

    while eleccion != 0:
        # Carga de opcion
        eleccion = int(input("Ingrese opcion: "))

        # Error en la carga de eleccion
        if 1 <= eleccion <= 10:
            eleccion = eleccion
        else:
            print("Numero invalido")

        if eleccion == 1:
            # Punto 1
            print(15 * "-", "1", 15 * "-")
            print("Cantidad de casos confirmados: ", positivos)
            print("Porcentaje total sobre los casos: ", porctotal, "%")

        elif eleccion == 2:
            # Punto 2
            print(15 * "-", "2", 15 * "-")
            if promedioedadriesgo == 0:
                print("No hay pacientes que pertenezcan al grupo de riesgo")
            else:
                print("Edad promedio de los pacientes que pertenecen a grupo de riesgo: ", promedioedadriesgo, "años")

        elif eleccion == 3:
            # Punto 3
            print(15 * "-", "3", 15 * "-")
            print("Cantidad del personal de salud infectados: ", respdesalud)
            print("Porcentaje sobre los positivos totales: ", porcpsalud, "%")

        elif eleccion == 4:
            # Punto 4
            print(15 * "-", "4", 15 * "-")
            print("Edad promedio entre los casos confirmados: ", promedioedad)

        elif eleccion == 5:
            # Punto 5
            if menor == 0:
                print("No existe caso menor autoctono")
            else:
                print(15 * "-", "5", 15 * "-")
                print("Menor edad entre los casos autoctonos(Gran Cordoba): ", menor)

        elif eleccion == 6:
            # Punto 6
            print(15 * "-", "6", 15 * "-")
            print("Cantidad de casos confirmados por región y porcentaje sobre los infectados")
            print("Capital: ", contcapital, "con un porcentaje de: ", promediocapital, "%")
            print("Gran Córdoba: ", contgrancordoba, "con un porcentaje de: ", promediograncordoba, "%")
            print("Norte: ", contnorte, "con un porcentaje de: ", promedionorte, "%")
            print("Sur: ", contsur, "con un porcentaje de: ", promediosur, "%")

        elif eleccion == 7:
            # Punto 7
            print(15 * "-", "7", 15 * "-")
            print("Cantidad de casos confirmados con viaje al exterior: ", contviaje)

        elif eleccion == 8:
            # Punto 8
            print(15 * "-", "8", 15 * "-")
            print("Cantidad de casos sospechosos en contacto con casos confirmados: ", contcontacto)

        elif eleccion == 9:
            # Punto 9
            print(15 * "-", "9", 15 * "-")
            # Mostrar regiones sin casos confirmados
            if capitalunconfirmed:
                print("La region capital no contiene casos confirmados")
            if grancordobaunconfirmed:
                print("La region Gran Córdoba no contiene casos confirmados")
            if norteunconfirmed:
                print("La region norte no contiene casos confirmados")
            if surunconfirmed:
                print("La region sur no contiene casos confirmados")
            if capitalunconfirmed is False and grancordobaunconfirmed is False and norteunconfirmed is False and \
                    surunconfirmed is False:
                print("Todas las regiones poseen casos positivos")

        elif eleccion == 10:
            print(15 * "-", "10", 15 * "-")
            print("Porcentaje de casos positivos autóctonos sobre el total de positivos: ",
                  promedioautoctonopositivo,
                  "%")
        print(30 * "-")
        choise = input("¿Desea continuar?si/no: ")
        print(30 * "-")
        if ("si" or "Si" or "SI" or "sI") in choise:
            eleccion = 1
        elif ("no" or "No" or "NO" or "nO") in choise:
            eleccion = 0
            print("Gracias por usar nuestro generador de estadisticas")
            eleccion = 0
        else:
            print("Opcion invalida, saldra del programa")
            print("Gracias por usar nuestro generador de estadisticas")
            eleccion = 0
else:
    # En caso de ser incorrecta notificar
    print("Error al ingresar el usuario, vuelva a intentar el programa")
