"""

Voltear cadena y guardarla en un variable llamada 'cadenaVolteada'
Extraer Nombre, Apellido, Nota y Materia y mostrar

"""

# Variables del ejercicio
cadena_corrupta = "airotsiH,6.7,aícraG nómaR"

# Completa el ejercicio
cadena_volteada = cadena_corrupta[::-1]
print(cadena_volteada)

nombre = cadena_volteada[:5]
apellido = cadena_volteada[6:12]
nota = cadena_volteada[13:16]
materia = cadena_volteada[17:]

print("Nombre:", nombre)
print("Apellido:", apellido)
print("Nota:", nota)
print("Materia:", materia)
