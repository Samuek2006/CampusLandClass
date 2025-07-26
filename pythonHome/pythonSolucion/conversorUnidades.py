"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script es un conversor de unidades de medida.
"""

conversion = input("Ingrese la conversión que desea realizar (pon el numero de la opcion): \n1. Kilometros a millas \n2. Celsius a Fahrenheit \n3. Kilogramos a libras\n   ")

match conversion:
    case "1":
        resultado = conversion * 0.621371
        print(f"El resultado es: {resultado} millas")
    case "2":
        resultado = (conversion * 9/5) + 32
        print(f"El resultado es: {resultado} Fahrenheit")
    case "3":
        resultado = conversion * 2.20462
        print(f"El resultado es: {resultado} libras")