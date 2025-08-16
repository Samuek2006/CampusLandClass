"""
Autor: Samuel Felipe Calderon Soto
Fecha: 14 / 08 2025
Descripcion: clase 14 agosto - 
Tema: Persistencia
"""
#Comentario en Linea
"""
Funciones:
    - Open: Abre un archivo y permite leer su contenido.

Palabras reservadas:
    - with: Se utiliza para abrir archivos de manera segura, asegurando que se cierren correctamente después de su uso.
    - Modos de Apertura de Archivos:
        - "r" : Modo lectura (por defecto). Da error si el archivo no existe.
        - "w" : Modo escritura, sobrescribe el archivo si ya existe. Si no existe, lo crea.
        - "a" : Modo agregar (append). Agrega texto al final sin sobrescribir el contenido existente.
        - "x" : Modo creación exclusiva. Da error si el archivo ya existe.
        - "r+" : Lectura y escritura, sin borrar el contenido.
        - "w+" : Lectura y escritura, pero sobrescribe el contenido.
        - "a+" : Lectura y escritura, pero agrega datos al final.
        - "b" : Se usa junto con otros modos (rb, wb, ab) para archivos binarios.

"""

import os, time

def LimpiarConsola():
    limpiar = os.system('cls' if os.name == 'nt' else 'clear')
    return limpiar

try:
    with open('git2.pdf', 'r', encoding='utf-8')as archivo:
        contenido = archivo.read()
        print(contenido)
except (FileNotFoundError, UnicodeDecodeError) as e:
    if e == FileExistsError:
        print(f'Error {e}')
        with open("archivo.txt", "w", encoding="utf-8") as archivo:
            archivo.write("Hola, este es un archivo de prueba.\n")
    elif e == UnicodeDecodeError:
        print(f'Error {e}')

time.sleep(2)
LimpiarConsola()


