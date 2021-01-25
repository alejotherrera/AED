__author__ = "Alejo Herrera"

print("Analisis de palabra ")

#Ingreso de palabra
palabra = str(input("Ingrese palabra: "))

#Procesos
largo = len(palabra)
ultima_letra = palabra[largo - 1]

#Carteles finales
print("La palabra tiene: ", largo)
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print("La palabra termina con vocal")