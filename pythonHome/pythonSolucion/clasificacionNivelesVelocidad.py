"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script clasifica la velocidad de un vehículo en diferentes niveles según su velocidad.
"""

velocidad = float(input("Ingrese la velocidad del vehículo en km/h: "))

if velocidad >0 and velocidad <= 20:
    print("El nivel de velocidad es: Muy lento")
elif velocidad > 20 and velocidad <=60 :
    print('El nivel de velocidad es: Moderado')
elif velocidad > 60 and velocidad <= 120:
    print('El nivel de velocidad es: Rápido')
elif velocidad > 120:
    print('El nivel de velocidad es: Muy rápido')
else:
    print('La velocidad ingresada no es válida. Debe ser un número positivo.')
