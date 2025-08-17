"""
📔 Persistencia de datos con CSV
📌 Ejercicio: Gestión de Contactos

Este programa permite gestionar una agenda de contactos utilizando un archivo CSV.
Cada contacto tiene:
    - Nombre
    - Teléfono
    - Email

⚙️ Funcionalidades implementadas:
    - ➕ Agregar contactos con nombre, teléfono y correo electrónico.
    - 📄 Listar los contactos almacenados en el archivo `contactos.csv`.
    - 🔎 Buscar un contacto por nombre.
    - ❌ Eliminar un contacto por nombre.
    - 🖥️ Menú interactivo que permite seleccionar las opciones.

💡 Modo de persistencia:
    - Si el archivo CSV no existe, se crea automáticamente con los encabezados:
      ["Nombre", "Teléfono", "Email"]
    - Los contactos se guardan como filas dentro del archivo CSV.
"""

import csv
import os

# ==============================
# 📂 CONFIGURACIÓN DEL ARCHIVO
# ==============================

# Nombre del archivo donde se guardarán los contactos
ARCHIVO_CSV = "data/contactos.csv"


# ==============================
# 🏗️ FUNCIONES DE PERSISTENCIA
# ==============================

def inicializar_archivo():
    """
    Verifica si el archivo CSV existe.
    Si no existe, lo crea con los encabezados correspondientes:
    ["Nombre", "Teléfono", "Email"]
    """
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Nombre", "Teléfono", "Email"])  # Encabezados


def agregar_contacto(nombre, telefono, email):
    """
    Agrega un nuevo contacto al archivo CSV.
    
    Parámetros:
    - nombre (str): Nombre del contacto
    - telefono (str): Número de teléfono
    - email (str): Dirección de correo electrónico
    """
    with open(ARCHIVO_CSV, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, telefono, email])
    print(f"✅ Contacto {nombre} agregado correctamente.")


def listar_contactos():
    """
    Lista todos los contactos almacenados en el archivo CSV.
    Si no hay contactos (solo encabezado), muestra un mensaje informativo.
    """
    with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        contactos = list(lector)

    if len(contactos) <= 1:  # Solo tiene encabezado
        print("📂 No hay contactos almacenados.")
    else:
        print("\n📜 Lista de contactos:")
        for i, contacto in enumerate(contactos[1:], start=1):  # Saltar encabezado
            print(f"{i}. {contacto[0]} - {contacto[1]} - {contacto[2]}")


def buscar_contacto(nombre):
    """
    Busca un contacto en el archivo CSV por nombre.
    La búsqueda no distingue mayúsculas/minúsculas.
    
    Parámetros:
    - nombre (str): Nombre del contacto a buscar
    """
    with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Saltar encabezado

        for contacto in lector:
            if contacto[0].lower() == nombre.lower():
                print(f"🔍 Contacto encontrado: {contacto[0]} - {contacto[1]} - {contacto[2]}")
                return
    print(f"❌ Contacto '{nombre}' no encontrado.")


def eliminar_contacto(nombre):
    """
    Elimina un contacto del archivo CSV buscándolo por nombre.
    Si el contacto no existe, muestra un mensaje de error.
    
    Parámetros:
    - nombre (str): Nombre del contacto a eliminar
    """
    contactos_actualizados = []
    contacto_eliminado = False

    # Leer contactos actuales
    with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        contactos_actualizados.append(next(lector))  # Guardar encabezado

        for contacto in lector:
            if contacto[0].lower() == nombre.lower():
                contacto_eliminado = True
            else:
                contactos_actualizados.append(contacto)

    # Si se encontró el contacto, reescribir archivo sin ese contacto
    if contacto_eliminado:
        with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(contactos_actualizados)
        print(f"🗑️ Contacto '{nombre}' eliminado correctamente.")
    else:
        print(f"❌ Contacto '{nombre}' no encontrado.")


# ==============================
# 🖥️ MENÚ PRINCIPAL
# ==============================

def menu():
    """
    Menú interactivo para gestionar contactos.
    Permite al usuario elegir entre:
    1. Agregar contacto
    2. Listar contactos
    3. Buscar contacto
    4. Eliminar contacto
    5. Salir del programa
    """
    inicializar_archivo()

    while True:
        print("\n📞 Menú de Contactos")
        print("1️⃣ Agregar contacto")
        print("2️⃣ Listar contactos")
        print("3️⃣ Buscar contacto")
        print("4️⃣ Eliminar contacto")
        print("5️⃣ Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            agregar_contacto(nombre, telefono, email)

        elif opcion == "2":
            listar_contactos()

        elif opcion == "3":
            nombre = input("Ingresa el nombre a buscar: ")
            buscar_contacto(nombre)

        elif opcion == "4":
            nombre = input("Ingresa el nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)

        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break

        else:
            print("❌ Opción inválida. Inténtalo de nuevo.")
