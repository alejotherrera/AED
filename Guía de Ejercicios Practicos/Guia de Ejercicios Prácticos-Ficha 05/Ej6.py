__author__ = "Alejo Herrera"

#Ingreso de datos
#Ingreso maximo de niños por curso
cupos = int(input("Ingrese cupo maximo por curso: "))
#Ingreso primer curso
print("datos del primero curso: ")
codigo1 = (input("Ingrese codigo de identeficacion: "))
niños1 = int(input("Ingrese cantidad de niños: "))
niñas1 = int(input("Ingrese cantidad de niñas: "))
#Ingreso segundo curso
print("datos del segundo curso: ")
codigo2 = (input("Ingrese codigo de identificacion: "))
niños2 = int(input("Ingrese cantidad de niños: "))
niñas2 = int(input("Ingrese cantidad de niñas: "))
#Ingreso tercer curso
print("datos del tercer curso: ")
codigo3 = (input("Ingrese codigo de identificacion: "))
niños3 = int(input("Ingrese cantidad de niños: "))
niñas3 = int(input("Ingrese cantidad de niñas: "))

# Proceso de condiciones

# Código de identificación del curso que tenga menos alumnos inscriptos
total1=niños1+niñas1
total2=niños2+niñas2
total3=niños3+niñas3


if total1 < total2 and total1 < total3:
    print("A):", codigo1)
elif total2 < total1 and total2 < total3:
    print("B):", codigo2)
elif total3 < total1 and total3 < total2:
    print("C):", codigo3)

# Porcentaje de niñas de cada curso
porcentajeniñas1 = niñas1 * 100 / cupos
print("Curso: ",codigo1," porcentaje de niñas: %",porcentajeniñas1)
porcentajeniñas2 = niñas2 * 100 / cupos
print("Curso: ",codigo2," porcentaje de niñas: %",porcentajeniñas2)
porcentajeniñas3 = niñas3 * 100 / cupos
print("Curso: ",codigo3," porcentaje de niñas: %",porcentajeniñas3)

# Porcentaje de niños de cada curso
porcentajeniños1 = niños1 * 100 / cupos
print("Curso: ",codigo1," porcentaje de niños: %",porcentajeniños1)
porcentajeniños2 = niños2 * 100 / cupos
print("Curso: ",codigo2," porcentaje de niños: %",porcentajeniños2)
porcentajeniños3 = niños3 * 100 / cupos
print("Curso: ",codigo3," porcentaje de niños: %",porcentajeniños3)

#Promedio general de alumnos
promediogeneral = (total1+total2+total3) / 3
print("El promedio general es: ", promediogeneral)

#cartel si se supera cantidad de cupos maximo por curso
if total1>cupos or total2>cupos or total3>cupos:
    print("Considere crear otra divison, se supero el cupo maximo en uno de los cursos")


