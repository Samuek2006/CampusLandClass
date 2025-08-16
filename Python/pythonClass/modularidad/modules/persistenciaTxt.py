"""
📔Persistencia con Archivos de texto:
Ejemplo práctico que utiliza el manejo de archivos de texto en Python. Implementaremos un gestor de tareas, donde el usuario podrá:

✅ Agregar tareas ✅ Listar tareas ✅ Marcar tareas como completadas ✅ Eliminar tareas ✅ Guardar todas las tareas en un archivo de texto (tareas.txt)**

🔍 Explicación del Código
    -inicializar_archivo()
        Crea el archivo tareas.txt si no existe.
    - agregar_tarea(tarea)
        Añade una nueva tarea al archivo, marcándola como Pendiente.
    - listar_tareas()
        Muestra todas las tareas guardadas en el archivo.
    - completar_tarea(numero)
        Cambia el estado de una tarea de Pendiente a Completada.
    - eliminar_tarea(numero)
        Borra una tarea específica del archivo.
    - menu()
        Muestra un menú interactivo para gestionar las tareas.
"""

import os

ARCHIVO_TAREAS = "data/tareas.txt"

# Función para inicializar el archivo de tareas
def inicializar_archivo():
    if not os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            archivo.write("")

# Función para agregar una tarea
def agregar_tarea(tarea):
    with open(ARCHIVO_TAREAS, "a", encoding="utf-8") as archivo:
        archivo.write(f"{tarea}\n")
    print(f"✅ Tarea agregada: {tarea}")

# Función para listar todas las tareas
def listar_tareas():
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        tareas = archivo.readlines()

    if not tareas:
        print("📂 No hay tareas registradas.")
    else:
        print("\n📋 Lista de Tareas:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea.strip()}")

# Función para marcar una tarea como completada
def completar_tarea(numero):
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        tareas = archivo.readlines()

    if 1 <= numero <= len(tareas):
        tareas[numero - 1] = tareas[numero - 1].replace("Pendiente", "Completada")
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            archivo.writelines(tareas)
        print(f"✅ Tarea {numero} marcada como completada.")
    else:
        print("❌ Número de tarea inválido.")

        # Función para eliminar una tarea
def eliminar_tarea(numero):
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        tareas = archivo.readlines()

    if 1 <= numero <= len(tareas):
        tarea_eliminada = tareas.pop(numero - 1)
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            archivo.writelines(tareas)
        print(f"🗑️ Tarea eliminada: {tarea_eliminada.strip()}")
    else:
        print("❌ Número de tarea inválido.")

# Función principal con menú interactivo
def menu():
    inicializar_archivo()
    while True:
        print("\n📌 Menú de Gestor de Tareas")
        print("1️⃣ Agregar tarea")
        print("2️⃣ Listar tareas")
        print("3️⃣ Marcar tarea como completada")
        print("4️⃣ Eliminar tarea")
        print("5️⃣ Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tarea = input("Descripción de la tarea: ")
            agregar_tarea(tarea)
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            listar_tareas()
            num = int(input("Número de la tarea a completar: "))
            completar_tarea(num)
        elif opcion == "4":
            listar_tareas()
            num = int(input("Número de la tarea a eliminar: "))
            eliminar_tarea(num)
        elif opcion == "5":
            print("👋 Saliendo del gestor de tareas...")
            break
        else:
            print("❌ Opción inválida. Inténtalo de nuevo.")