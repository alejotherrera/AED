def separar():
    print("-" * 100)


# ----------------------------------------------------------------------------------------------------------------------
def menu_arreglos_unidimensionales():
    print('\t\t\t\033[1;35;7m✨Menu de Arreglos Unidimensionales✨\033[0m')
    opc = -1
    while opc != 7:
        v = [2, 7, 4, 8, 5]
        print("\nMenu interactivo de vectores. Se reiniciara el Vector al original en cada uso :)")
        print("{:^60}".format("\033[35m>> Vector original: [2, 7, 4, 8, 5]\033[0m"))
        print("\n1 - Mostrar elementos del vector")
        print("2 - Agregar elementos al final del Vector.")
        print("3 - Agregar elementos en cualquier parte.")
        print("4 - Cambiar elementos.")
        print("5 - Borrar elementos.")
        print("6 - Copiar vectores.")
        print("7 - Volver atras ;)")
        opc = int(input("Ingrese a donde desee ir: "))
        separar()
        if opc == 1:
            print("Elementos del vector de pruebas: ", v)
            separar()

        elif opc == 2:
            print("Para agregar elementos al final de un vector/lista, debemos agregar la palabra \n"
                  "'.append()' a la derecha de la varible del vector, con el elemento que queremos \n"
                  "agregar dentro del parentesis.\nEjemplo: v.append(2)\n")
            v.append(2)
            print("\nComo vemos, hemos agregado el 2 al final del vector: ", v)
            separar()

        elif opc == 3:
            print("Dado el vector: ", v)
            print("\nPara agregar elementos a cualquier posicion del vector, solamente debemos \n"
                  "escribir la posicion en que queremos el nuevo elemento de esta forma: \n"
                  "'v[2:2] = [100]'.")
            v[2:2] = [100]
            print("\nNuevo vector: ", v)
            print("\nComo vemos, hemos agregado el valor '100' en la posicion '2', agrandando el vector :).")
            separar()

        elif opc == 4:
            print("Para remplazar elementos en cualquier seccion del vector, se puede hacer de varias maneras.\n"
                  "Podemos remplazar solo UN elemento en el vector o varios a la vez, veamos: \n\n"
                  "Dado el vector de prueba: ", v, "cambiemos el valor que hay en la posicion '1'.")
            print("Para remplazar el elemento de la posicion 1, debemos escribir 'v[1] = 11'")
            v[1] = 11
            print("\nNuevo vector: ", v)
            print("\nComo vemos, hemos cambiado en la posicion 1, el 7 por el 11: ", v)
            print("\nTambien podemos cambiar elementos desde la reversa o el final, solamente \n"
                  "en la posicion donde deseemos cambiar, ponemos '-1' o '-2' o '-3', etc.")
            print("Ejemplifiquemos: Quiero cambiar el elemento de la posicion '4', \nponemos "
                  "v[-1] = 33")
            v[-1] = 33
            print("\nNuevo vector: ", v,
                  "\n\nComo vemos, hemos cambiado el '5' por el '33'. \nAsi mismo, podemos seguir cambiando el resto "
                  "en reversa,\nsi seguimos disminuyendo la posicion :)")
            separar()
            print("\nAhora, dado el vector modificado: ", v, "quiero remplazar los elementos del indice \n'0' al "
                                                             "indice '2'.")
            print("Escribimos 'v[0:3] = 20, 30, 40'. ")
            v[0:3] = 20, 30, 40
            print("\nVector modificado1: ", v)
            print("\nComo vemos, hemos cambiado los primeros TRES elementos del vector")
            print("\nNOTA: Si ponemos MAS valores de los que vamos a remplazar, se van a agregar igual \n"
                  "agrandando el vector ;)")
            separar()

        elif opc == 5:
            print("Dado el vector: ", v)
            print("\nPara eliminar elementos dentro de un vector, podemos efectuarlo de la siguiente manera: \n"
                  "Eliminando en cantidad: 'v[0:2] = []'")
            v[0:2] = []
            print("\nVector modificado: ", v)
            v = [2, 7, 4, 8, 5]
            print("\nEliminando un elemento: 'v[2:3] = []'")
            v[2:3] = []
            print("\nVector moficiado: ", v)
            separar()
        elif opc == 6:
            v_2 = []
            v_3 = []
            print("Dado el vector: ", v)
            print("\nPara copar vectores o elementos del mismo, podemos hacerlo de las siguientes maneras: \n"
                  "Copiar TODO el vector: 'v_2 = v[:]'")
            v_2 = v[:]
            print("\nHemos copiado los valores del vector 'v' al vector 'v_2': ", v_2)
            print("\nCopiar elementos especificos: 'v_3 = v[0:3]'")
            v_3 = v[0:3]
            print("Hemos copiado los elementos de las posiciones 0, 1 y 2 del vector 'v' al vector v_3: ", v_3)
            separar()
        elif opc == 7:
            print("\nVolvemos al menu principal ;)\n")
        else:
            print("\n\033[0;31m" + 60 * "-")
            print("\033[0;31m" + 26 * "-", "ERROR", 27 * "-")
            print("\033[0;31m" + 60 * "-")
            print()


