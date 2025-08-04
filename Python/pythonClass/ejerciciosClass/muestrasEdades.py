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