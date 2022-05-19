"""
1. Realiza un programa que lea un numero por teclado y lo almacene en una variable
2. Si es numero no es multiple de 5, debe repetirse la lectura
"""

numero = int(input("Ingrese un numero: "))

while numero % 5 != 0:
    numero = int(input("Ingrese un numero: "))

print("El numero:", numero, "es multiplo de 5")
