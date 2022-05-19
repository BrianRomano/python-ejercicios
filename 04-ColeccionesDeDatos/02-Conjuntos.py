"""
Sobre la variable grupo:
    1. Añadir los siguiente usuarios: Ana, Ramon, Marta, Eric y David
    2. Eliminar (*) los usuarios Mario, Miguel y Ramon
"""

grupo = {"Miguel", "Blanca", "Mario", "Andrés"}

# Completa el ejercicio
grupo.add("Ana")
grupo.add("Ramon")
grupo.add("Marta")
grupo.add("Eric")
grupo.add("David")
grupo.remove("Mario")
grupo.remove("Miguel")
grupo.remove("Ramon")

print(grupo)