def arreglos_unidimensionales():
    print('\t\t\t\033[1;35m✨Arreglos Unidimensionales✨\033[0m')
    print("\033[0;0m" + "Los arreglos unidimensionales: Se los puede llamar vectores (ya que en cierto aspecto \n"
                        "lo son) y estos mismos son como dice el nombre, vectores en una dimension.\nEstos mismos"
                        " pueden estar presentes en el eje 'X' o en el eje 'Y', \npero siempre se los piensa como "
                        "que estan en el eje 'X'. \nVamos a dar algunos ejemplos!")
    v = [2, 7, 4, 8, 5]
    print("\nEl vector de prueba es: ", v)
    print("\nHemos creado un vector, o arreglo uni-dimensional, en este caso con 5 elementos. \nSIEMPRE"
          " '''DATO: COMIENZA EN 0'''")
    print("\nHay que tener en cuenta que una LISTA (Vector/Arreglo unidimensional), NO es lo mismo \n"
          "que una TUPLA. La TUPLA no se puede modificar, ni agregar nuevos elementos, etc, \n"
          "en cambio la Lista, le podes agregar nuevos elementos, modificarla, etc.")
    print("\nAhora, veremos ciertas cosas que le podemos hacer a las Listas o Vectores.")
    separar()
    menu_arreglos_unidimensionales()

    separar()


# ----------------------------------------------------------------------------------------------------------------------
def ordenamiento_directo():
    print('\t\t\t\033[1;35m✨Ordenamiento Directo✨\033[0m')
    print(
        "\033[0;0m" + "Existen varios metodos de ordenamiento, tales como el Intercambio directo, Seleccion Directa \n"
                      "o Insercion Directa.\nUno puede optar para aprenderse CUALQUIER metodo de ordenamiento, \nsiempre y"
                      " cuando le sea comodo, por que cualquier metodo cumple su funcion, ordenar.")
    print("Aca solamente voy a presentar una variante de la Seleccion directa, cumple con su funcion \n"
          "no es muy complejo y tiene un termino medio de casi ser eficiente \n"
          "en el uso de recursos.\n")
    print("Se recomienda siempre utilizar cualquier metodo de ordenamiento en una funcion propia.\n(Ver codigo o pagina"
          " 306 - Ficha 13 )\n")

    def selection_sort(v):
        n = len(v)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if v[i] > v[j]:
                    v[i], v[j] = v[j], v[i]

    vector_ordenamiento = [23, 43, 12, 32, 2, 6, 3, 11, 16, 21, 9, 0]
    print("Haremos un ejemplo con el siguiente vector: ", vector_ordenamiento)
    selection_sort(vector_ordenamiento)
    print("Luego de aplicar la funcion de ordenamiento, nos quedo asi: ", vector_ordenamiento)


# ----------------------------------------------------------------------------------------------------------------------
def opcion_busqueda_secuencial():
    print('\t\t\t\033[1;35m✨Busqueda Secuencial✨\033[0m')
    print("\033[0;0m" + "Existen diversos tipos de busquedas en todos los lenguajes habidos y por haber. \nEn "
                        "AED y al menos en primer año, veran la 'Busqueda secuencial' y la 'Busqueda Binaria'.")
    print("Ambas son necesarias y se deberan estudiar SI O SI. \nVan a existir ejercicios que se les va"
          " a pedir buscar con un metodo u otro, pero muy pocas \nveces tendran la oportunidad de elegir ustedes.")
    print("\nEn este caso veremos la busqueda secuencial:")
    print("\nDamos por ejemplo el vector: v_busqueda = [1, 42, 23, 434, 100, 23, 4, 2, 7, 9, 13, 77, 87, 11] \nAplicamos "
          "la busqueda secuencial (ver codigo) para buscar el numero 11.")

    def busqueda_secuencial(v, x):
        n = len(v)
        for i in range(n):
            if x == v[i]:
                return i
        return -1

    v_busqueda = [1, 42, 23, 434, 100, 23, 4, 2, 7, 9, 13, 77, 87, 11]
    x = (int(input("\nIngrese un numero a buscar: ")))
    busqueda = busqueda_secuencial(v_busqueda, x)
    if busqueda == -1:
        print("No se ha encontrado el numero", x, "en el vector")
    else:
        print("El numero esta en la posicion: ", busqueda)
    print("\nComo vemos, si se encuentra el numero, retornara la posicion donde lo encontro.\n"
          "Si no lo hubiera encontrado, retornaria un '-1', por ende efectue una condicion \n"
          "donde si retornaba ese valor, decia que no se pudo encontrar nada.")


