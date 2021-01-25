__author__ = "Alejo Herrera-85969"

# Desarrolle un programa completo en Python, sin usar las funciones predefinidas min() y max(), que permita cargar
# por teclado tres valores que representan la capacidad ocupada de tres cartuchos de tinta de impresora de los
# colores cian, magenta y amarillo. Considerando que cada cartucho tiene una capacidad máxima de 5ml., calcular y
# mostrar para cada cartucho su porcentaje de carga (nivel de carga actual del cartucho * 100 / 5). Mostrar el
# porcentaje menor, y si el menor fuese igual a cero, indicar con un mensaje que al menos uno de los cartuchos debe
# ser reemplazado.

def pograma():

    # Ingreso de datos
    cartucho1 = float(input("Ingrese capacidad ocupada del cartucho cian: "))
    cartucho2 = float(input("Ingrese capacidad ocupada del cartucho magenta: "))
    cartucho3 = float(input("Ingrese capacidad ocupada del cartucho amarillo: "))

    # Porcentajes
    porcentaje1 = cartucho1 * 100 / 5
    porcentaje2 = cartucho2 * 100 / 5
    porcentaje3 = cartucho3 * 100 / 5

    # Mostrar para cada cartucho su porcentaje de carga
    print("Cian: %", porcentaje1)
    print("Magenta: %", porcentaje2)
    print("Amarillo: %", porcentaje3)

    # Determinar el porcentaje menor
    if porcentaje1 < porcentaje2 and porcentaje1 < porcentaje3:
        menor = porcentaje1
        nombre = "cian"
    elif porcentaje2 < porcentaje3:
        menor = porcentaje2
        nombre = "magenta"
    else:
        menor = porcentaje3
        nombre = "amarillo"

    # Mostrar por pantalla el porcentaje menor
    print("El porcentaje menor fue el color", nombre, "con un total de: %", menor)

    # Si el menor fuese 0
    if menor == 0:
        print("Al menos uno de los cartuchos debe ser cambiados")

pograma()