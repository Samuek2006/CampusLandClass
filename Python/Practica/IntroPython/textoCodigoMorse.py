"""
Se requiere un algoritmo que permita traducir texto a codigo morse y viceversa, debe permitir transformar un texto a lenguaje natural, la funcion debe manejar letras, numeros y algunos caracteres especiales basicos, Debe cumplir con los siguientes requerimientos:

    - Tabla de conversion a Morse:
        - Crear una tabla de referencia (diccionario) en el codigo para traducir cada letra y numero al equivlente en codigo morse. Ejemplo basico:
            - A = .-
            - B = -...
            - 1 = .----
            - 2 = ..---
        - La tabla debe incluir letras (A-Z), numeros (0-9) y algunos caracteres especiales basicos (.,.,?,/).
    - Funcion de traduccion de texto a morse:
        - Crear una funcion que reciba una cadena de texto (solo letras, numerios y los caracteres especiales soportados) y devuelva su equivalente en codigo morse.
        - El texto en morse debe separar cada letra con un espacio y cada palabra con una barra inclinada(/) Ejemplo:
            - Entrada: "Hola Mundo"
            - Salida: ".... --- .-.. .- / -- ..--. -.. ---"
    - Funcion de traduccion de morse a texto natural:
        - Crear una funcion que reciba una cadena en codigo morse y devuelva su equivalente en texto.
        - La funcion debe manejar espacion para separar letras y la barra inclinada (/) para separar palabras.
        - Ejemplo:
            - Entrada: ".... --- .-.. .- / -- ..--. -.. ---"
            - Salida: "Hola Mundo"
"""

import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

# Diccionario de traducción de texto a Morse
texto_a_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '/': '-..-.', ' ': '/'
}

# Diccionario inverso para traducir de Morse a texto
morse_a_texto = {morse: letra for letra, morse in texto_a_morse.items()}

# Variables globales para almacenar traducciones
historial_traducciones = []

# Función de limpiar la consola
def LimpiarConsola():
    limpiar = os.system('cls' if os.name == 'nt' else 'clear')
    return limpiar

# Función para traducir texto a código Morse
def traducir_texto_a_morse(texto):
    try:
        texto = texto.upper()
        morse_resultado = []

        for caracter in texto:
            if caracter in texto_a_morse:
                if caracter == ' ':
                    morse_resultado.append('/')
                else:
                    morse_resultado.append(texto_a_morse[caracter])
            else:
                print(Fore.YELLOW + f'Advertencia: El caracter "{caracter}" no está soportado y será ignorado')

        resultado = ' '.join(morse_resultado)
        return resultado

    except Exception as e:
        print(Fore.RED + f'Error al traducir texto a Morse: {e}')
        return None

# Función para traducir código Morse a texto
def traducir_morse_a_texto(morse):
    try:
        # Dividir por espacios para obtener cada código Morse individual
        codigos_morse = morse.split(' ')
        texto_resultado = []

        for codigo in codigos_morse:
            if codigo == '/':
                texto_resultado.append(' ')
            elif codigo in morse_a_texto:
                if morse_a_texto[codigo] != ' ':
                    texto_resultado.append(morse_a_texto[codigo])
            elif codigo == '':
                continue
            else:
                print(Fore.YELLOW + f'Advertencia: El código Morse "{codigo}" no es válido y será ignorado')

        resultado = ''.join(texto_resultado)
        return resultado

    except Exception as e:
        print(Fore.RED + f'Error al traducir Morse a texto: {e}')
        return None

# Función para guardar traducción en el historial
def guardar_en_historial(original, traducido, tipo):
    historial_traducciones.append({
        'original': original,
        'traducido': traducido,
        'tipo': tipo,
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    })
    print(Fore.GREEN + 'Traducción guardada en el historial')

# Función para mostrar el historial
def mostrar_historial():
    if not historial_traducciones:
        print(Fore.YELLOW + 'No hay traducciones en el historial')
        return

    print(Fore.CYAN + 'HISTORIAL DE TRADUCCIONES')
    print('=' * 50)

    for i, traduccion in enumerate(historial_traducciones, 1):
        print(Fore.YELLOW + f'{i}. [{traduccion["timestamp"]}] - {traduccion["tipo"]}')
        print(Fore.WHITE + f'Original: {traduccion["original"]}')
        print(Fore.GREEN + f'Traducido: {traduccion["traducido"]}')
        print('-' * 30)

# Función para mostrar la tabla de códigos Morse
def mostrar_tabla_morse():
    print(Fore.CYAN + 'TABLA DE CÓDIGOS MORSE')
    print('=' * 30)

    # Mostrar letras
    print(Fore.YELLOW + 'LETRAS:')
    letras = {k: v for k, v in texto_a_morse.items() if k.isalpha()}
    for i, (letra, morse) in enumerate(letras.items()):
        if i % 3 == 0 and i != 0:
            print()
        print(f'{letra}: {morse}', end='  ')

    print('\n')

    # Mostrar números
    print(Fore.YELLOW + 'NÚMEROS:')
    numeros = {k: v for k, v in texto_a_morse.items() if k.isdigit()}
    for numero, morse in numeros.items():
        print(f'{numero}: {morse}', end='  ')

    print('\n')

    # Mostrar caracteres especiales
    print(Fore.YELLOW + 'CARACTERES ESPECIALES:')
    especiales = {k: v for k, v in texto_a_morse.items() if not k.isalnum() and k != ' '}
    for char, morse in especiales.items():
        print(f'{char}: {morse}', end='  ')

    print('\n')

