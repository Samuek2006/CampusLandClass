"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script es un simulador de alarma de peligro que se activa cuando cierta cantidad de sensores se activan.
"""

sensoresActivos = int(input("Ingrese la cantidad de sensores activos: "))

if sensoresActivos >= 1 and sensoresActivos <= 2 :
    print("Alarma de peligro: Nivel bajo")
elif sensoresActivos >= 3 and sensoresActivos <= 5 :
    print("Alarma de peligro: Nivel medio")
elif sensoresActivos >= 6 :
    print("Alarma de peligro: Nivel alto")
else:
    print("No hay sensores activos, no se activa la alarma.")