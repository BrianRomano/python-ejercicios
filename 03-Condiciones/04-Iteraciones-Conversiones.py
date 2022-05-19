"""
1. Pedir al usuario que introduzca un numero entero por teclado entre 0 y 9 (ambos incluidos) y guardarlo en la variable
'numero'. Debes asegurarte de que la variable 'numero' contiene un numero entero del 0 al 9, utiliza un bucle para
repetir la lectura hasta que se cumpla esa condicion
2. Generar una lista llamada multiplos que contenga los multiplos de 'numero' entre 0 y 100 (ambos incluidos)
Nota:
    - La funcion range() permite especificar un salto en un tercer argumento, pero tener presente que ese tercer
    argumento sea 0, deberas manejar el caso en que el numero sea cero manualmente.
        Probar este ejemplo: list(range(0, 30, 5)) -> RANGO CON SALTO DE 5
"""

multiplos = []

numero = int(input("Ingrese un numero entero entre 0 y 9: "))

while numero < 0 or numero > 9:
    numero = int(input("Ingrese un numero entero entre 0 y 9: "))

if numero == 0:
    multiplos = [0]
else:
    multiplos = list(range(0, 101, numero))

print(multiplos)
