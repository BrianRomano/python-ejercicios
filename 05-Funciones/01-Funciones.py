"""
Realizar una funcion llamada par_o_impar(numero) que imprima por pantalla PAR o IMPAR
"""

numero = int(input("Ingrese un numero: "))


def par_o_impar(num):
    if num % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")


par_o_impar(numero)
