__author__ = "Alejo Herrera"

# Sucesión 3n + 1 o Sucesión de Collatz

# Ingreso por teclado
n = int(input("Ingrese numero:"))

# Variables a usar
i = 0
vueltas = 1
num = n
orbita = []
ant = 0
promedio = 1
mayor = 0
# Repetitiva/Loop
while n != 1:
    if n == 1:
        pass
    promedio += n
    mayor = max (ant,n,mayor)
    ant = n
    if n % 2 == 0:
        n = n / 2
        print("%d," % (n), end="")
    else:
        n = 3 * n + 1
        print("%d," % (n), end="")

    vueltas += 1

#Determinar promedio
totalpromedio = promedio / vueltas

# Mostrar valores
print(" ")
print("n = ", num)
print("Orbita de n =", num)
print("Longitud de la orbita(Cantidad de valores calculados hasta llegar al 1):", vueltas)
print("Promedio de todos los valores de la órbita:",totalpromedio)
print("Mayor numero de los numeros en esa orbita",mayor)
