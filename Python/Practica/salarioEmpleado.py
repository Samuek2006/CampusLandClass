"""
Se necesita realizar un algoritmo que permita calcular el salario a pagar a un empleado, segun la categoria a la que pertenece segun su salario basse, el departamento de nomina realiza el proceso de liquidacion teniendo en cuenta los siguientes parametros:

    - Los Dias trabajados del empleado
    - Las Horas extras trabajadas por el empleado, cada hora extra se paga teniendo en cuenta si es Diurna o Nocturna, la hora Diurna equivale a $10000 la hora nocturna $25000
    - El algoritmo debe mostrar el salario base, el total a pagar por concepto de horas extras y el sueldo total a pagar.

"""

import os, time
from colorama import Fore, Style, init
init(autoreset=True)

#Datos del empleado
empleado = []
rtas = ['S', 's']

#Variables
valorHoraDiurna = 10000
valorHoraNocturna = 25000

#Funcion Limpiar Consola
def LimpiarConsola():
    limpiar = os.system('cls' if os.name == 'nt' else 'clear')
    return limpiar

#Funcion agregar empleado
def AddEmpleado(name):
    empleado.append([name, []])
    print(Fore.BLUE + f'Empleado {name} agregado exitosamente')
    input(Fore.MAGENTA + 'Enter para continuar')

#Funcion Dias Trabajados
def DiasTrabajados(dayWorked, pay):
    if dayWorked <= 30:
        if dayWorked == 30:
            sueldoBase = pay
        else:
            valorDia = pay / 30
            sueldoBase = valorDia * dayWorked
            print(Fore.BLUE + f'El empleado solo trabajo {dayWorked} dias, el valor del sueldo base por los dias trabajados: ${sueldoBase:.2f}')
            input(Fore.MAGENTA + 'Enter para continuar')
    else:
        print(Fore.RED + 'El empleado no puede trabajar mas de 30 dias')
        time.sleep(1)

    return sueldoBase

#Funcion Horas Extras
def HorasExtras(diurna : int , nocturna : int):
    diurna *= valorHoraDiurna
    nocturna *= valorHoraNocturna
    return diurna + nocturna

#Funcion para la carga dinamica
def Cargando():
    progreso = 10
    LimpiarConsola()
    for i in range(progreso + 1):
        barra = '- ' * i
        porcentaje = (i * 10)
        texto = f'{Fore.RED}({barra:<20}) {porcentaje} / 100'
        print(texto.ljust(40), end='\r')  # .ljust rellena con espacios
        time.sleep(0.1)
    print()  # Salto de línea final
    time.sleep(0.5)
    LimpiarConsola()

