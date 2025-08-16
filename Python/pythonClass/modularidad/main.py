#Se importa de otra carpeta o archivo, y se connvierte en una libreria
import modules.persistenciaTxt as cr
import modules.persistenciaCvs as persistenciaCvs
import modules.persistenciaJson as persistenciaJson

if __name__ == "__main__":
    cr.menu()

# Ejecutar el menú
if __name__ == "__main__":
    persistenciaCvs.menu()

if __name__ == "__main__":
    camperscampus = {}
    camperscampus = persistenciaJson.read_json("data/campers.json")
    camper = {
        'nombre' : 'carlos'
    }

    #camperscampus.update({str(len(camperscampus)+1).zfill(3):camper})
    persistenciaJson.initialize_json('data/campers.json')
    persistenciaJson.update_json('data/campers.json', camper['002']['nombre'])
    persistenciaJson.delete_json('data/campers.json')