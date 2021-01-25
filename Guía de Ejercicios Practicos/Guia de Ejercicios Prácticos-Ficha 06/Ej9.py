__author__ = "Alejo Herrera"

#Comisión de Vendedores

# Declarar variables
categoria = 1
totalventa = 0
ventacat1 = 0
ventacat2 = 0
ventacat3 = 0
ventacat4 = 0

#Estructura repetitiva
while categoria != 0:
    categoria = int(input("Ingrese categoria: "))
    if categoria != 0:
        totalventa = float(input("Ingrese total de ventas: "))
        if categoria == 1:
         ventacat1 = (totalventa * 10 / 100) + ventacat1
        elif categoria == 2:
         ventacat2 = (totalventa * 25 / 100) + ventacat2
        elif categoria == 3:
            ventacat3 = (totalventa * 30 / 100) + ventacat3
        elif categoria == 4:
            ventacat4 = (totalventa * 40 / 100) + ventacat4
        else:
         print("ingrese categoria valida")

print("Categoria 1:", ventacat1)
print("Categoria 2:", ventacat2)
print("Categoria 3:", ventacat3)
print("Categoria 4:", ventacat4)


