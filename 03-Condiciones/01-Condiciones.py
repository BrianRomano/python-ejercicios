"""
Utilizando una condicion if-elif-else debes realizar un programa que compare la longitud
de dos variables (cadena_1, cadena_2) y en funcion del resultado almacene un valor en otra variable
llamada 'resultado':
    - Si cadena_1 es más larga que cadena_2, la variable 'resultado' debe tener el valor 1
    - Si cadena_1 es más corta que cadena_2, la variable 'resultado' debe tener el valor 2
    - Si cadena_1 tiene la misma logitud que cadena_2 la variable 'resultado' debe tener el valor 0
"""

cadena_1 = input("Ingrese la primer cadena: ")
cadena_2 = input("Ingrese la segunda cadena: ")

resultado = ''

if len(cadena_1) > len(cadena_2):
    resultado = 1
elif len(cadena_1) < len(cadena_2):
    resultado = 2
else:
    resultado = 0

print("El valor de resultado es:", resultado)
