"""
A partir de una variable llamada tupla, imprimir por pantalla los siguiente
    1. El ultimo elemento de la tupla
    2. El numero de elementos que tiene la tupla
    3. La posicion donde se encuentra el numero 123 de la tupla
    4. Una lista con los primeros tres elementos de la tupla
    5. El elemento que hay en la posicion con indice 4 de la tupla
    6. El numero de veces que aparece el 4 en la tupla
"""

tupla = (100, "Hola", 4, 123, -50, 4, "Adios")

print(tupla[-1])
print(len(tupla))
print(tupla.index(123))
print(tupla[:3])
print(tupla[4])
print(tupla.count(4))
