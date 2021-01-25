__author__ = "Alejo Herrera"

n = -1
contm6 = anterior = contdiv = cantidad_secuencia = contascc = contn = secuencia_ascendente = 0
contasc = 1

n = int(input("Ingrese un numero (la carga finaliza cuando ingrese 0): "))

while n != 0:

    contn += 1
    # Punto A
    if n % 6 == 0:
        contm6 += n
    # Punto B
    if contn > 1:
        if anterior % n == 0:
            contdiv += 1
        # PuntoC
        contasc += 2
        if anterior % 2 != 0 and n % 2 != 0 > anterior:
            contascc += 1
        else:
            if secuencia_ascendente >= 2:
                cantidad_secuencia += 1
            secuencia_ascendente = 0

    anterior = n
    n = int(input("Ingrese otro numero: "))

promedio6 = round(contm6 / contn,2)

print("El promedio de los numeros que son multiplo de 6 es: ", promedio6)
print("La cantidad de numeros que son divisor exacto del anterior es: ", contdiv)
print("La cantidad de veces que se genero una secuencia ascendente de 3 o mas numeros impares: ",cantidad_secuencia)
