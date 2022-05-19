"""
1. Añadir al diccionario las claves perro, gato y rana, con sus respectivos valores, dog, cat y frog
2. Modifica las claves caballo y vaca con los valores horse y cow respectivamente
3. Eliminar las claves rana y vaca
"""
animales = {"caballo": "", "vaca": ""}

# completa el ejercicio
animales["perro"] = "dog"
animales["gato"] = "cat"
animales["rana"] = "frog"
animales["caballo"] = "horse"
animales["vaca"] = "cow"
del(animales["rana"])
del(animales["vaca"])

print(animales)
