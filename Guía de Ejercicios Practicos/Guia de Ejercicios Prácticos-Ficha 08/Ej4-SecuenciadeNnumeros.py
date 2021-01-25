__author__ = "Alejo Herrera"

n = -1
# Carga de variables
cont5 = contn = ig = contig = contmay = anterior = 0

# Ciclo
while n != 0:
    n = int(input("Ingrese n: "))
    contn += 1
    # PuntoB
    if contn == 1:
        ig = n
    else:
        if ig == n:
            contig += 1
    # PuntoA
    if n % 10 == 5:
        cont5 += 1
    # PuntoB
    if n > anterior:
        contmay += 1
    anterior = n

# Imprimir resultados
print("Los numeros ingresados terminados en 5 son: ",cont5)
print("La cantidad de veces que esta el primer num es: ",contig)
print("La cantidad de mayores al anterior es: ",contmay)