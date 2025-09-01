import modules.menus as menus

def menu_camper():
    while True:
        print("""Indicanos si ya estas registrado o deseas registrarte
            \n1. Ya me encuentro registrado
            \n2. Deseo registrarme
            \n3. Volver al menu principal """)
        opcion = int(input('Ingresa una opcion: '))
        
        match opcion:
            case 1:
                pass
            case 2:
                pass
            case 3:
                menus.menu_roles
            case _:
                print('Ingrese una opcion valida')
            