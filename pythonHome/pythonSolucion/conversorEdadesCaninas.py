"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script convierte la edad de un perro a su equivalente en años humanos.
"""

edadCanino = int(input("Ingrese la edad del perro en años: "))

if edadCanino <= 0:
    print("Por favor, ingrese una edad válida mayor a 0.")
elif edadCanino <= 2:
    edadHumana = edadCanino * 10.5
    print(f"La edad equivalente en años humanos es: {edadHumana}")
else:
    edadHumana = 2 * 10.5 + (edadCanino - 2) * 4
    print(f"La edad equivalente en años humanos es: {edadHumana}")