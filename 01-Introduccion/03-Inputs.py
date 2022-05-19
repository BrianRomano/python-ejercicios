"""
Debe leer por teclado dos cadenas de caracteres, una llamada nombre y otra apellido
Debe leer por teclado un numero entero llamado edad
Debe leer por teclado un numero flotante llamado numero_magico
Crear una variable llamada cadena_final con el siguiente formato:
    NOMBRE APELLIDO: 'numeroDelaSuerte = edad*numero_magico
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
numero_magico = float(input("Ingrese un numero flotante: "))

cadena_final = nombre + " " + apellido + ": Tu numero de la suerte es el " + str(edad * numero_magico)
print(cadena_final)
