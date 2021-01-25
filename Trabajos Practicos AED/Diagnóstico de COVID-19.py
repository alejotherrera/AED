# Se solicita desarrollar un programa que permita facilitar el diagnóstico a los pacientes que presentan síntomas
# Compatibles con COVID-19.# Mas detalles de consigna en el UV del Trabajo Practico

__author__ = "Grupo: TP1-G358 (Herrera Alejo Tomas 85969, DeLlamas Agustin 87360)"

# Desarollo del codigo fuente
print("Bienvenido al test de COVID-19")

# Descartamos rapidamente el caso de neumonia confirmada a partir de la siguiente condicion.
neumoniaconfirmada = str(input(
    "¿Padece neumonia con diagnostico clinico y radiologico, sin otra etilogia que explique el cuadro clinico? SI/NO:"))
if neumoniaconfirmada == "SI" or neumoniaconfirmada == "si" or neumoniaconfirmada == "Si":
    # Solicitamos el ingreso de datos basico
    edad = int(input("Ingresar edad: "))
    temperaturacorporal = float(input("Ingrese temperatura corporal: "))
    # Determinamos grupo de riesgo
    if edad >= 60:
        print("Es grupo de riesgo al ser mayor de 60 años")
        print("Si es un caso sospechoso de COVID-19")
    else:
        print("Si es un caso sospechoso de COVID-19")

else:
    # Rama falsa, continuamos con el diagnostico
    if neumoniaconfirmada == "NO" or neumoniaconfirmada == "no" or neumoniaconfirmada == "No":
        # Ingreso de datos (Edad y Temperatura corporal) y determinamos si hay fiebre
        print("Ingrese los siguientes datos porfavor:")
        edad = int(input("Edad: "))
        temperaturacorporal = float(input("Temperatura Corporal: "))
        if temperaturacorporal > 37:
            # A partir de fiebre confirmada, se solicitan mas datos (Sintomas Adicionales)
            sintomasadicionales = str(
                input("¿Presenta algun sintoma de tos, odinofagia y/o dificultad respiratoria? SI/NO: "))
            if sintomasadicionales == "SI" or sintomasadicionales == "Si" or sintomasadicionales == "si":
                # Determinamos caso sospechoso del personal de salud
                personaldesalud = str(input("¿Es personal de salud? SI/NO: "))
                if personaldesalud == "SI" or personaldesalud == "Si" or personaldesalud == "si":
                    print("Es caso sospechoso de COVID-19 al ser personal de salud")
                else:
                    # Determinamos actividad en los ultimos 14 dias
                    print("Responder segun actividades en los ultimos 14 dias: ")
                    print(
                        "Si tuvo contacto con casos confirmados en argentina ingrese 1\nSi viajo al exterior ingrese "
                        "2\nSi estuvo en zonas nacionales con casos de transmisión local confirmados ingrese 3\nSi no "
                        "corresponde a ninguna de las actividades mencionadas ingrese 4")
                    ultimos14dias = int(input("opcion: "))
                    # Determinamos las opciones y el diagnostico final
                    if ultimos14dias == 1:
                        # Determinamos la primer opcion
                        print(
                            "Si es un caso sospechoso autoctono de COVID-19, ya que se considera que es dentro de "
                            "argentina")
                    if ultimos14dias == 2:
                        # Determinamos la segunda opcion
                        print(
                            "Si es un caso sospechoso extranjero de COVID-19, ya que el contacto se produjo fuera de "
                            "argentina")
                    if ultimos14dias == 3:
                        # Determinamos la tercer opcion
                        print("Si es un caso sospechoso autoctono de COVID-19")
                    if ultimos14dias == 4:
                        # Determinamos la cuarta opcion y el grupo de riesgo segun la edad
                        if edad >= 60:
                            print(
                                "No es un caso sospechoso de COVID-19, pero pertenece al grupo de riesgo debido a la "
                                "edad(mayor de 60 años)")
                        else:
                            print("No es un caso sospechoso de COVID-19")
            else:

                # Al no presentar sintomas adicionales descartamos el caso rapidamente
                # Determinamos el grupo de riesgo segun la edad
                if edad >= 60:
                    print("No es un caso sospechoso de COVID-19, pero pertenece al grupo de riesgo debido a la edad")
                else:
                    print("No es un caso sospechoso de COVID-19")

        else:

            # Al no presentar fiebre, descartamos rapidamente el caso
            # Determinamos el grupo de riesgo segun la edad
            if edad >= 60:
                print("No es un caso sospechoso de COVID-19, pero pertenece al grupo de riesgo debido a la edad")
            else:
                print("No es un caso sospechoso de COVID-19")
