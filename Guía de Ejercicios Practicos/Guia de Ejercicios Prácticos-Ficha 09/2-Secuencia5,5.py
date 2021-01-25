__author__ = "Alejo Herrera"

# Ingreso de n por teclado
n = int(input("Ingrese numero(Con 0 finaliza el proceso de carga): "))
n1 = n2 = mayores_n1 = mayores_n2 = cont_n = cont_5 = 0
# Banderas
flagn1 = flagn2 = ingr5 = True
impar = suecesion = ingr55 =False

while n != 0:

    # Punto A
    if flagn1 and flagn2:
        n1 = int(input("Ingrese n1: "))
        n2 = int(input("Ingrese n2: "))
        flagn1 = flagn2 = False
    else:
        # Determinar mayores a n1 y n2
        if n > n1:
            mayores_n1 += 1
        if n > n2:
            mayores_n2 += 1
        # Contador de numeros ingresados
        cont_n += 1
        # Impar seguido inmediatamente de un par
        if n % 2 != 0:
            impar = True
        else:
            if impar and n % 2 == 0:
                suecesion = True
            impar = False
        # Determinar 5 seguido de otro 5
        if n == 5 and ingr5:
            ingr55 = True
            ingr5 = False
        else:
            if n == 5 and ingr55:
                cont_5 += 1
            ingr55 = False
        ingr5 = True

        # Carga del siguiente numero
        n = int(input("Ingrese numero nuevamente (0 para salir): "))

# Porcentaje del total de numeros calculados
prom1 = round(mayores_n1 / cont_n)
prom2 = round(mayores_n2 / cont_n)

# Imprimir resultados
print("Cuantos numeros son mayores que n1: ",mayores_n1)
print("Cuantos numeros son mayores que n2: ",mayores_n2)
print("Promedio de n1: ",prom1,"y promedio de n2: ",prom2)
if suecesion:
    print("Si se ingreso un impar seguido de un par ")
print("Se ingreso: ",cont_5,"veces un 5 seguido de otro 5")