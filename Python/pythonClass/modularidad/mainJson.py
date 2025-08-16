import modules.persistenciaJson as cf
import json

# Inicialización
DB_FILE = "database.json"

def menu_principal():
    while True:
        print("\n🎯 SISTEMA DE GESTIÓN ACADÉMICA")
        print("1. Gestionar Campers")
        print("2. Gestionar Rutas")
        print("3. Ver datos")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            menu_campers()
        elif opcion == "2":
            menu_rutas()
        elif opcion == "3":
            mostrar_datos()
        elif opcion == "4":
            print("¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción inválida")

def menu_campers():
    while True:
        print("\n👥 GESTIÓN DE CAMPERS")
        print("1. Agregar camper")
        print("2. Editar camper")
        print("3. Eliminar camper")
        print("4. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            id_camper = input("ID del camper: ")
            nombre = input("Nombre: ")
            edad = input("Edad: ")

            nuevo_camper = {
                id_camper: {
                    "nombre": nombre,
                    "edad": edad
                }
            }

            cf.update_json(DB_FILE, nuevo_camper, ["campers"])
            print("✅ Camper agregado exitosamente")

        elif opcion == "2":
            id_camper = input("ID del camper a editar: ")
            datos = cf.read_json(DB_FILE)

            if id_camper in datos.get("campers", {}):
                print("\nDatos actuales:")
                print(f"Nombre: {datos['campers'][id_camper]['nombre']}")
                print(f"Edad: {datos['campers'][id_camper]['edad']}")

                nombre = input("\nNuevo nombre (Enter para mantener actual): ")
                edad = input("Nueva edad (Enter para mantener actual): ")

                camper_actualizado = {}
                if nombre:
                    camper_actualizado["nombre"] = nombre
                else:
                    camper_actualizado["nombre"] = datos['campers'][id_camper]['nombre']

                if edad:
                    camper_actualizado["edad"] = edad
                else:
                    camper_actualizado["edad"] = datos['campers'][id_camper]['edad']

                cf.update_json(DB_FILE, camper_actualizado, ["campers", id_camper])
                print("✅ Camper actualizado exitosamente")
            else:
                print("❌ Camper no encontrado")

        elif opcion == "3":
            id_camper = input("ID del camper a eliminar: ")
            cf.delete_json(DB_FILE, ["campers", id_camper])
            print("🗑️ Camper eliminado exitosamente")

        elif opcion == "4":
            break
        else:
            print("❌ Opción inválida")

def menu_rutas():
    while True:
        print("\n📚 GESTIÓN DE RUTAS")
        print("1. Crear nueva ruta")
        print("2. Editar ruta")
        print("3. Agregar nivel a ruta")
        print("4. Eliminar ruta")
        print("5. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            nombre_ruta = input("Nombre de la ruta: ")
            nueva_ruta = {
                nombre_ruta: {
                    "nivel1": {},
                    "nivel2": {},
                    "nivel3": {}
                }
            }
            cf.update_json(DB_FILE, nueva_ruta, ["rutas"])
            print("✅ Ruta creada exitosamente")

        elif opcion == "2":
            nombre_ruta = input("Nombre de la ruta a editar: ")
            datos = cf.read_json(DB_FILE)

            if nombre_ruta in datos.get("rutas", {}):
                nivel = input("Nivel a editar (nivel1/nivel2/nivel3): ")

                if nivel in datos["rutas"][nombre_ruta]:
                    print("\nDatos actuales:")
                    nivel_actual = datos["rutas"][nombre_ruta][nivel]
                    if "trainer" in nivel_actual:
                        print(f"Trainer actual: {nivel_actual['trainer']}")

                    nuevo_trainer = input("\nNuevo trainer (Enter para mantener actual): ")

                    if nuevo_trainer:
                        info_nivel = {
                            "trainer": nuevo_trainer,
                            "estudiantes": nivel_actual.get("estudiantes", {})
                        }
                        cf.update_json(DB_FILE, info_nivel, ["rutas", nombre_ruta, nivel])
                        print("✅ Ruta actualizada exitosamente")
                else:
                    print("❌ Nivel no encontrado")
            else:
                print("❌ Ruta no encontrada")

        elif opcion == "3":
            ruta = input("Nombre de la ruta: ")
            nivel = input("Nivel (nivel1/nivel2/nivel3): ")
            trainer = input("Nombre del trainer: ")

            info_nivel = {
                "trainer": trainer,
                "estudiantes": {}
            }

            cf.update_json(DB_FILE, info_nivel, ["rutas", ruta, nivel])
            print("✅ Nivel agregado exitosamente")

        elif opcion == "4":
            ruta = input("Nombre de la ruta a eliminar: ")
            cf.delete_json(DB_FILE, ["rutas", ruta])
            print("🗑️ Ruta eliminada exitosamente")

        elif opcion == "5":
            break
        else:
            print("❌ Opción inválida")

def mostrar_datos():
    datos = cf.read_json(DB_FILE)
    print("\n📊 DATOS ACTUALES:")
    print(json.dumps(datos, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    estructura_inicial = {
        "campers": {},
        "rutas": {}
    }
    cf.initialize_json(DB_FILE, estructura_inicial)
    menu_principal()