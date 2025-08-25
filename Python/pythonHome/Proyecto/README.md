# Autor
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

## 📂 Estructura del Proyecto
```
CampusLands  
├── main.py # Archivo principal de ejecución  
├── data/ # Archivos JSON con la información  
│ ├── AreasSalones.json  
│ ├── CampusLands.json  
│ ├── Grupos.json  
│ └── RutasAprendizaje.json  
├── modules/ # Módulos del sistema  
│ ├── menus.py  
│ ├── admin/ # Funciones de administrador  
│ ├── vistaCamper/ # Funciones de campers  
│ └── vistaTrainer/ # Funciones de trainers  
├── util/ # Utilidades (login, sesión, manejo de archivos)  
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