"""
Crear una funcion llamada recortar(numero, minimo, maximo)
    1. El primero es el numero a recortar
    2. El segundo es el limite inferior
    3. El tercero es el limite superior
La funcion tendra que cumplir lo siguiente:
    1. Devolver el limite inferior si el numero es menor que este
    2. Devolver el limite superior si el numero es mayor que este
    3. Devolver el numero sin cambios si no se supera ningun limite
"""

numero = int(input("Ingrese un numero: "))
minimo = int(input("Ingrese un numero minimo: "))
maximo = int(input("Ingrese un numero maximo: "))


def recortar(num, min, max):
    if num < min:
        print(min)
    elif num > max:
        print(max)
    else:
        print(num)


recortar(numero, minimo, maximo)
