"""
Se necesita realizar un algoritmo para un conjunto residencial que permita conocer el total recaudado por concepto del pago de la administracion de los residentes, El valor fijado por la administracion es de $200000. El algoritmo debe permitir mostrar la siguiente informacion:

    - Total de dinero recaudado
    - Total de dinero pendiente por pago
    - Total de residentes que pagaron el total de la administracion
    - Total de residentes que no pagaron la administracion
    - Total de residentes que abonaron a la Administracion

"""
import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

# Constantes del sistema
VALOR_ADMINISTRACION = 200000
TOTAL_RESIDENTES = 20

# Variables globales
residentes = []

# Función de limpiar la consola
def LimpiarConsola():
    limpiar = os.system('cls' if os.name == 'nt' else 'clear')
    return limpiar

# Función para formatear números como moneda
def formatear_dinero(valor):
    return f"${valor:,.0f}".replace(",", ".")

# Función para agregar un residente
def agregar_residente(nombre):
    try:
        if len(residentes) >= TOTAL_RESIDENTES:
            print(Fore.RED + f'Error: No se pueden agregar más de {TOTAL_RESIDENTES} residentes')
            return False

        # Verificar si el residente ya existe
        for residente in residentes:
            if residente['nombre'].lower() == nombre.lower():
                print(Fore.RED + f'Error: El residente {nombre} ya está registrado')
                return False

        residente = {
            'nombre': nombre,
            'pagos': [],
            'total_pagado': 0,
            'estado': 'NO PAGADO'  # NO PAGADO, ABONO, PAGADO
        }

        residentes.append(residente)
        print(Fore.GREEN + f'✅ Residente {nombre} agregado exitosamente')
        return True

    except Exception as e:
        print(Fore.RED + f'Error al agregar residente: {e}')
        return False

# Función para buscar un residente
def buscar_residente(nombre):
    for residente in residentes:
        if residente['nombre'].lower() == nombre.lower():
            return residente
    return None

# Función para registrar pago
def registrar_pago(nombre, valor_pago):
    try:
        residente = buscar_residente(nombre)
        if not residente:
            print(Fore.RED + f'Error: Residente {nombre} no encontrado')
            return False

        if valor_pago <= 0:
            print(Fore.RED + 'Error: El valor del pago debe ser mayor a 0')
            return False

        # Verificar que no pague más de lo debido
        deuda_pendiente = VALOR_ADMINISTRACION - residente['total_pagado']
        if valor_pago > deuda_pendiente:
            print(Fore.RED + f'Error: El pago ({formatear_dinero(valor_pago)}) excede la deuda pendiente ({formatear_dinero(deuda_pendiente)})')
            return False

        # Registrar el pago
        residente['pagos'].append({
            'valor': valor_pago,
            'fecha': time.strftime('%Y-%m-%d %H:%M:%S')
        })

        residente['total_pagado'] += valor_pago

        # Actualizar estado del residente
        if residente['total_pagado'] >= VALOR_ADMINISTRACION:
            residente['estado'] = 'PAGADO'
        elif residente['total_pagado'] > 0:
            residente['estado'] = 'ABONO'
        else:
            residente['estado'] = 'NO PAGADO'

        print(Fore.GREEN + f'✅ Pago de {formatear_dinero(valor_pago)} registrado para {nombre}')
        print(Fore.CYAN + f'Total pagado: {formatear_dinero(residente["total_pagado"])}')
        print(Fore.YELLOW + f'Deuda pendiente: {formatear_dinero(VALOR_ADMINISTRACION - residente["total_pagado"])}')

        return True

    except Exception as e:
        print(Fore.RED + f'Error al registrar pago: {e}')
        return False

