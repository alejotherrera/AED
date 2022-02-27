def principal():
    cadena = input("Ingrese la cadena: ")
    cont = cumple = 0
    letras = "abcdefghijkmñlopqrstuvwxyzaeiouáéíóú"
    cadena = cadena.lower()
    for i in cadena:
        if i != " " and i != ".":
            if i in letras:
                cont += 1
        else:
            if cont > 4:
                cumple += 1
            cont = 0
    print(cumple)

# Script princial...
if __name__ == '__main__':
    principal()