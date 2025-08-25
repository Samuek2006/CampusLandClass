# Autor
Sahiam Valentina Esteban Esteban  
Samuel Felipe Calderon Soto

# 📚 Proyecto de Gestión - CampusLands

Este proyecto es un sistema en **Python** para la gestión de datos de un campus, incluyendo **áreas, salones, grupos, rutas de aprendizaje, campers y trainers**.  
Toda la información se administra mediante menús y s    e guarda en archivos **JSON**.

---

## 🚀 Características

- 📂 Gestión de **Áreas y Salones**  
- 👥 Administración de **Grupos**  
- 🛣️ Manejo de **Rutas de Aprendizaje**  
- 🎓 Funcionalidades para **Campers** (información y control de riesgo)  
- 👨‍🏫 Funcionalidades para **Trainers**  
- 🔑 Sistema de **login** y **sesiones**  
- 💾 Persistencia de datos en archivos `.json`

---

## 🛠️ Tecnologías utilizadas

- **Python 3.10+**
- Manejo de datos en **JSON**
- Organización modular en carpetas

---

## Librerias Utilizadas

- **Time**: Libreria para manejar el tiempo de ejecuciones en el sistema.  
- **Os**: Libreria para usar comandos de consola.  
- **Random**: Libreria para dar datos aleatorios.  
- **Getpass**: Libreria que me permite ocultar, variables en consola, principalmente para las Passwork.  
- **Json**: Libreria para manejar Json, en el sistema.  

---

## 📂 Estructura del Proyecto
```
CampusLands  
├── data/  
│ ├── AreasSalones.json  
│ ├── CampusLands.json  
│ ├── Grupos.json  
│ ├── horarios.json  
│ └── RutasAprendizaje.json  
├── modules/  
│ ├── menus.py  
│ ├── admin/  
│ │ ├── admin.py  
│ │ ├── areasSalones.py  
│ │ ├── grupos.py  
│ │ └── rutas.py  
│ ├── vistaCamper/  
│ │ ├── camper.py  
│ │ └── riesgo.py  
│ └── vistaTrainer/  
│   └── trainer.py  
├── util/  
│   ├── corefiles.py  
│   ├── login.py  
│   ├── session.py  
│   └── utilidades.py  
├── main.py  
└── README.md # Este archivo  
```

---

## ▶️ Ejecución

1. Clona este repositorio o descarga el proyecto.  
2. Asegúrate de tener **Python 3.10 o superior** instalado.  
3. Ejecuta el programa con:

```bash
python main.py
```