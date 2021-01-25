__author__ = "Herrera Alejo/Galanti Matias/Dellamas Agustin -   Grupo: TP4-G139"

import os.path
from TP4_Clases import *
from TP4_Module import *


def main():
    fixture = []
    archive = "paises.csv"
    if os.path.exists(archive):
        vector = extraer_paises(archive)
        opcion = 0
        while opcion != 8:
            opcion = menudeopciones()
            separacion()
            if opcion == 1:
                show(vector)
            elif opcion == 2:
                op2(vector)
            elif opcion == 3:
                paises_conf_cpg(vector)
            elif opcion == 4:
                newvector, conf = create_conf(vector)
                binary_save(newvector, conf)
            elif opcion == 5:
                op5(vector)
            elif opcion == 6:
                fixture = preparar_proximofixture(vector)
            elif opcion == 7:
                if len(fixture) != 0:
                    nombre = str(input("Ingrese nombre a buscar: "))
                    res = buscar_nombre(fixture, nombre)
                    if res != -1:
                        grupo = grup(res)
                        print("El equipo: " + str(nombre) + " esta en el grupo " + str(grupo))
                    else:
                        print("No se puede procesar la solicitud(Equipo no encontrado)")
                else:
                    print("Primero debe generar el fixture(opcion 6)")
            elif opcion == 8:
                print("¡¡Gracias por utilizar el programa!!")
            else:
                print("Opcion incorrecta,porfavor ingrese una opcion valida")
    else:
        print("Archivo 'paises.csv' no encontrado")


if __name__ == '__main__':
    main()

