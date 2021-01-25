__author__ = "Alejo Herrera"


# Ingreso de n por teclado
n = int(input("Ingrese numero(Con 0 finaliza el proceso de carga): "))

# Carga de variables
div_4 = anterior = mayorimpar = primer_n = cont_primern = cont_123 = 0
primimpar = flag1 = flag2 = False
primer_vuelta = True

# Script principal
while n != 0:

    # Punto A
    if n % 4 == 0:
        div_4 += 1

    # Punto B
    if n % 2 != 0:
        if not primimpar:
            mayorimpar = n
            primimpar = True
        elif n > mayorimpar:
            mayorimpar = n

    # Punto C
    if primer_vuelta:
        primer_n = n
        primer_vuelta = False

    if n == primer_n:
        cont_primern += 1

    if n == 1:
        flag1 = True
        flag2 = False
    else:
        if n == 2 and flag1:
            flag2 = True
        else:
            if n == 3 and flag2:
                cont_123 += 1
            flag2 = False
        flag1 = False

    # Carga del siguiente numero
    n = int(input("Ingrese numero nuevamente (0 para salir): "))


print("1-La cantidad de numeros divisibles por 4 es: ",div_4)
print("2-Mayor de los impares es: ",mayorimpar)
print("3-El primer numero fue el: ",primer_n," y se ingreso: ",cont_primern," veces")
print("4-Cantidad de secuencia 1 2 3 es: ",cont_123)