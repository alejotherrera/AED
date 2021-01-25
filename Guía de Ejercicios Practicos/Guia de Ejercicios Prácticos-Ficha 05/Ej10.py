__author__ = "Alejo Herrera"

print("Calculo de impuesto automotor")

# Ingreso de datos
print("Datos del auto")
modelo = int(input("Ingrese modelo del auto(año de fabricacion): "))
print("Ingrese tipo de auto(solo letra correspondiente): \np:particular\nt:taxi\nr:remiss")
tipo = str(input("Tipo: "))

# Proceso de determinacion de impuesto
if tipo == "p" or tipo == "t":
    if 2010 < modelo < 2020:
        monto = 200
    elif 2000 < modelo < 2010:
        monto = 150
    else:
        monto = 0
    if tipo == "t":
        monto = monto + 150
elif tipo == "r":
    antiguedad = 2020 - modelo
    monto = antiguedad * 100

print("El monto a pagar es: ", monto)
