__author__ = "Alejo Herrera"

#Datos de los postulantes
print("Datos del postulante 1")
nombre1=str(input("Nombre: "))
rtarealizadas1=int(input("Respuestas realizadas: "))
rtacorrectas1=int(input("Respuestas correctas: "))

print("Datos del postulante 2")
nombre2=str(input("Nombre: "))
rtarealizadas2=int(input("Respuestas realizadas: "))
rtacorrectas2=int(input("Respuestas correctas: "))

print("Datos del postulante 3")
nombre3=str(input("Nombre: "))
rtarealizadas3=int(input("Respuestas realizadas: "))
rtacorrectas3=int(input("Respuestas correctas: "))

#Proceso de porcentaje
porcentaje1=rtacorrectas1*100/rtarealizadas1
porcentaje2=rtacorrectas2*100/rtarealizadas2
porcentaje3=rtacorrectas3*100/rtarealizadas3

print("Nivel Superior:Porcentaje >= 90%\nNivel Medio:75% <= Porcentaje < 90%\nNivel Regular:50% <= Porcentaje < 75%\nFuera de Nivel:Porcentaje < 50%")

#Definir el mejor
maximo=max(porcentaje1, porcentaje2, porcentaje3)

if maximo==porcentaje1:
    nombreganador=nombre1
elif maximo==porcentaje2:
    nombreganador=nombre2
else:
    nombreganador=nombre3

if maximo>=90:
    print("El ganador es:", nombreganador)
    print("Con un porcentaje de %",maximo)
    print("Nivel superior")
elif 75<=maximo<90:
    print("El ganador es:", nombreganador)
    print("Con un porcentaje de %", maximo)
    print("Nivel Medio")
elif 50<=maximo<75:
    print("El ganador es:", nombreganador)
    print("Con un porcentaje de %", maximo)
    print("Nivel Regular")
else:
    print("El ganador es:", nombreganador)
    print("Con un porcentaje de %", maximo)
    print("Fuera de Nivel")



