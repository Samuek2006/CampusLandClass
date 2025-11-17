# Proyecto de Desarrollo de un LMS (Learning Management System)

La Institución educativa ABC, en aras de mejorar la calidad de educación que imparte, ha decidido implementar una herramienta que les permita a la comunidad educativa (estudiantes, docentes y administrativos) acceder a la información de forma práctica y potenciar la experiencia de aprendizaje.

Usted es el encargado de cumplir con el reto que se ha impuesto la institución educativa, diseñando y construyendo un LMS (Learning Management System), el cuál debe permitir la gestión de docentes, cursos, módulos y lecciones.



## **CONTEXTO**



- **Cursos**: Son un conjunto de clases o un plan de estudio estructurado (módulo), que se enfoca en un tema específico con objetivos de aprendizaje definidos.
- **Módulos:** Son una unidad de estudio completa dentro de un curso y suelen incluir varias lecciones.
- **Lecciones:** Son un grupo de actividades que contribuyen a un objetivo docente o a un resultado, estos pueden estar compuestos por contenidos multimedia (vídeos, PDFs, enlaces).
- **Docentes:** Profesional de la enseñanza que se dedica a guiar y acompañar a los estudiantes en su proceso de aprendizaje.
- **Administrativos**: Es un profesional que ofrece apoyo y asistencia en las tareas administrativas de la institución, como gestión de docentes, cursos, módulos, lecciones, entre otras.



## **REQUERIMIENTOS**

La Institución educativa requiere lo siguiente:

Interfaz moderna e intuitiva con buena UX que permita el fácil uso de la plataforma. Puede tomar como referencia el siguiente ejemplo: https://astounding-clafoutis-196412.netlify.app 



### **Gestión de docentes**: Módulo del programa que permitirá la creación, visualización, edición y eliminación de docentes (CRUD). Los datos a gestionar son: Código, identificación, nombres, apellidos, email, url de la foto del docente, área académica (Biología, Informática, etc).



### **Gestión de cursos:** Módulo del programa que permitirá la creación, visualización, edición y eliminación de cursos, módulos y lecciones (CRUD).

Los datos a gestionar son:

- Cursos: Código, nombre, descripción, docente que dirige el curso.
- Módulos: código, nombre, descripción.
- Lecciones: título, intensidad horaria, contenido (texto con el material de estudio), multimedia (recursos adicionales al contenido que aporta profundidad al tema de estudio como videos, pdf, imágenes, etc).



### **Gestión de Administrativos:** Módulo del programa que permitirá la creación, visualización, edición y eliminación de administrativos (CRUD).

Los datos a gestionar son: identificación, nombres, apellidos, email, teléfono, cargo.

Hay algunas restricciones que debe tener en cuenta:

- Debe tener en cuenta que para la eliminación de docentes, estos no pueden estar asociados a un curso.
- En esta etapa, solo se tendrá un MVP (Producto mínimo viable), por tal motivo, la plataforma estará abierta al público para visualización de los cursos.
- La plataforma debe contar con un mecanismo de autenticación que permita a los administrativos ingresar a la plataforma para su gestión.



## **Consideraciones adicionales**

- Debe utilizar las tecnologías aprendidas HTML, CSS, JS.
- La persistencia de datos debe implementarse con localStorage.
- La autenticación (login) debe ser mediante email y contraseña.



# Resultado esperado

El camper debe utilizar el conocimiento adquirido durante el skill y construir lo siguiente:

### **Login**

### **Dashboard Principal**

- Visualización resumida de estadísticas: número de cursos activos.
- Accesos rápidos a acciones comunes (crear cursos, gestionar docentes, etc).

### **Gestión de Cursos**

- Creación y edición de cursos con categorías, descripciones, duración, etiquetas y visibilidad.
- Asignación de docentes a cada curso.
- Vista en tabla con filtros por estado, fecha y tipo de curso.

### **Gestión de Docentes**

- Registro y edición de docentes.
- Asignación de cursos a cargo.
- Panel individual con su carga académica.

### **Lecciones y Contenidos**

- Estructuración de módulos de aprendizaje por curso.
- Subida de contenidos: videos, documentos, imágenes, enlaces.

### **Modulo Administrador**

- Interfaces de usuario para la gestión de información de los cursos, docentes y administrativos.



El proyecto debe ser cargado a Github. Debe incluir un read me donde se explique el proyecto, las tecnologías (lenguajes, librerías, motores de bases de datos, etc) utilizadas, un breve manual de instrucciones de como ejecutar la aplicación y la documentación de vista o modulo construido.