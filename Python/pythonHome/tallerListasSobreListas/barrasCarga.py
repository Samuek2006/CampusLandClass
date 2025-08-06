import os, time
from colorama import Fore, Style, init
init(autoreset=True)

def LimpiarConsola():
    limpiar = os.system('cls')
    return limpiar

barraCircular = [
    """
       ◜       ◝
      ║ -
       ◟       ◞
    """,
    """
       ◜══════◝
        --
       ◟      ◞
    """,
    """
       ◜      ◝
        ----   ║
       ◟      ◞
    """,
    """
       ◜       ◝
        ----->
       ◟══════◞
    """,
]

for i in range(1):
    for frame in barraCircular:
        LimpiarConsola()
        print(Fore.CYAN + frame , f'{i + 50} / 100', end=' ', )
        time.sleep(0.2)

def Cargando():
    progreso = 11
    LimpiarConsola()
    for i in range(progreso - 1):
        barra = '- ' * i
        print(f'{Fore.RED}({barra}) {i + 1} / 10', end='\r' )
        time.sleep(0.05)
    print()
    time.sleep(0.5)
    LimpiarConsola()
