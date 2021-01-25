__author__ = "Alejo Herrera"


# Modulos

def separacion():
    print("------------------------------------------------")

def carga_datos():
    n = int(input("Ingrese cantidad de temperaturas: "))
    separacion()
    temperaturas = [0] * n
    regiones = [0] * n
    dias = [0] * n
    for i in range(n):
        dia = int(input("Ingrese dia: "))
        region = int(input("Ingrese region: "))
        temperatura = float(input("Ingrese temperatura: "))
        dias[i] = dia
        regiones[i] = region
        temperaturas[i] = temperatura
        separacion()
    return (dias, regiones, temperaturas)


def menudeopciones():
    print("1 _ Cargar datos")
    print("2 _ Promedio de temperaturas")
    print("3 _ Mostrar temperatura de una región")
    print("4 _ Buscar temperaturas mayores a x")
    print("5 _ Salir")
    opcion = int(input("Ingrese opcion: "))
    separacion()
    return opcion


def promediotemperaturas(temperaturas):
    sumatemp = int(0)
    canttemp = len(temperaturas)
    for i in range(canttemp):
        sumatemp += temperaturas[i]
    promedio = sumatemp / canttemp
    return promedio


def buscar_temperatura(regiones, temperatura, region, x):
    exist = False
    for i in range(len(regiones)):
        if regiones[i] == region and temperatura[i] < x:
            exist = True
            break
    return exist


def ordenar(dias, regiones, temperaturas):
    n = len(dias)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if dias[i] > dias[j]:
                dias[i], dias[j] = dias[j], dias[i]
                regiones[i], regiones[j] = regiones[j], regiones[i]
                temperaturas[i], temperaturas[j] = temperaturas[j], temperaturas[i]


def mostrar_temperaturas(dias, regiones, temperaturas, reg):
    print("Dia \t\t Temperatura")
    for i in range(len(regiones)):
        if regiones[i] == reg:
            print(dias[i], "\t\t\t", temperaturas[i])


def main():
    opcion = 0
    while opcion != 5:
        opcion = menudeopciones()
        if opcion == 1:
            dias, regiones, temperaturas = carga_datos()
        elif opcion == 2:
            promedio = promediotemperaturas(temperaturas)
            print("El promedio de temperaturas fue: ", promedio)
            separacion()
        elif opcion == 3:
            ordenar(dias, regiones, temperaturas)
            reg = int(input("Ingrese region: "))
            mostrar_temperaturas(dias, regiones, temperaturas, reg)
            separacion()
        elif opcion == 4:
            reg = int(input("Ingrese region a analizar: "))
            x = int(input("Ingrese temperatura a controlar: "))
            exist = buscar_temperatura(regiones, temperaturas, reg, x)
            if exist:
                resultado = "Hay al menos una temperatura menor a"
            else:
                resultado = "No hay temperaturas menores a"
            print(resultado, x, "en la region analizada")
            separacion()
        elif opcion == 5:
            print("Hasta despues")
            separacion()
        else:
            print("Error, opcion incorrecta")
            separacion()

if __name__ == "__main__":
    main()
