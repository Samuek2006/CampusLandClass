"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script es un conversor de unidades de medida.
"""

conversion = input("Ingrese la conversión que desea realizar (pon el numero de la opcion): \n1. Kilometros a millas \n2. Celsius a Fahrenheit \n3. Kilogramos a libras\n   ")
unidad = float(input("Ingrese el valor a convertir: "))

match conversion:
    case "1":
        if unidad < 0:
            print("No se puede convertir una distancia negativa.")
        else:
            resultado = unidad * 0.621371
            print(f"El resultado es: {resultado:.2f} millas")
    case "2":
        resultado = (unidad * 9/5) + 32
        print(f"El resultado es: {resultado:.2f} Fahrenheit")
    case "3":
        if unidad < 0:
            print("No se puede convertir un peso negativo.")
        else:
            resultado = unidad * 2.20462
            print(f"El resultado es: {resultado:.2f} libras")