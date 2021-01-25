__author__ = "Alejo Herrera"

print("Índice de Masa Corporal (IMC)")
masa = float(input("Ingrese su peso: "))
alt = float(input("Ingrese su altura: "))

# Calculo IMC(Indice de masa corporal)
imc = masa / (alt ** 2)

if imc <= 16:
    print("Necesita asistencia de un médico, los riesgos para su salud son muy altos")
elif imc <= 17:
    print("Usted tiene infrapeso, aliméntese más")
elif imc <= 18:
    print("Usted tiene bajo peso, aliméntese mejor")
elif 18 < imc <= 26:
    print("Usted tiene un peso saludable, continúe así!")
elif 26 < imc < 30:
    print("Tiene sobrepeso de grado I, hoy es un buen día para empezar a hacer ejercicios")
elif 30 <= imc <= 35:
    print("Tiene obesidad de grado II, necesita el apoyo de un plan nutricional")
elif 35 < imc <= 40:
    print("Tiene obesidad grado III (pre-mórbida), consulte con su médico los riesgos para su salud")
else:
    print(
        "Usted tiene obesidad de grado IV (mórbida), los riesgos para su salud son muy altos, consulte con su médico "
        "a la brevedad")