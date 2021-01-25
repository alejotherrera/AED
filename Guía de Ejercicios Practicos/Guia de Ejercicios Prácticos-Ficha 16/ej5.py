
import random


def separacion():
    print("-" * 30)


def carga_automatica(n):
    tabla = [[0] * 3 for f in range(10)]
    for i in range(n):
        caja = random.randrange(10)
        turno = random.randrange(3)
        monto = random.randrange(100,1000)
        tabla[caja][turno] += monto
    return tabla

def principal():
    n = int(input("Ingrese n cobranzas realizadas: "))
    tabla = carga_automatica(n)




if __name__ == '__main__':
    principal()