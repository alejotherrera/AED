__author__ = "Alejo Herrera"

masculino = 0
femenino = 0
sexo = "enter"
medadescolar = 0
supera = bool
while sexo == "M" or sexo == "F" or sexo == "enter":
    sexo = (input("Ingrese sexo M/F: "))
    if sexo == "M":
        masculino = masculino + 1
    elif sexo == "F":
        femenino = femenino + 1

    edad = int(input("Ingrese edad: "))
    if 4 <= edad <= 18 and sexo == "F":
        medadescolar += 1
    if sexo == "M" and edad >= 80:
        supera = True

if masculino > femenino:
    print("Hay mas hombres: ", masculino)
elif masculino == femenino:
    print("Hay la misma cantidad de hombres y mujeres")
else:
    print("Hay mas mujeres: ", femenino)
if supera == True:
    print("Hay al menos un varon que supere los 80 años de edad")

