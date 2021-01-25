__author__ = "Alejo Herrera"

#Complejo de cines

#Declarar variables
cont = 1
espec = " "
contdesc = 0
total = 0
while espec != 0:
    espec = 0
    espec = int(input("Ingrese cantidad de espectadores : "))
    desc = str(input("Descuento S/N: "))
    if desc == "S":
        precio = 50
        contdesc = contdesc + 1
    else:
        precio = 75
    total = espec * precio + total
    precio = 0


print("El total recaudado es:",total)

print("Se efectuaron:",contdesc,"con descuento")