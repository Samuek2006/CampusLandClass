"""
Autor: Samuel Felipe Calderon Soto
Fecha: 29 / 07 2025
Descripcion: Clase 29 de Julio - Iteraciones y Excepciones en Python
Tema: Iteraciones con for, continue, break, else, try, except, finally y manejo de excepciones.
"""

"""
Funciones:
    - for: permite iterar sobre una secuencia (como una lista, tupla o cadena) y ejecutar un bloque de código para cada elemento.
    - continue: salta a la siguiente iteración del bucle, omitiendo el resto del código en el bloque actual.
    - break: interrumpe el ciclo actual.
    - else: se ejecuta un bloque de código si la condición del bucle for es falsa.
    - try: se utiliza para manejar excepciones y errores en el código.
    - except: se utiliza para capturar y manejar excepciones específicas que pueden ocurrir en el bloque try.
    - finally: se ejecuta siempre al final del bloque try, independientemente de si se produjo una excepción o no.

Palabras reservadas:
    - i: variable de iteración que se utiliza en el bucle for.
    - range: genera una secuencia de números enteros.

Cadena de texto - Métodos comunes:
    - len: devuelve la longitud de un objeto, como una lista o cadena.
    - lower: convierte una cadena a minúsculas.
    - upper: convierte una cadena a mayúsculas.
    - strip: elimina los espacios en blanco al principio y al final de una cadena.
    -replace: reemplaza una subcadena por otra en una cadena.
    - split: divide una cadena en una lista de subcadenas utilizando un separador específico.
    - join: une una lista de cadenas en una sola cadena utilizando un separador específico.
    - sep: especifica el separador a utilizar al imprimir varios elementos.

Metodos de Validacion:
    - isdigit: verifica si todos los caracteres de una cadena son dígitos.
    - isalpha: verifica si todos los caracteres de una cadena son letras.
    - isalnum: verifica si todos los caracteres de una cadena son alfanuméricos (letras o dígitos).
    - isspace: verifica si todos los caracteres de una cadena son espacios en blanco.
    - startswith: verifica si una cadena comienza con un prefijo específico.
    - endswith: verifica si una cadena termina con un sufijo específico.

Metodos de Formateo:
    - center: centra una cadena dentro de un ancho específico.
    - ljust: alinea una cadena a la izquierda dentro de un ancho específico.
    - rjust: alinea una cadena a la derecha dentro de un ancho específico.
    - zfill: rellena una cadena con ceros a la izquierda hasta alcanzar un ancho específico.
    - format: formatea una cadena utilizando marcadores de posición.
    - f-string: permite insertar expresiones dentro de cadenas utilizando llaves {}.

Listas:
    - append: agrega un elemento al final de una lista.
    - insert: inserta un elemento en una posición específica de una lista.
    - remove: elimina la primera aparición de un elemento de una lista.
    - pop: elimina y devuelve el último elemento de una lista.
    - pop(index): elimina y devuelve el elemento en la posición especificada de una lista.
    - clear: elimina todos los elementos de una lista.
    - index: devuelve el índice de la primera aparición de un elemento en una lista.
    - count: devuelve el número de veces que un elemento aparece en una lista.

Excepciones:
    - FileNotFoundError: excepción que se produce cuando se intenta acceder a un archivo que no existe.
    - ZeroDivisionError: excepción que se produce cuando se intenta dividir por cero.
    - ValueError: excepción que se produce cuando se pasa un valor no válido a una función o método.
    - (e): variable que captura la excepción en el bloque except.
"""

msg = "Hola, bienvenido al programa de iteración."
for letra in msg:
    if letra == ' ':
        continue
    print(letra, end=' ')
print()  # Imprime una nueva línea al final

for i in range(10):
    if i == 5:
        break  # Interrumpe el ciclo cuando i es igual a 5
    print(i, end=' ')
print()  # Imprime una nueva línea al final

# Iteracion bucle for con iteracion 2 en 2, recorriendo un rango de 1 a 10
print("Iterando de 1 a 10 en pasos de 2:")
for i in range(1, 10, 2):
    print(i, end=' ')
print()  # Imprime una nueva línea al final

# Listas
import os
canasta = ["Manzana", "Mango", "Pera", "Naranja", "Plátano", "Kiwi"]

# Limpia la consola
os.system("cls" if os.name == "nt" else "clear")

print(f'la canasta contiene {len(canasta)} frutas.')
print(canasta)
print(canasta[0])  # Imprime el primer elemento de la lista

for fruta in canasta:
    print(fruta, end=' ')
print()  # Imprime una nueva línea al final

# Agrega una nueva fruta a la canasta
canasta.append("Fresa")
# Inserta "mango" en la posición 2
canasta.insert(2, "mango")
# Elimina la primera aparición de "Mango"
canasta.remove("Mango")
# Elimina y devuelve el último elemento de la lista
print(canasta.pop())
#elimina y devuelve el elemento en la posición 2
print(canasta.pop(2))
# Elimina y devuelve el elemento en la posición de "Naranja"
print(canasta.pop(canasta.index("Naranja")))
print(canasta)

for idx, fruta in enumerate(canasta):
    print(f'Fruta {idx + 1}, Fruta: {fruta}')