__author__ = "Grupo: TP3-G233 (Herrera Alejo Tomas 85969, Dellamas Agustin 87360)"

from Module import *


# -------------------------------------------------
def main():
    print("-" * 5, "Bienvenidos al Sistema de Gestion de una Competencia", "-" * 5)
    input("Presiona una tecla para continuar...")
    tercerpuesto = False
    segundopuesto = False
    v_participantes = carga_vector()
    v_aux = v_participantes[:]
    ordenamiento_ranking(v_participantes)
    cant_continente(v_participantes)
    mostrar(v_participantes)
    # ----------------------------
    print("\033[4;35m" + "-" * 20, "OCTAVOS DE FINAL!", "-" * 20 + "\033[0;m")
    print("\033[4;36m" + "Fixture" + "\033[0;m")
    v_cruce = cruce(v_participantes)
    mostrar_onlycruce(v_cruce)
    separacion()
    totalpuntos = promediopuntos(v_cruce)
    print("El promedio de puntos en octavos fue de: ", totalpuntos)
    separacion()
    print("Los participantes se estan enfrentando")
    input("Presiona una tecla para continuar...")
    mostrar_cruce(v_cruce)
    separacion()
    v_participantes = verify1(v_cruce, tercerpuesto, segundopuesto)
    print("Gandores de octavos: ")
    mostrar(v_participantes)
    print()
    # -----------------------------
    print("\033[4;35m" + "-" * 20, "CUARTOS DE FINAL!", "-" * 20 + "\033[0;m")
    print("\033[4;36m" + "Fixture" + "\033[0;m")
    v_cruce = cruce(v_participantes)
    mostrar_onlycruce(v_cruce)
    totalpuntos = promediopuntos(v_cruce)
    separacion()
    print("El promedio de puntos en cuartos fue de: ", totalpuntos)
    separacion()
    print("Los participantes se estan enfrentando")
    mostrar_cruce(v_cruce)
    v_participantes = verify1(v_cruce, tercerpuesto, segundopuesto)
    separacion()
    print("Gandores de cuartos: ")
    mostrar(v_participantes)
    print()
    # -----------------------------
    print("\033[4;35m" + "-" * 20, "SEMIFINAL!", "-" * 20 + "\033[0;m")
    print("\033[4;36m" + "Fixture" + "\033[0;m")
    v_cruce = cruce(v_participantes)
    mostrar_onlycruce(v_cruce)
    totalpuntos = promediopuntos(v_cruce)
    separacion()
    print("El promedio de puntos en semifinal fue de: ", totalpuntos)
    separacion()
    print("Los participantes se estan enfrentando")
    input("Presiona una tecla para continuar...")
    mostrar_cruce(v_cruce)
    tercerpuesto = True
    v_participantes, v_tercerpuesto = verify1(v_cruce, tercerpuesto, segundopuesto)
    tercerpuesto = False
    print()
    # -----------------------------
    print("\033[4;35m" + "-" * 20, "FINAL!", "-" * 20 + "\033[0;m")
    print("\033[4;36m" + "Fixture" + "\033[0;m")
    v_cruce = cruce(v_participantes)
    mostrar_onlycruce(v_cruce)
    separacion()
    print("Los participantes se estan enfrentando")
    input("Presiona una tecla para continuar...")
    mostrar_cruce(v_cruce)
    segundopuesto = True
    v_participantes, v_segundopuesto = verify1(v_cruce, tercerpuesto, segundopuesto)
    segundopuesto = False
    print()
    # -----------------------------
    print("\033[4;35m" + "-" * 20, "TERCER PUESTO!", "-" * 20 + "\033[0;m")
    print("\033[4;36m" + "Fixture" + "\033[0;m")
    v_tercerpuesto = cruce(v_tercerpuesto)
    mostrar_onlycruce(v_tercerpuesto)
    separacion()
    print("Los participantes se estan enfrentando")
    input("Presiona una tecla para continuar...")
    mostrar_cruce(v_tercerpuesto)
    v_tercerpuesto = verify1(v_tercerpuesto, tercerpuesto, segundopuesto)
    print("\033[4;35m" + "-" * 55 + "\033[0;m")
    # Podio-------------------------
    print("\033[1;34m" + "\t\t\t\t\t\tPODIO:" + '\033[0;m')
    print("Primer Puesto: ")
    mostrar(v_participantes)
    print()
    print("Segundo Puesto: ")
    mostrar(v_segundopuesto)
    print()
    print("Tercer Puesto: ")
    mostrar(v_tercerpuesto)
    # -----------------------------
    separacion()
    print("Actualizacion de rankings: ")
    v_aux = new_rank(v_participantes,v_segundopuesto,v_tercerpuesto,v_aux)
    ordenamiento_ranking(v_aux)
    mostrar(v_aux)

if __name__ == "__main__":
    main()
