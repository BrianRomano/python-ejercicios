"""
Realizar un sumatorio de todos los numeros desde 0 hasta 'numero' incluido, exceptuando los multiplos de 5 y 7, y
almacenarlo en la variable 'suma'
"""

numero = int(input("Ingrese un numero: "))

suma = 0

for num in range(numero + 1):
    if num % 5 != 0 and num % 7 != 0:
        suma += num

print(suma)