while True:
    try:
        Cargando()
        LimpiarConsola()
        print(Fore.RED + 'Bienvenido al sistema de liquidación de salarios')
        print()
        opcion = int(input(Fore.CYAN + 'Que hay para hacer hoy:' + Fore.YELLOW + '\n1. Agregar empleado \n2. Liquidar salario \n0. Salir' + Fore.MAGENTA + '\n \nIngresa una opcion: '))
        match opcion:

            case 1:
                LimpiarConsola()
                print(Fore.CYAN + 'Registro de Trabajador')
                trabajador = input(Fore.MAGENTA + 'Ingresa el nombre del trabajador a registrar: ')
                AddEmpleado(trabajador)
                time.sleep(1)
                LimpiarConsola()

            case 2:
                LimpiarConsola()
                while True:
                    print(Fore.CYAN + 'Liquidación de Salario')
                    trabajador = input(Fore.MAGENTA + 'Ingresa el nombre del trabajador a liquidar: ')
                    LimpiarConsola()
                    print(Fore.RED + 'Buscando Empleado...')
                    time.sleep(0.5)
                    LimpiarConsola()
                    for empleado in empleado:

                        if empleado[0] == trabajador:
                            print(Fore.RED + 'Empleado encontrado ...')
                            time.sleep(0.5)
                            LimpiarConsola()
                            categoria = input(Fore.MAGENTA + 'Ingresa la categoria del trabajador (A, B, C) salir(0): ').upper()

                            if categoria == 'A':
                                sueldoBase = 2000000
                                dayWorked = int(input(Fore.MAGENTA + 'Ingresa los dias trabajados : '))
                                salarioBase = DiasTrabajados(dayWorked, sueldoBase)
                                LimpiarConsola()

                                horasExtraDiurnas = int(input(Fore.MAGENTA + 'ingresa las horas extras diurnas: '))
                                horasExtraNocturnas = int(input(Fore.MAGENTA + 'ingresa las horas extras nocturnas: '))
                                salarioHorasExtra = HorasExtras(horasExtraDiurnas, horasExtraNocturnas)
                                LimpiarConsola()

                                print(Fore.CYAN + f'El sueldo base del empleado {trabajador} es: ${salarioBase:.2f} \nEl total a pagar por concepto de horas extra es: ${salarioHorasExtra} \nEl sueldo total a pagar al empleado {trabajador} es de: ${(salarioBase + salarioHorasExtra):.2f}')
                                input(Fore.MAGENTA + 'Enter para continuar...')
                                LimpiarConsola()

                            elif categoria == 'B':
                                sueldoBase = 2500000
                                dayWorked = int(input(Fore.MAGENTA + 'Ingresa los dias trabajados : '))
                                DiasTrabajados(dayWorked, sueldoBase)
                                salarioBase = DiasTrabajados(dayWorked, sueldoBase)
                                LimpiarConsola()

                                horasExtraDiurnas = int(input(Fore.MAGENTA + 'ingresa las horas extras diurnas: '))
                                horasExtraNocturnas = int(input(Fore.MAGENTA + 'ingresa las horas extras nocturnas: '))
                                salarioHorasExtra = HorasExtras(horasExtraDiurnas, horasExtraNocturnas)
                                LimpiarConsola()

                                print(Fore.CYAN + f'El sueldo base del empleado {trabajador} es: ${salarioBase:.2f} \nEl total a pagar por concepto de horas extra es: ${salarioHorasExtra} \nEl sueldo total a pagar al empleado {trabajador} es de: ${(salarioBase + salarioHorasExtra):.2f}')
                                input(Fore.MAGENTA + 'Enter para continuar...')
                                LimpiarConsola()

                            elif categoria == 'C':
                                sueldoBase = 3000000
                                dayWorked = int(input(Fore.MAGENTA + 'Ingresa los dias trabajados : '))
                                DiasTrabajados(dayWorked, sueldoBase)
                                salarioBase = DiasTrabajados(dayWorked, sueldoBase)
                                LimpiarConsola()

                                horasExtraDiurnas = int(input(Fore.MAGENTA + 'ingresa las horas extras diurnas: '))
                                horasExtraNocturnas = int(input(Fore.MAGENTA + 'ingresa las horas extras nocturnas: '))
                                salarioHorasExtra = HorasExtras(horasExtraDiurnas, horasExtraNocturnas)
                                LimpiarConsola()

                                print(Fore.CYAN + f'El sueldo base del empleado {trabajador} es: ${salarioBase:.2f} \nEl total a pagar por concepto de horas extra es: ${salarioHorasExtra} \nEl sueldo total a pagar al empleado {trabajador} es de: ${(salarioBase + salarioHorasExtra):.2f}')
                                input(Fore.MAGENTA + 'Enter para continuar...')
                                LimpiarConsola()

                            elif categoria == '0':
                                break

                            else:
                                print(Fore.RED + 'Categoria no valida')
                        else:
                            print(Fore.RED + 'Empleado no Esta Registrado ...')
                            time.sleep(0.5)
                            LimpiarConsola()

            case 0:
                Cargando()
                LimpiarConsola()
                print(Fore.RED + 'Hasta luego vuelva pronto')
                time.sleep(1)
                LimpiarConsola()
                break

    except (ValueError, KeyboardInterrupt, TypeError, IndexError, UnboundLocalError) as e:
        print(f'Error: {e}')