# ----------------------------------------------------------------------------------------------------------------------


def opcion_busqueda_binaria():
    print('\t\t\t\033[1;35m✨Busqueda Binaria✨\033[0m')
    print("\033[0;0m" + "Existen diversos tipos de busquedas en todos los lenguajes habidos y por haber. \nEn "
                        "AED y al menos en primer año, veran la 'Busqueda secuencial' y la 'Busqueda Binaria'.")
    print("Ambas son necesarias y se deberan estudiar SI O SI. \nVan a existir ejercicios que se les va"
          " a pedir buscar con un metodo u otro, pero muy pocas \nveces tendran la oportunidad de elegir ustedes.")
    print("\nEn este caso veremos la Busqueda Binaria:")
    print("\nDamos por ejemplo el vector: v_busqueda = [1, 42, 23, 434, 100, 23, 4, 2, 7, 9, 13, 77, 87, 11]\nAplicamos "
          "la busqueda secuencial (ver codigo) para buscar el numero 11.")
    print("DATO, TIENE QUE ESTAR TODO ORDENADO PARA APLICAR LA BUSQUEDA BINARIA")

    def binary_search(v, x):
        n = len(v)
        izq, der = 0, n - 1
        while izq <= der:
            c = (izq + der) // 2
            if x == v[c]:
                return c
            if x < v[c]:
                der = c - 1
            else:
                izq = c + 1
        return -1


    def selection_sort(v):
        n = len(v)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if v[i] > v[j]:
                    v[i], v[j] = v[j], v[i]

    v_busqueda = [1, 42, 23, 434, 100, 23, 4, 2, 7, 9, 13, 77, 87, 11]
    selection_sort(v_busqueda)
    print("\nDespues de ordenar, nos quedo el vector asi: ", v_busqueda)
    print("Ahora podemos aplicar la busqueda Binaria")
    x = (int(input("\nIngrese un numero a buscar: ")))
    busqueda = binary_search(v_busqueda, x)
    if busqueda == -1:
        print("No se ha encontrado el numero", x, "en el vector")
    else:
        print("El numero esta en la posicion: ", busqueda)
        print("\nComo vemos, si se encuentra el numero, retornara la posicion donde lo encontro.\n"
              "Si no lo hubiera encontrado, retornaria un '-1', por ende efectue una condicion \n"
              "donde si retornaba ese valor, decia que no se pudo encontrar nada.")

# ----------------------------------------------------------------------------------------------------------------------



def test():
    print('{:^70}'.format('\033[1;35;7m✨ BIENVENIDO ✨\033[0m'))
    print('\n\033[3mElige una opcion y descubre todo lo que necesitas para el TP3 y el parcial (no incluye matrices) :D\033[0m')
    opc = -1
    while opc != 0:
        separar()
        print("\033[3;35m" + "1 - Arreglos Uni-dimensionales")
        print("2 - Ordenamiento por seleccion directa (Selecion Sort)")
        print("3 - Busqueda Secuencial (Linear Search)")
        print("4 - Busqueda Binaria (Binary Search)")
        print("0 - Salir")
        opc = int(input("Ingrese a donde desee ir:"))
        separar()

        if opc == 1:
            arreglos_unidimensionales()

        elif opc == 2:
            ordenamiento_directo()

        elif opc == 3:
            opcion_busqueda_secuencial()

        elif opc == 4:
            opcion_busqueda_binaria()

        elif opc == 0:
            print()
            print("\033[1;34m" + 60 * "-")
            print("\033[1;34m" + "|" + 19 * " " + "Fin del programa" + 23 * " " + "|")
            print(60 * "-")

        else:
            print("\n\033[0;31m" + 60 * "-")
            print("\033[0;31m" + 26 * "-", "ERROR", 27 * "-")
            print("\033[0;31m" + 60 * "-")
            print()


test()
