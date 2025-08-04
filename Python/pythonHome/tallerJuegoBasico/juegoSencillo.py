"""
Autor: Samuel Felipe Calderón Soto
Fecha: 29/07/2025
Descripcion: Este Script es de Un juego basico alucivo al clasico juego del ahorcado
"""

import random, os, time, colorama
#Juego del Ahorcado
"""
Juego del Ahorcado
    debe imprimir las lineas que corresponda a la longitud de la palabra que se seleccione aleatoriamente, debe tener contador de intentos, mostras las letras que ya han sido utilizadas, en la linea de la palabra si el jugador pone una letra que corresponda con dicha palabra debe mostrarla en la posicion correspondiente, si el jugador no acierta debe restar un intento, y si adivina una de las letras que corresponda a la palabra no debe descontar intentos de adivinanza.
"""

#Inicializacion de la libreria Colorama, con sus archivos necesarios
from colorama import Fore, Style, init
init(autoreset=True)

#Palabras con pistas
palabras_con_pistas = {
    "computadora": "Dispositivo electrónico con teclado y pantalla.",
    "python": "Lenguaje de programación popular y fácil de leer.",
    "ahorcado": "Juego clásico de adivinar palabras con dibujos.",
    "programa": "Conjunto de instrucciones que ejecuta una computadora.",
    "teclado": "Lo usas para escribir en la computadora.",
    "pantalla": "Parte de la computadora donde ves la información.",
    "internet": "Red global para compartir información.",
    "juego": "Actividad divertida, a veces competitiva.",
    "clase": "Lugar o momento donde aprendes algo.",
    "codigo": "Instrucciones que entiende una computadora."
}


#Dibujo Errores en cada Oportunidad
ahorcadoFacil = [
    """
        +---+
        |   |
            |
            |
            |
            |
    =============
    """,
    """
        +---+
        |   |
        O   |
            |
            |
            |
    =============
    """,
    """
        +---+
        |   |
        O   |
        |   |
            |
            |
    =============
    """,
    """
        +---+
        |   |
        O   |
       /|   |
            |
            |
    =============
    """,
    """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
    =============
    """,
    """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
    =============
    """,
    """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
    =============
    """
]

ahorcadoMedio = [
    """
        +---+
        |   |
            |
            |
            |
            |
    =============
    """,
    """
        +---+
        |   |
        O   |
            |
            |
            |
    =============
    """,
    """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
    =============
    """,
    """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
    =============
    """,
    """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
    =============
    """
]

ahorcadoDificil = [
    """
        +---+
        |   |
            |
            |
            |
            |
    =============
    """,
    """
        +---+
        |   |
        O   |
       /|   |
            |
            |
    =============
    """,
    """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
    =============
    """,
    """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
    =============
    """
]

