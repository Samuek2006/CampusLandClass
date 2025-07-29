import random, os, time
#Juego del Ahorcado
"""
Juego del Ahorcado
    debe imprimir las lineas que corresponda a la longitud de la palabra que se seleccione aleatoriamente, debe tener contador de intentos, mostras las letras que ya han sido utilizadas, en la linea de la palabra si el jugador pone una letra que corresponda con dicha palabra debe mostrarla en la posicion correspondiente, si el jugador no acierta debe restar un intento, y si adivina una de las letras que corresponda a la palabra no debe descontar intentos de adivinanza.
"""

#10 palabras aleatorias
palabrasAleatorias = [
    "computadora",
    "python",
    "ahorcado",
    "programa",
    "teclado",
    "pantalla",
    "internet",
    "juego",
    "clase",
    "codigo"
]

#Dibujo Errores en cada Oportunidad
ahorcado_dibujo = [
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


# Menu de Inicio
while True:
    try:
        os.system('cls')

        #contador de intentos
        intentos = 4
        letrasUsadas = []

        palabraElegida = (random.choice(palabrasAleatorias))
        print(palabraElegida)

        opcion = int(input('Bienvenido al Juego del Ahorcado \n1. Iniciar Juego \n0. Salir del Juego \nIngresa una Opcion: '))

        match opcion:
            case 1:
                # Juego Iniciado - Con palabra elegida
                os.system('cls')
                progreso = ['_ '] * len(palabraElegida)

                errores = 0

                while intentos > 0:
                    try:
                        print(ahorcado_dibujo[errores])
                        print('letras usadas: ', letrasUsadas)
                        print('progreso: ', ''.join(progreso))

                        letra = input("Ingresa una letra: ").lower()

                        # Validacion si se uso la letra que el usuario ingreso
                        if letra in letrasUsadas:
                            print('ya usaste esa letra.')
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
                            print('Letra incorrecta. Intentos restantes:', intentos)
                            time.sleep(1)
                            os.system('cls')

                        # Condiciones de Victoria
                        if '_ ' not in progreso:
                            print('Felicidades! Has adivinado la palabra: ', palabraElegida)
                            input("Presiona Enter para volver al menú...")
                            break
                    except (ValueError, KeyboardInterrupt, EOFError) as e:
                        print(f'Error: {e}')

                # Perdio la partida
                if intentos == 0:
                    print(ahorcado_dibujo[-1])
                    print("Perdiste. La palabra era:", palabraElegida)
                    input("Presiona Enter para volver al menú...")

            case 0:
                os.system('cls')
                eleccion = input('Deseas salir del juego?  (S/N)').upper()
                if eleccion == 'S':
                    print('Gracias por Jugar, Vuelva Pronto')
                    time.sleep(3)
                    break
                else:
                    print('Opcion Invalidad')
                    time.sleep(1)
            case _:
                print('Ingresa un opcion valida')
                time.sleep(1)

    except (ValueError, KeyboardInterrupt, EOFError) as e:
        print(f'Error: {e}')

