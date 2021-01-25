__author__ = "Alejo Herrera"

def menuprint():
    print("1 superficie de un triángulo")
    print("2 mostrar el perímetro del triángulo")
    print("3 informar la longitud del lado menor")

def menuproceso():
    opcion = int(input("Elija opcion: "))
    if opcion != 1 and opcion != 2 and opcion != 3:
        print("Error, ingrese opcion valida")
    if opcion == 1:
        altura = float(input("Ingrese altura del triangulo: "))
        base = float(input("Ingrese base del triangulo: "))
        superficie = (base * altura) / 2
        print("La superficie es: ", superficie)
    if opcion == 2:
        lado1 = float(input("Ingrese lado 1: "))
        lado2 = float(input("Ingrese lado 2: "))
        lado3 = float(input("Ingrese lado 3: "))
        perimetro = lado1+lado2+lado3
        print ("El perimetro es: ",perimetro)
    if opcion == 3:
        lado1 = float(input("Ingrese lado 1: "))
        lado2 = float(input("Ingrese lado 2: "))
        lado3 = float(input("Ingrese lado 3: "))
        menor = min(lado1, lado2, lado3)
        print("El lado menor es: ", menor)

menuprint()

menuproceso()