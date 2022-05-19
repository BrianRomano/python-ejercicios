"""
Dadas dos listas se debe realizar diferentes tareas por el orden indicado:
1. Añade a la lista1 el numero 1234 y luego el texto 'Hola'
2. Añade a la lista2 el texto 'Adios' y luego el numero 1234
3. Genera una lista3 con todos los elementos de la lista 1, excepto el ultimo
4. Genera una lista4 con todos los elementos de la lista2, excepto el primero y el ultimo
5. Genera una lista5 con todos los elementos de la lista4 + lista3
"""

# listas
lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

# completa el ejercicio
lista1.append(1234)
lista1.append("Hola")
lista2.append("Adios")
lista2.append(1234)

lista3 = lista1[:-1]
lista4 = lista2[1:-1]
lista5 = lista4 + lista3

print(lista3)
print(lista4)
print(lista5)
