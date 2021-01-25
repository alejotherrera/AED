__author__ = "Alejo Herrera"


def validacion():
    n = int(input("Ingrese cantidad de ventas: "))
    while n <= 0:
        print("Error, ingrese un numero mayor a 0")
    return n


def separacion():
    print("------------------------------------------------")


def carga(n):
    articulos = []
    vendida = []
    for i in range(n):
        print("Articulo: ",i+1)
        articulos.append(input("Ingrese articulo(0 al 3): "))
        vendida.append(input("Cantidad vendida del articulo: "))
        separacion()
    return articulos,vendida

def cantidadvendida(articulos,vendida):
    print("Articulo:", "\t\t","Total vendidos:")
    for i in range(len(articulos)):
        print(articulos[i], "\t\t\t\t",vendida[i])


def main():
    n = validacion()
    separacion()
    #Carga de datos
    articulos,vendida = carga(n)
    cantidadvendida(articulos,vendida)

if __name__ == "__main__":
    main()
