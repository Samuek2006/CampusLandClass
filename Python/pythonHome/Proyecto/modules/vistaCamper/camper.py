from modules.util import utilidades as util
from modules.admin import admin as admin
import modules.menu as menu

def userRegister():
    print('=== REGISTRARSE A CAMPUSLANDS ===')
    admin.addCamper()
    print('''
=== Para Poder Ingresar a CampusLands debes presentar una Pruba Logica ===

=== Logeate nuevamente para que se te Asigne la Prueba Logica ===
''')
    util.Stop()

def pruebaLogica():
    nota = util.Random()