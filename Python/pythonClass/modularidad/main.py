# ==============================
# 📂 Importación de librerías personalizadas
# ==============================
# Se importan los módulos creados en la carpeta "modules"
# Cada uno maneja la persistencia de datos en un formato diferente:
# - persistenciaTxt: para archivos .txt
# - persistenciaCvs: para archivos .csv
# - persistenciaJson: para archivos .json
import modules.persistenciaTxt as cr
import modules.persistenciaCvs as persistenciaCvs
import modules.persistenciaJson as persistenciaJson


# ==============================
# 📝 EJECUCIÓN DEL MENÚ TXT
# ==============================
if __name__ == "__main__":
    # Llama al menú de persistencia en formato TXT
    # (La función menu() debe estar implementada en persistenciaTxt)
    cr.menu()


# ==============================
# 📝 EJECUCIÓN DEL MENÚ CSV
# ==============================
if __name__ == "__main__":
    # Llama al menú de persistencia en formato CSV
    persistenciaCvs.menu()


# ==============================
# 📊 GESTIÓN DE CAMPERS EN JSON
# ==============================
if __name__ == "__main__":
    # Diccionario donde se guardarán los campers leídos del archivo JSON
    camperscampus = {}

    # Leer datos existentes del archivo JSON "campers.json"
    camperscampus = persistenciaJson.read_json("data/campers.json")

    # Nuevo camper que se quiere registrar
    camper = {
        'nombre': 'carlos'
    }

    # 👇 Ejemplo comentado para agregar un nuevo camper con ID autogenerado
    # camperscampus.update({str(len(camperscampus)+1).zfill(3):camper})

    # Inicializar (crear o reiniciar) el archivo JSON de campers
    persistenciaJson.initialize_json('data/campers.json')

    # Actualizar archivo JSON → 🚨 Este ejemplo está incompleto
    # Aquí se está intentando actualizar directamente con camper['002']['nombre'],
    # pero "camper" solo tiene la clave 'nombre', por lo que generaría un error.
    # Debería estructurarse primero el diccionario con un ID.
    persistenciaJson.update_json('data/campers.json', camper['002']['nombre'])

    # Eliminar archivo JSON → 🚨 Según cómo esté implementado delete_json,
    # puede borrar un nodo específico o todo el archivo.
    persistenciaJson.delete_json('data/campers.json')
