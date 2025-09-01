import os, time

def limpiarConsola():
    limpiar = os.system('cls' if os.name == 'nt' else 'clear')
    return limpiar

def stop():
    time.sleep(1)