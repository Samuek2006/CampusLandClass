"""
Autor: Samuel Felipe Calderon Soto
Fecha: 28 / 07 2025
Descripcion: Clase 28 de Julio - Match, While y Excepciones en Python
Tema: Estructuras de control match, while, manejo de excepciones y validaciones.
"""

"""
Funciones:
    - match: permite realizar comparaciones de patrones.
    - while: permite ejecutar un bloque de código mientras una condición sea verdadera.
    - try: permite manejar excepciones y errores en tiempo de ejecución.
    - except: captura excepciones específicas o generales.
    - lower: convierte una cadena a minúsculas.

Palabras reservadas:
    - pass: omitir condicion
    - break: interrumpe el ciclo actual.
    - ValueError: excepción que se lanza cuando una operación recibe un argumento con el tipo correcto pero un valor inapropiado.
"""

# Match - Estructura de control
dia = 1
match dia:
    case 1:
        print("Hoy es Domingo")
    case 2:
        print("Hoy es Lunes")
    case _:
        print("Hoy es otro dia")

# While - Estructura de control
while True:
    try:
        dia = int(input("Ingrese el dia de la semana (1-7): "))
        match dia:
            case 1:
                print("Hoy es Domingo")
            case 2:
                print("Hoy es Lunes")
            case 3:
                print("Hoy es Martes")
            case 4:
                print("Hoy es Miercoles")
            case 5:
                print("Hoy es Jueves")
            case 6:
                print("Hoy es Viernes")
            case 7:
                print("Hoy es Sabado")
            case _:
                print("Dia no valido")
                break # Interrumpe el ciclo si el dia no es valido
    except (ValueError, KeyboardInterrupt):
        print("Por favor ingrese un numero valido.")

#Ejercicio 1 EdadNpersonasCalculos

#se requiere realizar un programa que permita leer la edad de N cantidad de personas, si el usuario que esta ingresando la informacion ingresa el numerro 0, el programa me debe mostrar la cantidad de personas que se registraron, el promedio de la edad de personas, cantidad de personas mayores de edad y cantidad de personas menores de edad y cuantas personas son mayores al promedio.

n_personas = int(0)
edad_total = int(0)
mayores_edad = int(0)
menores_edad = int(0)

while True:
    try:
        edad = int(input("Ingrese la edad de la persona (0 para terminar): "))
        match edad:
            case 0:
                if n_personas > 0:
                    promedio = edad_total / n_personas
                else:
                    print("No se registraron personas.")
                print(f"Cantidad de personas registradas: {n_personas}")
                print(f"Promedio de edad: {promedio:.2f}")
                print(f"Cantidad de mayores de edad: {mayores_edad}")
                print(f"Cantidad de menores de edad: {menores_edad}")
                print(f"Personas mayores al promedio: {sum(1 for _ in range(n_personas) if edad > promedio)}")
                break
            case edad if edad >= 18:
                mayores_edad += 1
                edad_total += edad
                n_personas += 1
            case edad if edad < 18:
                menores_edad += 1
                edad_total += edad
                n_personas += 1
            case _:
                print("Edad no valida.")
    except ValueError:
        print("Por favor ingrese un numero valido.")

edad = 0
sumaEdades = 0
contadorPersonas = 0
mayoresEdad = 0
menoresEdad = 0
promedioEdad = 0

while True:
    edad = int(input("Ingrese la edad de la persona (0 para terminar): "))
    if edad == 0:
        break
    elif edad > 0:
        sumaEdades += edad
        contadorPersonas += 1
        if edad < 18:
            menoresEdad += 1
        else:
            mayoresEdad += 1

promedioEdad = sumaEdades / contadorPersonas
print(f"Cantidad de personas registradas: {contadorPersonas}")
print(f"Promedio de edad: {promedioEdad:.2f}")
print(f"Cantidad de mayores de edad: {mayoresEdad}")
print(f"Cantidad de menores de edad: {menoresEdad}")
print(f"Personas mayores al promedio: {sum(1 for _ in range(contadorPersonas) if edad > promedioEdad)}")

#Ejercicio Muestras Edades
cantEdades = 0
menoresEdad = 0
mayoresEdad = 0
promedioEdad = 0
cantRegistro = 0

while True:
    try:
        registroMuestras = input('ingresa una opcion: \n0. para salir \n1. para registrar edad \n2. para calcular promedio \n3. Para ver Estadisticas\n')
        match registroMuestras:
            case '0':
                print("No se registraron muestras.")
                break
            case '1':
                edad = int(input("Ingrese la edad de la persona (0 para terminar): "))
                if edad == 0:
                    print("Registro de muestras completado.")
                    break
                elif edad > 0:
                    cantEdades += edad
                    cantRegistro += 1
                    if edad < 18:
                        menoresEdad += 1
                    else:
                        mayoresEdad += 1
            case '2':
                promedioEdad = cantEdades / registroMuestras
                print(f"Cantidad de personas registradas: {registroMuestras}")
                print(f"Promedio de edad: {promedioEdad:.2f}")
            case '3':
                while True:
                    try:
                        opcionEstadistica = input('Ingresa una opcion para ver las estadisticas: \n1. Mayores de edad \n2. Menores de edad \n3. Volver al menu principal\n')
                        match opcionEstadistica:
                            case '1':
                                print(f"Cantidad de mayores de edad: {mayoresEdad}")
                            case '2':
                                print(f"Cantidad de menores de edad: {menoresEdad}")
                            case '3':
                                continuar = input("¿Desea volver al menu principal? (s/n): ")
                                if continuar.lower() == 's':
                                    break
                                continue
                            case _:
                                print("Opcion no valida, por favor intente de nuevo.")
                                continue
                    except ValueError:
                        print("Por favor ingrese un numero valido.")
            case _:
                print("Opcion no valida, por favor intente de nuevo.")
                continue
    except ValueError:
        print("Por favor ingrese un numero valido.")