# Función para calcular estadísticas
def calcular_estadisticas():
    total_recaudado = 0
    residentes_pagados = 0
    residentes_no_pagados = 0
    residentes_abono = 0

    for residente in residentes:
        total_recaudado += residente['total_pagado']

        if residente['estado'] == 'PAGADO':
            residentes_pagados += 1
        elif residente['estado'] == 'NO PAGADO':
            residentes_no_pagados += 1
        elif residente['estado'] == 'ABONO':
            residentes_abono += 1

    total_esperado = VALOR_ADMINISTRACION * len(residentes)
    total_pendiente = total_esperado - total_recaudado

    return {
        'total_recaudado': total_recaudado,
        'total_pendiente': total_pendiente,
        'total_esperado': total_esperado,
        'residentes_pagados': residentes_pagados,
        'residentes_no_pagados': residentes_no_pagados,
        'residentes_abono': residentes_abono,
        'residentes_registrados': len(residentes)
    }

# Función para mostrar resumen de un residente
def mostrar_resumen_residente(nombre):
    residente = buscar_residente(nombre)
    if not residente:
        print(Fore.RED + f'Residente {nombre} no encontrado')
        return

    print(Fore.CYAN + f'📋 RESUMEN DE PAGOS - {residente["nombre"].upper()}')
    print('=' * 50)
    print(Fore.YELLOW + f'Estado: {residente["estado"]}')
    print(Fore.WHITE + f'Total pagado: {formatear_dinero(residente["total_pagado"])}')
    print(Fore.MAGENTA + f'Deuda pendiente: {formatear_dinero(VALOR_ADMINISTRACION - residente["total_pagado"])}')

    if residente['pagos']:
        print(Fore.CYAN + '\nHistorial de pagos:')
        for i, pago in enumerate(residente['pagos'], 1):
            print(Fore.WHITE + f'{i}. {formatear_dinero(pago["valor"])} - {pago["fecha"]}')
    else:
        print(Fore.RED + '\nNo hay pagos registrados')

# Función para listar todos los residentes
def listar_residentes():
    if not residentes:
        print(Fore.YELLOW + 'No hay residentes registrados')
        return

    print(Fore.CYAN + '👥 LISTA DE RESIDENTES')
    print('=' * 60)
    print(f'{"#":<3} {"NOMBRE":<20} {"ESTADO":<12} {"PAGADO":<15} {"PENDIENTE":<15}')
    print('-' * 60)

    for i, residente in enumerate(residentes, 1):
        pendiente = VALOR_ADMINISTRACION - residente['total_pagado']

        # Colores según el estado
        if residente['estado'] == 'PAGADO':
            color = Fore.GREEN
        elif residente['estado'] == 'ABONO':
            color = Fore.YELLOW
        else:
            color = Fore.RED

        print(color + f'{i:<3} {residente["nombre"]:<20} {residente["estado"]:<12} {formatear_dinero(residente["total_pagado"]):<15} {formatear_dinero(pendiente):<15}')

