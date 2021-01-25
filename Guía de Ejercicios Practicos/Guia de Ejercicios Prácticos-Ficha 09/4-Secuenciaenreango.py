__author__ = "Alejo Herrera"

#Desarrollar un programa de Python que permita cargar por teclado un secuencia de números, uno por uno.
# Siempre se supone que el usuario cargará un 0(cero) para indicar el final del proceso de carga.
# El cero no debe considerarse un dato a procesar. El programa debe:

#a) Determinar cuantos números se encuentran en el rango definido por 2 números p y q previamente ingresados
# (validar que los números que definen el rango son mayores a cero)

#b) Determinar la cantidad de veces que se ingresaron 2 números contiguos pares.

#c) Determinar la cantidad de números que son múltiplos del primer numero de la secuencia

#d) Determinar el porcentaje que representa la cantidad del primer punto sobre el total de números de la secuencia

p = int(input("Ingrese p:"))
q = int(input("Ingrese q:"))
primer_vuelta = True
pares = False
cont_entrepq = cont_paresseguidos = cont_multiprimern = n_anterior = 0
n = -1
while n != 0:
    n = int(input("Ingrese numero(0 para finalizar): "))
    if n == 0:
        break
    #PuntoA
    if p<n<q or p>n>q:
        cont_entrepq += 1
    #PuntoB
    if n % 2 == 0 and not pares:
        pares = True
    else:
        if pares and n % 2 == 0:
            cont_paresseguidos += 1
            pares = False
    n_anterior = n
    #PuntoC
    if primer_vuelta:
        primer_n = n
        primer_vuelta = False
    else:
        if n % primer_n == 0 and not primer_vuelta:
            cont_multiprimern += 1


print("La cantidad de numeros entre",p,"y",q, "es:",cont_entrepq)
print("La cantidad de pares contiguos fueron: ",cont_paresseguidos)
print("La cantidad de muplitplos del primer numero de la secuencia es: ",cont_multiprimern)