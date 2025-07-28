# #se requiere realizar un programa que permita leer la edad de N cantidad de personas, si el usuario que esta ingresando la informacion ingresa el numerro 0, el programa me debe mostrar la cantidad de personas que se registraron, el promedio de la edad de personas, cantidad de personas mayores de edad y cantidad de personas menores de edad y cuantas personas son mayores al promedio.

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

"""
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
"""