# Ejecución Principal
while True:
    try:
        LimpiarConsola()
        print(Fore.CYAN + '🏢 CONJUNTO RESIDENCIAL CONUCOS 🏢')
        print(Fore.CYAN + '     SISTEMA DE ADMINISTRACIÓN')
        print('=' * 45)
        print(Fore.WHITE + f'Valor Administración: {formatear_dinero(VALOR_ADMINISTRACION)}')
        print(Fore.WHITE + f'Total Residentes Permitidos: {TOTAL_RESIDENTES}')
        print('=' * 45)

        opcion = int(input(Fore.YELLOW +
            '\n1. Registrar Residente'
            '\n2. Registrar Pago'
            '\n3. Ver Resumen de Residente'
            '\n4. Listar Todos los Residentes'
            '\n5. Estadísticas Generales'
            '\n6. Reporte Detallado'
            '\n0. Salir'
            + Fore.MAGENTA + '\nIngrese una opción: '))

        match opcion:
            case 1:
                LimpiarConsola()
                print(Fore.CYAN + '👤 REGISTRAR NUEVO RESIDENTE')
                print('-' * 30)
                print(Fore.WHITE + f'Residentes registrados: {len(residentes)}/{TOTAL_RESIDENTES}')

                if len(residentes) >= TOTAL_RESIDENTES:
                    print(Fore.RED + f'⚠️  Ya se han registrado los {TOTAL_RESIDENTES} residentes permitidos')
                    input(Fore.MAGENTA + 'Presione Enter para continuar...')
                    continue

                nombre = input(Fore.MAGENTA + '\nIngrese el nombre del residente: ').strip()

                if not nombre:
                    print(Fore.RED + 'Error: El nombre no puede estar vacío')
                    input(Fore.MAGENTA + 'Presione Enter para continuar...')
                    continue

                print(Fore.YELLOW + 'Registrando residente...')
                time.sleep(0.5)

                if agregar_residente(nombre):
                    time.sleep(1)

                input(Fore.MAGENTA + 'Presione Enter para continuar...')

            case 2:
                LimpiarConsola()
                print(Fore.CYAN + '💰 REGISTRAR PAGO DE ADMINISTRACIÓN')
                print('-' * 40)

                if not residentes:
                    print(Fore.RED + 'No hay residentes registrados')
                    input(Fore.MAGENTA + 'Presione Enter para continuar...')
                    continue

                nombre = input(Fore.MAGENTA + 'Ingrese el nombre del residente: ').strip()

                if not nombre:
                    print(Fore.RED + 'Error: El nombre no puede estar vacío')
                    input(Fore.MAGENTA + 'Presione Enter para continuar...')
                    continue

                # Verificar si el residente existe y mostrar su estado
                residente = buscar_residente(nombre)
                if residente:
                    print(Fore.GREEN + f'✅ Residente encontrado: {residente["nombre"]}')
                    print(Fore.CYAN + f'Estado actual: {residente["estado"]}')
                    print(Fore.WHITE + f'Total pagado: {formatear_dinero(residente["total_pagado"])}')
                    deuda = VALOR_ADMINISTRACION - residente["total_pagado"]
                    print(Fore.YELLOW + f'Deuda pendiente: {formatear_dinero(deuda)}')

                    if deuda <= 0:
                        print(Fore.GREEN + '✅ Este residente ya ha pagado completamente')
                        input(Fore.MAGENTA + 'Presione Enter para continuar...')
                        continue
                else:
                    print(Fore.RED + f'❌ Residente {nombre} no encontrado')
                    input(Fore.MAGENTA + 'Presione Enter para continuar...')
                    continue

                try:
                    valor_pago = int(input(Fore.MAGENTA + f'\nIngrese el valor del pago (máximo {formatear_dinero(deuda)}): '))

                    print(Fore.YELLOW + 'Procesando pago...')
                    time.sleep(0.5)

                    if registrar_pago(nombre, valor_pago):
                        time.sleep(1)

                except ValueError:
                    print(Fore.RED + 'Error: Ingrese un valor numérico válido')

                input(Fore.MAGENTA + 'Presione Enter para continuar...')

            case 3:
                LimpiarConsola()
                print(Fore.CYAN + '📋 RESUMEN DE RESIDENTE')
                print('-' * 25)

                if not residentes:
                    print(Fore.RED + 'No hay residentes registrados')
                    input(Fore.MAGENTA + 'Presione Enter para continuar...')
                    continue

                nombre = input(Fore.MAGENTA + 'Ingrese el nombre del residente: ').strip()

                if nombre:
                    mostrar_resumen_residente(nombre)
                else:
                    print(Fore.RED + 'Error: El nombre no puede estar vacío')

                input(Fore.MAGENTA + '\nPresione Enter para continuar...')

            case 4:
                LimpiarConsola()
                listar_residentes()
                input(Fore.MAGENTA + '\nPresione Enter para continuar...')

            case 5:
                LimpiarConsola()
                print(Fore.CYAN + '📊 ESTADÍSTICAS GENERALES')
                print('=' * 35)

                stats = calcular_estadisticas()

                print(Fore.YELLOW + '💰 INFORMACIÓN FINANCIERA:')
                print(Fore.GREEN + f'  • Total recaudado: {formatear_dinero(stats["total_recaudado"])}')
                print(Fore.RED + f'  • Total pendiente: {formatear_dinero(stats["total_pendiente"])}')
                print(Fore.CYAN + f'  • Total esperado: {formatear_dinero(stats["total_esperado"])}')

                if stats['total_esperado'] > 0:
                    porcentaje_recaudado = (stats['total_recaudado'] / stats['total_esperado']) * 100
                    print(Fore.MAGENTA + f'  • Porcentaje recaudado: {porcentaje_recaudado:.1f}%')

                print(Fore.YELLOW + '\n👥 INFORMACIÓN DE RESIDENTES:')
                print(Fore.WHITE + f'  • Residentes registrados: {stats["residentes_registrados"]}/{TOTAL_RESIDENTES}')
                print(Fore.GREEN + f'  • Residentes que pagaron completo: {stats["residentes_pagados"]}')
                print(Fore.YELLOW + f'  • Residentes con abono: {stats["residentes_abono"]}')
                print(Fore.RED + f'  • Residentes sin pagar: {stats["residentes_no_pagados"]}')

                input(Fore.MAGENTA + '\nPresione Enter para continuar...')

            case 6:
                LimpiarConsola()
                print(Fore.CYAN + '📈 REPORTE DETALLADO')
                print('=' * 30)

                stats = calcular_estadisticas()

                print(Fore.CYAN + f'CONJUNTO RESIDENCIAL CONUCOS')
                print(Fore.CYAN + f'Reporte generado: {time.strftime("%Y-%m-%d %H:%M:%S")}')
                print('=' * 50)

                # Resumen financiero
                print(Fore.YELLOW + '\n💰 RESUMEN FINANCIERO:')
                print(f'Valor administración por residente: {formatear_dinero(VALOR_ADMINISTRACION)}')
                print(f'Total esperado ({stats["residentes_registrados"]} residentes): {formatear_dinero(stats["total_esperado"])}')
                print(Fore.GREEN + f'Total recaudado: {formatear_dinero(stats["total_recaudado"])}')
                print(Fore.RED + f'Total pendiente: {formatear_dinero(stats["total_pendiente"])}')

                # Desglose por estado
                print(Fore.YELLOW + '\n👥 DESGLOSE POR ESTADO:')
                print(Fore.GREEN + f'✅ Pagado completo: {stats["residentes_pagados"]} residentes')
                print(Fore.YELLOW + f'🔶 Con abono: {stats["residentes_abono"]} residentes')
                print(Fore.RED + f'❌ Sin pagar: {stats["residentes_no_pagados"]} residentes')

                # Lista detallada
                print(Fore.YELLOW + '\n📋 DETALLE POR RESIDENTE:')
                if residentes:
                    for residente in residentes:
                        pendiente = VALOR_ADMINISTRACION - residente['total_pagado']
                        if residente['estado'] == 'PAGADO':
                            color = Fore.GREEN + '✅'
                        elif residente['estado'] == 'ABONO':
                            color = Fore.YELLOW + '🔶'
                        else:
                            color = Fore.RED + '❌'

                        print(f'{color} {residente["nombre"]} - Pagado: {formatear_dinero(residente["total_pagado"])} - Pendiente: {formatear_dinero(pendiente)}')
                else:
                    print(Fore.RED + 'No hay residentes registrados')

                input(Fore.MAGENTA + '\nPresione Enter para continuar...')

            case 0:
                LimpiarConsola()
                print(Fore.RED + '👋 Saliendo del sistema...')
                print(Fore.CYAN + '¡Gracias por usar el Sistema de Administración!')
                time.sleep(1)
                break

            case _:
                print(Fore.RED + '❌ Opción inválida. Intente nuevamente...')
                time.sleep(1)

    except (ValueError, KeyboardInterrupt) as e:
        if isinstance(e, KeyboardInterrupt):
            print(Fore.RED + '\n\nPrograma interrumpido por el usuario')
            break
        else:
            print(Fore.RED + f'❌ Error: Ingrese un número válido')
            time.sleep(1)
    except Exception as e:
        print(Fore.RED + f'❌ Error inesperado: {e}')
        time.sleep(1)