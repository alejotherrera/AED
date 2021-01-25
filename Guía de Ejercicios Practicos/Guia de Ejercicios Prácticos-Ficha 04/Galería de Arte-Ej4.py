__author__="Alejo Herrera"

#Ingreso de cuadros
cuadro1 = int(input("Ingrese cuadro 1"))
cuadro2 = int(input("Ingrese cuadro 2"))
cuadro3 = int(input("Ingrese cuadro 3"))

#Condiciones
if cuadro1>1901 and cuadro1>2000 and cuadro2>1901 and cuadro2>2000 and cuadro3>1901 and cuadro3>2000:
    print("Todos los cuadros pertenecen al siglo xx")

if cuadro1 < 2010 or cuadro2<2010 or cuadro3<2010:
    print ("Renovar stock")