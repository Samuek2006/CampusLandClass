from modules.util import corefiles as core
from modules.util import utilidades as util
from modules.vistaCamper import camper as camper
import getpass

DB_Cuentas = 'data/cuentasCampusLands.json'

def login():
    user = input('Ingresa Tu Correo: ')
    password = getpass.getpass('Ingresa tu contraseña: ')
    cuenta = {
        user: {
            "Contraseña": password
        }
    }

    core.update_json(DB_Cuentas, cuenta, ["cuentasCampusLands"] )

def register():
    user = input("Ingresa tu correo: ")
    password = getpass.getpass("Crea una contraseña: ")
    confirm = getpass.getpass("Confirma tu contraseña: ")

    if password == confirm:
        cuenta = {
            user : {
                "Contraseña" : password
            }
        }

        core.update_json(DB_Cuentas, cuenta, ["cuentasCampusLands"])
        print(f"\n✅ Usuario {user} registrado con éxito")

        util.Limpiar_consola()
        camper.userRegister()
        util.Limpiar_consola()

    else:
        print("\n❌ Las contraseñas no coinciden. Intenta de nuevo.")