partidasGanadas = 0
partidasPerdidas = 0
# Menu de Inicio
while True:
    try:
        os.system('cls')

        #contador de intentos
        intentos = 4
        letrasUsadas = []

        palabraElegida = random.choice(list(palabras_con_pistas.keys()))

        opcion = int(input('Bienvenido al Juego del Ahorcado \n1. Modo de juego \n2. Estadisticas \n0. Salir del Juego \nIngresa una Opcion: '))

        match opcion:
            case 1:
                os.system('cls')
                print("Iniciando el Juego...")
                time.sleep(0.5)

                modoJuego = int(input('1. Solitario \n2. Multijugador Local \3Regresar \nIngresa una Opcion: '))
                match modoJuego:
                    case 1:
                        os.system('cls')
                        #Elegir Dificultad
                        dificultad = int(input('1. Fácil (6 intentos) \n2. Media (4 intentos) \n3. Difícil (3 intentos) \nIngresa una Opcion: '))

                        os.system('cls')
                        print("Preparando Palabra...")
                        time.sleep(0.5)
                        os.system('cls')

                        match dificultad:
                            case 1:
                                intentos = 6
                                ahorcado_dibujo_actual = ahorcadoFacil
                            case 2:
                                intentos = 4
                                ahorcado_dibujo_actual = ahorcadoMedio
                            case 3:
                                intentos = 3
                                ahorcado_dibujo_actual = ahorcadoDificil
                            case _:
                                print("Opción inválida. Se asigna dificultad media.")
                                time.sleep(2)
                                ahorcado_dibujo_actual = ahorcadoMedio
                                intentos = 4
                    case 2:
                        os.system('cls')
                        palabraElegida = input("Jugador 1, ingresa la palabra: ").lower()
                        pistaPersonalizada = input("Ingresa una pista para esa palabra: ")

                        palabras_con_pistas[palabraElegida] = pistaPersonalizada

                        os.system('cls')
                        #Elegir Dificultad
                        dificultad = int(input('1. Fácil (6 intentos) \n2. Media (4 intentos) \n3. Difícil (3 intentos) \nIngresa una Opcion: '))

                        os.system('cls')
                        print("Preparando Palabra...")
                        time.sleep(0.5)
                        os.system('cls')

                        match dificultad:
                            case 1:
                                intentos = 6
                                ahorcado_dibujo_actual = ahorcadoFacil
                            case 2:
                                intentos = 4
                                ahorcado_dibujo_actual = ahorcadoMedio
                            case 3:
                                intentos = 3
                                ahorcado_dibujo_actual = ahorcadoDificil
                            case _:
                                print("Opción inválida. Se asigna dificultad media.")
                                time.sleep(2)
                                ahorcado_dibujo_actual = ahorcadoMedio
                                intentos = 4

                    case 3:
                        continue
                    case _:
                        print('Opcion Invalida')

                # Juego Iniciado - Con palabra elegida
                os.system('cls')
                progreso = ['_ '] * len(palabraElegida)

                errores = 0

                while intentos > 0:
                    try:
                        print(Fore.CYAN + ahorcado_dibujo_actual[errores])
                        print(Fore.MAGENTA + "Pista:", palabras_con_pistas[palabraElegida])
                        print('')
                        print(Fore.YELLOW + 'letras usadas: ', letrasUsadas)
                        print(Fore.RED + 'Intentos Restantes: ', intentos)
                        print('')
                        print('progreso: ', ''.join(progreso))

                        letra = input("Ingresa una letra: ").lower()

                        os.system('cls')
                        print("Procesando letra...")
                        time.sleep(0.5)

                        # Validar entrada de una sola letra del abecedario
                        if len(letra) != 1 or not letra.isalpha():
                            print(Fore.RED + 'Entrada inválida. Ingresa solo UNA letra (a-z).')
                            time.sleep(1)
                            os.system('cls')
                            continue

                        # Validacion si se uso la letra que el usuario ingreso
                        if letra in letrasUsadas:
                            print(Fore.YELLOW + '¡Ya usaste esa letra!')
                            time.sleep(1)
                            os.system('cls')
                            continue

                        letrasUsadas.append(letra)

                        # Comprobar si esta la letra en la palabra
                        if letra in palabraElegida:
                            for i in range(len(palabraElegida)):
                                if palabraElegida[i] == letra:
                                    progreso[i] = letra
                                    os.system('cls')
                        else:
                            errores += 1
                            intentos -= 1
                            print(Fore.RED + 'Letra incorrecta. Intentos restantes:', intentos)
                            time.sleep(1)
                            os.system('cls')

                        # Condiciones de Victoria
                        if '_ ' not in progreso:
                            print(Fore.GREEN + '🎉 ¡Felicidades! Has adivinado la palabra: ', palabraElegida)
                            partidasGanadas += 1
                            input("Presiona Enter para volver al menú...")

                            os.system('cls')
                            print("Cargando Menu...")
                            time.sleep(0.5)
                            os.system('cls')
                            break
                    except (ValueError, KeyboardInterrupt, EOFError) as e:
                        print(f'Error: {e}')

                # Perdio la partida
                if intentos == 0:
                    print(Fore.RED + ahorcado_dibujo_actual[-1])
                    print('progreso: ', ''.join(progreso))
                    print(Fore.RED + "💀 Perdiste. La palabra era:", palabraElegida)
                    input("Presiona Enter para volver al menú...")
                    partidasPerdidas += 1

                    os.system('cls')
                    print("Cargando Menu...")
                    time.sleep(0.5)
                    os.system('cls')

            case 2:
                os.system('cls')
                print(Fore.GREEN + f'📈 Partidas Ganadas: {partidasGanadas}')
                print(Fore.RED + f'💀 Partidas Perdidas: {partidasPerdidas}')
                input(Fore.YELLOW + "\nPresiona Enter para volver al menú...")

            case 0:
                os.system('cls')
                print("Cargando...")
                time.sleep(0.5)

                os.system('cls')
                eleccion = input('Deseas salir del juego?  (S/N)').upper()
                if eleccion == 'S':
                    print('Gracias por Jugar, Vuelva Pronto')
                    time.sleep(2)

                    os.system('cls')
                    print("Cerrando El juego...")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                else:
                    print('Opcion Invalidad')
                    time.sleep(1)
            case _:
                print('Ingresa un opcion valida')
                time.sleep(1)

    except (ValueError, KeyboardInterrupt, EOFError) as e:
        print(f'Error: {e}')

