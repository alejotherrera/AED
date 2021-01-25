def cargar():
    lote = []
    n = 1
    # Validacion
    while n > 0:
        n = int(input("Ingrese valor a cargar(0 para salir): "))
        if n <= 0:
            break
        lote.append(n)
    return lote


def separacion():
    print("--------------------------------------------------")


def opcion1(lote):
    pr = int(input("Ingrese el primer valor: "))
    seg = int(input("Ingrese el segundo valor: "))
    suma = 0
    if pr > seg:
        inf = seg
        sup = pr
    else:
        inf = pr
        sup = seg

    for i in range(len(lote)):
        if inf < lote[i] < sup:
            suma += lote[1]
    promedio = suma / len(lote)
    return promedio


def opcion2(lote):
    entry = True
    menor = 0
    for i in range(len(lote)):
        if lote[i] % 2 != 0 and entry:
            entry = False
            menor = lote[i]
        if lote[i] % 2 != 0:
            menor = min(menor, lote[i])
    return menor


def listar_multiplos(lote):
    multiplo = int(input("Ingrese valor multiplo: "))
    res = ''
    for pos in range(len(lote)):
        if lote[pos] % multiplo == 0:
            res += str(lote[pos]) + ', '
    return res

def menu():
    print("1-Obtener el promedio de los números comprendidos entre dos valores ingresados por el usuario")
    print("2-Obtener el menor número impar del lote")
    print("3-Imprimir todos los números múltiplos de un valor ingresado por el usuario separados por comas")
    print("4-Salir")


def main():
    lote = cargar()
    print(lote)
    separacion()
    op = 0
    while op != 4:
        menu()
        separacion()
        op = int(input("Ingrese opcion: "))
        separacion()
        if op == 1:
            promedio = opcion1(lote)
            print("El promedio es: ", promedio)
        elif op == 2:
            menor = opcion2(lote)
            print("El menor es: ", menor)
        elif op == 3:
            print(listar_multiplos(lote))
        else:
            print("Gracias por usar el programa")


if __name__ == '__main__':
    main()
