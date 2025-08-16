import modules.utilidades as utilidades
import modules.operaciones as operaciones

time = utilidades.Stop()
consola = utilidades.Limpiar_consola()

#Funcion Menu Principal
def menuPrincipal():
    while True:
        print('''
    Seleccione una opción:
    1. Crear cuenta
    2. Depositar
    3. Solicitar Crédito
    4. Retirar Dinero
    5. Pago Cuota Crédito
    6. Cancelar Cuenta
    7. Estadisticas
    0. Salir
            ''')

        opcion = int(input('Ingresa una Opcion: '))

        match opcion:
            case 1:
                operaciones.crear_cuenta()

            case 2:
                operaciones.depositar()

            case 3:
                operaciones.solicitarCredito()

            case 4:
                operaciones.retirar()

            case 5:
                operaciones.pagoCuota()

            case 6:
                operaciones.cancelarCuenta()

            case 7:
                menuClientes()

            case 0:
                print('Saliendo del sistema')
                time
                break

            case _:
                print('Elija una opcion valida')
                time

#Funcion Menu Clientes
def menuClientes():
    while True:
        print('''
    Seleccione una opción:
    1. Datos Cliente
    2. Saldos
    3. Creditos
    4. Inversiones
    0.Salir
            ''')

        opcion = int(input('Ingresa una opcion: '))

        match opcion:
            case 1:
                pass

            case 2:
                menuSaldos()

            case 3:
                menuCreditos()

            case 4:
                pass

            case 0:
                print('Saliendo del sistema')
                time
                break

            case _:
                print('Elija una opcion valida')
                time

#Funcion Menu Saldos
def menuSaldos():
    while True:
        print('''
    Seleccione una opción:
    1. Cta Ahorros
    2. Cta Corriente
    0. Salir
            ''')

        opcion = int(input('Ingresa una opcion: '))

        match opcion:
            case 1:
                producto = 'Cuenta de Ahorros'

            case 2:
                producto = 'Cuenta Corriente'

            case 0:
                print('Saliendo del sistema')
                time
                break

            case _:
                print('Elija una opcion correcta')
                time

#Funcion Menu Creditos
def menuCreditos():
    while True:
        print('''
    Seleccione una opción:
    1. Credito Libre Inversion
    2. Credito Vivienda
    3. Credito Compra AutoMovil
    0. Salir
            ''')

        opcion = int(input('Ingresa una opcion: '))

        match opcion:
            case 1:
                producto = 'Credito'
                break

            case 2:
                producto = 'Credito'
                break

            case 3:
                producto = 'Credito'
                break

            case 0:
                print('Saliendo del sistema')
                time
                break

            case _:
                print('Elija una opcion correcta')
                time

    return producto

#Funcion Menu Portafolio
def menuPortafolio():
    while True:
        print('''
    Seleccione una opción:
    1. Cta Ahorros
    2. Cta Corriente
    3. CDT
    0. Salir
            ''')

        opcion = int(input('Ingresa una opcion: '))

        match opcion:
            case 1:
                producto = 'Cuenta Ahorros'
                break

            case 2:
                producto = 'Cuenta Corriente'
                break

            case 3:
                producto = 'CDT'
                break

            case 0:
                print('Saliendo del sistema')
                time
                break

            case _:
                print('Elija una opcion correcta')
                time

    return producto

def leer_opcion():
    try:
        return int(input("Seleccione una opción: "))
    except ValueError:
        print("⚠ Ingrese un número válido.")
        return -1