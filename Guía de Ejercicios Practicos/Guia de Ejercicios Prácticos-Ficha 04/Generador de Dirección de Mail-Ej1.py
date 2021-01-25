#Generador de Dirección de Mail

__author__="Alejo herrera"

#Solicitar nombre#
nombre=input("Ingrese su nombre: ")
#Solicitar apellido#
apellido=input("Ingrese su apellido: ")
#Solicitar dominio#
dominio=input("Ingrese su dominio: ")
#Comparacion de primer letra del nombre con letra del apellido##
primeraletranombre=nombre[0]
primeraletraapellido=apellido[0]
if primeraletranombre == primeraletraapellido:
    print(nombre,".",apellido,"@",dominio,".edu.ar")
else:
    print("Su nuevo generado es:", primeraletranombre + apellido, "@", dominio, ".edu.ar")