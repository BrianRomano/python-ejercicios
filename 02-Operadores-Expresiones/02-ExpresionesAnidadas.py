"""
A partir de dos variables 'nombre' y 'edad' crea una variable 'expresion' que almacene si se cumplen TODAS las siguiente
condiciones encandenando operadores logicos en una sola linea:
    1. Que 'nombre' sea diferente de cuatro asteriscos
    2. Que 'edad' sea mayor que 10 y a su vez menor que 18
    3. Que la longitud del 'nombre' sea mayor o igual que 3 pero a la vez menor que 10
"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

expresion = (nombre != "****") and (10 < edad < 18) and (3 <= len(nombre) < 10)

print(expresion)