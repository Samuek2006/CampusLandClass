"""
Sistema de Gestión de Cuentas Bancarias
1. Crear cuenta
2. Depositar
3. Solicitar Credito
4. Retirar Dinero
5. Pago Cuota Credito
6. Cancelar Cuenta
7. Salir

Portafolio - Banco
- cta Ahorros
- cta Corriente
- CDT
- Credito:
    - Libre Inv.
- Credito:
    - Vivienda
- Credito:
    - Compra Auto
    - Movil

Datos Cliente
- CC
- Nombre
- Email
- Edad
- Contacto:
    - Movil
    - Fijo
- Ubicacion:
    - Pais
    - Departamento
    - Ciudad
    - Direccion

ProductoClient
- CC
- Producto:
    - idProducto
    - fechaInicio
    - Estado(Activo, Inactivo, Cancelado, Pagado)
    - Saldo - pendiente en el producto
    - Historial:
        - id
        - fechaMovimiento
        - Valor
        - Tipo Movimiento
"""
import os

cuentasBancarias = {}

def LimpiarConsola():
    limpiar = os.system("cls" if os.name == "nt" else "clear")
    return limpiar

def addCuenta(numeroCuenta, titular, cc, correo, edad, movil, fijo, pais, dep, ciudad, direccion):
    if numeroCuenta in cuentasBancarias:
        print("La cuenta ya existe.")
    else:
        cuentasBancarias[numeroCuenta] = {
            "CC": cc,
            "titular": titular,
            "Correo": correo,
            "Edad": edad,
            "Contacto": {
                "Movil": movil,
                "Fijo": fijo
            },
            "Ubicacion": {
                "Pais": pais,
                "Departamento": dep,
                "Ciudad": ciudad,
                "Direccion": direccion
            },
            "Productos": {},
            "Historia": {}
        }
    print("Cuenta creada exitosamente.")

def addProducto():
    pass
#Variables
numeroCuenta = 4000

while True:
    try:
        opcion = int(input("Seleccione una opción:\n1. Crear cuenta\n2. Depositar\n3. Solicitar Crédito\n4. Retirar Dinero\n5. Pago Cuota Crédito\n6. Cancelar Cuenta\n0. Salir\n"))
        match opcion:
            case 1:
                print("Crear Cuenta")
                numeroCuenta += 499
                print(f'Número de cuenta: {numeroCuenta}')
                titular = input("Ingrese el nombre del titular: ")
                addCuenta(numeroCuenta, titular)

                print(cuentasBancarias)
                input("Presione Enter para continuar...")

            case 2:
                print("Depositar Dinero")
                numeroCuenta = int(input("Ingrese el número de cuenta: "))
                if numeroCuenta in cuentasBancarias:
                    monto = float(input("Ingrese el monto a depositar: "))
                    cuentasBancarias[numeroCuenta]["saldo"] += monto
                    print("Depósito realizado con éxito.")
                else:
                    print("La cuenta no existe.")

                input("Presione Enter para continuar...")

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass

            case 6:
                pass

            case 0:
                print("Saliendo del sistema...")
                break

    except (ValueError, TypeError) as e:
        print(f"Error: {e}. Por favor, ingrese un valor válido.")
        continue