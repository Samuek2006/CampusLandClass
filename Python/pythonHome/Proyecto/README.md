# Autor
Sahiam Valentina Esteban Esteban  
Samuel Felipe Calderon Soto

# 📚 Proyecto de Gestión - CampusLands

Este proyecto es un sistema en **Python** para la gestión de datos de un campus, incluyendo **áreas, salones, grupos, rutas de aprendizaje, campers y trainers**.  
Toda la información se administra mediante menús y se guarda en archivos **JSON**.

---

## 🚀 Características

- 📂 Gestión de **Áreas y Salones**  
- 👥 Administración de **Grupos**  
- 🛣️ Manejo de **Rutas de Aprendizaje**  
- 🎓 Funcionalidades para **Campers**  
  - Consulta de grupo y trainer asignado  
  - Historial de módulos cursados  
  - Notas finales por módulo  
  - Estado de módulos (aprobado/reprobado)  
  - Cálculo de promedio general  
  - Visualización del riesgo académico  
- 👨‍🏫 Funcionalidades para **Trainers**  
  - Consulta de grupos y campers asignados  
  - Visualización de la ruta de enseñanza  
  - Reportes de campers aprobados o en riesgo  
- 🔑 Sistema de **login** y **sesiones**  
- 💾 Persistencia de datos en archivos `.json`

---

## 🛠️ Tecnologías utilizadas

- **Python 3.10+**
- Manejo de datos en **JSON**
- Organización modular en carpetas

---

## 📚 Librerías Utilizadas

- **time** → manejo de tiempos en la ejecución  
- **os** → uso de comandos de consola  
- **random** → generación de datos aleatorios  
- **getpass** → ocultar contraseñas en consola  
- **json** → lectura y escritura de archivos JSON  

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
│ └── trainer.py
├── util/
│ ├── corefiles.py
│ ├── login.py
│ ├── session.py
│ └── utilidades.py
├── main.py
└── README.md
```

---

## ▶️ Ejecución

1. Clona este repositorio o descarga el proyecto.  
2. Asegúrate de tener **Python 3.10 o superior** instalado.  
3. Ejecuta el programa con:

```bash
python main.py
```

---

## EJEMPLO EJECUCION  

# 🔑 Inicio de Sesión y Roles

El sistema inicia siempre en un **login**, donde el usuario debe ingresar sus credenciales.  
Dependiendo del **rol** al que pertenezca la cuenta, accederá a un menú distinto (**Camper, Trainer o Admin**).

---

## 👥 Cuentas de Prueba

Estas cuentas están precargadas para que puedas probar el sistema sin necesidad de abrir los archivos JSON:

### 🧑‍🎓 Camper
- **Usuario:** `camper`  
- **Contraseña:** `Camper1234`

### 👨‍🏫 Trainer
- **Usuario:** `trainer`  
- **Contraseña:** `Trainer1234`

### 🛠 Admin
- **Usuario:** `admin`  
- **Contraseña:** `Admin1234`

---

## ▶️ Ejemplo de Flujo

### 1️⃣ Login
```plaintext
=== 🔑 Login CampusLands ===
Correo: camper
Contraseña: ****
✅ Sesión iniciada correctamente.
```

# 2️⃣ Menú según el rol  
Si es **Camper**:  
```plaintext
=== 🧑‍🎓 Menú Camper ===
1. Mi información
2. Mi matrícula
3. Mi progreso
0. Salir
```

Si es **Trainer**:  
```plaintext
=== 👨‍🏫 Menú Trainer ===
1. Mi información
2. Campers asignados
3. Registrar notas por módulo
4. Ver resultados de mis campers
0. Salir

```

Si es **Admin**:
```plaintext
=== 🛠 Menú Coordinador ===
1. Gestión de Campers
2. Admisiones
3. Gestión de Trainers
4. Gestión de Rutas
5. Gestión de Áreas/Salones
6. Matrículas
7. Reportes
8. Gestión de Coordinadores
0. Salir
```

✅ De esta manera, basta con iniciar sesión con una de las cuentas de prueba para acceder directamente al menú correspondiente sin necesidad de explorar los archivos JSON.

# 📌 Notas

- Todas las funcionalidades trabajan con persistencia en archivos JSON.  
- Se recomienda no editar los archivos JSON manualmente para evitar errores de consistencia.  
- El sistema está diseñado para ser modular y escalable, por lo que se pueden añadir más vistas fácilmente.  