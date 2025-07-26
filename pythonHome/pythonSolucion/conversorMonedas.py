"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script es un conversor de unidades de medida.
"""

monto = float(input('Ingresa el monto a realizar el cambio'))
cambio = input('Ingresa a que moneda deseas realizar el cambio (Euro (EUR), Pesos Colombianos (COP), Yenes Japoneses (JPY))')

if cambio == 'Euro':
    monto = monto * 0.85
elif cambio == 'Pesos Colombianos':
    monto = monto * 4100
elif cambio == 'Yenes Japoneses':
    monto = monto * 110
else:
    print('Moneda no reconocida')
print(f'El monto convertido es: {monto:.2f} {cambio}')