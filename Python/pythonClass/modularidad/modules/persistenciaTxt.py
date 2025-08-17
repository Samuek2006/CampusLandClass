"""
📔 Persistencia con Archivos de Texto: Gestor de Tareas
======================================================

Este programa implementa un gestor de tareas simple utilizando archivos de texto (.txt).  
Permite al usuario:

✅ Agregar tareas  
✅ Listar tareas  
✅ Marcar tareas como completadas  
✅ Eliminar tareas  
✅ Guardar todas las tareas en un archivo (tareas.txt)

-----------------------------------
🔍 Explicación de Funciones:
-----------------------------------
- inicializar_archivo():
    Crea el archivo tareas.txt si no existe.

- agregar_tarea(tarea):
    Añade una nueva tarea al archivo.

- listar_tareas():
    Muestra todas las tareas guardadas en el archivo.

- completar_tarea(numero):
    Marca una tarea como "Completada".

- eliminar_tarea(numero):
    Borra una tarea específica del archivo.

- menu():
    Muestra un menú interactivo para gestionar las tareas.
"""

import os

# Nombre del archivo donde se guardarán las tareas
ARCHIVO_TAREAS = "data/tareas.txt"


# ================================
# INICIALIZAR ARCHIVO
# ================================
def inicializar_archivo():
    """
    Crea el archivo de tareas si no existe.
    """
    if not os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            archivo.write("")


# ================================
# AGREGAR TAREA
# ================================
def agregar_tarea(tarea: str):
    """
    Agrega una tarea nueva al archivo, marcada como "Pendiente".

    Args:
        tarea (str): Descripción de la tarea.

    Ejemplo:
        agregar_tarea("Estudiar Python")
    """
    with open(ARCHIVO_TAREAS, "a", encoding="utf-8") as archivo:
        archivo.write(f"{tarea} - Pendiente\n")
    print(f"✅ Tarea agregada: {tarea}")


# ================================
# LISTAR TAREAS
# ================================
def listar_tareas():
    """
    Muestra todas las tareas guardadas en el archivo con su estado.

    Ejemplo de salida:
        1. Estudiar Python - Pendiente
        2. Hacer ejercicio - Completada
    """
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        tareas = archivo.readlines()

    if not tareas:
        print("📂 No hay tareas registradas.")
    else:
        print("\n📋 Lista de Tareas:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea.strip()}")


# ================================
# COMPLETAR TAREA
# ================================
def completar_tarea(numero: int):
    """
    Marca una tarea como "Completada".

    Args:
        numero (int): Número de la tarea en la lista.

    Ejemplo:
        completar_tarea(2)  # Marca como completada la tarea número 2
    """
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        tareas = archivo.readlines()

    if 1 <= numero <= len(tareas):
        tareas[numero - 1] = tareas[numero - 1].replace("Pendiente", "Completada")
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            archivo.writelines(tareas)
        print(f"✅ Tarea {numero} marcada como completada.")
    else:
        print("❌ Número de tarea inválido.")


# ================================
# ELIMINAR TAREA
# ================================
def eliminar_tarea(numero: int):
    """
    Elimina una tarea específica del archivo.

    Args:
        numero (int): Número de la tarea en la lista.

    Ejemplo:
        eliminar_tarea(1)  # Elimina la primera tarea
    """
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        tareas = archivo.readlines()

    if 1 <= numero <= len(tareas):
        tarea_eliminada = tareas.pop(numero - 1)
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            archivo.writelines(tareas)
        print(f"🗑️ Tarea eliminada: {tarea_eliminada.strip()}")
    else:
        print("❌ Número de tarea inválido.")


# ================================
# MENÚ INTERACTIVO
# ================================
def menu():
    """
    Muestra un menú interactivo para gestionar las tareas.
    Permite agregar, listar, completar o eliminar tareas.
    """
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
