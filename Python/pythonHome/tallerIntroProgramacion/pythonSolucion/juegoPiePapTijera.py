"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script es un juego de Piedra, Papel o Tijera para dos jugadores.
"""

jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").upper()
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").upper()

if jugador1 == jugador2:
    print("¡Empate!")
elif (jugador1 == "PIEDRA" and jugador2 == "TIJERA") or \
        (jugador1 == "PAPEL" and jugador2 == "PIEDRA") or \
        (jugador1 == "TIJERA" and jugador2 == "PAPEL"):
    print("¡Gana Jugador 1!")
elif (jugador2 == "PIEDRA" and jugador1 == "TIJERA") or \
        (jugador2 == "PAPEL" and jugador1 == "PIEDRA") or \
        (jugador2 == "TIJERA" and jugador1 == "PAPEL"):
    print("¡Gana Jugador 2!")
else:
    print("Opción no válida. Por favor elige entre piedra, papel o tijera.")

