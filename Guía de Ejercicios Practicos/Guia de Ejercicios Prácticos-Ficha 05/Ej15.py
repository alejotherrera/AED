__author__ = "Alejo Herrera"

print("importe final a pagar a un determinado proveedor")
# Ingreso de datos
categoria = str(input("Ingrese categoria A/B: "))
importe = float(input("Ingrese importe original a abonar: "))

# Procesos
if categoria=="A":
    if importe>=1000:
        descuento = 5 * importe / 100
        total = importe - descuento
    else:
        total = importe
elif categoria=="B":
    if 1500<importe<2500:
        descuento = 5 * importe / 100
        total = importe -descuento
    else:
        total = importe

print("El importe final a pagar es:",total)
