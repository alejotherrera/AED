print("-----------Parcial 3-----------")


# Recordar poner comentarios y ctr+alt+l

def separacion():
    print("-" * 100)


# Tabulacion
print("\t")


def write(vector):
    r = ""
    r += "{:<15}".format(":" + str(vector))
    print()


class vec:
    def __init__(self, a):
        self.a = a


def ordenamientodirecto(vector):
    n = len(vector)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vector[i] > vector[j]:
                vector[i], vector[j] = vector[j], vector[i]
    return vector


def busqueda_secuencial(vector, x):
    for i in range(len(vector)):
        if x == vector[i]:
            return i
    return -1


def busqueda_binaria(vector, x):
    n = len(vector)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == vector[c]:
            return c
        if x < vector[c]:
            der = c - 1
        else:
            izq = c + 1
        return -1


def menu():
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6")
