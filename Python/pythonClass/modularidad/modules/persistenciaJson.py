import os
import json
from typing import Dict, List, Optional

# ==========================
# LECTURA DE ARCHIVO JSON
# ==========================
def read_json(file_path: str) -> Dict:
    """
    Lee y retorna el contenido completo de un archivo JSON.

    Args:
        file_path (str): Ruta al archivo JSON que se desea leer.

    Returns:
        Dict: Contenido del archivo en forma de diccionario.
              Si el archivo no existe, retorna un diccionario vacío.

    Ejemplo:
        data = read_json("data/campers.json")
        print(data)
    """
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# ==========================
# ESCRITURA EN ARCHIVO JSON
# ==========================
def write_json(file_path: str, data: Dict) -> None:
    """
    Sobrescribe el contenido de un archivo JSON con los datos pasados.

    Args:
        file_path (str): Ruta del archivo JSON donde se guardarán los datos.
        data (Dict): Diccionario con los datos a guardar.

    Ejemplo:
        write_json("data/campers.json", {"001": {"nombre": "Carlos"}})
    """
    with open(file_path, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)


# ==========================
# ACTUALIZACIÓN DE DATOS JSON
# ==========================
def update_json(file_path: str, data: Dict, path: Optional[List[str]] = None) -> None:
    """
    Actualiza un archivo JSON con nuevos datos.  
    Puede actualizar directamente el archivo completo o en una ruta específica.

    Args:
        file_path (str): Ruta del archivo JSON.
        data (Dict): Datos que se desean añadir o actualizar.
        path (List[str], opcional): Lista de claves que definen la ruta dentro
                                    del JSON donde insertar los datos.

    Ejemplo:
        # Actualización en el nivel raíz
        update_json("db.json", {"003": {"nombre": "Ana"}})

        # Actualización en una ruta específica
        update_json("db.json", {"materia": "Python"}, ["campers", "003"])
    """
    current_data = read_json(file_path)

    if not path:
        # Si no se especifica ruta → actualizar raíz
        current_data.update(data)
    else:
        # Navegar hasta la ruta especificada
        current = current_data
        for key in path[:-1]:
            current = current.setdefault(key, {})
        current.setdefault(path[-1], {}).update(data)

    write_json(file_path, current_data)


# ==========================
# ELIMINAR DATOS DEL JSON
# ==========================
def delete_json(file_path: str, path: List[str]) -> bool:
    """
    Elimina un dato dentro del JSON siguiendo una ruta específica.

    Args:
        file_path (str): Ruta del archivo JSON.
        path (List[str]): Lista de claves que representan la ruta
                          hasta el dato a eliminar.

    Returns:
        bool: True si se eliminó con éxito, False si no se encontró la ruta.

    Ejemplo:
        # Eliminar un camper con ID '002'
        delete_json("data/campers.json", ["002"])
    """
    data = read_json(file_path)
    current = data

    for key in path[:-1]:
        if key not in current:
            return False
        current = current[key]

    if path and path[-1] in current:
        del current[path[-1]]
        write_json(file_path, data)
        return True
    return False


# ==========================
# INICIALIZAR ARCHIVO JSON
# ==========================
def initialize_json(file_path: str, initial_structure: Dict) -> None:
    """
    Crea un archivo JSON con una estructura base si no existe.  
    Si ya existe, añade las claves de la estructura base que falten.

    Args:
        file_path (str): Ruta del archivo JSON.
        initial_structure (Dict): Estructura inicial mínima que debe tener.

    Ejemplo:
        initialize_json("data/campers.json", {"001": {"nombre": "Carlos"}})
    """
    if not os.path.isfile(file_path):
        write_json(file_path, initial_structure)
    else:
        current_data = read_json(file_path)
        for key, value in initial_structure.items():
            if key not in current_data:
                current_data[key] = value
        write_json(file_path, current_data)
