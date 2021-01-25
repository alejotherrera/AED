# Ingreso de datos
print("Datos del primer articulo")
nom1 = (input("Nombre: "))
cant1 = int(input("Cantidad vendida del articulo: "))
precio1 = int(input("Precio unitario: "))

print("Datos del segundo articulo")
nom2 = (input("Nombre: "))
cant2 = int(input("Cantidad vendida del articulo: "))
precio2 = int(input("Precio unitario: "))

print("Datos del tercer articulo")
nom3 = (input("Nombre: "))
cant3 = int(input("Cantidad vendida del articulo: "))
precio3 = int(input("Precio unitario: "))

# Productos vendidos
venta1 = cant1 * precio1
venta2 = cant2 * precio2
venta3 = cant3 * precio3

# Maximo
absoluto = venta1+venta2+venta3
maximo = float(max(venta1,venta2,venta3))

# Proceso
if maximo == venta1:
    nombremaximo=nom1
elif maximo == venta2:
    nombremaximo=nom2
else:
    nombremaximo=nom3

mayoraporte = int((maximo * 100) / absoluto)

print("El mayor aporte fue:",nombremaximo,"con un total de %",mayoraporte)