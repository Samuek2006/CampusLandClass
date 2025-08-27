session = {
    "is_logged_in": False,
    "user": None,
    "rol": None
}


def cerrar_sesion():
    global session

    session_default = '''session = {
    "is_logged_in": False,
    "user": None,
    "rol": None
}'''
    session = session_default