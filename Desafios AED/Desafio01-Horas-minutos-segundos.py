#Desarrolle un programa o script Python que permita cargar por teclado un número entero que representa la  cantidad de segundos que pasaron desde un evento dado.
#El programa debe convertir esa cantidad de segundos  a la cantidad de horas, minutos y segundos que transcurrieron.

__author__= "Alejo Herrera"
#Ingreso de segundos#
segundosingresados = int(input("ingrese segundos: "))
#Guardado y pasaje a variable auxiliar#
aux = segundosingresados
#Determinar valor de Hora,Minutos y segundos#
horas = 0
minutos = 0
segundos = 0
#Determinar cantidad de Hora minutos y segundos apartir de auxiliar#
while aux>0:
    if (aux-60)>0:
        minutos = minutos+1
    if minutos == 60:
        horas = horas+1
        minutos = 0
    if (aux-60)<0:
        segundos = aux
    aux = aux-60
#Printear de resultado#
print (horas,minutos,segundos)


##Quinta adicional##
horas = int(input("Ingrese horas: "))
minutos = int(input("Ingrese minutos: "))
segundos1 = int(input("Ingrese segundos: "))
aux1 = (horas*3600)+(minutos*60)+segundos1
print ("Los segundos totales son: ", aux1)
