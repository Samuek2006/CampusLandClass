"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script ejecuta una calculadora de descuentos para productos.
"""

precioProducto = float(input("Ingrese el precio del producto: "))
tipoCliente = input("Ingrese el tipo de cliente (a, b, c): ").upper()

if tipoCliente == "A":
    descuento = 0.3
elif tipoCliente == "B":
    descuento = 0.2
elif tipoCliente == "C":
    descuento = 0.1
else:
    descuento = 0

precioFinal = precioProducto - (precioProducto * descuento)
print(f"El precio final del producto es: {precioFinal}")