# Función para validar entrada de código Morse
def validar_morse(morse_input):
    caracteres_validos = set('.-/ ')
    return all(c in caracteres_validos for c in morse_input)

# Ejecución Principal
while True:
    try:
        LimpiarConsola()
        print(Fore.CYAN + '🔤 TRADUCTOR DE CÓDIGO MORSE 🔤')
        print('=' * 40)

        opcion = int(input(Fore.YELLOW +
            '\n1. Traducir Texto a Código Morse'
            '\n2. Traducir Código Morse a Texto'
            '\n3. Ver Tabla de Códigos Morse'
            '\n4. Ver Historial de Traducciones'
            '\n5. Limpiar Historial'
            '\n0. Salir'
            + Fore.MAGENTA + '\nIngrese una opción: '))

        match opcion:
            case 1:
                LimpiarConsola()
                print(Fore.CYAN + '📝 TRADUCIR TEXTO A CÓDIGO MORSE')
                print('-' * 35)

                texto_input = input(Fore.MAGENTA + 'Ingrese el texto a traducir: ')

                if not texto_input.strip():
                    print(Fore.RED + 'Error: No puede ingresar un texto vacío')
                    input(Fore.MAGENTA + 'Presione Enter para continuar...')
                    continue

                print(Fore.YELLOW + '\nTraduciendo...')
                time.sleep(0.5)

                resultado_morse = traducir_texto_a_morse(texto_input)

                if resultado_morse:
                    print(Fore.GREEN + '\n✅ TRADUCCIÓN COMPLETADA')
                    print(Fore.WHITE + f'Texto original: {texto_input}')
                    print(Fore.CYAN + f'Código Morse: {resultado_morse}')

                    # Preguntar si desea guardar en historial
                    guardar = input(Fore.MAGENTA + '\n¿Desea guardar esta traducción en el historial? (s/n): ')
                    if guardar.lower() == 's':
                        guardar_en_historial(texto_input, resultado_morse, 'Texto → Morse')
                else:
                    print(Fore.RED + 'Error en la traducción')

                input(Fore.MAGENTA + '\nPresione Enter para continuar...')

            case 2:
                LimpiarConsola()
                print(Fore.CYAN + '🔤 TRADUCIR CÓDIGO MORSE A TEXTO')
                print('-' * 35)
                print(Fore.YELLOW + 'Formato: Use espacios entre letras y "/" entre palabras')
                print(Fore.YELLOW + 'Ejemplo: .... --- .-.. .- / -- ..- -. -.. ---')

                morse_input = input(Fore.MAGENTA + '\nIngrese el código Morse: ')

                if not morse_input.strip():
                    print(Fore.RED + 'Error: No puede ingresar un código vacío')
                    input(Fore.MAGENTA + 'Presione Enter para continuar...')
                    continue

                # Validar que solo contenga caracteres válidos de Morse
                if not validar_morse(morse_input):
                    print(Fore.RED + 'Error: El código Morse solo puede contener puntos (.), guiones (-), espacios y barras (/)')
                    input(Fore.MAGENTA + 'Presione Enter para continuar...')
                    continue

                print(Fore.YELLOW + '\nTraduciendo...')
                time.sleep(0.5)

                resultado_texto = traducir_morse_a_texto(morse_input)

                if resultado_texto:
                    print(Fore.GREEN + '\n✅ TRADUCCIÓN COMPLETADA')
                    print(Fore.CYAN + f'Código Morse: {morse_input}')
                    print(Fore.WHITE + f'Texto traducido: {resultado_texto}')

                    # Preguntar si desea guardar en historial
                    guardar = input(Fore.MAGENTA + '\n¿Desea guardar esta traducción en el historial? (s/n): ')
                    if guardar.lower() == 's':
                        guardar_en_historial(morse_input, resultado_texto, 'Morse → Texto')
                else:
                    print(Fore.RED + 'Error en la traducción')

                input(Fore.MAGENTA + '\nPresione Enter para continuar...')

            case 3:
                LimpiarConsola()
                mostrar_tabla_morse()
                input(Fore.MAGENTA + '\nPresione Enter para continuar...')

            case 4:
                LimpiarConsola()
                mostrar_historial()
                input(Fore.MAGENTA + '\nPresione Enter para continuar...')

            case 5:
                LimpiarConsola()
                if historial_traducciones:
                    confirmar = input(Fore.RED + '¿Está seguro de que desea limpiar el historial? (s/n): ')
                    if confirmar.lower() == 's':
                        historial_traducciones.clear()
                        print(Fore.GREEN + 'Historial limpiado correctamente')
                    else:
                        print(Fore.YELLOW + 'Operación cancelada')
                else:
                    print(Fore.YELLOW + 'El historial ya está vacío')

                input(Fore.MAGENTA + 'Presione Enter para continuar...')

            case 0:
                LimpiarConsola()
                print(Fore.RED + '👋 Saliendo del programa...')
                print(Fore.CYAN + '¡Gracias por usar el Traductor de Código Morse!')
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