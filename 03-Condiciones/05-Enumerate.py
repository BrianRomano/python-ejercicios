"""
Dada una lista con un numero de strings, modificar los strings de la lista por la letra inicial utilizando enumerate
"""
iniciales = ["Hola", "Mundo"]

for i, cadena in enumerate(iniciales):
    iniciales[i] = iniciales[i][0]

print(iniciales)
