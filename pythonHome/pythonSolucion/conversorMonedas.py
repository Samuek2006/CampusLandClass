"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script es un conversor de unidades de medida.
"""

monto = float(input('Ingresa el monto a realizar el cambio '))
cambio = input('Ingresa a que moneda deseas realizar el cambio (Euro (EUR), Pesos Colombianos (COP), Yenes Japoneses (JPY)) ').upper()

if monto > 0:
    match cambio:
        case 'EUR':
            monto = monto * 0.85
        case 'COP':
            monto = monto * 4100
        case 'JPY':
            monto = monto * 110
        case _:
            print('Moneda no reconocida')
    print(f'El monto convertido es: {monto:.2f} {cambio}')
else:
    print('El monto debe ser mayor a 0')