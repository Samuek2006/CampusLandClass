# Autor
Samuel Felipe Calderon Soto

---

# Examen sobre el Proyecto de Gestion - CampusLands
Este es una actualizacion sobre el proyecto de **Gestion - CampusLands** donde se pide que se necesita tener un reporte de los **Trainers** asignados a las diferentes rutas que tiene actualmente **CampusLands**.

---

# Características

- Gestion de **Trainer y rutas**  
- Generar **Reporte Trainer Rutas** en archivo *json* con informacion:  
    - **ID** Trainer
    - **Nombre** Trainer
    - **Rutas** Asignadas
    - Imprimir el resumen con la **cantidad de Trainers**
    - Imprimir el resumen del **total de rutas Activas**
- json: **reporte_trainers_rutas.json**- Se encarga de guardar los reportes de los t**rainer asignados a las rutas**  
- json: **RutasAprendizaje.json** - se encarga de guardar las rutas que existen en **CampusLands**
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

## En la vista de Admin, se genera los reportes de los trainers activos con rutas asignadas en CampusLands


**ADMIN**  
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
9. Trainer Asignados A Rutas
0. Salir
```

# Opcion 9 Del menu de ADMIN  
```plaintext
=== Menu Visualizacion ===  
1. Visualizar Trainer Asignados Rutas  
2. Listar rutas existentes  
0. Regresar al menu Principal  
```


# 1. Visualizar Trainer Asignados Rutas  
```plaintext
=== Visualizar Trainer Asignados Rutas ===  
=== Trainers Activos Y Rutas a las que esta asignado ===

ID: IDTrainer | NombreTrainer ApellidoTrainer | Rutas: ['Ruta1', 'Ruta2'] 
```

# 2. Listar rutas existentes  
```plaintext
=== Rutas de Aprendizaje ===

NombreRuta
Modulo 1: Nombre Modulo
Modulo 2: Nombre Modulo

```