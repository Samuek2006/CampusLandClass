"""
📔Persistencia de datos CSV:
📌 Ejercicio: Gestión de Contactos
Crea un programa en Python que permita:

    - Agregar contactos con nombre, teléfono y correo electrónico.
    - Listar los contactos guardados en el archivo contactos.csv.
    - Buscar un contacto por nombre.
    - Eliminar un contacto por nombre.

💡 Explicación del Código
    - 📂 Crea un archivo CSV si no existe, con encabezados (Nombre, Teléfono, Email).
    - ➕ Agrega contactos escribiéndolos en el archivo CSV.
    - 📄 Lista los contactos leyéndolos del archivo CSV.
    - 🔎 Busca un contacto comparando el nombre ingresado con los datos guardados.
    - ❌ Elimina un contacto reescribiendo el archivo sin el contacto seleccionado.
    - 🖥️ Menú interactivo que permite elegir entre las diferentes opciones.
"""

import csv
import os

# Nombre del archivo CSV
ARCHIVO_CSV = "data/contactos.csv"

# Función para verificar si el archivo CSV existe, si no, lo crea con encabezados
def inicializar_archivo():
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Nombre", "Teléfono", "Email"])

# Función para agregar un contacto
def agregar_contacto(nombre, telefono, email):
    with open(ARCHIVO_CSV, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, telefono, email])
    print(f"✅ Contacto {nombre} agregado correctamente.")

# Función para listar contactos
def listar_contactos():
    with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        contactos = list(lector)

    if len(contactos) <= 1:
        print("📂 No hay contactos almacenados.")
    else:
        print("\n📜 Lista de contactos:")
        for i, contacto in enumerate(contactos[1:], start=1):  # Saltar encabezado
            print(f"{i}. {contacto[0]} - {contacto[1]} - {contacto[2]}")

# Función para buscar un contacto por nombre
def buscar_contacto(nombre):
    with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Saltar encabezado
        for contacto in lector:
            if contacto[0].lower() == nombre.lower():
                print(f"🔍 Contacto encontrado: {contacto[0]} - {contacto[1]} - {contacto[2]}")
                return
    print(f"❌ Contacto '{nombre}' no encontrado.")

# Función para eliminar un contacto por nombre
def eliminar_contacto(nombre):
    contactos_actualizados = []
    contacto_eliminado = False

    with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        contactos_actualizados.append(next(lector))  # Guardar encabezado

        for contacto in lector:
            if contacto[0].lower() == nombre.lower():
                contacto_eliminado = True
            else:
                contactos_actualizados.append(contacto)

    if contacto_eliminado:
        with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(contactos_actualizados)
        print(f"🗑️ Contacto '{nombre}' eliminado correctamente.")
    else:
        print(f"❌ Contacto '{nombre}' no encontrado.")

# Función principal para el menú interactivo
def menu():
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

