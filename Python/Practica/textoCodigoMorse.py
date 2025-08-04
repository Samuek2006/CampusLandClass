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