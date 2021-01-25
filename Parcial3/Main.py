

# Una fabrica de productos alimenticios nos pide un programa para procesar los datos de los Productos que estan siendo
# fabricados y distribuidos. Por cada Producto se conoce sú codigo de identificación (un entero),
# su nombre, el tipo de producto (un valor del 0 al 19, por ejemplo: 0: Fideos, 1: Enlatados, 2: Mermeladas, etc.)
# y el precio de venta de dicho producto. Se desea almacenar la información referida a los n productos  en un arreglo de
# registros de tipo Producto (definir el tipo Producto  y cargar n por teclado).

# Se pide desarrollar un programa en Python controlado por un menú de opciones,  que permita gestionar las siguientes tareas:

# 1-Cargar el arreglo con los datos de los n productos. Valide que el precio de venta sea mayor a cero y que los tipo de
# producto esté en el rango especificado. Puede hacer la carga en forma manual, o puede generar los datos en forma
# automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

# 2-Mostrar todos los datos de todos los productos, en un listado ordenado de menor a mayor según los códigos de identificación.

# 3-Determinar el importe total de venta por cada tipo de producto, 20 acumuladores en total en vector de acumulación.

# 4-Determinar y mostrar el producto con mayor precio de venta. Mostrar además la diferencia entre este precio mayor, y el
# precio promedio entre todos los productos del vector.

# 5-Determinar si existe un producto cuyo nombre sea igual x, siendo x un valor que se carga por teclado. Si existe, mostrar
# sus datos, cambiar el valor del precio de venta por otro valor p que se carga por teclado, y volver a mostrar sus datos.
# Si no existe, informar con un mensaje. Si existe mas de un registro que coincida con esos parámetros de búsqueda, debe
# mostrar sólo el primero que encuentre.


class Producto:
    def __init__(self, codigo, nombre, tipo, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio


def separacion():
    print("-" * 100)


def validar_datos(n):
    precio = tipo = 0
    vector = [0] * n
    for i in range(n):
        back = True
        back2 = True
        print("Carga de datos")
        codigo = int(input("Ingrese codigo: "))
        nombre = input("Ingrese nombre: ")
        while back:
            if 0 <= tipo <= 19:
                tipo = int(input("Ingrese tipo: "))
                back = False
            else:
                print(10 * "_", "Error", 10 * "_")
                print("tipo invalido, porfavor ingrese tipo entre 0 y 19")
        while back2:
            if precio >= 0:
                precio = (input("Ingrese el precio: "))
                back2 = False
            else:
                print(10 * "_", "Error", 10 * "_")
                print("Precio invalido, porfavor ingrese un precio mayor a 0")
        vector[i] = Producto(codigo, nombre, tipo, precio)
        separacion()
    return vector


def ordenamientodirecto(productos):
    n = len(productos)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if productos[i].codigo > productos[j].codigo:
                productos[i], productos[j] = productos[j], productos[i]
    return productos


def mostrar(productos):
    m = ""
    m += "{:<15}".format("codigo: " + str(productos.codigo))
    m += "{:<15}".format("nombre: " + str(productos.nombre))
    m += "{:<15}".format("tipo: " + str(productos.tipo))
    m += "{:<15}".format("precio: " + str(productos.precio))
    print()
    print(m)


def show(a):
    n = len(a)
    for i in range(n):
        mostrar(a[i])


def promedio_precios(productos):
    suma = 0
    n = len(productos)
    for i in range(n):
        suma += int(productos[i].precio)

    promedio = (suma / n)
    return promedio


def precio_mayor(productos):
    n = len(productos)
    mayor = (productos[0].precio)
    nombre = productos[0].nombre
    codigo = productos[0].codigo
    for i in range(n):
        if mayor < productos[i].precio:
            mayor = productos[i].precio
            nombre = productos[i].nombre
            codigo = productos[i].codigo

    return mayor, nombre, codigo


def busqueda_x(productos, x):
    print("Ingrese nombre a buscar: ")
    n = len(productos)
    izq, der = 0, n - 1
    while izq <= der:
        a = (izq + der) // 2
        if x == productos[a].nombre:
            return a
        if x < productos[a].nombre:
            der = a - 1
        else:
            izq = a + 1
        return -1


def menu():
    separacion()
    print("1-Cargar el arreglo")
    print("2-Mostrar todos los productos")
    print("3-Determinar el importe de venta total por acada tipo de producto")
    print("4-Determinar y mostrar el precio mayor de venta.")
    print("5-Buscar producto y cambiarle su precio")
    print("6-Para salir")


def main():
    print("Bienvenido a la gestion de productos alimenticios")
    n = int(input("Ingrese cantidad de productos: "))
    op = 0
    while op != 6:
        menu()
        op = int(input("Ingrese opcion: "))
        separacion()
        if op == 1:
            print(10 * "-", "Productos", 10 * "-")
            productos = validar_datos(n)
        elif op == 2:
            for i in range(n):
                show(productos)
        elif op == 3:
            break
        elif op == 4:
            mayor, nombre, codigo = precio_mayor(productos)
            print("El producto con mayor precio es: ", nombre)
            print("Con el codigo: ", codigo)
            prom = str(promedio_precios(productos))
            if prom > mayor:
                diferencia = prom - mayor
                print("No supera el promedio de precios, le falta", "$", diferencia)
            else:
                diferencia = mayor - promedio_precios(productos)
                print("Supera el promedio de precios por", "$", diferencia)
        elif op == 5:
            x = input("Ingrese el nombre del producto a buscar: ")
            if x == -1:
                print("No se encontro un producto con el nombre ingresado")
            else:
                pos = busqueda_x(productos, x)
                productos.precio[pos:pos] = input("Ingrese nuevo precio: ")


if __name__ == "__main__":
    main()
