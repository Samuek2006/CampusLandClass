"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script realiza la simulación de un sistema de calificaciones para estudiantes.
"""

calificacion = float(input("Ingrese la calificación del estudiante: (0-100): "))

if (calificacion >= 90) and (calificacion <=100):
    print('El estudiante ha obtenido una calificación A')
elif (calificacion >= 80) and (calificacion < 90):
    print('El estudiante ha obtenido una calificación B')
elif (calificacion >= 70) and (calificacion < 80):
    print('El estudiante ha obtenido una calificación C')
elif (calificacion >= 60) and (calificacion < 70):
    print('El estudiante ha obtenido una calificación D')
elif (calificacion >= 0) and (calificacion < 60):
    print('El estudiante ha obtenido una calificación F')
else:
    print('La calificación ingresada no es válida. Debe estar entre 0 y 100.')
