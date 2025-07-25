"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script implementa tarifas de estacionamiento por hora.
"""

horaEstacionamiento = int(input("Ingrese la cantidad de horas de estacionamiento: "))
if (horaEstacionamiento <= 1):
    tarifa = 5
elif (horaEstacionamiento >= 2) and (horaEstacionamiento <= 3):
    tarifa = 10
else:
    tarifa = 15

print(f"La tarifa por {horaEstacionamiento} horas de estacionamiento es: ${tarifa}")