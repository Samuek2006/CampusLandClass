[TOC]





# 1. Fundamentos SpringBoot

## 1.1 ¿Qué son los frameworks?

Los *frameworks* son “*marcos de trabajo*” o conocidos por ser entornos de trabajo que buscan apoyar el desarrollo de aplicaciones profesionales que sean estables y dinámicas. Estos *Frameworks* vienen con un conjunto de paquetes (librerías), herramientas y diversas utilidades que buscan apoyar el desarrollo de un macro-proyecto.

Un *framework* busca ser parte del paradigma del desarrollo de software ágil , con el fin de desarrollar proyectos de manera productiva y en menos tiempo. En este caso, desarrollar aplicativos web que tengan alta complejidad de consumo a nivel de información y contenido será de gran ayuda al momento de implementar *frameworks* en el proyecto.

Las características principales de un *framework* son las siguientes :

- **📮Escalabilidad** : Un proyecto basado en un *framework* permite crearlo al ritmo y necesidades del cliente en el momento que sea necesario.
- **📮Inversión de Control (IoC)**: Permite reutilizar código en diversas partes del programa sin necesidad de que gestionen sus propias dependencias, pues estas estarán delegadas a un contenedor o *framework* de más alto nivel.
- 📮**Modelo Vista - Controlador (MVC):** Al estar ligado al modelo vista-controlador permitirá tener una estructura estandarizada, no solamente para manejar los elementos internos sino también para consumir correctamente la información proveída
- 📮**Minimizar la escritura de código repetitivo**: Gracias a los elementos anteriormente mencionados, se puede minimizar la creación de código anteriormente establecido, pues su utilidad es referenciar dicho código para su posterior implementación.
- 📮**Bases generales auto-gestionadas**: Elementos tales como la seguridad, manejo de información, implementación de vistas serán elementos que podrán ser gestionados con mayor facilidad desde un framework.

## 1.2. ¿Que es una API?

Una interfaz de programación de aplicaciones (API) es una especificación diseñada para ser utilizada como interfaz por componentes de software para comunicarse entre sí. Una API puede incluir especificaciones para rutinas, estructuras de datos, clases de objetos y variables. La especificación de una API puede adoptar diversas formas, como un Estándar Internacional, documentación del proveedor o las bibliotecas de un lenguaje de programación, como la Biblioteca de Plantillas Estándar en C++ o la API de Java.

### Protocolos en APIs

📮**SOAP (Simple Object Access Protocol):** SOAP, lanzado a finales de la década de 1990, es un protocolo de comunicación que utiliza XML para el formato de datos. Su fortaleza clave radica en su amplio uso y aceptación en entornos empresariales. Proporciona estándares robustos para la seguridad y las transacciones, siendo comúnmente empleado en servicios web donde la interoperabilidad entre sistemas diversos es esencial.

**📮REST (Representational State Transfer):** Introducido en el año 2000, REST es una arquitectura de estilo que utiliza los métodos estándar de HTTP para el diseño de servicios web. Se destaca por su flexibilidad en el formato de datos, permitiendo el uso de varios formatos como JSON o XML. REST se centra en la simplicidad y escalabilidad, siendo ampliamente adoptado en el desarrollo web y móvil debido a su enfoque en la representación de recursos.

**📮JSON-RPC:** JSON-RPC, desarrollado a mediados de la década de 2000, es un protocolo ligero que utiliza el formato JSON para la comunicación entre sistemas. Su fortaleza principal reside en la simplicidad de implementación, ya que define una estructura clara para el envío de llamadas a procedimientos remotos y la recepción de respuestas.

**📮gRPC:** Lanzado en 2015, gRPC es un framework de comunicación desarrollado por Google. Utiliza Protocol Buffers como formato de datos por defecto, pero también es compatible con JSON y otros. La fortaleza clave de gRPC radica en su capacidad para definir cualquier tipo de función, proporcionando eficiencia y soporte para características avanzadas como la bidireccionalidad y el streaming.

**📮GraphQL:** GraphQL, surgido en 2015, es un lenguaje de consulta para APIs que permite a los clientes solicitar datos de manera personalizada. Utilizando JSON como formato de datos, su principal fortaleza es la flexibilidad en la estructuración de datos. Los clientes pueden especificar la forma y la cantidad exacta de datos que necesitan, evitando la sobreobtención de información.

**📮Thrift:** Thrift, desarrollado en 2007 por Apache, es un framework para servicios RPC que puede utilizar JSON o formato binario. Su fortaleza clave es su capacidad para adaptarse a diversos casos de uso. Conocido por su velocidad y eficiencia, Thrift es utilizado en una variedad de aplicaciones y sistemas distribuidos para la comunicación eficiente entre componentes.

## 1.3. ¿Qué es SpringBoot?

Spring Boot es un marco de desarrollo avanzado que ha revolucionado el panorama de desarrollo de aplicaciones Java empresariales. Diseñado para simplificar el proceso de creación, configuración y despliegue de aplicaciones, Spring Boot se destaca por su enfoque en la convención sobre la configuración, lo que significa que los desarrolladores pueden concentrarse en la lógica de negocio sin la carga de configuraciones extensas. Al utilizar anotaciones y proporcionar una estructura de proyecto bien definida, Spring Boot elimina gran parte de la complejidad asociada con la configuración manual de un proyecto Spring tradicional.

Una característica distintiva de Spring Boot es su capacidad para empaquetar aplicaciones como archivos ejecutables independientes, ya sea en formato JAR o WAR, lo que simplifica significativamente el despliegue y la gestión de dependencias. Además, Spring Boot ofrece una amplia integración con tecnologías modernas, como Spring Data JPA para el acceso a bases de datos, Spring Security para la implementación de medidas de seguridad, y Thymeleaf para el desarrollo de vistas en aplicaciones web.

Al igual que esto hay otras características representativas las cuales son las siguientes:

- 📮**Configuración Automática:** Spring Boot realiza la configuración automática, lo que significa que intenta configurar la aplicación basándose en las dependencias presentes en el proyecto. Esto reduce la cantidad de configuración manual que un desarrollador necesita realizar.
- 📮**Incrustación de Servidor:** Spring Boot incluye servidores integrados como Tomcat, Jetty o Undertow, lo que significa que no es necesario configurar un servidor por separado para ejecutar la aplicación. Puedes empaquetar la aplicación como un archivo JAR ejecutable o un archivo WAR para implementarla en un servidor.
- **📮Inicio Rápido:** Spring Boot facilita la creación de aplicaciones con un inicio rápido. Con unas pocas anotaciones y configuraciones mínimas, puedes desarrollar aplicaciones funcionales de manera rápida.
- **📮Microservicios:** Spring Boot es ampliamente utilizado en el desarrollo de arquitecturas de microservicios. Facilita la creación de servicios independientes que se pueden implementar y escalar de manera independiente.
- 📮**Gestión de Dependencias:** Spring Boot utiliza Spring Boot Starter, que son dependencias preconfiguradas para varias tecnologías y frameworks. Esto facilita la inclusión de las dependencias necesarias en tu proyecto.
- 📮**Monitorización y Actuadores:** Spring Boot incluye un conjunto de actuadores que proporcionan características de monitorización y administración, como la información sobre la aplicación, la salud del sistema y la gestión de los beans de Spring.
- 📮**Soporte para Spring Ecosystem:** Spring Boot se integra bien con otros proyectos del ecosistema Spring, como Spring Data, Spring Security y Spring Cloud, para facilitar el desarrollo de aplicaciones más completas.

## 1.4. ¿Qué es un Java Bean?

Un "Bean" en el contexto del framework Spring se define como **un objeto administrado, creado y controlado por el contenedor de Spring**. Estos objetos son utilizados para encapsular y proveer servicios, utilidades y funcionalidades a otros componentes dentro de una aplicación. En Spring Boot se usa la anotación "@Bean" declarar un método como un bean. Este método debe retornar un objeto que se desea registrar como un bean en el contenedor de Spring y este último se encargará entonces de gestionar el ciclo de vida y de inyectarlo en otros componentes según sea necesario.

Los Java Bean tienen una serie de características y funcionalidades, las cuales son las siguientes:

1. 📮**Reutilizable**: Los Beans están diseñados para ser empleados en distintas aplicaciones, lo que simplifica el proceso de desarrollo y mantenimiento del software.
2. 📮**Manipulable visualmente**: Los Beans pueden ser manejados de manera visual en herramientas de desarrollo como los Entornos de Desarrollo Integrados (IDEs), facilitando así su utilización por parte de los desarrolladores.
3. 📮**Serializable**: Los Beans pueden ser convertidos en una secuencia de bytes, lo que posibilita su almacenamiento y transmisión entre diferentes sistemas a través de la red o en dispositivos de almacenamiento.
4. 📮**Propiedades**: Los Beans poseen propiedades que encapsulan tanto datos como comportamiento. Estas propiedades pueden ser de solo lectura o de lectura y escritura, dependiendo de la configuración deseada.
5. 📮**Métodos**: Los Beans contienen métodos que permiten acceder y modificar sus propiedades. Los más comunes son los métodos getter, que permiten obtener el valor de una propiedad, y los setter, que permiten establecer o modificar el valor de una propiedad.
6. 📮**Eventos**: Los Beans tienen la capacidad de generar eventos para informar a otros componentes sobre cambios en su estado, lo que facilita la comunicación entre distintos elementos de un sistema.
7. **📮Introspección**: Los Beans pueden ser examinados por herramientas de desarrollo para obtener información sobre sus propiedades y métodos, lo que facilita su manipulación y utilización en el proceso de desarrollo de software.

### 1.4.1 Ciclo de vida de Bean

El ciclo de vida de un bean en Spring Boot es el conjunto de fases que atraviesa un bean desde su creación hasta su destrucción. El contenedor de Spring Boot administra el ciclo de vida de los beans, proporcionando una serie de métodos de devolución de llamada que pueden ser usados para realizar tareas específicas en cada fase.

Las fases del ciclo de vida de un bean en Spring Boot son las siguientes:

- 📮**Instantiation:** En esta fase, el contenedor de Spring Boot crea una instancia del bean.
- 📮**Configuration:** En esta fase, el contenedor de Spring Boot llama a los métodos de configuración del bean.
- 📮**Initialization:** En esta fase, el contenedor de Spring Boot llama a los métodos de inicialización del bean.
- **📮Ready:** En esta fase, el bean está listo para ser utilizado.
- 📮**Destruction:** En esta fase, el contenedor de Spring Boot destruye el bean.

## 1.5. Configuración JDK y JRE

### 1.5.1 El JDK: La Base para Programar en Java

El **JDK** (Java Development Kit) es esencial para comenzar a programar en Java, ya que proporciona todas las herramientas necesarias para compilar, ejecutar y depurar aplicaciones.

📮Pasos para Ejecutar un Programa en Java

🔑**Instalar el JDK**: Es indispensable para compilar y ejecutar programas Java.

🔑**Configurar un IDE o Editor**: Un entorno de desarrollo integrado, como IntelliJ IDEA o Apache NetBeans, facilita la escritura y depuración del código.

**🔑Escribir el Código**: Desarrolla tu programa en un archivo con la extensión `.java`.

**🔑Compilar el Código**: Usa el comando `javac` para convertir el código fuente en bytecode.

**🔑Ejecutar el Programa**: Emplea el comando `java` para ejecutar el bytecode generado.

### 1.5.2 Datos Importantes

🔑El **JDK** contiene todas las herramientas necesarias para desarrollar y ejecutar programas Java.

🔑Un **IDE** como IntelliJ IDEA, Apache NetBeans o Eclipse ofrece funcionalidades adicionales que simplifican el desarrollo.

🔑Los pasos de **compilación** y **ejecución** son fundamentales para transformar el código en una aplicación funcional.

------

### 1.5.3 ¿Qué es un Compilador y Por Qué es Necesario en Java?

Un **compilador** es una herramienta que traduce el código fuente escrito en un lenguaje de alto nivel (como Java) a un lenguaje de bajo nivel o código máquina que puede ser ejecutado directamente por el sistema operativo.

📮Importancia del Compilador en Java

En Java, el compilador **`javac`** convierte el código fuente (archivos `.java`) en **bytecode** (archivos `.class`). El bytecode es un formato intermedio que no depende de ninguna plataforma específica. Esto permite que el programa sea ejecutado en cualquier sistema operativo que tenga una **Máquina Virtual Java (JVM)** instalada.

### 1.5.4 ¿Qué es el JDK?

El **Java Development Kit (JDK)** es un conjunto de herramientas esenciales para desarrollar aplicaciones en Java. Sus principales componentes incluyen:

1. **Compilador (javac)**: Convierte el código fuente Java en bytecode.
2. **Java Runtime Environment (JRE)**: Contiene las bibliotecas y la JVM necesarias para ejecutar el bytecode.
3. **Herramientas de Desarrollo**: Incluye utilidades como el depurador (**jdb**) y el empaquetador (**jar**), entre otras.

### 1.5.5 ¿Qué es el JRE?

El **Java Runtime Environment (JRE)** es un subconjunto del JDK diseñado exclusivamente para ejecutar programas Java. Sus componentes clave son:

1. **JVM (Java Virtual Machine)**: Responsable de interpretar y ejecutar el bytecode.
2. **Bibliotecas de Clase**: Proveen las funcionalidades necesarias para que las aplicaciones Java puedan ejecutarse.
3. **Otros Componentes**: Incluyen archivos de configuración, bibliotecas nativas y otros elementos de soporte.

------

### 1.5.6 Relación entre JDK y JRE

- **JDK**: Es más completo, ya que incluye el JRE junto con las herramientas de desarrollo necesarias, como el compilador y depuradores.
- **JRE**: Está enfocado únicamente en la ejecución de aplicaciones Java, sin herramientas de desarrollo.

### 1.5.7 Instalación

1. Ingrese al sitio web oficial https://adoptium.net/es/temurin/releases/

2. Seleccione el sistema operativo, la arquitectura, el tipo de paquete y la versión a instalar. Para el desarrollo de esta guia sugerimos la siguiente configuración para sistemas operativos Windows.

   > Descargue los instaladores .msi para mayor facilidad y confiabilidad en el proceso de instalación

   ![](https://i.ibb.co/cY8vq8f/image.png)

3. Instale primero el JDK y posteriormente el JRE

## 1.2 Configuración IDE

### 1.2.1 Visual Studio Code

Visual Studio Code (VS Code) es un editor de texto y desarrollador de código en línea gratuito que se basa en el proyecto Visual Studio. Es similar a Microsoft Word o Notepad++, pero con características más avanzadas y funcionalidades adicionales.

**Características clave de VS Code:**

1. **Compatibilidad con proyectos de desarrollo**: VS Code puede trabajar con todos los proyectos de desarrollo, incluyendo IDEs como IntelliJ IDEA, Eclipse, NetBeans y más.
2. **Integración con lenguajes de programación**: VS Code se integra bien con varios lenguajes de programación, incluyendo JavaScript, Python, Java, C#, C++, Ruby, etc.
3. **Soporte para múltiples entornos de desarrollo**: VS Code ofrece soporte para desarrolladores que trabajan en diferentes entornos de desarrollo, como Azure, AWS, Heroku, etc.
4. **Integración con herramientas de desarrollo**: VS Code ofrece integraciones con herramientas de desarrollo populares, como Git, Node.js, React, Angular, Vue.js, etc.
5. **Compatibilidad con bases de datos relativas y absolutas**: VS Code puede trabajar con bases de datos relativas y absolutas, incluyendo MySQL, PostgreSQL, MongoDB, SQLite, etc.
6. **Soporte para el código de código fuente**: VS Code tiene un sistema de gestión de código de fuente muy avanzado, lo que permite a los desarrolladores crear y mantener proyectos más complejos.
7. **Compatibilidad con la plataforma Mac y Windows**: VS Code está disponible para ambos sistemas operativos.

**Funcionalidades adicionales de VS Code:**

1. **Integración con lenguajes de programación orientados a objetos (OOP)**: VS Code tiene una gran cantidad de extensiones que integran con los lenguajes de OOP populares, como Java, C#, Python, JavaScript, etc.
2. **Soporte para la programación de microservicios**: VS Code ofrece herramientas y funcionalidades específicas para el desarrollo de microservicios, como la creación de servicios RESTful y la integración con servidores en tiempo real.
3. **Integración con lenguajes de programación de Python y R**: VS Code tiene extensões que integran con Python y R, lo que permite a los desarrolladores trabajar con estos lenguajes de programación de manera más efectiva.

**Ventajas de usar VS Code:**

1. **Flexibilidad y personalización**: VS Code ofrece una gran cantidad de configuraciones y extensiones personalizables para adaptarse a las necesidades específicas de cada proyecto.
2. **Productividad**: VS Code es un editor de código que se enfoca en la eficiencia y la productividad, lo que puede ayudar a los desarrolladores a escribir más rápido y a realizar tareas de código más rápidamente.
3. **Compatibilidad con proyectos de desarrollo modernos**: VS Code está diseñado para trabajar con proyectos de desarrollo modernos, incluyendo aquellos que utilizan tecnologías como Docker, Kubernetes, etc.

**Desventajas de usar VS Code:**

1. **Costo**: VS Code puede ser más costoso que otros editors de código, especialmente si se utiliza en un entorno profesional.
2. **Aprendizaje y configuración**: Los desarrolladores pueden necesitar un poco de tiempo para aprender a utilizar VS Code y adaptarse a sus necesidades específicas.

En resumen, VS Code es un editor de código y desarrollador de código en línea que ofrece una gran cantidad de características y funcionalidades para trabajar con proyectos de desarrollo modernos.

### 1.2.2 Configuración VisualStudio Code

1. Instalar visual studio code desde la pagina oficial  https://code.visualstudio.com/

   ![](https://i.ibb.co/M5C57X52/image.png)

   2. Después de instalar visual studio code abralo y cree un nuevo perfil como desarrollador JavaSpringBoot

      ![](https://i.ibb.co/F4DKdtF1/image.png)

      en la ventana de creación de perfiles haga clic en el boton New Profile

      ![](https://i.ibb.co/9mKh29jd/image.png)

      Llene el formulario con el nombre del nuevo perfil y si desea que el perfil que se esta creando herede las caracteristicas de otro perfil lo puede seleccionar en las opciones indicadas.

      ![](https://i.ibb.co/JwnzCv4C/image.png)

      **1️⃣- Nombre del Perfil:**

      - Esta opción permite asignar un nombre personalizado al nuevo perfil que se está creando. En la imagen, el usuario ha nombrado el perfil como **"JavaSpringBoot"**.
      - Los perfiles en Visual Studio Code permiten personalizar la configuración, extensiones y preferencias para diferentes proyectos o entornos de trabajo.

      **2️⃣ - Copiar desde otro perfil:**

      - Esta opción permite seleccionar un perfil existente como base para el nuevo perfil.
      - Si se elige un perfil en el desplegable, el nuevo perfil copiará configuraciones y preferencias del perfil seleccionado.
      - En la imagen, la opción seleccionada es **"None"**, lo que significa que el nuevo perfil se creará vacío sin copiar configuraciones de otro perfil.

      **3️⃣ - Contenido del Perfil:**

      - Esta sección permite definir qué configuraciones específicas se incluirán en el nuevo perfil.
      - Se pueden configurar diferentes contenidos como:
        - **Settings (Configuraciones)**
        - **Keyboard Shortcuts (Atajos de teclado)**
        - **Tasks (Tareas)**
      - En la columna "Source", se muestra si estos elementos serán heredados del perfil "Default" o si estarán vacíos ("None").
   
   3. Haga clic en el boton Create para finalizar la creación del nuevo perfil
   
      ![](https://i.ibb.co/wZsfQfFC/image.png)
   
   4. Para finalizar puede activar el perfil por defecto haciendo clic en el botón ✔
   
      ![](https://i.ibb.co/SwVrHSHH/image.png)
   
   5. Haga clic en el boton de Administración de extensiones en visual studio code para instalar y personalizar las extensiones de desarrollo teniendo en cuenta la tecnología a usar.
   
      ![](https://i.ibb.co/tTp91nDb/image.png)
   
      Extensiones requeridas:
   
      ![](https://i.ibb.co/Tx0wFXbg/image.png)
   
      La extensión **"Extension Pack for Java"** de Microsoft para Visual Studio Code es un paquete de extensiones diseñadas para facilitar el desarrollo en Java dentro del editor. Su propósito es proporcionar herramientas esenciales para programar en Java con funcionalidades avanzadas.
   
      ### **¿Qué ofrece esta extensión?**
   
      Este paquete incluye varias extensiones populares para el desarrollo en Java, tales como:
   
      1. **Java IntelliSense** – Proporciona autocompletado inteligente y sugerencias mientras escribes código.
      2. **Depuración (Debugging)** – Permite ejecutar y depurar aplicaciones Java directamente en VS Code.
      3. **Testing** – Soporte para escribir y ejecutar pruebas unitarias en Java.
      4. **Maven/Gradle** – Integración con herramientas de construcción como Maven y Gradle para gestionar dependencias y compilaciones.
      5. **Soporte para Servidores y Frameworks** – Compatibilidad con Spring Boot, Quarkus y otras herramientas de backend en Java.
      6. **Explorador de proyectos** – Facilita la navegación entre archivos, clases y métodos dentro de proyectos Java.
   
      ![](https://i.ibb.co/5WpRKxnr/image.png) 
   
      La extensión **"Spring Boot Dashboard"** para **Visual Studio Code** es una herramienta diseñada para facilitar el desarrollo y la gestión de aplicaciones **Spring Boot** dentro del editor.
   
      ### **¿Para qué sirve esta extensión?**
   
      Esta extensión proporciona un **panel de control (dashboard)** para gestionar y monitorear proyectos de **Spring Boot** directamente desde VS Code. Sus funcionalidades incluyen:
   
      1. **Inicio y detención de aplicaciones Spring Boot** desde el panel sin necesidad de usar la terminal.
      2. **Visualización de aplicaciones en ejecución**, permitiendo ver detalles como puertos, perfiles y configuración activa.
      3. **Monitoreo de logs en tiempo real**, facilitando la depuración de aplicaciones.
      4. **Integración con Spring Boot Actuator**, permitiendo acceder a métricas, endpoints y estado de la aplicación de forma rápida.
      5. **Manejo de múltiples proyectos Spring Boot**, ideal si trabajas en microservicios o varias aplicaciones simultáneamente.
   
      ![](https://i.ibb.co/7x1tfRCM/image.png)
   
      La extensión **"Spring Boot Tools"** para **Visual Studio Code**, desarrollada por **VMware**, está diseñada para mejorar la experiencia de desarrollo con **Spring Boot**, proporcionando herramientas esenciales para la configuración y validación de archivos de propiedades.
   
      ### **¿Para qué sirve esta extensión?**
   
      Esta extensión facilita el trabajo con archivos de configuración de **Spring Boot**, específicamente:
   
      1. **Asistencia en la configuración de archivos**
         - Proporciona autocompletado y sugerencias en archivos `application.properties` y `application.yml`.
         - Ayuda a evitar errores de sintaxis y configuraciones incorrectas.
      2. **Validación de configuración**
         - Detecta errores en las propiedades de configuración de Spring Boot.
         - Advierte sobre propiedades obsoletas o mal configuradas.
      3. **Mejor integración con Spring Boot Actuator**
         - Proporciona herramientas para gestionar y monitorear la aplicación.
         - Permite visualizar endpoints disponibles y configuraciones activas.
      4. **Optimización del flujo de trabajo**
         - Mejora la edición y navegación en proyectos Spring Boot.
         - Compatible con otras extensiones de Spring Boot para VS Code.
      
      ![](https://i.ibb.co/JRLzx1nq/image.png)
   

# 2. Introducción a SpringBoot

## 2.1. Creación de proyectos SpringBoot

Para la creación de un proyecto siga las siguientes recomendaciones:

1. Cree una carpeta principal donde se almacenaran todos los proyectos que va a desarrollar

2. El nombre de la carpeta no debe tener espacios en blanco ni caracteres especiales.

   Para este esta guia se creara un folder llamado springprojects

   | ![Screenshot_1](Manuales\imgspring\Screenshot_1.png) |
   | :----------------------------------------------------------- |

3. Abra Visual Studio Code y presione Ctrl+Shif+P para abrir la paleta de comandos

![paletaComandos](d:\Breakline\Manuales\imgspring\paletaComandos.png)

en la caja de texto escriba Spring init:

![Screenshot_2](https://i.ibb.co/4tRQYW5/Screenshot-2.png)

**Spring Initializr: Add Starters...**

- Esta opción permite **agregar dependencias (starters)** a un proyecto de Spring Boot existente. Los *starters* son conjuntos predefinidos de dependencias que proporcionan funcionalidades como desarrollo web, seguridad, bases de datos, mensajería, entre otros.

**Spring Initializr: Create a Gradle Project...**

- Esta opción ayuda a generar un **nuevo proyecto de Spring Boot** utilizando **Gradle** como herramienta de construcción (*build tool*). Gradle es una alternativa a Maven y se usa por su rapidez en la resolución de dependencias y su flexibilidad en la configuración de proyectos.

**Spring Initializr: Create a Maven Project...**

- Esta opción permite generar un **nuevo proyecto de Spring Boot** utilizando **Maven** como herramienta de construcción. Maven es muy popular en el ecosistema Java para la gestión de dependencias y la automatización de compilaciones.

Para esta guia se usara maven. y la version LTS de spring (3.2.6) no se recomienda usar la versión  SNAPSHOOT.



![Screenshot_5](d:\Breakline\Manuales\imgspring\Screenshot_5.png)

![](https://i.ibb.co/0p1YxmC2/image.png)

Como lenguaje de desarrollo se usara Java.

![Screenshot_7](d:\Breakline\Manuales\imgspring\Screenshot_7.png)

A continuación especifique el grupo ID. el grupo Id debe tener el formato com.company.project

![Screenshot_8](d:\Breakline\Manuales\imgspring\Screenshot_8.png)

**¿Qué es el Group ID?**

El **Group ID** es un identificador único para tu proyecto, siguiendo la convención de nombres de paquetes en Java (generalmente en notación de nombre de dominio en reversa).
Ayuda a **organizar e identificar** tu proyecto de manera única dentro de un ecosistema más amplio.

**Ejemplos de Group ID:**

- `com.example`
- `org.mycompany`
- `com.tunombre.proyecto`

**¿Cuándo lo necesitas?**

- Al configurar un **nuevo proyecto de Spring Boot** en **Maven o Gradle**.
- Se usa en la **estructura de paquetes** de tus clases en Java.
- Es un campo **obligatorio** en los archivos **`pom.xml` (Maven)** o **`build.gradle` (Gradle)**.

**¿Cómo elegir un Group ID?**

✅ **Si trabajas en un proyecto personal:**

- Usa algo como: `com.tunombre.proyecto`

🏢 **Si trabajas en un proyecto empresarial:**

- Usa el dominio de tu empresa en reversa, por ejemplo: `com.empresa.aplicacion`

🌍 **Si es un proyecto de código abierto:**

- Sigue una convención general, como: `org.ejemplo.proyecto`

Especifique el nombre del proyecto:

![Screenshot_9](d:\Breakline\Manuales\imgspring\Screenshot_9.png)

**¿Qué es el Artifact ID?**

- El **Artifact ID** es el **nombre de tu proyecto** y se utilizará como el **nombre base para tu archivo JAR o WAR** al compilar la aplicación.
- Generalmente es un **identificador corto en minúsculas** que representa el proyecto.

**Ejemplos de Artifact ID:**

- `miaplicacion`
- `spring-demo`
- `ecommerce-backend`

Especifique el tipo de empaquetado. Para esta guia se usara Jar.

![Screenshot_10](d:\Breakline\Manuales\imgspring\Screenshot_10.png)

Seleccione la versión del JDK. Para esta versión se debe usar la versión 17 o 21

![Screenshot_11](d:\Breakline\Manuales\imgspring\Screenshot_11.png)

**Versiones de Java:**

1. **Java 17** (LTS - Soporte a Largo Plazo) ✅ **Recomendado**
   - Estable y ampliamente utilizado.
   - Versión **LTS oficial** con soporte hasta **al menos 2029**.
   - Compatible con **Spring Boot 3+**.
   - La mejor opción para la mayoría de las **aplicaciones empresariales**.
2. **Java 21** (LTS - Soporte a Largo Plazo)
   - La versión **LTS más reciente**, lanzada en **septiembre de 2023**.
   - Ofrece **mejoras de rendimiento** y nuevas características.
   - Totalmente compatible con **Spring Boot 3+**.
   - Buena opción si deseas las últimas características de un LTS.
3. **Java 23** (No-LTS, Versión Futura)
   - **No es una versión LTS**.
   - Puede incluir características experimentales.
   - Aún no es ampliamente adoptado en entornos de producción.
   - Solo elige esta opción si deseas probar funciones avanzadas en desarrollo.

**¿Cuál deberías elegir?**

- ✅ **Java 17** → **Mejor opción por estabilidad y compatibilidad**.
- 🚀 **Java 21** → Buena opción si deseas la última versión LTS.
- ⚠️ **Java 23** → Solo para pruebas de nuevas características.

Seleccione las dependencia a incorporar en el proyecto. Para esta guía incorporar las siguientes dependencias.

![](https://i.ibb.co/DmCSn8L/image.png)

**Dependencias Seleccionadas:**

1. **Spring Web** 🌐 (Para construir APIs RESTful y aplicaciones web)
   - Necesario para desarrollar **servicios web RESTful** y **aplicaciones Spring MVC**.
   - Usa **Apache Tomcat** como servidor embebido predeterminado.
2. **MySQL Driver** 🛢️ (Para conectarse a bases de datos MySQL)
   - Proporciona el **controlador JDBC** necesario para interactuar con una **base de datos MySQL**.
3. **Spring Boot DevTools** ⚡ (Para recarga en caliente y desarrollo más rápido)
   - Habilita **LiveReload**, **reinicio automático de la aplicación**, y configuraciones optimizadas para desarrollo.
4. **Lombok** ✍️ (Para reducir el código repetitivo)
   - Biblioteca de Java que reduce el **código boilerplate** proporcionando **generación automática de getters/setters**, **constructores** y **registro de logs** a través de anotaciones.
5. **Spring Data JPA** 📦 (Para interacción con bases de datos usando JPA/Hibernate)
   - Simplifica el **acceso a bases de datos** utilizando **Spring Data**.
   - Funciona con **Hibernate** como proveedor JPA predeterminado.
6. **Thymeleaf** 🖥️ (Para renderización de HTML en el servidor)
   - Un **motor de plantillas** utilizado para renderizar dinámicamente **vistas HTML**.
   - Comúnmente utilizado en **aplicaciones web basadas en MVC**.

**¿Qué te permite construir esta configuración?**

- Una **aplicación web** con una **base de datos MySQL**.
- Usa **Spring Data JPA** para la persistencia de datos.
- Proporciona **recarga en caliente** con **DevTools**.
- Reduce el **código repetitivo** con **Lombok**.
- Usa **Thymeleaf** para renderizar páginas HTML dinámicamente.

**¿Es esta configuración adecuada para tu proyecto?**

✅ **Ideal para:**

- Aplicaciones web con **Spring MVC**.
- Aplicaciones **CRUD** con **MySQL**.
- Proyectos que requieren **desarrollo rápido con DevTools**.

💡 **Si planeas construir solo una API REST sin vistas**, puedes **omitir Thymeleaf**. 🚀

Seleccione la carpeta donde se creara el proyecto. Recuerde que es necesario contar con conexión a internet.

<img src="Manuales\imgspring\Screenshot_15.png" alt="Screenshot_15" style="zoom:67%;" />

## 2.2 Abriendo el proyecto en visual studio code

1. Abra visual studio code

2. Haga clic en el menu file Open Folder y seleccione la carpeta del proyecto que creo.

   ![](https://i.ibb.co/KcFT4vhk/image.png)

   ![](https://i.ibb.co/XxHXcTw3/image.png)

## 2.3 Estructura de archivos del proyecto

![](https://i.ibb.co/yn35z869/image.png)

📁 **.mvn/**

- Carpeta interna de **Maven Wrapper**, contiene archivos de configuración para ejecutar Maven sin necesidad de instalarlo manualmente.

📁 **.vscode/**

- Carpeta específica de **Visual Studio Code** que almacena configuraciones del editor para este proyecto.

📁 **src/**

- Contiene el 

  código fuente del proyecto

  . Se divide en dos subdirectorios principales:

  - **`src/main/java/`** → Contiene las clases Java del proyecto.
  - **`src/main/resources/`** → Contiene recursos como archivos de configuración (`application.properties` o `application.yml`), plantillas HTML (si usas **Thymeleaf**) y otros archivos estáticos.
  - **`src/test/java/`** → Contiene las pruebas unitarias y de integración.

📁 **target/**

- Carpeta donde se **compilan y empaquetan los archivos del proyecto**. Se genera al ejecutar `mvn package` o `mvn install`.

📄 **.gitattributes**

- Archivo de **Git** que define configuraciones específicas para manejar archivos en el repositorio.

📄 **.gitignore**

- Archivo de **Git** que define qué archivos o carpetas deben **excluirse** del control de versiones, como `target/` y archivos temporales.

📄 **HELP.md**

- Archivo de ayuda generado por **Spring Initializr**, contiene información sobre la estructura del proyecto y cómo ejecutarlo.

📄 **mvnw** y **mvnw.cmd**

- Maven Wrapper

  : Permite ejecutar Maven sin necesidad de instalarlo globalmente en el sistema.

  - **`mvnw`** → Se usa en **Linux/macOS**.
  - **`mvnw.cmd`** → Se usa en **Windows**.

📄 **pom.xml**

- Archivo de configuración principal de Maven

  - Define **dependencias** del proyecto (Spring Boot, JPA, Lombok, etc.).

  - Configura **versiones**, **plugins** y otros parámetros del proyecto.

  - Se ejecuta con comandos como:

    ```
    shCopiarEditarmvn clean install  # Compila y empaqueta el proyecto
    mvn spring-boot:run  # Ejecuta la aplicación
    ```

------

✅ **Resumen**

- 📂 **`src/`** → Código fuente del proyecto.
- 📂 **`target/`** → Carpeta de salida con el JAR/WAR compilado.
- 📄 **`pom.xml`** → Configuración principal del proyecto (dependencias, plugins, etc.).
- 📄 **`mvnw` y `mvnw.cmd`** → Scripts para ejecutar Maven sin instalación.
- 📄 **`.gitignore` y `.gitattributes`** → Configuraciones para Git.

Clase principal @SpringBootApplication

![Screenshot_22](https://i.ibb.co/YDYnJh1/Screenshot-22.png)

<img src="Manuales\imgspring\Screenshot_23.png" alt="Screenshot_23" style="zoom:80%;" />

`@SpringBootApplication` es una anotación en Spring Boot que se utiliza para marcar una clase principal de la aplicación Spring Boot. Esta anotación combina varias anotaciones de Spring en una sola, simplificando la configuración y el inicio de la aplicación.

A continuación se listan algunas funciones especiales de @SpringBootApplication

1. **Configuración de la aplicación**: Esta anotación incluye `@Configuration`, lo que significa que la clase marcada con `@SpringBootApplication` puede contener métodos anotados con `@Bean`, los cuales definirán los componentes y configuraciones de Spring.
2. **Component scanning**: `@SpringBootApplication` incluye `@ComponentScan`, que permite a Spring Boot escanear y detectar automáticamente los componentes de la aplicación (como controladores, servicios y repositorios) dentro del paquete base de la clase anotada y sus subpaquetes.
3. **Arranque de la aplicación**: `@SpringBootApplication` incluye `@EnableAutoConfiguration`, que permite la configuración automática de la aplicación basada en las dependencias presentes en el classpath. Esto simplifica significativamente la configuración de la aplicación al reducir la necesidad de configuración manual.
4. **Clase principal de la aplicación**: Al marcar una clase con `@SpringBootApplication` y especificarla como la clase principal en el archivo `pom.xml` o `build.gradle`, se define el punto de entrada de la aplicación Spring Boot. Esta clase contiene el método `main()` que inicia la aplicación y carga el contexto de Spring.

# 3. **Introduccion a Thymeleaf**

## 3.1 ¿Qué es Thymeleaf?

Thymeleaf es una librería que proporciona la herramienta necesaria para crear plantillas HTML con facilidad. Las plantillas son archivos HTML personalizados que se pueden utilizar en diferentes partes del proyecto, como los encabezados, el cuerpo y los pies de página.

## 3.2 Características clave de Thymeleaf

*   **Compatibilidad**: Thymeleaf está diseñado para trabajar con Java 5 y superior.
*   **Flexibilidad**: Permite la creación de plantillas personalizadas con diferentes partes del proyecto.
*   **Simplicidad**: Fácil de utilizar, incluso para desarrolladores no especializados en Java.
*   **Integración con Spring**: Es compatible con el framework Spring.
*   **Optimización**: Es una librería muy rápida y eficiente.

## 3.2.1 Beneficios

*   **Mejora la experiencia del usuario**: Las plantillas personalizadas permiten crear una interfaz más atractiva y fácil de usar.
*   **Reducción del tiempo de desarrollo**: La automatización de la creación de plantillas permite un enfoque más orientado al negocio.
*   **Más eficiente el uso del espacio de memoria**: Las plantillas se pueden almacenar de manera eficiente, especialmente si se utilizan para plantillas con muchas variables.

## 3.3 Creación de paginas usando Thymeleaf

### 3.3.1 Requerimientos

#### 3.3.1.1 . Requisitos previos

Antes de empezar, asegúrate de tener lo siguiente instalado:

- **Java** (JDK 8 o superior).
- **Spring Boot** configurado en tu proyecto.
- Un **IDE** como IntelliJ IDEA o VS Code con soporte para Spring Boot.
- **Maven** o **Gradle** para la gestión de dependencias.

------

#### 3.3.1.2. Agregar la dependencia de Thymeleaf

Si usas **Maven**, en tu archivo `pom.xml`, agrega:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```

Si usas **Gradle**, en `build.gradle` agrega:

```
{
    implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'
}
```

> Se recomienda realizar la importacion de Thymeleaf cuando este creando el proyecto.

Para comenzar a trabajar con Thymeleaf vamos a crear un nuevo proyecto utilizando el asistente de creación de proyectos de Spring boot. Recordemos que para iniciar el panel de comandos de visual Studio code debemos presionar las teclas Ctrl + Shift + P.

Para esta guía vamos a utilizar únicamente 3 dependencias las cuales se muestran en la figura a continuación 

![](https://i.ibb.co/PvYdMGkN/image.png)

Como recomendacion  personal les aconsejo trabajar con la pestaña de Java Project ya que podremos visualizar la estructura del proyecto como la visualizaríamos típicamente en entornos de desarrollo integrados como netbeans, eclipse. 

<img src="https://i.ibb.co/ZzjF4sqh/image.png" style="zoom:80%;" />

Otro tip importante al momento de trabajar con visual Studio es activar la opción de visualización en forma de jerarquía ya que nos va a permitir visualizar todos los archivos y estructura del proyecto de una manera más amplia y entendible. 

![](https://i.ibb.co/B2HL4hsK/image.png)

Cuando se crea el proyecto utilizando el inicializador de Spring bood automáticamente se crea una estructura base la cual nos va a permitir organizar de forma adecuada cada una de las clases y artefactos de software que tenemos que crear durante el proceso de desarrollo. En la estructura del proyecto vamos a encontrar un paquete llamado src/main/resources y de dentro de dicho paquete vamos a encontrar una carpeta llamada templates y static. En la carpeta templates debemos crear todas las vistas HTML de nuestro proyecto en la carpeta static vamos a poder ubicar recursos externos o archivos externos al proyecto como imágenes script de javascript e incluso estilo CSS. 

## 3.4 Como crear documentos Web(Html)

Para la creación del documento web HTML se debe seleccionar el paquete resource y dar clic derecho sobre la carpeta templates y a continuación seleccionar la opción file. Otra forma de crear el archivo es haciendo clic sobre el icono + el cual se encuentra ubicado a la derecha del título templates. 

**Opcion 1**

![](https://i.ibb.co/nMbZPczq/image.png)

**Opcion 2**

<img src="https://i.ibb.co/8LJPbBTc/image.png" style="zoom:80%;" />

> Recuerde pulsar enter cuando ingrese el nombre del recurso a crear.

Cree un documento html llamado index.html ![](https://i.ibb.co/SXkG47nC/image.png) 

## 3.5 Creacion del Controlador

Para crear un controlador lo primero que tenemos que llevar a cabo es la creación de un paquete el cual se encuentra referenciado al paquete principal para esto se debe seleccionar el paquete principal del proyecto y se hace clic en el icono representado con el símbolo + para la creación de un nuevo recurso de Java ya sea clase, paquete, interfaz etc. 

![](https://i.ibb.co/dwc8Zsdw/image.png)

![](https://i.ibb.co/Y4X1j0qW/image.png)

### 3.5.1¿Qué es un Controlador en Spring Boot?

Un **controlador** en Spring Boot es una clase que gestiona las solicitudes HTTP y define cómo se procesan las peticiones y respuestas dentro de la aplicación. Se encarga de recibir datos desde el cliente (navegador, API, etc.), procesarlos y devolver una respuesta.

------

### 3.5.2 Tipos de Controladores en Spring Boot

En Spring Boot, hay dos tipos principales de controladores:

1. **Controladores para aplicaciones web con vistas (Thymeleaf, JSP, etc.)**
   - Usan la anotación `@Controller`
   - Devuelven vistas HTML renderizadas con datos.
2. **Controladores para API REST**
   - Usan la anotación `@RestController`
   - Devuelven datos en formato JSON o XML.

------

#### 3.5.2.1 Controlador con `@Controller` para Vistas Web

Cuando trabajas con **Thymeleaf**, debes usar `@Controller` para manejar las peticiones y devolver vistas HTML.

**Ejemplo: Controlador para cargar una vista**

```java
package com.example.demo.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("mensaje", "¡Bienvenido a mi aplicación con Spring Boot!");
        return "index"; // Carga la plantilla index.html desde src/main/resources/templates/
    }
}
```

**Explicación**

- `@Controller`: Define la clase como un controlador para manejar vistas web.
- `@GetMapping("/")`: Indica que el método responderá a una petición `GET` en la URL raíz `/`.
- `Model model`: Se usa para enviar datos a la vista (`index.html`).
- `return "index"`: Devuelve la vista `index.html`.

------

#### 3.5.2.2 Controlador REST con `@RestController`

La anotación `@RestController` en Spring Boot sirve para marcar una clase como un controlador especializado en la creación de servicios web RESTful. Esta anotación combina las funcionalidades de `@Controller` y `@ResponseBody`, lo que significa que los métodos de la clase anotada con `@RestController` devuelven directamente objetos serializados en formato JSON o XML como respuesta a las solicitudes HTTP, en lugar de depender de las vistas tradicionales.

⚠**características importantes de `@RestController`:**

​	1️⃣**Gestión de solicitudes HTTP**: Al igual que con `@Controller`, los métodos dentro de una clase anotada con `@RestController` pueden manejar las solicitudes HTTP mediante anotaciones como `@RequestMapping`, `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`, etc.

​	2️⃣**Respuestas RESTful**: La anotación `@RestController` agrega automáticamente la anotación `@ResponseBody` a cada método en la clase, lo que indica que los resultados de los métodos son enviados directamente al cuerpo de la respuesta HTTP en lugar de ser tratados como nombres de vistas. Esto facilita la creación de servicios RESTful que devuelven datos estructurados como JSON o XML.

​	3️⃣**Serialización automática**: Spring Boot, junto con bibliotecas como Jackson, se encarga de serializar automáticamente los objetos devueltos por los métodos de un controlador `@RestController` en el formato adecuado (JSON o XML) antes de enviarlos como respuesta al cliente.

​	4️⃣**Facilidad de uso**: Al utilizar `@RestController`, se simplifica la configuración y el desarrollo de servicios web RESTful, ya que elimina la necesidad de anotar métodos individualmente con `@ResponseBody`.

**Ejemplo: Controlador REST que devuelve JSON**

```java
package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ApiController {

    @GetMapping("/saludo")
    public String saludo(@RequestParam(name = "nombre", defaultValue = "Usuario") String nombre) {
        return "¡Hola, " + nombre + "! Bienvenido a la API.";
    }
}
```

**Explicación**

- `@RestController`: Indica que el controlador devuelve respuestas en **JSON** en lugar de vistas HTML.
- `@GetMapping("/saludo")`: Maneja peticiones `GET` en la URL `/saludo`.
- `@RequestParam(name = "nombre", defaultValue = "Usuario")`: Recibe un parámetro opcional llamado `nombre`.

### 3.5.3 Creando el primer controlador

Para este primer ejercicio vamos a crear un controlador que nos permita abrir la plantilla HTML llamada index que se ha creado previamente. Para crear el controlador nos ubicamos en el paquete que hemos creado previamente llamado Controller y damos clic en el símbolo + en la ventana de selección de recursos debemos seleccionar clases y a continuación ingresamos el nombre del controlador; el identificador o nombre del controlador se recomienda que tenga el prefijo Controller después del nombre que le hemos dado al controlador. 

> Es de buena práctica que el nombre del controlador tenga el mismo nombre del documento o plantilla HTML que deseamos visualizar. 

![](https://i.ibb.co/bRCkgmzB/image.png)

![](https://i.ibb.co/M5BMSnBY/image.png)



En la clase creada se debe agregar la anotación @Controller : **La anotación `@Controller` en Spring Boot cumple una función importante al marcar una clase como un controlador en el patrón de diseño Modelo-Vista-Controlador (MVC). Esta anotación específica es parte del ecosistema de Spring MVC, que es un framework de desarrollo web basado en el patrón MVC y utilizado ampliamente en aplicaciones Spring**.

![](https://i.ibb.co/vCGT13pC/image.png)

El `import` trae la anotación `@Controller` del paquete `org.springframework.stereotype`. Esta anotación se usa en Spring Boot para marcar una clase como **controlador**, lo que significa que manejará peticiones HTTP y devolverá vistas.

Para poder visualizar el documento HTML creado agregue la siguiente funcionalidad a la clase index Controller. 

```java
package com.usingthymeleaf.thymeleaf_app.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class indexController {
    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("mensaje", "Bienvenido a Spring Boot con Thymeleaf");
        return "index"; // Nombre de la vista Thymeleaf (index.html)
    }
}
```

En el documento web creado realice los siguientes cambios: 

En etiqueta HTML agregue el atributo:  ![](https://i.ibb.co/z0gd7jJ/image.png) Este atributo define un espacio de nombres XML para las funciones de Thymeleaf. Le indica al navegador y a Thymeleaf que todos los atributos que comienzan con `th:` pertenecen a **Thymeleaf** y deben ser procesados en el servidor.

Agregue un encabezado h1 y en el encabezado h1 agregue el atributo ![](https://i.ibb.co/fz8jntSK/image.png) El atributo `th:text` en Thymeleaf se usa para **reemplazar el contenido de un elemento HTML con un valor dinámico** proveniente del modelo de datos en **Spring Boot**.

![](https://i.ibb.co/QF0ndQp8/image.png)

### 3.5.4 Ejecución proyecto

Para poder ejecutar el proyecto de Spring boot vamos a hacer uso del dashboard, recordemos que el liderazgo es el panel administrar y gestionar la ejecución de proyectos y poder verificar diferentes endpoint que se encuentran configurados en el proyecto. Mientras Cuba también vamos a poder visualizar los diferentes Beans creados en el Proyecto. 

<img src="https://i.ibb.co/LX8bL9BF/image.png" style="zoom:67%;" />

Para ejecutar el proyecto nos dijimos a la sección de apps en el dashboard le hacemos clic sobre el botón de ejecución run, automáticamente se levanta el servidor integrado de tomcat y podremos observar en la terminal de visual Studio code la información de inicio donde nos muestra el puerto y la o r a la cual podemos acceder desde el navegador web por defecto la dirección URL local es localhost. 

![](https://i.ibb.co/XcRBXkZ/image.png)

![](https://i.ibb.co/HDrY9hyN/image.png)

Cuando finalice la carga del servidor tomcat y todos los servicios necesarios el siguiente paso es abrir el navegador web de su preferencia y en la URL escribir la URL localhost: 8080 

![](https://i.ibb.co/6049PLXf/image.png)

## 3.6 Parametros

Cuando se desarrollen aplicaciones web interactivas es necesario habilitar el envío de información durante la ejecución / renderizado de las vistas(páginas web) para esto es necesario utilizar los parámetros en el interfaz grafica y en el controlador. en este apartado nos centraremos en el envío y recepción de parámetros hacia un endpoint. 

### 3.6.1 Representación de datos con Model

**Model** se utiliza dentro del patrón **MVC (Model-View-Controller)**. En este contexto, el **modelo (Model)** representa los datos de la aplicación y cómo estos se gestionan.

📌 **Uso del Model en Controladores Spring MVC**

Si usas Spring MVC para manejar peticiones web, puedes inyectar objetos en el modelo con la anotación `@ModelAttribute` o el parámetro `Model` en el controlador.

**Ejemplo**

⌨**Clase indexController**

```java
package com.usingthymeleaf.thymeleaf_app.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class indexController {
    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("mensaje", "Bienvenido a Spring Boot con Thymeleaf");
        model.addAttribute("nombre", "Johlver Jose Pardo");
        model.addAttribute("profesion", "Ingeniero FullStack");
        return "index"; // Nombre de la vista Thymeleaf (index.html)
    }
}
```

⌨**View index.html**

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Perfil</title>
</head>
<body>
    <h1 th:text="${mensaje}">Texto por defecto</h1>
    <h2 th:text="${nombre}">Nombre por defecto</h2>
    <p th:text="${profesion}">Profesión por defecto</p>
</body>
</html>
```

> El comando `./mvnw spring-boot:run` permite ejecutar el proyecto (Windows)

<img src="https://i.ibb.co/sJPKKzfz/image.png" style="zoom:67%;" />

#### 3.6.2 @ModelAttribute

En **Spring Boot**, `@ModelAttribute` es una anotación utilizada en **controladores** para **preparar datos y vincular objetos a la vista** en aplicaciones web con **Thymeleaf**. Se usa principalmente para:

1. **Pasar datos a la vista antes de renderizarla**.
2. **Mapear datos del formulario al objeto en el controlador** automáticamente.
3. **Inicializar valores antes de procesar una petición**.

```java
    @ModelAttribute("users")
    public List<User> usersModel() {
        List<User> users = Arrays.asList(
            new User("Pepa", "Gonzalez"),
            new User("Lalo", "Perez", "lalo@correo.com"),
            new User("Juanita", "Roe", "juana@correo.com"),
            new User("Andres", "Doe")
        );
        return users;
    }
```

**Uso de `@ModelAttribute` en un Controlador**

La anotación `@ModelAttribute` se puede utilizar en dos formas principales:

1. **En métodos del controlador**, para añadir atributos al `Model`.
2. **En parámetros de métodos**, para enlazar los datos de un formulario con un objeto Java.

**Ejemplo 1: Cargar datos en la vista antes de renderizarla**

Cuando usas `@ModelAttribute` en un método, este se ejecuta **antes** de que se ejecute cualquier otro método controlador en la misma clase.

📌 **Ejemplo: Pasar una lista de roles a la vista antes de que se cargue el formulario**

```java
@Controller
@RequestMapping("/usuarios")
public class UsuarioController {

    @ModelAttribute("roles")
    public List<String> roles() {
        return List.asList("ADMIN", "USUARIO", "INVITADO");
    }

    @GetMapping("/form")
    public String mostrarFormulario(Model model) {
        model.addAttribute("usuario", new Usuario());
        return "formulario";
    }
}

```

**📌 Plantilla Thymeleaf `formulario.html`**

```html
<form action="/usuarios/guardar" method="post" th:object="${usuario}">
    <label>Nombre:</label>
    <input type="text" th:field="*{nombre}" />

    <label>Rol:</label>
    <select th:field="*{rol}">
        <option th:each="rol : ${roles}" th:value="${rol}" th:text="${rol}"></option>
    </select>

    <button type="submit">Guardar</button>
</form>
```

**Ejemplo 2: Enlazar Datos de un Formulario a un Objeto con `@ModelAttribute`**

Cuando un usuario envía un formulario, `@ModelAttribute` puede convertir los datos enviados en un **objeto Java** automáticamente.

**📌 Controlador**

```java
@Controller
@RequestMapping("/usuarios")
public class UsuarioController {

    @GetMapping("/form")
    public String mostrarFormulario(Model model) {
        model.addAttribute("usuario", new Usuario());
        return "formulario";
    }

    @PostMapping("/guardar")
    public String guardarUsuario(@ModelAttribute Usuario usuario, Model model) {
        model.addAttribute("mensaje", "Usuario guardado con éxito: " + usuario.getNombre());
        return "resultado";
    }
}
```

------

**📌 Modelo `Usuario.java`**

```
public class Usuario {
    private String nombre;
    private String rol;

    // Constructor vacío
    public Usuario() {}

    // Getters y Setters
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public String getRol() { return rol; }
    public void setRol(String rol) { this.rol = rol; }
}
```

------

**📌 Plantilla `formulario.html`**

```
<form action="/usuarios/guardar" method="post" th:object="${usuario}">
    <label>Nombre:</label>
    <input type="text" th:field="*{nombre}" />

    <label>Rol:</label>
    <input type="text" th:field="*{rol}" />

    <button type="submit">Guardar</button>
</form>
```

------

**📌 Plantilla `resultado.html`**

```
<h2 th:text="${mensaje}"></h2>
```

🎯 **¿Cuándo Usar `@ModelAttribute`?**

1. **Para pasar datos comunes a todas las vistas** (por ejemplo, listas de opciones, configuración, datos compartidos).
2. **Para mapear automáticamente los datos de un formulario a un objeto** (evita escribir `request.getParameter("nombre")`).
3. **Para predefinir valores de un formulario antes de cargarlo** (como usuario por defecto o valores iniciales).

### 3.6.2 Map y HashMap

En **Spring Boot**, `Map` es una **interfaz de Java** que pertenece a `java.util` y se usa para almacenar pares **clave-valor**. Se utiliza en múltiples escenarios dentro de una aplicación Spring Boot, como la gestión de configuraciones, respuesta de controladores, inyección de dependencias, entre otros.

1️⃣**Declaración de un `Map`**

```java
import java.util.*;

Map<KeyType, ValueType> nombreDelMapa = new HashMap<>();
```

📍 **Ejemplo con tipos específicos:**

```java
Map<String, Integer> edades = new HashMap<>();
```

Aquí, las **claves** son `String` (nombres de personas) y los **valores** son `Integer` (edades).

2️⃣**Tipos de `Map` en Java**

Existen diferentes implementaciones de `Map` en Java:

| Tipo                      | Características                                              |
| ------------------------- | ------------------------------------------------------------ |
| `HashMap<K, V>`           | No mantiene orden de inserción, permite `null` en claves y valores. |
| `TreeMap<K, V>`           | Mantiene los elementos ordenados por clave (requiere `Comparable`). |
| `LinkedHashMap<K, V>`     | Mantiene el orden de inserción de los elementos.             |
| `ConcurrentHashMap<K, V>` | Similar a `HashMap` pero con soporte para concurrencia (hilos). |

3️⃣**Métodos Principales de `Map`**

| Método                   | Descripción                                                  |
| ------------------------ | ------------------------------------------------------------ |
| `put(K key, V value)`    | Agrega un par clave-valor o actualiza uno existente.         |
| `get(K key)`             | Obtiene el valor asociado a una clave.                       |
| `remove(K key)`          | Elimina un par clave-valor.                                  |
| `containsKey(K key)`     | Verifica si la clave existe en el mapa.                      |
| `containsValue(V value)` | Verifica si el valor existe en el mapa.                      |
| `size()`                 | Devuelve la cantidad de pares clave-valor.                   |
| `keySet()`               | Retorna un `Set` con todas las claves.                       |
| `values()`               | Retorna una colección con todos los valores.                 |
| `entrySet()`             | Retorna un `Set` de `Map.Entry<K,V>`, útil para recorrer el mapa. |

### 3.6.3 HashMap

`HashMap` es una estructura de datos en Java que implementa la interfaz `Map`. Representa un conjunto de pares clave-valor, donde cada clave está asociada a un valor. Esta estructura permite el almacenamiento y recuperación eficiente de datos mediante el uso de una función de dispersión (hashing).

**características clave de `HashMap`:**

1. **Pares clave-valor**: Los elementos en un `HashMap` se almacenan como pares clave-valor, donde cada clave es única dentro del mapa y está asociada a un solo valor.
2. **Eficiencia**: La búsqueda, inserción y eliminación de elementos en un `HashMap` se realizan en tiempo constante en promedio (O(1)), siempre y cuando la función de dispersión esté bien diseñada y haya pocos conflictos de hash.
3. **No ordenado**: A diferencia de algunas implementaciones de `Map` como `LinkedHashMap`, los elementos en un `HashMap` no tienen un orden específico. Es decir, no hay garantía sobre el orden en que se devolverán las claves o los valores al iterar sobre el mapa.
4. **Permite valores nulos**: `HashMap` puede contener pares clave-valor donde tanto la clave como el valor pueden ser `null`. Sin embargo, normalmente se evita usar `null` como clave debido a que no se puede distinguir entre una clave `null` y la ausencia de una clave en el mapa.
5. **No sincronizado**: La implementación estándar de `HashMap` en Java (la clase `java.util.HashMap`) no es sincronizada, lo que significa que no es segura para su uso en entornos con múltiples hilos concurrentes sin sincronización externa. Sin embargo, existe una versión sincronizada llamada `Hashtable` que puede ser utilizada en tales casos, aunque con un costo de rendimiento.

#### 3.6.3.1 Métodos clave de `HashMap`:

- `put(K key, V value)`: Agrega un par clave-valor.
- `get(Object key)`: Obtiene el valor asociado a la clave.
- `remove(Object key)`: Elimina una clave y su valor asociado.
- `containsKey(Object key)`: Verifica si existe una clave.
- `containsValue(Object value)`: Verifica si existe un valor.
- `size()`: Devuelve el número de elementos en el `HashMap`.

⌨**Clase indexController**

```java
package com.usingthymeleaf.thymeleaf_app.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import java.util.HashMap;
import java.util.Map;

@Controller
public class indexController {
    @GetMapping("/")
    public String home(Model model) {
        Map<String, Object> datos = new HashMap<>();
        
        datos.put("mensaje", "Bienvenido a Spring Boot con Thymeleaf");
        datos.put("nombre", "Johlver Jose Pardo");
        datos.put("profesion", "Ingeniero FullStack");
        
        // Agregamos algunos datos adicionales para demostrar el uso del Map
        datos.put("experiencia", 5);
        datos.put("tecnologias", new String[]{"Java", "Spring", "JavaScript", "Angular"});
        
        model.addAttribute("datos", datos);
        return "index";
    }
}
```

⌨**View index.html**

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Perfil</title>
</head>
<body>
    <h1 th:text="${datos.mensaje}">Texto por defecto</h1>
    <h2 th:text="${datos.nombre}">Nombre por defecto</h2>
    <p th:text="${datos.profesion}">Profesión por defecto</p>
    
    <p>Años de experiencia: <span th:text="${datos.experiencia}"></span></p>
    
    <h3>Tecnologías:</h3>
    <ul>
        <li th:each="tech : ${datos.tecnologias}" th:text="${tech}"></li>
    </ul>
</body>
</html>
```



#### 3.6.3.2 @Restcontroller con `Map`

Esta sección esta enfocada en  la integración entre la anotación @RestController y Map. Para el caso para vamos a crear un nada controlador que nos permitirá realizar esa integración para casos prácticos de esta guía el controlador se denominará userController. en el cual definiremos un endpoint el cual nos permitirá visualizar información establecida en el map; a diferencia de los casos anteriores no se renderizara la información en una página web o view, el resultado será retornado en formato json.

**Controlador userController**

```java
package com.usingthymeleaf.thymeleaf_app.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.HashMap;
import java.util.Map;

@RestController
public class userController {
    
    @GetMapping("/welcome")
    public Map<String, Object> getWelcomeMessage() {
        Map<String, Object> response = new HashMap<>();
        response.put("mensaje", "¡Bienvenido al mundo del desarrollo backend!");
        response.put("autor", "Johlver Pardo");
        return response;
    }
}
```

> Ejecute el proyecto con el comando: ./mvnw spring-boot:run (Windows)

![](https://i.ibb.co/VYx32DPg/image.png)

**📌 Resumen**

- `Map` es una estructura clave-valor en **Java** que es ampliamente utilizada en **Spring Boot**.
- Se usa en **controladores** para devolver respuestas JSON.
- Permite inyectar configuraciones desde `application.properties`.
- Se emplea en **servicios** para almacenar datos dinámicos y procesar información.

#### 3.6.3.3 @RequestMapping

`@RequestMapping` es una anotación fundamental en Spring MVC (y también en Spring Boot) que se utiliza para mapear solicitudes HTTP a métodos específicos dentro de un controlador. Esta anotación es bastante versátil y puede ser utilizada para mapear una variedad de tipos de solicitudes HTTP (GET, POST, PUT, DELETE, etc.) a métodos en un controlador.

formas en que se puede usar `@RequestMapping`:

1. **Mapeo de URLs**: `@RequestMapping` permite mapear una URL específica a un método en un controlador. Por ejemplo, `@RequestMapping("/hello")` mapea la URL "/hello" a un método en el controlador.
2. **Mapeo de métodos HTTP**: `@RequestMapping` permite especificar el método HTTP al que responde un método en el controlador. Por ejemplo, `@RequestMapping(value="/hello", method=RequestMethod.GET)` indica que el método en el controlador responde únicamente a solicitudes GET.
3. **Múltiples URLs y métodos**: `@RequestMapping` permite mapear múltiples URLs y métodos HTTP al mismo método en el controlador. Por ejemplo, `@RequestMapping(value={"/hello", "/greetings"}, method={RequestMethod.GET, RequestMethod.POST})` mapea los métodos GET y POST a las URLs "/hello" y "/greetings".
4. **Parámetros de solicitud**: `@RequestMapping` también puede tener parámetros adicionales para especificar condiciones de solicitud más complejas, como parámetros de consulta, encabezados de solicitud, tipo de contenido, etc.

```java
package com.usingthymeleaf.thymeleaf_app.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/v1/users")
public class userController {
    
    @GetMapping("/welcome")
    public Map<String, Object> getWelcomeMessage() {
        Map<String, Object> response = new HashMap<>();
        response.put("mensaje", "¡Bienvenido al mundo del desarrollo backend!");
        response.put("autor", "Tu Nombre");
        return response;
    }
}
```

![](https://i.ibb.co/tpKqKfTk/image.png)

### 3.6.4 ArrayList

**¿Qué es un ArrayList?**

Un `ArrayList` en Java es una implementación de la interfaz `List` del paquete `java.util`. Es una colección de objetos redimensionable que se puede utilizar para almacenar y manipular una lista ordenada de elementos. A diferencia de los arrays tradicionales de Java, que tienen un tamaño fijo, los `ArrayList` pueden crecer o reducirse dinámicamente según sea necesario.

**Características principales de ArrayList:**

- **Ordenado:** Los elementos se almacenan en un orden específico basado en el índice. Puede acceder a los elementos por su índice (posición).
- **Redimensionable:** Puede agregar o eliminar elementos del `ArrayList` en tiempo de ejecución. El `ArrayList` se agranda o reduce automáticamente para adaptarse al número de elementos.
- **Basado en arrays:** Internamente, un `ArrayList` utiliza un array para almacenar los elementos. Sin embargo, a diferencia de los arrays fijos, el `ArrayList` gestiona automáticamente el tamaño del array subyacente.

En el siguiente ejemplo se implementara un nuevo endpoint que retorne un listado de usuarios almacenados en un arrayList.

1. Edite la clase UserRestController y agregue el siguiente metodo.

   ```java
       @GetMapping("/list-details")
       public List<User> listdetails(){
           User user = new User("Juan","Perez");
           User userA = new User("Camilo","Hernandez");
           User userB = new User("Martha","Estupiñan");
           List<User> lstUsers = new ArrayList<>();
           lstUsers.add(user);
           lstUsers.add(userA);
           lstUsers.add(userB);
           return lstUsers;
       }
   ```

   <img src="Manuales\imgspring\Screenshot_72.png" alt="Screenshot_72" style="zoom:67%;" />

### 3.6.5 Models

En las aplicaciones Spring Boot que siguen el patrón de diseño Modelo-Vista-Controlador (MVC), el Modelo sirve como contenedor para los datos que necesitan ser pasados entre el Controlador y la Vista. Actúa como un puente, permitiendo al Controlador compartir información con la Vista para su presentación.

Para esta guía se creara un modelo que represente los datos de un usuario.

1. Cree un nuevo paquete llamado models. El paquete debe depender el paquete principal del proyecto.

   <img src="https://i.ibb.co/zTLcFLHR/image.png" style="zoom:67%;" />

   <img src="https://i.ibb.co/35LXmm6d/image.png" style="zoom:67%;" />

1. Cree una nueva clase en el paquete models y llamela User

   <img src="https://i.ibb.co/BVD7T9N7/image.png" style="zoom:67%;" />

   <img src="https://i.ibb.co/nH5KYL9/image.png" style="zoom:67%;" />

   ```java
   package com.usingthymeleaf.thymeleaf_app.models;
   
   public class User {
       private String name;
       private String lastName;
   }
   

#### 3.6.5.1 Getters (métodos de acceso):

   - Los getters son métodos públicos que **devuelven el valor** de una variable privada de la clase.
   - Su nombre suele empezar por `get` seguido del nombre de la variable con la primera letra en mayúscula (por ejemplo, `getName()` para una variable privada `name`).
   - No toman ningún parámetro (argumentos).

**Setters (métodos modificadores):**

   - Los setters son métodos públicos que **establecen o actualizan el valor** de una variable privada de la clase.
   - Su nombre suele empezar por `set` seguido del nombre de la variable con la primera letra en mayúscula (por ejemplo, `setName()` para una variable privada `name`).
   - Toman un parámetro del mismo tipo de dato que la variable privada.

**Ventajas de usar getters y setters:**

- **Encapsulación:** Al mantener las variables privadas y proporcionar acceso controlado a través de getters y setters, se protege el estado interno de la clase de modificaciones no deseadas.
   - **Validación:** Se pueden incluir validaciones dentro de los setters para garantizar que solo se asignen valores válidos a las variables. Por ejemplo, un setter para una edad podría comprobar que el valor sea positivo.
   - **Mayor flexibilidad:** Los getters y setters pueden personalizarse para realizar tareas adicionales, como el registro de cambios o la notificación a otras partes del código cuando se modifica una variable.
   
   Para agregar los métodos haga clic derecho en un espacio vacio dentro de la clase y seleccione la opción Source Action
   
   <img src="https://i.ibb.co/LhSSXvZQ/image.png" style="zoom:67%;" />
   
   en el asistente de creacion de los metodos seleccione los atributos a los se les va a crear los get y set.
   
   ![](https://i.ibb.co/v6ZWvxYk/image.png)
   
   Como resultado la clase User quedara de asi:
   
   <img src="https://i.ibb.co/VcDJjJ0P/image.png" style="zoom:67%;" />

```
   package com.usingthymeleaf.thymeleaf_app.models;
   
   public class User {
       private String name;
       private String lastName;
       public String getName() {
           return name;
       }
       public void setName(String name) {
           this.name = name;
       }
       public String getLastName() {
           return lastName;
       }
       public void setLastName(String lastName) {
           this.lastName = lastName;
       }
       
   }
```

#### 3.6.5.2 Constructor de la clase

En programación orientada a objetos, un constructor es un método especial que se utiliza para **inicializar** un objeto recién creado. Se llama automáticamente **cuando se crea una instancia de una clase**.

**Características clave de los constructores:**

- **Nombre:** El nombre del constructor **debe ser el mismo que el nombre de la clase**.

- **Tipo de retorno:** Los constructores **no tienen tipo de retorno**. Esto se debe a que su función principal es inicializar el objeto, no devolver ningún valor.

- **Parámetros:** Los constructores pueden tener **parámetros** para recibir valores iniciales para las variables de instancia del objeto. Esto permite personalizar la creación del objeto con diferentes configuraciones.

- Inicialización:

   Dentro del constructor, se 

  asigna valores a las variables de instancia

   del objeto. Esto puede implicar:

  - Asignar valores predeterminados.
  - Validar los valores proporcionados como parámetros.
  - Realizar otras tareas de inicialización necesarias para que el objeto esté listo para su uso.

**Tipos de constructores:**

- **Constructor por defecto:** Un constructor **sin parámetros** que se invoca cuando no se proporcionan valores explícitos al crear un objeto. Asigna valores predeterminados a las variables de instancia.
- **Constructor con parámetros:** Un constructor que **recibe parámetros** para inicializar las variables de instancia con valores específicos proporcionados por el usuario.

Para crear el constructor de la clase haga clic derecho en un espacio vacío de la clase y en el menu contextual seleccione la opcion Source Action

<img src="Manuales\imgspring\Screenshot_61.png" style="zoom:80%;" />

<img src="Manuales\imgspring\Screenshot_62.png" alt="Screenshot_62" style="zoom:80%;" />

Seleccione los atributos que desea pasar por parámetro en el constructor.

![](https://i.ibb.co/hxg4xjPJ/image.png)

Como resultado del proceso obtendremos el constructor en la clase:

```java
package com.usingthymeleaf.thymeleaf_app.models;

public class User {
    private String name;
    private String lastName;

    public User(String name, String lastName) {
        this.name = name;
        this.lastName = lastName;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getLastName() {
        return lastName;
    }
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
    
}
```

Ajustando el controlador.....

```java
package com.usingthymeleaf.thymeleaf_app.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.usingthymeleaf.thymeleaf_app.models.User;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/v1/users")
public class userController {
    
    @GetMapping("/welcome")
    public Map<String, Object> getWelcomeMessage() {
        User user = new User("Johlver","Pardo");
        Map<String,Object> body = new HashMap<>();
        body.put("title", "Desarrollando con Spring boot CreativeCode");
        body.put("user", user);
        return body;
    }
}

```

Modificando UserController utilizando Model....

```java
package com.usingthymeleaf.thymeleaf_app.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.usingthymeleaf.thymeleaf_app.models.User;

@Controller
public class indexController {
    @GetMapping("/")
    public String home(Model model) {
        User user = new User("Johlver","Pardo");
        model.addAttribute("title", "Desarrollando con Spring boot CreativeCode");
        model.addAttribute("user", user);
        return "index";
    }
}
```

Modificando template view (details.html)

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title th:text="${title}">Document</title>
</head>
<body>
    <h1 th:text="${user.name}"></h1>
    <h2 th:text="${user.lastName}"></h2>
</body>
</html>
```

> Ejecute el proyecto con el comando: ./mvnw spring-boot:run (Windows)
>

<img src="https://i.ibb.co/8DX2NTJs/image.png" style="zoom:67%;" />

## 3.7 Directivas

Las directivas en Thymeleaf son atributos especiales en las etiquetas HTML que permiten manipular contenido de manera dinámica.

### 3.7.1`th:text`  

**Modifica el contenido de un elemento**

Este atributo reemplaza el contenido del elemento HTML con el valor proporcionado en la expresión.

🔹 **Ejemplo**: Mostrar el nombre de un usuario

📌 **Código Thymeleaf**

```
<p th:text="${usuario.nombre}">Nombre por defecto</p>
```

📌 **Controlador Spring Boot**

```java
@Controller
public class UsuarioController {
    @GetMapping("/usuario")
    public String usuario(Model model) {
        model.addAttribute("usuario", new Usuario("Javier"));
        return "usuario";
    }
}
```

📌 **Salida HTML Generada**

```java
<p>Javier</p>
```

------

### 3.7.2`th:utext` 

**Renderiza contenido HTML dentro de la plantilla**

A diferencia de `th:text`, este permite interpretar contenido HTML.

🔹 **Ejemplo**: Mostrar texto en negrita usando HTML

📌 **Código Thymeleaf**

```java
<p th:utext="${mensaje}"></p>
```

📌 **Controlador Spring Boot**

```java
@Controller
public class MensajeController {
    @GetMapping("/mensaje")
    public String mensaje(Model model) {
        model.addAttribute("mensaje", "<strong>¡Bienvenido a nuestra página!</strong>");
        return "mensaje";
    }
}
```

📌 **Salida HTML Generada**

```java
<p><strong>¡Bienvenido a nuestra página!</strong></p>
```

------

### 3.7.3`th:if` y `th:unless` 

**Condicionales en Thymeleaf**

Estos atributos permiten renderizar elementos HTML de acuerdo a una condición.

🔹 **Ejemplo**: Mostrar mensaje según si el usuario está autenticado

📌 **Código Thymeleaf**

```java
<p th:if="${usuario != null}">Bienvenido, <span th:text="${usuario.nombre}"></span></p>
<p th:unless="${usuario != null}">Por favor, inicia sesión.</p>
```

📌 **Controlador Spring Boot**

```java
@Controller
public class LoginController {
    @GetMapping("/home")
    public String home(Model model) {
        model.addAttribute("usuario", null); // Usuario no autenticado
        return "home";
    }
}
```

📌 **Salida HTML Generada**

```
<p>Por favor, inicia sesión.</p>
```

------

### 3.7.5`th:each` 

**Iterar sobre listas**

Este atributo permite recorrer listas o colecciones de objetos.

🔹 **Ejemplo**: Mostrar una lista de productos

📌 **Código Thymeleaf**

```java
<ul>
    <li th:each="producto : ${productos}">
        <span th:text="${producto.nombre}"></span> - $<span th:text="${producto.precio}"></span>
    </li>
</ul>
```

📌 **Controlador Spring Boot**

```java
@Controller
public class ProductoController {
    @GetMapping("/productos")
    public String productos(Model model) {
        List<Producto> lista = Arrays.asList(
            new Producto("Laptop", 1200),
            new Producto("Mouse", 50),
            new Producto("Teclado", 80)
        );
        model.addAttribute("productos", lista);
        return "productos";
    }
}
```

📌 **Salida HTML Generada**

```
<ul>
    <li>Laptop - $1200</li>
    <li>Mouse - $50</li>
    <li>Teclado - $80</li>
</ul>
```

------

### 3.7.5`th:href` y `th:src` 

**Manipulación de enlaces e imágenes**

Estos atributos permiten asignar dinámicamente URLs y rutas a imágenes.

🔹 **Ejemplo**: Enlace dinámico y carga de imagen

📌 **Código Thymeleaf**

```java
<a th:href="@{/perfil/{id}(id=${usuario.id})}">Ver Perfil</a>
<img th:src="@{/images/avatar.png}" alt="Avatar">
```

📌 **Salida HTML Generada**

```java
<a href="/perfil/5">Ver Perfil</a>
<img src="/images/avatar.png" alt="Avatar">
```

------

### 3.7.6`th:value` 

**Asignar valores en formularios**

Se usa para establecer valores en los inputs.

🔹 **Ejemplo**: Formulario con datos precargados

📌 **Código Thymeleaf**

```
htmlCopiarEditar<form>
    <input type="text" th:value="${usuario.nombre}" />
</form>
```

📌 **Salida HTML Generada**

```
htmlCopiarEditar<form>
    <input type="text" value="Carlos" />
</form>
```

------

### 3.7.7`th:switch` y `th:case` 

**Estructura `switch` en Thymeleaf**

Estos atributos permiten evaluar un valor y ejecutar diferentes opciones.

🔹 **Ejemplo**: Mostrar diferentes mensajes según el rol del usuario

📌 **Código Thymeleaf**

```
<div th:switch="${usuario.rol}">
    <p th:case="'admin'">Eres un administrador.</p>
    <p th:case="'usuario'">Eres un usuario registrado.</p>
    <p th:case="*">Rol desconocido.</p>
</div>
```

📌 **Salida HTML Generada** (si el usuario es admin)

```
<p>Eres un administrador.</p>
```

------

### 3.7.8.`th:replace` y `th:include` 

**Fragmentos reutilizables**

Permiten reutilizar partes de código HTML.

🔹 **Ejemplo**: Incluir un fragmento de cabecera

📌 **Fragmento `header.html`**

```java
<header th:fragment="cabecera">
    <h1>Mi Aplicación</h1>
</header>
```

📌 **Código Thymeleaf**

```java
<div th:replace="fragments/header :: cabecera"></div>
```

📌 **Salida HTML Generada**

```java
<header>
    <h1>Mi Aplicación</h1>
</header>
```

------

### 3.7.9.`th:classappend` y `th:styleappend` 

**Clases y estilos dinámicos**

Estos atributos permiten agregar clases o estilos dinámicamente.

🔹 **Ejemplo**: Resaltar usuarios activos con clases CSS

📌 **Código Thymeleaf**

```
<p th:classappend="${usuario.activo} ? 'text-success' : 'text-danger'">
    <span th:text="${usuario.nombre}"></span>
</p>
```

📌 **Salida HTML Generada** (si el usuario está activo)

```
<p class="text-success">Carlos</p>
```

## 3.8 Taller practico usando each y @ModelAttribute

1 Agregue el atributo email a la clase user que se encuentra en el paquete model.

```java
package com.usingthymeleaf.thymeleaf_app.models;

public class User {
    private String name;
    private String lastName;
    private String email;

    public User(String name, String lastName) {
        this.name = name;
        this.lastName = lastName;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getLastName() {
        return lastName;
    }
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    
}
```

2. En el controlador **indexController** agregue el metodo **usersModel** y el endpoint **list**

```java
package com.usingthymeleaf.thymeleaf_app.controllers;

import java.util.Arrays;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;

import com.usingthymeleaf.thymeleaf_app.models.User;

@Controller
public class indexController {
    @GetMapping("/")
    public String home(Model model) {
        User user = new User("Johlver","Pardo");
        model.addAttribute("title", "Desarrollando con Spring boot CreativeCode");
        model.addAttribute("user", user);
        return "index";
    }
    @GetMapping("/list")
    public String list(ModelMap model){

        model.addAttribute("title", "Listado de Usuarios");
        return "list";
    }
    @ModelAttribute("users")
    public List<User> usersModel() {
        List<User> users = Arrays.asList(
            new User("Pepa", "Gonzalez"),
            new User("Lalo", "Perez", "lalo@correo.com"),
            new User("Juanita", "Roe", "juana@correo.com"),
            new User("Andres", "Doe")
        );
        return users;
    }
}

```

3. Cree un nuevo documento html en templates y llamelo list.html y agregue el siguiente codigo

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title th:text="${title}">Document</title>
</head>
<body>
    <h1 th:text="${title}"></h1>
    <div th:if="${users.isEmpty()}">No se encontro ningun registro....</div>
    <table th:if="${not (users.isEmpty())}">
        <thead>
            <tr>
                <th>Nombre de usuario</th>
                <th>Apellidos de usuario</th>
                <th>Correo electronico</th>
            </tr>
        </thead>
        <tbody>
            <tr th:each="user: ${users}">
                <td th:text="${user.name}"></td>
                <td th:text="${user.lastName}"></td>
                <td th:if="${user.email}" th:text="${user.email}"></td>
                <td th:if="${not (user.email != null)}" th:text="${'Email no disponible'}"></td>
            </tr>
        </tbody>
    </table>
</body>
</html>
```



# 4. SpringBoot Intermedio

## 4.1 Modificar el puerto por defecto

Cuando ejecutamos una aplicación Spring Boot, por defecto, el servidor embebido (Tomcat, Jetty o Undertow) se inicia en el puerto **8080**. Sin embargo, en muchos casos es necesario cambiar este puerto para evitar conflictos con otras aplicaciones, ajustarlo a los estándares de un entorno de despliegue o cumplir con requisitos específicos del sistema.

Spring Boot ofrece múltiples formas de modificar el puerto del servidor, ya sea mediante archivos de configuración (`application.properties` o `application.yml`), argumentos de línea de comandos o configuración programática. Este capítulo explorará cada una de estas opciones, proporcionando ejemplos prácticos para personalizar el puerto de tu aplicación de manera sencilla y efectiva.

Al finalizar este capítulo, serás capaz de:

- Cambiar el puerto del servidor usando **propiedades de configuración**.
- Modificar el puerto a través de **variables de entorno o argumentos de línea de comandos**.
- Configurar el puerto mediante **código Java** en una clase de configuración.

1️⃣ Cambiar el puerto en `application.properties` o `application.yml`

La forma más sencilla y recomendada para modificar el puerto del servidor en Spring Boot es configurarlo en los archivos de propiedades o YAML.

🔹 Usando `application.properties`

En el archivo `src/main/resources/application.properties`, agrega la siguiente línea:

```
server.port=9090
```

Esto hará que la aplicación se inicie en el puerto **9090** en lugar del puerto predeterminado **8080**.

🔹 Usando `application.yml`

Si prefieres usar YAML, agrega la siguiente configuración en `src/main/resources/application.yml`:

```
server:
  port: 9090
```

Ambas opciones lograrán el mismo resultado y se recomienda utilizar este método porque es simple, claro y fácil de mantener.

------

2️⃣ Cambiar el puerto con argumentos de línea de comandos

Si necesitas cambiar el puerto de forma dinámica sin modificar el código fuente, puedes hacerlo al ejecutar la aplicación con un argumento en la línea de comandos.

Ejecuta tu aplicación con:

```
mvn spring-boot:run -Dspring-boot.run.arguments=--server.port=9090
```

O si ejecutas el JAR directamente:

```
java -jar mi-aplicacion.jar --server.port=9090
```

Este método es útil cuando despliegas tu aplicación en diferentes entornos y necesitas definir el puerto en tiempo de ejecución.

------

3️⃣ Cambiar el puerto con variables de entorno

Otra alternativa flexible es usar variables de entorno. En Linux y macOS, puedes establecer la variable antes de ejecutar la aplicación:

```
export SERVER_PORT=9090
mvn spring-boot:run
```

En Windows (cmd):

```
set SERVER_PORT=9090
mvn spring-boot:run
```

O si usas PowerShell:

```
$env:SERVER_PORT=9090
mvn spring-boot:run
```

Este método es útil cuando trabajas en **contenedores Docker** o despliegues en la nube.

------

4️⃣ Cambiar el puerto de forma programática en una clase de configuración

Si necesitas un mayor control sobre la configuración del puerto, puedes definirlo en una **clase Java** dentro del código de la aplicación.

```java
public static void main(String[] args) {
    SpringApplication app = new SpringApplication(
        BetplayAppApplication.class);
    app.setDefaultProperties(Collections.singletonMap("server.port", "8085"));
    app.run(args);
    //SpringApplication.run(BetplayAppApplication.class, args);
}

@Bean
WebMvcConfigurer corsConfigurer() {
    return new WebMvcConfigurer() {
        @SuppressWarnings("null")
        @Override
        public void addCorsMappings(CorsRegistry registry) {
            registry.addMapping("/**").allowedOrigins("http://localhost:4200","http://localhost",
            "http://localhost:8080").allowedMethods("*").allowedHeaders("*");
        }
    };
}
```

https://gist.github.com/21faa9fb918ececaa7e3e4d9a816975d.git

## 4.2 DTO

En el desarrollo de aplicaciones con **Spring Boot**, es fundamental mantener una separación clara entre la lógica de negocio y la exposición de datos. **DTO (Data Transfer Object)** es un patrón de diseño que nos permite lograr esta separación al actuar como una capa intermedia entre la entidad de base de datos y la respuesta que se envía al cliente.

Los **DTOs** se utilizan principalmente para:

✅ **Evitar exponer directamente las entidades del modelo de datos** en las respuestas de la API.
✅ **Reducir el tamaño de la carga de datos** en las respuestas, incluyendo solo la información necesaria.
✅ **Validar y transformar datos** antes de enviarlos al cliente o antes de guardarlos en la base de datos.
✅ **Asegurar el cumplimiento de principios SOLID**, específicamente el principio de **Responsabilidad Única (SRP)**.

En este capítulo, exploraremos cómo implementar DTOs en Spring Boot, abordando:

1️⃣ **Cómo definir un DTO** y cuándo utilizarlo.
2️⃣ **Cómo mapear entidades a DTOs** con herramientas como `ModelMapper` o `MapStruct`.
3️⃣ **Cómo integrar DTOs en controladores y servicios**.
4️⃣ **Buenas prácticas** en el uso de DTOs para garantizar un código limpio y mantenible.

Los DTO (**Objetos de Transferencia de Datos** por sus siglas en español) son un patrón de diseño común en programación utilizado para transferir datos entre diferentes capas de una aplicación. Son especialmente útiles en arquitecturas como la de Capas (Layered Architecture) o la arquitectura Limpia (Clean Architecture).

**Ejercicio:** Usando DTO exponer de la clase User la propiedad name y lastName.

1. Se crea un nuevo paquete llamado Dtos en el paquete Models. El identificador de la clase se recomieda agregarle las iniciales Dto al final del identificador de la clas ej. userDto.

   ![](https://i.ibb.co/ccGtgvt2/image.png)

2. Defina las propiedades que desea exponer con el Dto; genere los metodos getter y setter. Para el ejemplo se va a exponer una propiedad llamada titulo y la clase user(name,lastName y email)

   ```java
   package com.usingthymeleaf.thymeleaf_app.models.Dtos;
   
   import com.usingthymeleaf.thymeleaf_app.models.User;
   
   public class UserDto {
       private String title;
       private User user;
       public String getTitle() {
           return title;
       }
       public void setTitle(String title) {
           this.title = title;
       }
       public User getUser() {
           return user;
       }
       public void setUser(User user) {
           this.user = user;
       }
   }
   
   ```

3. Agregue el siguiente fragmento de codigo al controlador llamado userController.

   ```java
   @GetMapping("/veruser")
   public UserDto geUserDto() {
       UserDto userDto = new UserDto();
       User user = new User("Johlver","Pardo","userdemo@gmail.com");
       userDto.setTitle("Usuario registrado");
       userDto.setUser(user);
       return userDto;
   }
   ```

4. Ejecute el proyecto haciendo uso del **Dashboard** de Spring desde Visual Studio Code.

   <img src="https://i.ibb.co/KjGdPG3P/image.png" style="zoom:67%;" />

   <img src="https://i.ibb.co/Q7KdfMn5/image.png" style="zoom:67%;" />

   ![](https://i.ibb.co/Vfb46R4/image.png)

   



Modifique la clase UserRestController.....

<img src="Manuales\imgspring\Screenshot_71.png" alt="Screenshot_71" style="zoom:80%;" />

1. 

   ![Screenshot_73](Manuales\imgspring\Screenshot_73.png)
   
   
   
   Usando la clase La clase Arrays; La clase `Arrays` en Java es parte del paquete `java.util` y proporciona una colección de métodos estáticos para trabajar con arrays de Java. Estos métodos facilitan la manipulación de arrays, como ordenarlos, buscar elementos, comparar arrays y copiarlos. La clase `Arrays` no requiere que se cree un objeto, ya que todos sus métodos son estáticos.
   
   **Funcionalidades clave de la clase Arrays:**
   
   **1. Ordenar arrays:**
   
   - `Arrays.sort(array)`: Ordena un array de enteros, flotantes, caracteres o Strings.
   - `Arrays.sort(array, comparator)`: Ordena un array utilizando un comparador personalizado.
   
   **2. Buscar elementos:**
   
   - `Arrays.binarySearch(array, value)`: Busca un valor específico en un array ordenado usando la búsqueda binaria.
   - `Arrays.indexOf(array, value)`: Devuelve el índice de la primera aparición de un valor en un array.
   - `Arrays.lastIndexOf(array, value)`: Devuelve el índice de la última aparición de un valor en un array.
   
   **3. Comparar arrays:**
   
   - `Arrays.equals(array1, array2)`: Comprueba si dos arrays son iguales.
   - `Arrays.compare(array1, array2)`: Compara dos arrays lexicográficamente y devuelve un entero que indica la diferencia.

   **4. Copiar arrays:**
   
   - `Arrays.copyOf(array, length)`: Crea una nueva copia de un array con la longitud especificada.
   - `Arrays.copyOfRange(array, fromIndex, toIndex)`: Crea una nueva copia de un subconjunto de un array.

   **5. Rellenar arrays:**
   
   - `Arrays.fill(array, value)`: Rellena un array con un valor específico.
   
   **6. Convertir arrays a otras estructuras:**

   - `Arrays.asList(array)`: Convierte un array en una lista inmutable.
   - `Arrays.toString(array)`: Devuelve una cadena que representa el contenido de un array.
   
   Cree un nuevo endpoint llamado list-array-details e inserte el siguiente código:

   ```java
       @GetMapping("/list-array-details")
       public List<User> listarraydetails(){
           User user = new User("Juan","Perez");
           User userA = new User("Camilo","Hernandez");
           User userB = new User("Martha","Estupiñan");
           List<User> lstUsers = Arrays.asList(user,userA,userB);
           return lstUsers;
       }
   ```
   
   ![Screenshot_75](Manuales\imgspring\Screenshot_75.png)
   
   # Directiva if en thymeleaf
   
   En Thymeleaf, la directiva `th:if` se utiliza para incluir condicionalmente un bloque de contenido HTML en función de una expresión booleana. Es una herramienta útil para controlar lo que se muestra en tu plantilla en función de los datos disponibles en el contexto.
   
   Sintaxis:
   
   ```html
   <th:block th:if="${condición}">
     </th:block>
   ```
   
   Modifique la clase User y agregue un nuevo atributo llamado email y cree los métodos getter y seteer para email.
   
   ```java
   public class User {
       private String nombre;
       private String apellido;
       private String email;
       
       //Constructor de clase
       public User(String nombre, String apellido) {
           this.nombre = nombre;
           this.apellido = apellido;
       }
       public String getNombre() {
           return nombre;
       }
       public void setNombre(String nombre) {
           this.nombre = nombre;
       }
       public String getApellido() {
           return apellido;
       }
       public void setApellido(String apellido) {
           this.apellido = apellido;
       }
       public String getEmail() {
           return email;
       }
       public void setEmail(String email) {
           this.email = email;
       }
       
   }
   ```
   
   Modifique la plantilla html details.
   
   ```html
   <!DOCTYPE html>
   <html lang="en" xmlns:th="http://www.thymeleaf.org">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title th:text="${title}">Document</title>
   </head>
   <body>
       <ul>
           <li th:text="${user.nombre}"></li>
           <li th:text="${user.apellido}"></li>
           <li th:text="${user.email}"></li>
       </ul>
   </body>
   </html>
   ```
   
   Cuando se renderiza se puede observar que se crea un item vacío en la lista porque el email es nuill para los datos del objeto user.
   
   ![Screenshot_76](Manuales\imgspring\Screenshot_76.png)
   
   Para dar solución a este inconveniente se implementa la directiva if en la plantilla html.
   
   ```html
   <!DOCTYPE html>
   <html lang="en" xmlns:th="http://www.thymeleaf.org">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title th:text="${title}">Document</title>
   </head>
   <body>
       <ul>
           <li th:text="${user.nombre}"></li>
           <li th:text="${user.apellido}"></li>
           <li th:if="${user.email}" th:text="${user.email}"></li>
           <li th:if="${user.email == null}" th:text="${'el usuario no tiene email'}"></li>
       </ul>
   </body>
   </html>
   ```
   
   ![Screenshot_77](https://i.ibb.co/DkZ80bk/Screenshot-77.png)
   
   Modifique la clase UserController y asigne un email al usuario que se encuentra hardCodeado.
   
   ```java
       @GetMapping("/details")
       public String details(Model model){
           User user = new User("Johlver","Pardo");
           user.setEmail("jjpardo2002@gmail.com"); //Email del usuario
           model.addAttribute("title", "Desarrollando con Spring boot CreativeCode");
           model.addAttribute("user", user);
           return "details";
       }
   ```
   
   ![Screenshot_78](Manuales\imgspring\Screenshot_78.png)
   
   ## Mostrando Información de una lista en el view
   
   1. Cree una plantilla html llamada list.html
   
      ![Screenshot_80](Manuales\imgspring\Screenshot_80.png)
   
   2. En clase UserController cree un nuevo metodo llamado list.
   
      ```java
          @GetMapping("/list")
          public String list(ModelMap model){
              List<User> users = new ArrayList<>();
              model.addAttribute("title", "Listado de Usuarios");
              model.addAttribute("users", users);
              return "list";
          }
      ```

      <img src="Manuales\imgspring\Screenshot_81.png" alt="Screenshot_81" style="zoom:80%;" />

      3. Modifique nuevamente el template list.

      ```html
      <!DOCTYPE html>
      <html lang="en" xmlns:th="http://www.thymeleaf.org">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title th:text="${title}">Document</title>
      </head>
      <body>
          <h1 th:text="${title}"></h1>
          <div th:if="${users.size == 0}">No se encontro ningun registro....</div>
      </body>
      </html>
      ```
   
      4. Agregue informacion a la lista usando el handler Arrays.
   
      ```java
          @GetMapping("/list")
          public String list(ModelMap model){
              List<User> users = Arrays.asList(
                  new User("Carlos", "Perez"),
                  new User("Martha","Sanchez"),
                  new User("Vicente","Camargo")
              );
              model.addAttribute("title", "Listado de Usuarios");
              model.addAttribute("users", users);
              return "list";
          }
      ```

## 4.3 @RequestParam

La anotación `@RequestParam` en Spring MVC se utiliza para extraer parámetros de la solicitud HTTP y vincularlos a los parámetros de un método en un controlador. Específicamente, permite acceder a los parámetros de la cadena de consulta, los datos del formulario y otras partes de la solicitud.

Usos y Beneficios de `@RequestParam`

### **4.3.1 Extracción de Parámetros de la Cadena de Consulta**:

- `@RequestParam` se utiliza comúnmente para obtener valores de la cadena de consulta en las URL.

```java
@GetMapping("/greeting")
public String greeting(@RequestParam(name = "name", defaultValue = "World") String name, Model model) {
    model.addAttribute("name", name);
    return "greeting";
}

```

### **4.3.2 Especificar el Nombre del Parámetro**:

- Puede especificar el nombre del parámetro que esperas en la solicitud HTTP utilizando el atributo `name` o `value`.

```java
@GetMapping("/search")
public String search(@RequestParam("query") String query, Model model) {
    model.addAttribute("query", query);
    return "searchResults";
}

```

### **4.3.3 Valores Predeterminados**:

- Se puede  proporcionar un valor predeterminado si el parámetro no está presente en la solicitud utilizando el atributo `defaultValue`.

```java
@GetMapping("/greeting")
public String greeting(@RequestParam(name = "name", defaultValue = "World") String name, Model model) {
    model.addAttribute("name", name);
    return "greeting";
}

```

Si el parámetro `name` no está presente en la solicitud, se utilizará el valor `"World"` como valor predeterminado.

### **4.3.4 Parámetros Obligatorios y Opcionales**:

- Por defecto, los parámetros marcados con `@RequestParam` son obligatorios. Se pueden hacer  opcionales configurando `required = false`.

```java
@GetMapping("/user")
public String user(@RequestParam(name = "id", required = false) String id, Model model) {
    model.addAttribute("id", id);
    return "userProfile";
}
```

## Ejercicio

Cree un nuevo controller en el Paquete Controller.

| <img src="Manuales\imgspring\news\02.png" alt="02" style="zoom: 67%;" /> | <img src="Manuales\imgspring\news\03.png" alt="03" style="zoom:67%;" /> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="Manuales\imgspring\news\04.png" alt="04" style="zoom:67%;" /> | <img src="Manuales\imgspring\news\05.png" alt="05" style="zoom:67%;" /> |

Cree una clase DTO llamada ParamsDto

```java
package com.breakline.farmville.farmville.models.dto;

public class ParamsDto {
    private String message;

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    
}
```

Agregue el siguiente codigo en la clase RequestParamsController

```java
package com.breakline.farmville.farmville.controllers;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.breakline.farmville.farmville.models.dto.ParamsDto;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;


@RestController
@RequestMapping("api/params")
public class RequestParamsController {
    @GetMapping("/foo")
    public ParamsDto foot(@RequestParam(required = false, defaultValue = "Hola Mundo") String message) {

        ParamsDto param = new ParamsDto();
        param.setMessage(message);
        return param;

    }
    
}
```

### Probando solución

<img src="Manuales\imgspring\news\06.png" alt="06" style="zoom:80%;" />

<img src="Manuales\imgspring\news\07.png" alt="07" style="zoom:80%;" />

## Pasando Multiples Parametros

```java
@GetMapping("/bar")
public ParamsDto bar(@RequestParam String text, @RequestParam Integer code) {
    ParamsDto params = new ParamsDto();
    params.setMessage(text);
    params.setCode(code);
    return params;
}
```

**`@GetMapping("/bar")`**:

- Esta anotación indica que el método `bar` responderá a solicitudes HTTP GET en la ruta `/bar`.

**Método `bar`**:

- El método `bar` está definido para aceptar dos parámetros de solicitud: `text` y `code`, que se obtienen usando `@RequestParam`.
- Retorna un objeto de tipo `ParamsDto`.

**Parámetros del Método**:

- **`@RequestParam String text`**: Este parámetro captura el valor del parámetro de solicitud `text` y lo vincula a la variable `text`.
- **`@RequestParam Integer code`**: Este parámetro captura el valor del parámetro de solicitud `code` y lo vincula a la variable `code`.

**Creación y Configuración de `ParamDto`**:

- Se crea una instancia de `ParamDto`.
- Se configuran sus propiedades utilizando los valores de los parámetros `text` y `code` obtenidos de la solicitud.
- Se retorna el objeto `ParamsDto` configurado.

```java
package com.breakline.farmville.farmville.controllers;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.breakline.farmville.farmville.models.dto.ParamsDto;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@RestController
@RequestMapping("api/params")
public class RequestParamsController {
    @GetMapping("/foo")
    public ParamsDto foot(@RequestParam(required = false, defaultValue = "Hola Mundo") String message) {

        ParamsDto param = new ParamsDto();
        param.setMessage(message);
        return param;

    }

    @GetMapping("/bar")
    public ParamsDto bar(@RequestParam String text, @RequestParam Integer code) {
        ParamsDto params = new ParamsDto();
        params.setMessage(text);
        params.setCode(code);
        return params;
    }

}

```

<img src="Manuales\imgspring\news\08.png" alt="08" style="zoom:67%;" />

## Principales Usos y Beneficios de `HttpServletRequest`

La clase `HttpServletRequest` en Java es parte de la API Servlet y proporciona una interfaz que permite a los desarrolladores acceder a la información de las solicitudes HTTP. Específicamente, esta clase se utiliza en aplicaciones web basadas en servlets y frameworks como Spring para acceder a detalles de la solicitud HTTP entrante.

**Acceso a Parámetros de la Solicitud**:

- Permite obtener parámetros enviados en la URL (cadena de consulta) o en el cuerpo de la solicitud (en el caso de POST).

  ```java
  String paramValue = request.getParameter("paramName");
  ```

**Acceso a Atributos de la Solicitud**:

- Permite establecer y obtener atributos dentro del alcance de la solicitud.

```java
request.setAttribute("attributeName", attributeValue);
Object value = request.getAttribute("attributeName");

```

**Acceso a Información del Cliente**:

- Permite obtener información sobre el cliente que realiza la solicitud, como la dirección IP.

```java
String ipAddress = request.getRemoteAddr();

```

**Gestión de Cabeceras HTTP**:

- Permite acceder a las cabeceras HTTP enviadas por el cliente.

```java
String userAgent = request.getHeader("User-Agent");

```

**Gestión de Sesiones**:

- Permite obtener y gestionar sesiones HTTP.

```java
HttpSession session = request.getSession();
session.setAttribute("sessionAttributeName", value);

```

**Construcción de URLs y Contextos**:

- Permite obtener información sobre la URL de la solicitud y el contexto de la aplicación.

```java
String contextPath = request.getContextPath();

```

`HttpServletRequest` es una clase fundamental en las aplicaciones web Java, proporcionando un medio para interactuar con las solicitudes HTTP entrantes. Permite acceder a parámetros, cabeceras, atributos, información de sesión y otros detalles esenciales de la solicitud, lo que facilita la creación de aplicaciones web dinámicas y basadas en datos.

Ejemplo : Escribir el siguiente código en la clase RequestParamsController

```java
    @GetMapping("/request")
    public ParamMixDto request(HttpServletRequest request) {
        ParamMixDto params = new ParamMixDto();
        params.setCode(Integer.parseInt(request.getParameter("code")));
        params.setMessage(request.getParameter("message"));
        return params;
    }
```

Probando en el navegador

<img src="Manuales\imgspring\news\09.png" alt="09" style="zoom:67%;" />



El codigo anterior presenta una error al momento de pasar valores no validos; por ejemplo si se envia un texto en el codigo se dispara una excepcion de ejecución por tipo de datos. Para corregir este tipo de errores en tiempo de ejecución se recomienda usar un try..catch.

```java
    @GetMapping("/request")
    public ParamMixDto request(HttpServletRequest request) {
        Integer code = 0;
        try {
            code = Integer.parseInt(request.getParameter("code"));
        } catch (NumberFormatException e) {
            // TODO: handle exception
        }
        ParamMixDto params = new ParamMixDto();
        params.setCode(code);
        params.setMessage(request.getParameter("message"));
        return params;
    }
```

# @PathVariable

En Spring Boot, @PathVariable es una anotación utilizada para vincular valores de URL con métodos manejadores dentro de un controlador. La anotación ofrece una forma directa de vincular los parámetros de un método dentro de un controlador con una parte de la URL. La anotación se puede usar para pasar valores dinámicos en la URL a los métodos de los controladores.

## Ejemplo

```java
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetingController {

    @RequestMapping("/greeting/{name}")
    public String greeting(@PathVariable String name) {
        return "Hello, " + name + "!";
    }
}

```

En este ejemplo:

- La URL `http://localhost:8080/greeting/{name}` puede ser accedida con diferentes valores en lugar de `{name}`, como `http://localhost:8080/greeting/John`.
- El valor `{name}` en la URL se extrae y se pasa como parámetro al método `greeting`.

Si se requiere especificar el nombre del parámetro en el método y en la URL de manera explícita, puedes hacerlo de la siguiente manera:

```java
org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetingController {

    @RequestMapping("/greeting/{userName}")
    public String greeting(@PathVariable("userName") String name) {
        return "Hello, " + name + "!";
    }
}

```

Ejemplo:

Cree una nueva clase en el paquete controller. La clase se llamara PathVariableController

Agregue las anotaciones @ResController y @RequesMapping

<img src="Manuales\imgspring\news\10.png" alt="10" style="zoom:67%;" />

```java

```

Cree el endPoint llamado saludo

 <img src="Manuales\imgspring\news\11.png" alt="11" style="zoom:67%;" />

**`@GetMapping("/saludo/{message}")`**:

- **Propósito**: La anotación `@GetMapping` se usa para mapear solicitudes HTTP GET a métodos específicos en los controladores Spring.
- **Ruta**: `/saludo/{message}`. Aquí, `{message}` es una variable de ruta que se espera recibir en la solicitud.
- **Ejemplo de solicitud**: Si un cliente hace una solicitud GET a `http://localhost:8080/saludo/HelloWorld`, el segmento `HelloWorld` de la URL se vincula a la variable de ruta `message`.

**`public ParamsDto saludo(@PathVariable String message)`**:

- **Modificador de acceso**: `public`. El método es accesible desde cualquier lugar.
- **Tipo de retorno**: `ParamsDto`. El método devuelve un objeto de tipo `ParamsDto`.
- **Nombre del método**: `saludo`. Este es el nombre del método que se ejecutará cuando se haga una solicitud GET a la URL especificada.
- **Parámetro**: `@PathVariable String message`. La anotación `@PathVariable` indica que el valor del segmento `{message}` de la URL se pasará al parámetro `message` del método. En el ejemplo `http://localhost:8080/saludo/HelloWorld`, el valor `HelloWorld` se asignará a la variable `message`.

**Cuerpo del método**:

**`ParamsDto param = new ParamsDto();`**:

- Crea una nueva instancia de la clase `ParamsDto`.

**`param.setMessage(message);`**:

- Llama al método `setMessage` en el objeto `param` y establece su propiedad `message` con el valor del parámetro `message` recibido en la URL.

**`return param;`**:

- Retorna el objeto `ParamsDto` con la propiedad `message` establecida.

<img src="Manuales\imgspring\news\12.png" alt="12" style="zoom:67%;" />

## Pasando múltiples variables

<img src="Manuales\imgspring\news\13.png" alt="13" style="zoom:67%;" />

```java
    @GetMapping("/producto/{productname}/{id}")
    public Map<String,Object> getProduct(@PathVariable String productname,@PathVariable Long id ){
        Map<String,Object> jsonData = new HashMap<>();
        
        jsonData.put("product", productname);
        jsonData.put("id", id);

        return jsonData;
    }
```



# Enviar Json usando Post

![14](Manuales\imgspring\news\14.png)

```java
    @PostMapping("/createproduct")
    public User createproduct(@RequestBody User user){
        user.setNombre(user.getNombre().toUpperCase());
        return user;
    }
```

**`@PostMapping("/createproduct")`**:

- **Propósito**: La anotación `@PostMapping` se usa para mapear solicitudes HTTP POST a métodos específicos en los controladores Spring.
- **Ruta**: `/createproduct`. Este es el endpoint al que el cliente debe enviar la solicitud POST para que se ejecute este método.
- **Ejemplo de solicitud**: Si un cliente hace una solicitud POST a `http://localhost:8080/createproduct`, se ejecutará este método.

**Firma del método `public User createproduct(@RequestBody User user)`**:

- **Modificador de acceso**: `public`. El método es accesible desde cualquier lugar.
- **Tipo de retorno**: `User`. El método devuelve un objeto de tipo `User`.
- **Nombre del método**: `createproduct`. Este es el nombre del método que se ejecutará.
- **Parámetro**: `@RequestBody User user`. La anotación `@RequestBody` indica que el objeto `user` se debe poblar con los datos del cuerpo de la solicitud HTTP. Spring Boot automáticamente convierte el JSON del cuerpo de la solicitud a un objeto Java del tipo especificado (en este caso, `User`).

**`user.setNombre(user.getNombre().toUpperCase());`**:

- Obtiene el valor del campo `nombre` del objeto `user`, lo convierte a mayúsculas usando `toUpperCase()`, y vuelve a establecer este valor en el campo `nombre` del objeto `user`.

**`return user;`**:

- Retorna el objeto `user` modificado.

Este es solo un pequeño ejemplo de cómo aceptar HTTP POST dentro de un controlador de Spring Boot, cómo usar @RequestBody para atar implícitamente el cuerpo de la solicitud a un objeto Java, y cómo manipular el objeto y responder con el objeto en la respuesta. Esto es algo que se hace mucho al exponer una API RESTful para consumir datos estructurados y devolver datos estructurados.

## Usando Insomnia

1. Cree un nuevo folder

   <img src="Manuales\imgspring\news\15.png" alt="15" style="zoom:67%;" />

   2. Cree un nuevo request dentro de la carpeta creada

      <img src="Manuales\imgspring\news\16.png" alt="16" style="zoom:67%;" />

      3. En el nuevo request seleccione el método POST

         <img src="Manuales\imgspring\news\17.png" alt="17" style="zoom:67%;" />

         4. Escriba la URL del método creado en el controlador.

            <img src="Manuales\imgspring\news\18.png" alt="18" style="zoom:67%;" />

         5. Para enviar la información usando formato Json en insomnia siga los siguientes pasos

            1. Configure en la seccion Body la opcion JSON

               ![19](Manuales\imgspring\news\19.png)

            2. Escriba el objeto JSON contenedor de los datos. Tenga en cuenta que las llaves deben coincidir con el objeto que recibe la URL.

               ![20](Manuales\imgspring\news\20.png)

               <img src="Manuales\imgspring\news\21.png" alt="21" style="zoom:67%;" />

               <img src="Manuales\imgspring\news\22.png" alt="22" style="zoom:80%;" />

            Nota. La clase User debe tener un constructor vacio.

            <img src="Manuales\imgspring\news\23.png" alt="23" style="zoom:67%;" />

# @Value

La anotación @Value en Spring se utiliza para inyectar valores en los campos de una clase desde fuentes externas como propiedades de archivos, variables de entorno, argumentos de línea de comandos, etc. Esta es una de las funciones de Spring a través de la cual se puede realizar la inyección de dependencias y la configuración externa.

### Usos comunes de `@Value`

1. **Inyección de valores de propiedades**: Puedes inyectar valores definidos en archivos de propiedades.
2. **Inyección de variables de entorno**: Puedes inyectar valores de variables de entorno del sistema.
3. **Inyección de valores predeterminados**: Puedes especificar valores predeterminados que se usarán si no se encuentra el valor externo.

Ejemplo 1

1. En el archivo application.properties agregue los siguientes valores de prueba

```
app.name=FarmVille
app.version=2.1.0
app.message=Hola desde SpringBoot Niños
app.listwords=Cacao,Cafe,Algodon
app.listaroles=Administrador,Cliente,Financiero
```

2. En el controlador de PathVariableController agregue el siguiente codigo para acceder a las variables creadas.

```java
    @Value("${app.name}")
    private String name;
    @Value("${app.version}")
    private String version;
    @Value("${app.listwords}")
    private String[] listwords;
 	@Value("${app.listaroles}")
    private List<String> lstroles;
```

3. Cree un método GetMapping que permita retornar los valores de las variables

```java
    @GetMapping("/valores")
    public Map<String,Object> valores(){
        Map<String,Object> json = new HashMap<>();
        json.put("name", name);
        json.put("version",version);
        json.put("listwords",listwords);
        json.put("lstroles",lstroles)
        json.put("message",message);
        return json;
    }
```

Test

![24](Manuales\imgspring\news\36.png)

# Personalización file properties

El archivo de propiedades en Spring Boot (normalmente `application.properties` o `application.yml` si se usa YAML) se usa para ofrecer un enfoque coherente y más liviano para definir y actualizar los valores de configuración en una aplicación. Los archivos de propiedades permiten que la configuración de una aplicación se defina fuera del artefacto, lo cual es una buena práctica para actualizar la configuración de una aplicación sin cambiar el código fuente.

A continuación se creara un nuevo archivo de properties para separar los valores personalizados del archivo properties principal.

1. A nivel del paquete principal en resource haga clic en el (+)

​	<img src="Manuales\imgspring\news\25.png" alt="25" style="zoom:67%;" />

2. En la ventana de comando seleccionar file y agregar el nombre del archivo. Para fines de la guia se creara un archivo llamado values.properties

​	<img src="Manuales\imgspring\news\26.png" alt="26" style="zoom:67%;" />

<img src="Manuales\imgspring\news\27.png" alt="27" style="zoom:67%;" />

3. Corte los valores personalizados definidos en el archivo application.properties

​	<img src="Manuales\imgspring\news\28.png" alt="28" style="zoom:67%;" />

4. Pegue los valores en el archivo properties creado en el paso anterior.

   <img src="Manuales\imgspring\news\29.png" alt="29" style="zoom:67%;" />

5. Para que Spring reconozca el archivo properties creado por el desarrollador se debe inyectar en la clase principal usando la anotacion @PropertiesSource: **@PropertySource** en Spring se utiliza para definir la ubicación de uno o más archivos de propiedades para que las propiedades definidas en esos archivos puedan ser cargadas y puestas a disposición en el contexto de la aplicación, de modo que se puedan externalizar configuraciones y valores.	<img src="Manuales\imgspring\news\30.png" alt="30" style="zoom:67%;" />

Código ValuesConfig

```java
package com.breakline.farmville.farmville;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.context.annotation.PropertySources;

@Configuration
@PropertySources({
    @PropertySource(value="classpath:values.properties",encoding = "UTF-8")
})
public class ValuesConfig {

}
```



# Expresiones SpEL

Spring Expression Language (SpEL) es un potente lenguaje de expresión que se integra en el framework de Spring y permite evaluar expresiones de una manera similar a otros lenguajes de scripting. SpEL es muy flexible y se utiliza en una variedad de escenarios dentro de Spring, como la configuración de beans, la inyección de dependencias, la validación y la seguridad.

## Características de SpEL

1. **Acceso a propiedades**: Permite acceder a las propiedades de los objetos de una manera fácil.

```java
#person.name
```

2. **Invocación de métodos**: Permite llamar a métodos en los objetos.

```
#person.getName()
```

3. **Operadores**: Soporta operadores aritméticos (`+`, `-`, `*`, `/`), relacionales (`<`, `>`, `==`, `!=`), lógicos (`&&`, `||`, `!`) y otros.

```java
#a > #b
```

4. **Acceso a arrays, listas y mapas**: Permite acceder a elementos dentro de arrays, listas y mapas.

```
#list[0]
#map['key']
```

5. **Literales**: Soporta literales de números, cadenas, booleanos, y `null`.

```java
42
'Hello, World!'
true
null
```

6. **Plantillas de expresiones**: Permite incrustar expresiones dentro de cadenas.

```java
"Hello, #{#person.name}"
```

En el siguiente ejemplo se usa SpEL para construir un arreglo a partir de un split.

```java
 	@Value("#{'${app.listaroles}'.split(',')}")
    private List<String> customlstroles;
```

Script completo

```java
package com.breakline.farmville.farmville.controllers;

import org.springframework.web.bind.annotation.RestController;

import com.breakline.farmville.farmville.models.User;
import com.breakline.farmville.farmville.models.dto.ParamsDto;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.Map;
import java.util.HashMap;
import java.util.List;

@RestController
@RequestMapping("/api/demovar")

public class PathVariableController {

    @Value("${app.name}")
    private String name;
    @Value("${app.message}")
    private String message;
    @Value("${app.version}")
    private String version;
    @Value("${app.listwords}")
    private String[] listwords;
 	@Value("${app.listaroles}")
    private List<String> lstroles;
 	@Value("#{'${app.listaroles}'.split(',')}")
    private List<String> customlstroles;
 	@Value("#{'${app.listaroles}'.toUpperCase().split(',')}")
    private List<String> customlstrolesMayuscula;

    @GetMapping("/saludo/{message}")
    public ParamsDto saludo(@PathVariable String message) {
        ParamsDto param = new ParamsDto();
        param.setMessage(message);
        return param;
    }
    @GetMapping("/producto/{productname}/{id}")
    public Map<String,Object> getProduct(@PathVariable String productname,@PathVariable Long id ){
        Map<String,Object> jsonData = new HashMap<>();
        
        jsonData.put("product", productname);
        jsonData.put("id", id);

        return jsonData;
    }

    @PostMapping("/createproduct")
    public User createproduct(@RequestBody User user){
        user.setNombre(user.getNombre().toUpperCase());
        return user;
    }
    @GetMapping("/valores")
    public Map<String,Object> valores(){
        Map<String,Object> json = new HashMap<>();
        json.put("name", name);
        json.put("version",version);
        json.put("listwords",listwords);
        json.put("lstroles", lstroles);
        json.put("clstroles", customlstroles);
        json.put("clstrolesMayus", customlstrolesMayuscula);
        json.put("message",message);
        return json;
    }
}

```

![37](Manuales\imgspring\news\38.png)

## Anidamiento de objetos usando SpEL

Defina el valor con las propiedades en el archivo values.properties

```
app.inventory={code:'001',product:'Leche deslactosada',price:'2500'}
```

Código completo

```
app.name=FarmVille
app.version=2.1.0
app.message=Hola desde SpringBoot Niños
app.listwords=Cacao,Cafe,Algodon
app.listaroles=Administrador,Cliente,Financiero
app.inventory={code:'001',product:'Leche deslactosada',price:'2500'}

```

Codigo completo

```java
package com.breakline.farmville.farmville.controllers;

import org.springframework.web.bind.annotation.RestController;

import com.breakline.farmville.farmville.models.User;
import com.breakline.farmville.farmville.models.dto.ParamsDto;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.Map;
import java.util.HashMap;
import java.util.List;

@RestController
@RequestMapping("/api/demovar")

public class PathVariableController {

    @Value("${app.name}")
    private String name;
    @Value("${app.message}")
    private String message;
    @Value("${app.version}")
    private String version;
    @Value("${app.listwords}")
    private String[] listwords;
 	@Value("${app.listaroles}")
    private List<String> lstroles;
 	@Value("#{'${app.listaroles}'.split(',')}")
    private List<String> customlstroles;
 	@Value("#{'${app.listaroles}'.toUpperCase().split(',')}")
    private List<String> customlstrolesMayuscula;
    @Value("#{${app.inventory}}")
    private Map<String,Object> inventory;

    @GetMapping("/valores")
    public Map<String,Object> valores(){
        Map<String,Object> json = new HashMap<>();
        json.put("name", name);
        json.put("version",version);
        json.put("listwords",listwords);
        json.put("lstroles", lstroles);
        json.put("clstroles", customlstroles);
        json.put("clstrolesMayus", customlstrolesMayuscula);
        json.put("inventory", inventory);
        json.put("message",message);
        return json;
    }
}
```

Por ejemplo se desea calcular el total del valor del producto existente en el inventario.

```java
@Value("#{T(java.lang.Integer).parseInt(${app.inventory}['price']) * T(java.lang.Integer).parseInt(${app.inventory}['stock'])}")
private Long totalInv;
```

Ejemplo completo

```java
package com.breakline.farmville.farmville.controllers;

import org.springframework.web.bind.annotation.RestController;

import com.breakline.farmville.farmville.models.User;
import com.breakline.farmville.farmville.models.dto.ParamsDto;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.Map;
import java.util.HashMap;
import java.util.List;

@RestController
@RequestMapping("/api/demovar")

public class PathVariableController {

    @Value("${app.name}")
    private String name;
    @Value("${app.message}")
    private String message;
    @Value("${app.version}")
    private String version;
    @Value("${app.listwords}")
    private String[] listwords;
 	@Value("${app.listaroles}")
    private List<String> lstroles;
 	@Value("#{'${app.listaroles}'.split(',')}")
    private List<String> customlstroles;
 	@Value("#{'${app.listaroles}'.toUpperCase().split(',')}")
    private List<String> customlstrolesMayuscula;

    @Value("#{${app.inventory}}")
    private Map<String,Object> inventory;
    @Value("#{${app.inventory}.product}")
    private String producName;
    @Value("#{T(java.lang.Integer).parseInt(${app.inventory}['price']) * T(java.lang.Integer).parseInt(${app.inventory}['stock'])}")
    private Long totalInv;

    @GetMapping("/valores")
    public Map<String,Object> valores(){
        Map<String,Object> json = new HashMap<>();
        json.put("name", name);
        json.put("version",version);
        json.put("listwords",listwords);
        json.put("lstroles", lstroles);
        json.put("clstroles", customlstroles);
        json.put("clstrolesMayus", customlstrolesMayuscula);
        json.put("inventory", inventory);
        json.put("valor", totalInv);
        json.put("message",message);
        return json;
    }
}

```

<img src="Manuales\imgspring\news\39.png" alt="39" style="zoom:67%;" />

## Trabajando con el entorno spring (Enviroment)

### @Autowired

La anotación `@Autowired` es una de las anotaciones más utilizadas en Spring Framework. Su propósito principal es permitir la inyección automática de dependencias, es decir, permitir que Spring resuelva y suministre automáticamente los beans (objetos gestionados por el contenedor de Spring) necesarios para satisfacer una dependencia en una clase.

### ¿Qué hace `@Autowired`?

1. **Inyección de Dependencias**: `@Autowired` permite a Spring inyectar automáticamente el bean apropiado en un campo, un método setter, o un constructor de una clase. Esto elimina la necesidad de inicializar manualmente las dependencias y facilita la gestión de beans.
2. **Resolución Automática**: Spring utiliza su mecanismo de resolución de beans para encontrar un bean compatible que coincida con el tipo del campo, parámetro del método o constructor donde se coloca `@Autowired`.

Ejemplo

```java
//Usando Env
@Autowired
private Environment env;
```

llamado

```java
json.put("message2",env.getProperty("app.message"));
```

Codigo completo

```java
package com.breakline.farmville.farmville.controllers;

import org.springframework.web.bind.annotation.RestController;

import com.breakline.farmville.farmville.models.User;
import com.breakline.farmville.farmville.models.dto.ParamsDto;

import org.springframework.web.bind.annotation.RequestMapping;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.Map;
import java.util.HashMap;
import java.util.List;

@RestController
@RequestMapping("/api/demovar")

public class PathVariableController {

    @Value("${app.name}")
    private String name;
    @Value("${app.message}")
    private String message;
    @Value("${app.version}")
    private String version;
    @Value("${app.listwords}")
    private String[] listwords;
 	@Value("${app.listaroles}")
    private List<String> lstroles;
 	@Value("#{'${app.listaroles}'.split(',')}")
    private List<String> customlstroles;
 	@Value("#{'${app.listaroles}'.toUpperCase().split(',')}")
    private List<String> customlstrolesMayuscula;

    @Value("#{${app.inventory}}")
    private Map<String,Object> inventory;
    @Value("#{${app.inventory}.product}")
    private String producName;
    @Value("#{T(java.lang.Integer).parseInt(${app.inventory}['price']) * T(java.lang.Integer).parseInt(${app.inventory}['stock'])}")
    private Long totalInv;

    //Usando Env
    @Autowired
    private Environment env;

    @GetMapping("/saludo/{message}")
    public ParamsDto saludo(@PathVariable String message) {
        ParamsDto param = new ParamsDto();
        param.setMessage(message);
        return param;
    }
    @GetMapping("/producto/{productname}/{id}")
    public Map<String,Object> getProduct(@PathVariable String productname,@PathVariable Long id ){
        Map<String,Object> jsonData = new HashMap<>();
        
        jsonData.put("product", productname);
        jsonData.put("id", id);

        return jsonData;
    }

    @PostMapping("/createproduct")
    public User createproduct(@RequestBody User user){
        user.setNombre(user.getNombre().toUpperCase());
        return user;
    }
    @GetMapping("/valores")
    public Map<String,Object> valores(){
        Map<String,Object> json = new HashMap<>();
        json.put("name", name);
        json.put("version",version);
        json.put("listwords",listwords);
        json.put("lstroles", lstroles);
        json.put("clstroles", customlstroles);
        json.put("clstrolesMayus", customlstrolesMayuscula);
        json.put("inventory", inventory);
        json.put("valor", totalInv);
        json.put("message",message);
        json.put("message2",env.getProperty("app.message"));
        String data = env.getProperty("app.inventory");
        JSONObject jsonObject = new JSONObject(data);
        json.put("price2",jsonObject.getLong("price"));
        return json;
    }
}

```



# Añadiendo Clases de configuración

Las clases de configuración en Spring son clases Java que se utilizan para definir la configuración y los beans de una aplicación Spring de manera programática en lugar de usar archivos XML. Estas clases están anotadas con `@Configuration` y pueden contener métodos anotados con `@Bean` que definen los beans que el contenedor de Spring debe gestionar.

## Características Principales de las Clases de Configuración

1. **Anotación `@Configuration`**:
   - Marca la clase como una clase de configuración.
   - Spring la trata como una fuente de definiciones de beans.
2. **Definición de Beans con `@Bean`**:
   - Dentro de una clase de configuración, los métodos anotados con `@Bean` son utilizados para registrar beans en el contexto de Spring.
   - Estos métodos devuelven instancias de objetos que serán gestionados como beans por Spring.
3. **Sustitución de XML**:
   - Las clases de configuración Java son una alternativa al archivo `applicationContext.xml` tradicional.
   - Facilitan la configuración y mantenimiento al utilizar la fortaleza del lenguaje Java.

## Como Crear clases de configuración

1. Las clases de configuración se crean a nivel de paquete principal. Ubique el paquete principal del proyecto y haga clic en el boton (+) y seleccione Class. El nombre de la clase depende del criterio del desarrollador. Por ejemplo (AppConfig, ValuesConfig)

   <img src="Manuales\imgspring\news\31.png" alt="31" style="zoom:67%;" /><img src="Manuales\imgspring\news\32.png" alt="32" style="zoom: 50%;" />

   Para el caso practico de la guia se usara como nombre ValuesConfig

2. Agregue la anotacion @Configuration a nivel de la clase.

   ```java
   package com.breakline.farmville.farmville;
   
   import org.springframework.context.annotation.Configuration;
   
   @Configuration
   public class ValuesConfig {
   
   }
   ```

3. Corte la anotacion @PropertySource que se encuentra en la clase principal y pequela en la clase de configuración creada previamente. 

   <img src="Manuales\imgspring\news\33.png" alt="33" style="zoom: 33%;" /><img src="Manuales\imgspring\news\34.png" alt="34" style="zoom:50%;" />

# Soporte caracteres especiales

```JAVA
package com.breakline.farmville.farmville;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.context.annotation.PropertySources;

@Configuration
@PropertySources({
    @PropertySource(value="classpath:values.properties",encoding = "UTF-8")
})
public class ValuesConfig {

}
```

<img src="Manuales\imgspring\news\35.png" alt="35" style="zoom:67%;" />

# Redirect y Forward

En Spring Boot, puedes realizar tanto un "Forward" como un "Redirect" en un controlador para redirigir o reenviar solicitudes a diferentes rutas. 

## Forward

El "Forward" se utiliza para reenviar una solicitud desde un controlador a otra URL dentro de la misma aplicación sin cambiar la URL en el navegador del cliente.

### Redirect

El "Redirect" se utiliza para redirigir a una nueva URL. Esto hace que el navegador del cliente cambie la URL y envíe una nueva solicitud HTTP(La información se pierde).

## Forward vs Redirect: 

La diferencia es que con el Forward se mantiene dentro de la misma petición http, y no pierdes los parámetros que tienes dentro del request, tampoco cambia la ruta url, ya que no hace un refresh (refresca la página), sino que despacha a otra acción del controlador pero sin recargar la página, mientras que el redirect cambia la ruta url, reinicia el request y refresca el navegador, además que todos los parámetros del request que teníamos antes del redirect se pierden en este nuevo request.

## Taller Practico

1. Cree un nuevo controller llamado HomeController y agregue la anotacion @Controller

   ```java
   package com.breakline.farmville.farmville.controllers;
   
   import org.springframework.stereotype.Controller;
   
   @Controller
   public class HomeController {
   
   }
   ```

2. Cree el método home que se utilizara como endPoint, al método agreguele la anotacion GetMapping 

   ```java
   package com.breakline.farmville.farmville.controllers;
   
   import org.springframework.stereotype.Controller;
   import org.springframework.web.bind.annotation.GetMapping;
   
   
   
   @Controller
   public class HomeController {
   
       @GetMapping({"","/","/home"})
       public String home() {
          
       }
   }
   ```

3. Aplique el redireccionamiento usando Redirect

   ```java
       @GetMapping({"","/","/home"})
       public String home() {
           return "redirect:/list";
       }
   ```

4. Modifique el codigo y aplique redireccionamiento con forward

   ```java
   @GetMapping({"","/","/home"})
   public String home() {
      return "forward:/list";
   }
   ```

   <img src="Manuales\imgspring\news\40.png" alt="40" style="zoom:67%;" />

# Enlaces thymeleaf

Sintaxis

```
<a th:href="@{/url}">xxx</a>
```

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title th:text="${title}">Document</title>
</head>
<body>
    <ul>
        <li th:text="${user.nombre}"></li>
        <li th:text="${user.apellido}"></li>
        <li th:if="${user.email}" th:text="${user.email}"></li>
        <li th:if="${user.email == null}" th:text="${'el usuario no tiene email'}"></li>
    </ul>
    <a th:href="@{/list}">Ver lista</a>
</body>
</html>
```

Pasando parametros

```html
<a th:href="@{/url?Parameto=valor}">xxx</a>
<a th:href="@{/url(Parameto=valor)}">xxx</a>
<a th:href="@{/url(Parameto=valor,param2=valor2)}">xxx</a>
```

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title th:text="${title}">Document</title>
</head>
<body>
    <a th:href="@{/list}">Ver lista</a>
    <a th:href="@{/api/params/foo?message=Reportando desde el enlace}">Envio variable version 1</a>
    <a th:href="@{/api/params/foo(message='Reportando desde el enlace V2')}">Envio variable version 2</a>
    <a th:href="@{/api/params/bar(text='Reportando desde el enlace V3',code=586)}">Envio variable version 3</a>

</body>
</body>
</html>
```

# Despliegue aplicacion

1. Abrir el terminal del sistema operativo donde se encuentre trabajando. Puede usar tambien la terminal de visual studio code.

2. Ubicarse en la carpeta del proyecto que se va a desplegar.

3. Listar el contenido de la carpeta del proyecto con el comando ls si esta trabajando con  bash

   <img src="Manuales\imgspring\news\41.png" alt="41" style="zoom:80%;" />

4. Ejecute el comando ./mvnw clean package

   <img src="Manuales\imgspring\news\42.png" alt="42" style="zoom:80%;" />

5. Para verificar la generación del jar ubique la carpeta target.

   <img src="Manuales\imgspring\news\43.png" alt="43" style="zoom:67%;" />

6. Ejecute el comando

   ```
   java -jar NombreDelJar
   ```

   para ejecutar el empaquetado. El comando se debe ejecutar desde la carpeta target

   ![44](Manuales\imgspring\news\44.png)

   <img src="Manuales\imgspring\news\45.png" alt="45" style="zoom:50%;" />

   ![46](Manuales\imgspring\news\46.png)

​	Usando Powershell

​	<img src="Manuales\imgspring\news\47.png" alt="47" style="zoom:50%;" />

# Inyección de dependencias(IoC)

<img src="Manuales\imgspring\news\61.png" alt="61" style="zoom: 50%;" />

<img src="Manuales\imgspring\news\62.png" alt="62" style="zoom: 50%;" />

<img src="Manuales\imgspring\news\63.png" alt="63" style="zoom:50%;" />

<img src="Manuales\imgspring\news\64.png" alt="64" style="zoom: 50%;" />

<img src="Manuales\imgspring\news\65.png" alt="65" style="zoom:50%;" />

<img src="Manuales\imgspring\news\66.png" alt="66" style="zoom:50%;" />

<img src="Manuales\imgspring\news\67.png" alt="67" style="zoom:50%;" />

<img src="Manuales\imgspring\news\68.png" alt="68" style="zoom:50%;" />



Para esta nueva sección se generara un nuevo proyecto. En la creacion del proyecto seleccionar la version 3.3.2 de Spring

Para el caso del taller practico el proyecto se llamara <img src="Manuales\imgspring\news\48.png" alt="48" style="zoom: 50%;" />

El nombre del Artefacto para el caso practico : app-di

Agregar las siguientes dependencias:

![50](Manuales\imgspring\news\50.png)

Cree los paquetes controllers,models,repositories y services. Recuerde que estos paquetes se deben crear partiendo del paquete base.

<img src="Manuales\imgspring\news\51.png" alt="51" style="zoom:50%;" />

Cree una clase llamada Product en el paquete models. Usando POJO

POJO es un acrónimo de "Plain Old Java Object" (Objeto Java Antiguo y Simple). En términos simples, un POJO es una clase Java que no está sujeta a ninguna restricción especial aparte de las impuestas por el lenguaje Java. Es decir, no requiere que la clase implemente interfaces específicas, extienda clases predeterminadas o siga patrones particulares más allá de lo que Java estándar permite.

### Características de un POJO

1. **Simplicidad**: Un POJO es simplemente una clase Java con atributos, constructores, métodos getter y setter, y posiblemente algunos métodos adicionales para la lógica de negocio.
2. **Independencia de Frameworks**: No depende de frameworks específicos. No implementa interfaces ni extiende clases proporcionadas por frameworks de terceros.
3. **Ausencia de Anotaciones**: No requiere el uso de anotaciones especiales, aunque en la práctica moderna a veces se les añaden anotaciones para integrarse mejor con frameworks como Spring o JPA.
4. **Encapsulamiento**: Los atributos de un POJO generalmente son privados y se accede a ellos a través de métodos getter y setter.

<img src="Manuales\imgspring\news\52.png" alt="52" style="zoom: 80%;" />

Cree la clase repositorio en el paquete repositories.

## Que son los repositorios

En el contexto de desarrollo de aplicaciones con Spring Boot y JPA, un repositorio es una interfaz que proporciona mecanismos para realizar operaciones de persistencia y recuperación de datos desde una base de datos. En términos más simples, un repositorio se utiliza para interactuar con la base de datos.

### ¿Para qué sirve un repositorio?

1. **CRUD Operations**: Permite realizar operaciones básicas de creación, lectura, actualización y eliminación (Create, Read, Update, Delete) sobre las entidades de la base de datos.
2. **Abstracción del Acceso a Datos**: Proporciona una capa de abstracción que separa la lógica de negocio de la lógica de acceso a datos, facilitando el mantenimiento y la evolución del código.
3. **Consultas Personalizadas**: Además de las operaciones CRUD, los repositorios pueden definir consultas personalizadas utilizando el lenguaje de métodos de consulta de Spring Data JPA.
4. **Soporte para Paginación y Ordenación**: Ofrecen métodos integrados para paginar y ordenar los resultados de las consultas.

<img src="Manuales\imgspring\news\55.png" alt="55" style="zoom: 80%;" />

Cree la clase service en el paquete service.

## Que es un service

En el contexto del desarrollo de aplicaciones con Spring, un "service" (servicio) es una clase que contiene la lógica de negocio de la aplicación. Los servicios se utilizan para encapsular esta lógica, separándola de la capa de controladores y la capa de acceso a datos, lo que resulta en un diseño más limpio y fácil de mantener.

### Funciones de un Service

1. **Encapsulamiento de la Lógica de Negocio**: La principal función de un servicio es encapsular la lógica de negocio. Esto significa que cualquier operación que no sea directamente relacionada con la presentación de datos o con el acceso a la base de datos debería estar en la capa de servicios.
2. **Reutilización**: Al centralizar la lógica de negocio en servicios, esta lógica puede ser reutilizada por diferentes partes de la aplicación.
3. **Facilitar las Pruebas**: Al separar la lógica de negocio en servicios, es más fácil crear pruebas unitarias para esta lógica sin necesidad de involucrar la capa de presentación o la de acceso a datos.
4. **Desacoplamiento**: Los servicios ayudan a desacoplar diferentes partes de la aplicación, facilitando el mantenimiento y la evolución del código.

<img src="Manuales\imgspring\news\56.png" alt="56" style="zoom: 80%;" />

Cree la clase controller llamada BaseController.

## Que es un controller

En el contexto del desarrollo de aplicaciones con Spring, un "controller" (controlador) es una clase que gestiona las solicitudes HTTP entrantes y devuelve las respuestas apropiadas. Los controladores son una parte fundamental del patrón arquitectónico MVC (Modelo-Vista-Controlador) y se encargan de coordinar la interacción entre la vista (la presentación) y el modelo (los datos y la lógica de negocio).

### Funciones de un Controller

1. **Gestión de Solicitudes HTTP**: Los controladores manejan las solicitudes HTTP (GET, POST, PUT, DELETE, etc.) que llegan al servidor y determinan cómo se deben procesar.
2. **Delegación de Tareas**: Los controladores delegan tareas a los servicios, que contienen la lógica de negocio, y a los repositorios, que gestionan el acceso a los datos.
3. **Construcción de Respuestas**: Los controladores crean y devuelven las respuestas HTTP apropiadas a los clientes, que pueden incluir datos en formato JSON, vistas HTML, códigos de estado HTTP, entre otros.
4. **Enrutamiento**: Definen rutas o endpoints que los clientes pueden utilizar para interactuar con la aplicación.

<img src="Manuales\imgspring\news\58.png" alt="58" style="zoom: 80%;" />

# Principio de inmutabilidad

El principio de inmutabilidad es un concepto fundamental en programación, especialmente en lenguajes de programación orientados a objetos y funcionales. Un objeto es considerado inmutable si, una vez creado, su estado no puede ser modificado. En otras palabras, todos sus atributos son finales y no pueden ser cambiados después de la creación del objeto.

### Beneficios de la Inmutabilidad

1. **Simplicidad**: Los objetos inmutables son más fáciles de entender y razonar, ya que su estado no cambia una vez que han sido creados.
2. **Seguridad en Hilos (Thread Safety)**: Los objetos inmutables son inherentemente seguros en entornos concurrentes, ya que no hay riesgo de que su estado sea modificado por múltiples hilos simultáneamente.
3. **Facilita la Depuración y Pruebas**: Dado que el estado de un objeto inmutable no cambia, es más fácil rastrear y depurar errores. También simplifica las pruebas unitarias.
4. **Caché y Optimización**: Los objetos inmutables pueden ser reutilizados y compartidos sin riesgo de modificación, lo que permite optimizaciones como el almacenamiento en caché.

```java
package com.di.app.app_di.services;

import java.util.List;
import java.util.stream.Collectors;

import com.di.app.app_di.models.Product;
import com.di.app.app_di.repositories.ProductRepository;

public class ProductService {

    private ProductRepository repositoryProduct = new ProductRepository();

    public List<Product> findAll(){
        return repositoryProduct.findAll().stream().map(p ->{
            Double priceImp = p.getPrice() * 1.45d;
            Product newProduct = new Product(p.getId(), p.getName(), priceImp.longValue());
            // p.setPrice(priceImp.longValue());
            return newProduct;
        }).collect(Collectors.toList());
    }

    public Product findById(Long id){
        return repositoryProduct.findById(id);        
    }
}
```

Forma recomendada:

Implementar Clonable en la clase Product para el caso de la guia.

<img src="Manuales\imgspring\news\59.png" alt="59" style="zoom: 67%;" />

Sobreescribir el método clone. Para sobreecribir el metodo haga clic derecho en un espacio vacio de la clase y seleccione la opción Source Action>Override/Implements Method y seleccione el metodo clone de la lista y haga clic en aceptar.

<img src="Manuales\imgspring\news\60.png" alt="60" style="zoom:67%;" />

Codigo completo:

```java
package com.di.app.app_di.models;

public class Product implements Cloneable {
    private Long id;
    private String name;
    private Long price;
    public Product() {
    }
    public Product(Long id, String name, Long price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Long getPrice() {
        return price;
    }
    public void setPrice(Long price) {
        this.price = price;
    }
    @Override
    public Object clone()  {

        try {
            return super.clone();
        } catch (CloneNotSupportedException e) {
            return new Product(this.id, this.name, this.price);
        }
    }
    
}
```

Codigo final Service

```java
package com.di.app.app_di.services;

import java.util.List;
import java.util.stream.Collectors;

import com.di.app.app_di.models.Product;
import com.di.app.app_di.repositories.ProductRepository;

public class ProductService {

    private ProductRepository repositoryProduct = new ProductRepository();

    public List<Product> findAll(){
        return repositoryProduct.findAll().stream().map(p ->{
            Double priceTax = p.getPrice() * 1.45d;
            // Product newProduct = new Product(p.getId(), p.getName(), priceImp.longValue());
            Product newProduct = (Product) p.clone();
            // p.setPrice(priceImp.longValue());
            newProduct.setPrice(priceTax.longValue());
            return newProduct;
        }).collect(Collectors.toList());
    }

    public Product findById(Long id){
        return repositoryProduct.findById(id);        
    }
}

```

## Aplicando Inyeccion de dependencias

<img src="Manuales\imgspring\news\71.png" alt="71" style="zoom:67%;" />

<img src="Manuales\imgspring\news\72.png" alt="72" style="zoom:67%;" />

<img src="Manuales\imgspring\news\73.png" alt="73" style="zoom:67%;" />

> La solución presentada anteriormente presenta un acoplamiento fuerte y esto genera problemas de mantenibilidad y escalabilidad de la aplicacion.

## Implementación de Desacoplamiento (Solución)

Para aplicar desacoplamiento se debe realizar inyección desde la Interface.

### Services

```java
package com.di.app.app_di.services;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.di.app.app_di.models.Product;
import com.di.app.app_di.repositories.ProductRepository;

@Component
public class ProductServiceImpl implements ProductService {

    @Autowired
    private ProductRepository repositoryProduct;

    public List<Product> findAll(){
        return repositoryProduct.findAll().stream().map(p ->{
            Double priceTax = p.getPrice() * 1.45d;
            // Product newProduct = new Product(p.getId(), p.getName(), priceImp.longValue());
            Product newProduct = (Product) p.clone();
            // p.setPrice(priceImp.longValue());
            newProduct.setPrice(priceTax.longValue());
            return newProduct;
        }).collect(Collectors.toList());
    }

    public Product findById(Long id){
        return repositoryProduct.findById(id);        
    }
}

```

```java
package com.di.app.app_di.services;

import java.util.List;

import com.di.app.app_di.models.Product;

public interface ProductService {
    List<Product> findAll();
    Product findById(Long id);
}

```

### Repositories

```java
package com.di.app.app_di.repositories;

import java.util.Arrays;
import java.util.List;
import org.springframework.stereotype.Component;
import com.di.app.app_di.models.Product;

@Component
public class ProductRepositoryImpl implements ProductRepository {
        List<Product> products;

        public ProductRepositoryImpl() {
            this.products = Arrays.asList(
                new Product(1L, "Laptop", 4500000L),
                new Product(2L, "Smartphone", 2000000L),
                new Product(3L, "Tablet", 1200000L),
                new Product(4L, "Monitor", 800000L),
                new Product(5L, "Keyboard", 150000L),
                new Product(6L, "Mouse", 80000L),
                new Product(7L, "Printer", 700000L),
                new Product(8L, "External Hard Drive", 350000L),
                new Product(9L, "Headphones", 200000L),
                new Product(10L, "Webcam", 250000L)               
            );
        }
        @Override
        public List<Product> findAll(){
           return products; 
        }
        @Override
        public Product findById(Long id){
            return products.stream().filter(p -> p.getId().equals(id)).findFirst().orElseThrow();
        }
}
```

```java
package com.di.app.app_di.repositories;

import java.util.List;

import com.di.app.app_di.models.Product;

public interface ProductRepository {
    List<Product> findAll();
    Product findById(Long id);
}
```

### Controller

```java
import org.springframework.web.bind.annotation.RestController;

import com.di.app.app_di.models.Product;
import com.di.app.app_di.services.ProductService;

@RestController
@RequestMapping("/api")
public class BaseController {

    @Autowired
    private ProductService serviceProduct;

    @GetMapping
    public List<Product> list(){
        return serviceProduct.findAll();
    }
    @GetMapping("/{id}")
    public Product show(@PathVariable Long id){
        return serviceProduct.findById(id);
    }

}
```

### Model

```java
package com.di.app.app_di.models;

public class Product implements Cloneable {
    private Long id;
    private String name;
    private Long price;
    public Product() {
    }
    public Product(Long id, String name, Long price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Long getPrice() {
        return price;
    }
    public void setPrice(Long price) {
        this.price = price;
    }
    @Override
    public Object clone()  {

        try {
            return super.clone();
        } catch (CloneNotSupportedException e) {
            return new Product(this.id, this.name, this.price);
        }
    }
    
}
```

# Estereotipos (@Repository - @Service)

### `@Repository` 

en Spring es una especialización de la anotación `@Component`, que se utiliza para indicar que una clase es un componente de la capa de persistencia. En otras palabras, marca una clase como un mecanismo para interactuar con la base de datos. Esta anotación es parte del módulo Spring Data y se usa comúnmente en combinación con interfaces que extienden `CrudRepository`, `JpaRepository`, `PagingAndSortingRepository`, entre otras.

#### Funciones de la Anotación `@Repository`

1. **Indicación de Componente de Persistencia**: Al marcar una clase con `@Repository`, Spring la reconoce como un bean de Spring de la capa de persistencia y la maneja automáticamente.
2. **Manejo de Excepciones**: Spring proporciona una capa de traducción de excepciones. Las excepciones específicas de tecnologías de acceso a datos (por ejemplo, JDBC, JPA, Hibernate) se traducen en excepciones no verificadas (unchecked exceptions) de Spring, que son más genéricas. La anotación `@Repository` ayuda a Spring a realizar esta traducción.
3. **Configuración Automática**: En combinación con otras anotaciones de Spring, `@Repository` puede ayudar a configurar automáticamente los repositorios y el acceso a datos.

### **`@Service`** 

en Spring es una especialización de la anotación `@Component`. Se utiliza para marcar una clase como un servicio, que es un componente que contiene la lógica de negocio de la aplicación. La anotación `@Service` indica que una clase ofrece alguna funcionalidad y se utiliza en la capa de servicio de la aplicación.

#### Funciones de un Service

1. **Encapsulamiento de Lógica de Negocio**: Un servicio encapsula la lógica de negocio de la aplicación, separándola de la capa de presentación (controladores) y de la capa de acceso a datos (repositorios).
2. **Reutilización**: La lógica encapsulada en un servicio puede ser reutilizada por diferentes partes de la aplicación, promoviendo la DRY principle (Don't Repeat Yourself).
3. **Facilidad de Pruebas**: Al separar la lógica de negocio en servicios, es más fácil crear pruebas unitarias para esta lógica sin necesidad de involucrar la capa de presentación o la de acceso a datos.
4. **Desacoplamiento**: Los servicios ayudan a desacoplar diferentes partes de la aplicación, facilitando el mantenimiento y la evolución del código.

### Implementado @Repository y @Service

#### Service

```java
package com.di.app.app_di.services;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.di.app.app_di.models.Product;
import com.di.app.app_di.repositories.ProductRepository;

@Service
public class ProductServiceImpl implements ProductService {

    @Autowired
    private ProductRepository repositoryProduct;

    public List<Product> findAll(){
        return repositoryProduct.findAll().stream().map(p ->{
            Double priceTax = p.getPrice() * 1.45d;
            // Product newProduct = new Product(p.getId(), p.getName(), priceImp.longValue());
            Product newProduct = (Product) p.clone();
            // p.setPrice(priceImp.longValue());
            newProduct.setPrice(priceTax.longValue());
            return newProduct;
        }).collect(Collectors.toList());
    }

    public Product findById(Long id){
        return repositoryProduct.findById(id);        
    }
}

```

#### Repository

```java
package com.di.app.app_di.repositories;

import java.util.Arrays;
import java.util.List;
import org.springframework.stereotype.Repository;

import com.di.app.app_di.models.Product;

@Repository
public class ProductRepositoryImpl implements ProductRepository {
        List<Product> products;

        public ProductRepositoryImpl() {
            this.products = Arrays.asList(
                new Product(1L, "Laptop", 4500000L),
                new Product(2L, "Smartphone", 2000000L),
                new Product(3L, "Tablet", 1200000L),
                new Product(4L, "Monitor", 800000L),
                new Product(5L, "Keyboard", 150000L),
                new Product(6L, "Mouse", 80000L),
                new Product(7L, "Printer", 700000L),
                new Product(8L, "External Hard Drive", 350000L),
                new Product(9L, "Headphones", 200000L),
                new Product(10L, "Webcam", 250000L)               
            );
        }
        @Override
        public List<Product> findAll(){
           return products; 
        }
        @Override
        public Product findById(Long id){
            return products.stream().filter(p -> p.getId().equals(id)).findFirst().orElseThrow();
        }
}
```

# Inyección de dependencias por setter y constructor

## Inyeccion por setter

```java
package com.di.app.app_di.services;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.di.app.app_di.models.Product;
import com.di.app.app_di.repositories.ProductRepository;

@Service
public class ProductServiceImpl implements ProductService {


    private ProductRepository repositoryProduct;

    @Autowired
    public void setRepositoryProduct(ProductRepository repositoryProduct) {
        this.repositoryProduct = repositoryProduct;
    }
    

    public List<Product> findAll(){
        return repositoryProduct.findAll().stream().map(p ->{
            Double priceTax = p.getPrice() * 1.45d;
            // Product newProduct = new Product(p.getId(), p.getName(), priceImp.longValue());
            Product newProduct = (Product) p.clone();
            // p.setPrice(priceImp.longValue());
            newProduct.setPrice(priceTax.longValue());
            return newProduct;
        }).collect(Collectors.toList());
    }

    public Product findById(Long id){
        return repositoryProduct.findById(id);        
    }

}
```

# @Primary y @Qualifier

## @Primary

### ¿Qué es?

La anotación `@Primary` se utiliza para marcar un bean como el bean preferido cuando hay múltiples candidatos calificados para ser inyectados en un punto de inyección.

#### ¿Para qué se usa?

Se utiliza para evitar ambigüedades cuando existen múltiples beans del mismo tipo y no se ha especificado explícitamente cuál bean debe ser inyectado. Al marcar un bean con `@Primary`, se le da prioridad a ese bean sobre los otros.

#### Ejemplo de Uso

Supongamos que tenemos dos implementaciones de una interfaz `PaymentService`:

```java
public interface PaymentService {
    void processPayment();
}

@Service
public class CreditCardPaymentService implements PaymentService {
    @Override
    public void processPayment() {
        System.out.println("Processing payment with Credit Card");
    }
}

@Service
@Primary
public class PaypalPaymentService implements PaymentService {
    @Override
    public void processPayment() {
        System.out.println("Processing payment with PayPal");
    }
}

```

En este caso, si inyectamos `PaymentService` en otro bean sin especificar cuál implementación queremos, Spring elegirá `PaypalPaymentService` porque está marcado con `@Primary`.

```java
@Component
public class PaymentProcessor {

    private final PaymentService paymentService;

    @Autowired
    public PaymentProcessor(PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    public void makePayment() {
        paymentService.processPayment();
    }
}

```

Al llamar a `makePayment()`, se utilizará `PaypalPaymentService` debido a la anotación `@Primary`.

### @Qualifier

#### ¿Qué es?

La anotación `@Qualifier` se utiliza para resolver la ambigüedad especificando el nombre del bean que debe ser inyectado. Se utiliza junto con `@Autowired` para indicar a Spring exactamente cuál bean debe inyectarse cuando hay múltiples candidatos del mismo tipo.

#### ¿Para qué se usa?

Se usa para seleccionar explícitamente un bean específico cuando hay múltiples beans del mismo tipo disponibles en el contexto de la aplicación y se necesita más control sobre cuál bean debe ser inyectado.

#### Ejemplo de Uso

Continuando con el ejemplo anterior, supongamos que queremos inyectar específicamente `CreditCardPaymentService` en lugar de `PaypalPaymentService`.

```java
@Component
public class PaymentProcessor {

    private final PaymentService paymentService;

    @Autowired
    public PaymentProcessor(@Qualifier("creditCardPaymentService") PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    public void makePayment() {
        paymentService.processPayment();
    }
}

```

En este caso, `creditCardPaymentService` se inyectará en `PaymentProcessor` debido al uso de `@Qualifier`.

### Resumen

- **@Primary**: Se utiliza para marcar un bean como el predeterminado cuando hay múltiples beans del mismo tipo. Es útil cuando hay un bean que debe usarse la mayor parte del tiempo, pero no siempre.
- **@Qualifier**: Se utiliza para especificar explícitamente cuál bean debe inyectarse cuando hay múltiples beans del mismo tipo. Proporciona un control más granular sobre la inyección de dependencias.

# @RequestScope

## ¿Qué es @RequestScope?

`@RequestScope` es una especialización de la anotación `@Scope` de Spring y define que el ámbito del bean es una solicitud HTTP. En términos prácticos, esto significa que el bean existirá solamente durante la duración de una solicitud HTTP.

## ¿Para qué se usa @RequestScope?

Se usa para garantizar que un bean sea único y exclusivo para cada solicitud HTTP. Esto es útil en escenarios donde el estado del bean no debe ser compartido entre diferentes solicitudes y debe ser específico para cada una. Algunos ejemplos de uso incluyen:

1. **Datos de Usuario en una Sesión**: Mantener datos específicos del usuario que son necesarios solo durante la solicitud actual.
2. **Recursos Temporales**: Manejar recursos que son necesarios solo durante una solicitud específica y deben ser liberados inmediatamente después.
3. **Transacciones**: Cuando se necesita que cada solicitud tenga su propio contexto de transacción.

**Implementando en ejemplo base**

```java
package com.di.app.app_di.repositories;

import java.util.Arrays;
import java.util.List;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Repository;
import org.springframework.web.context.annotation.RequestScope;

import com.di.app.app_di.models.Product;

@RequestScope
@Primary
@Repository("productList")
public class ProductRepositoryImpl implements ProductRepository {
        List<Product> products;

        public ProductRepositoryImpl() {
            this.products = Arrays.asList(
                new Product(1L, "Laptop", 4500000L),
                new Product(2L, "Smartphone", 2000000L),
                new Product(3L, "Tablet", 1200000L),
                new Product(4L, "Monitor", 800000L),
                new Product(5L, "Keyboard", 150000L),
                new Product(6L, "Mouse", 80000L),
                new Product(7L, "Printer", 700000L),
                new Product(8L, "External Hard Drive", 350000L),
                new Product(9L, "Headphones", 200000L),
                new Product(10L, "Webcam", 250000L)               
            );
        }
        @Override
        public List<Product> findAll(){
           return products; 
        }
        @Override
        public Product findById(Long id){
            return products.stream().filter(p -> p.getId().equals(id)).findFirst().orElseThrow();
        }
}
```

# @SessionScope

## ¿Qué es @SessionScope?

`@SessionScope` es una especialización de la anotación `@Scope` de Spring que define que el ámbito del bean es una sesión HTTP. En términos prácticos, esto significa que el bean existirá durante la duración de la sesión del usuario y se compartirá entre múltiples solicitudes dentro de esa misma sesión.

## ¿Para qué se usa @SessionScope?

Se usa para mantener el estado del usuario a lo largo de una sesión. Esto es útil en escenarios donde se necesita que los datos persistan entre diferentes solicitudes del mismo usuario. Algunos ejemplos de uso incluyen:

1. **Carritos de Compras**: Mantener el estado del carrito de compras de un usuario mientras navega por una tienda en línea.
2. **Datos del Usuario**: Almacenar información específica del usuario que es necesaria durante toda la sesión, como detalles de autenticación o preferencias del usuario.
3. **Formularios en Varios Pasos**: Mantener el estado de un formulario que se completa en varios pasos a lo largo de la sesión del usuario.

**Implementando en el ejemplo base**

```java
package com.di.app.app_di.repositories;

import java.util.Arrays;
import java.util.List;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Repository;
//import org.springframework.web.context.annotation.RequestScope;
import org.springframework.web.context.annotation.SessionScope;

import com.di.app.app_di.models.Product;

// @RequestScope
@SessionScope
@Primary
@Repository("productList")
public class ProductRepositoryImpl implements ProductRepository {
        
    List<Product> products;

        public ProductRepositoryImpl() {
            this.products = Arrays.asList(
                new Product(1L, "Laptop", 450L),
                new Product(2L, "Smartphone", 200L),
                new Product(3L, "Tablet", 120L),
                new Product(4L, "Monitor", 800L),
                new Product(5L, "Keyboard", 150L),
                new Product(6L, "Mouse", 800L),
                new Product(7L, "Printer", 700L),
                new Product(8L, "External Hard Drive", 350L),
                new Product(9L, "Headphones", 200L),
                new Product(10L, "Webcam", 250L)               
            );
        }
        @Override
        public List<Product> findAll(){
           return products; 
        }
        @Override
        public Product findById(Long id){
            return products.stream().filter(p -> p.getId().equals(id)).findFirst().orElseThrow();
        }
}
```

# Ejercicio

Se requiere implementar una variable de entorno que permita almacenar el valor del porcentaje del impuesto que se  va aplicar a cada uno de los productos al momento de ser expuestos por el api. Recuerde que se debe crear un archivo de configuración independiente.

# Trabajando con Archivos JSON

1. Cree un archivo JSON en Resources. Para el caso practico llamares a el archivo products.json

2. Cree un nuevo repositorio llamado ProductRepositoryJson

```java
package com.di.app.app_di.repositories;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;

import org.springframework.core.io.ClassPathResource;

import com.di.app.app_di.models.Product;
import com.fasterxml.jackson.core.exc.StreamReadException;
import com.fasterxml.jackson.databind.DatabindException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class ProductRepositoryJson implements ProductRepository{
    private List<Product> list;

    public ProductRepositoryJson(){
        ClassPathResource resource = new ClassPathResource("products.json");
        ObjectMapper objectmapper = new ObjectMapper();
        try {
            list = Arrays.asList(objectmapper.readValue(resource.getFile(),Product[].class));
        } catch (StreamReadException e) {
            e.printStackTrace();
        } catch (DatabindException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Override
    public List<Product> findAll() {
        return list;
    }

    @Override
    public Product findById(Long id) {
        return list.stream().filter(p -> p.getId().equals(id)).findFirst().orElse(null);
    }

}
```

 **Carga del Archivo JSON**: En el constructor, se utiliza `ClassPathResource` para localizar el archivo `products.json` en el classpath. `ObjectMapper` de Jackson convierte el contenido de este archivo en una lista de objetos `Product`.

**Manejo de Excepciones**: El código captura y maneja varias excepciones que pueden ocurrir durante la lectura del archivo y el mapeo de datos JSON a objetos Java (`StreamReadException`, `DatabindException`, `IOException`).

**Interfaz `ProductRepository`**: Asume que existe una interfaz `ProductRepository` con métodos `findAll` y `findById`, que esta clase implementa.

**Método `findAll`**: Proporciona una forma de obtener todos los productos.

**Método `findById`**: Utiliza un stream para filtrar la lista de productos y encontrar uno por su ID.

En el archivo de configuracion AppConfig Agrega el siguiente código:

```java
    @Bean
    @Primary
    ProductRepository productRepositoryJson(){
        return new ProductRepositoryJson();
    }
```

Clase completa

```java
package com.di.app.app_di;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

import com.di.app.app_di.repositories.ProductRepository;
import com.di.app.app_di.repositories.ProductRepositoryJson;

@Configuration
@PropertySource("classpath:config.properties")
public class AppConfig {
    
    @Bean("productJson")
    ProductRepository productRepositoryJson(){
        return new ProductRepositoryJson();
    }
}
```

**Método `productRepositoryJson`**

- Este es un método en una clase de configuración de Spring (normalmente una clase anotada con `@Configuration`).
- El método define un bean de Spring que será gestionado por el contenedor de Spring.

**Anotación `@Bean`**

- La anotación `@Bean` se utiliza para indicar que un método produce un bean que debe ser gestionado por el contenedor de Spring.
- El método anotado con `@Bean` será invocado y su valor de retorno será registrado como un bean en el contexto de la aplicación de Spring.
- En este caso, el método `productRepositoryJson` define un bean de tipo `ProductRepository` que devuelve una instancia de `ProductRepositoryJson`.

**Anotación `@Primary`**

- La anotación `@Primary` se utiliza para indicar que este bean debe ser el bean preferido cuando hay múltiples beans del mismo tipo.
- Si hay varias implementaciones de `ProductRepository` disponibles, Spring seleccionará la marcada con `@Primary` por defecto.
- Esto es útil cuando se tienen múltiples beans de un mismo tipo y se quiere especificar cuál debe ser inyectado por defecto.

**Creación de un Bean `ProductRepository`**

- El método `productRepositoryJson` crea y devuelve una nueva instancia de `ProductRepositoryJson`.
- `ProductRepositoryJson` es una implementación de la interfaz `ProductRepository` que hemos visto anteriormente.



# Hibernate (https://hibernate.org/)

Es una herramienta de mapeo de objeto relacional (ORM) que permite trabajar los datos de una base de datos (RDBMS) en forma de clases y objetos (lenguaje POO).

<img src="Manuales\imgspring\news\75.png" alt="75" style="zoom: 50%;" />

## Tipos de consulta

### HQL

HQL, o Hibernate Query Language, es un lenguaje de consulta orientado a objetos similar a SQL, pero diseñado específicamente para trabajar con Hibernate, un framework de mapeo objeto-relacional (ORM) en Java. HQL permite realizar consultas y manipulaciones en la base de datos utilizando las clases y atributos del modelo de datos en lugar de las tablas y columnas de la base de datos.

#### Características de HQL

1. **Orientado a objetos**: HQL utiliza las entidades del modelo de datos de Hibernate en lugar de tablas de la base de datos.
2. **Consulta independiente de la base de datos**: HQL es independiente del sistema de gestión de bases de datos subyacente, lo que facilita la portabilidad del código.
3. **Similar a SQL**: Aunque HQL es un lenguaje propio de Hibernate, su sintaxis es muy similar a la de SQL, lo que facilita su aprendizaje para quienes ya conocen SQL.
4. **Soporte para funciones de agregación y subconsultas**: HQL admite funciones de agregación (como SUM, COUNT, AVG) y subconsultas, al igual que SQL.
5. **Operaciones de asociación y herencia**: HQL permite realizar consultas sobre asociaciones y herencias definidas en el modelo de datos, facilitando la navegación entre entidades relacionadas.

#### Ventajas de usar HQL

- **Abstracción del modelo de datos**: Permite trabajar a un nivel más alto de abstracción, utilizando objetos y sus relaciones.
- **Portabilidad**: Las consultas HQL no están vinculadas a un SGBD específico, lo que facilita cambiar de una base de datos a otra sin modificar el código de las consultas.
- **Integración con Hibernate**: HQL se integra perfectamente con las capacidades de Hibernate, como la caché de segundo nivel y las transacciones.

### Criteria API

La Criteria API en Spring Boot es una forma programática y tipada de construir consultas para bases de datos utilizando Hibernate como proveedor JPA. A diferencia de JPQL (Java Persistence Query Language), que utiliza cadenas de texto para definir consultas, la Criteria API permite construir consultas de manera fluida utilizando la API de Java, lo que facilita la creación de consultas dinámicas y refactorizables.

#### Características de la Criteria API

1. **Tipado seguro**: La Criteria API utiliza clases y métodos en lugar de cadenas de texto, lo que permite que el compilador de Java detecte errores de sintaxis y tipo.
2. **Consultas dinámicas**: Facilita la construcción de consultas dinámicas en función de los parámetros recibidos en tiempo de ejecución.
3. **Reutilización**: Las consultas Criteria pueden ser fácilmente reutilizadas y combinadas.
4. **Facilidad de mantenimiento**: Al estar escritas en código Java, las consultas son más fáciles de mantener y refactorizar.

### SQL Native

SQL nativo, también conocido como SQL puro o SQL sin procesar, se refiere al uso directo del lenguaje de consulta estructurado (SQL) para interactuar con una base de datos desde una aplicación. A diferencia de los ORM (Object-Relational Mapping) y otras abstracciones que proporcionan una capa intermedia entre el código de la aplicación y la base de datos, el uso de SQL nativo implica escribir consultas SQL directamente.

#### Características del SQL Nativo

1. **Directo y eficiente**: Permite un acceso directo a las capacidades de la base de datos, lo que puede resultar en un mejor rendimiento y control.
2. **Complejidad de las consultas**: Ideal para consultas complejas y específicas que pueden ser difíciles de expresar utilizando ORM o abstracciones de consultas.
3. **Dependencia del SGBD**: Las consultas SQL nativas pueden depender de las características específicas del sistema de gestión de bases de datos (SGBD) que se está utilizando, lo que puede afectar la portabilidad de la aplicación.

#### Ejemplo

```java
@Entity
public class Empleado {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nombre;
    private String departamento;
    private Double salario;

    // Getters y setters
}
```

```java
public interface EmpleadoRepository extends JpaRepository<Empleado, Long> {

    @Query(value = "SELECT * FROM Empleado WHERE departamento = ?1 AND salario >= ?2", nativeQuery = true)
    List<Empleado> encontrarPorDepartamentoYSalario(String departamento, Double salarioMinimo);
}
```

# Asociaciones(Relaciones)

@ManyToOne

@OneToMany

@OneToOne

@ManyToMany

## **@ManyToOne**

- **Descripción**: Representa una relación en la que muchos instancias de una entidad están relacionadas con una instancia de otra entidad. Es la parte "muchos" de una relación de uno a muchos.
- **Uso**: Se usa para definir una relación de muchos a uno en una entidad.

```java
@Entity
public class Empleado {
    @ManyToOne
    @JoinColumn(name = "departamento_id")
    private Departamento departamento;
}
```

## **@OneToMany**

- **Descripción**: Representa una relación en la que una instancia de una entidad está relacionada con muchas instancias de otra entidad. Es la parte "uno" de una relación de uno a muchos.
- **Uso**: Se usa para definir una relación de uno a muchos en una entidad.

```java
@Entity
public class Departamento {
        @OneToMany(mappedBy = "departamento")
        private List<Empleado> empleados;
}
```

## **Relación OneToMany Bidireccional**

Una relación bidireccional OneToMany (Uno a Muchos) en JPA (Java Persistence API) es una relación en la que una entidad tiene una colección de otra entidad, y esa otra entidad tiene una referencia de vuelta a la primera entidad. En otras palabras, ambas entidades están conscientes de la relación y pueden navegar a través de ella en ambas direcciones.  

En la entidad Padre se debe agregar la siguiente estructura:

```
@OneToMany(mappedBy = "survey", cascade = CascadeType.ALL)
@JsonManagedReference
private Set<Chapter> chapter = new HashSet<>();
```

**`@OneToMany`**: Indica que es una relación de "uno a muchos", donde un solo objeto de la entidad actual (por ejemplo, `Parent`) tiene múltiples objetos relacionados (en este caso, `Child`).

**`mappedBy = "survey"`**: El parámetro `mappedBy` indica el **lado inverso de la relación**, o sea, la propiedad en la entidad `Chapter` que mapea esta relación. Esto significa que en la entidad `Chapter`, hay una propiedad llamada `survey` que establece la relación con `Survey`. Básicamente, `Chapter` contiene una referencia a `Survey`.

**`cascade = CascadeType.ALL`**: Esto especifica el tipo de operaciones de cascada que deben aplicarse a las entidades relacionadas. `CascadeType.ALL` indica que cualquier operación (como `persist`, `merge`, `remove`, `refresh`) realizada sobre la entidad `Survey` se aplicará también a las entidades `Chapter` relacionadas. Por ejemplo, si se guarda o elimina un `Survey`, todos los `Chapter` asociados también serán guardados o eliminados.

**`Set<Chapter> chapter = new HashSet<>()`**: Esto define una colección de capítulos (`Chapter`) relacionados con esta entidad `Survey`. Estamos utilizando un `Set` para evitar elementos duplicados.

### **`@JsonManagedReference`**:

Esta es una anotación de **Jackson** que se utiliza para gestionar la serialización JSON en relaciones bidireccionales, evitando problemas de **recursión infinita** al serializar las entidades.

En la entidad Hija se debe agregar

```java
@ManyToOne
@JoinColumn(name = "survey_id")
@JsonBackReference
Survey survey;
```

### **`@ManyToOne`**:

La anotación `@ManyToOne` indica una relación de **muchos a uno** entre dos entidades. En este caso, una entidad (probablemente `Chapter`) tiene una relación con una entidad `Survey`. La relación de "muchos a uno" significa que **muchos objetos** de la entidad `Chapter` pueden estar asociados con **una sola** encuesta (`Survey`).

- **Relación bidireccional**: En este contexto, un `Chapter` pertenece a una `Survey`, y una `Survey` puede estar asociada con muchos `Chapter`. Esta es la relación inversa a la que tienes en la otra entidad (`Survey`).

Ejemplo:

```java
package com.asociacionesapp.app_relationship.entities;
import java.util.*;
import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.JoinTable;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
import jakarta.persistence.UniqueConstraint;
@Entity
@Table(name = "clients")
public class Client {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String lastname;
    // @JoinColumn(name = "client_id_address")
    @OneToMany(cascade = CascadeType.ALL, orphanRemoval = true)
    @JoinTable(
        name = "address_clients",
        joinColumns = @JoinColumn(name = "client_id"),
        inverseJoinColumns = @JoinColumn(name = "address_id"),
        uniqueConstraints = @UniqueConstraint(columnNames = {"address_id"})
	) 
    private List<Address> addresses = new ArrayList<>();
    
    //Aplicacion relacion bidireccional
    @OneToMany(cascade = CascadeType.ALL, orphanRemoval = true,mappedBy="client")
    private Set<Invoice> invoices;
    
    public Client() {
        invoices = = new HashSet<>();
    }
    
    public Client(String name, String lastname) {
    this.name = name;
    this.lastname = lastname;
    } 
    public Long getId() {
        return id;
    } 
    public void setId(Long id) {
    	this.id = id;
    } 
    public String getName() {
    	return name;
    } 
    public void setName(String name) {
    	this.name = name;
    } 
    public String getLastname() {
    	return lastname;
    } 
    public void setLastname(String lastname) {
    	this.lastname = lastname;
    } 
    public void setAddresses(List<Address> addresses) {
    	this.addresses = addresses;
    } 
    public List<Address> getAddresses() {
    	return addresses;
    } 
    public Set<Invoice> getInvoices() {
    	return invoices;
    } 
    public void setInvoices(Set<Invoice> invoices) {this.invoices = invoices;
    } 

        @Override
        public String toString() {
        return "{id=" + id + ", name=" + name + ", lastname=" + lastname +"}";
    }
}
```

```java
package com.asociacionesapp.app_relationship.entities;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "invoices")
public class Invoice {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String description;
    private Long total;

    // @JoinColumn(name = "client_id")
    @ManyToOne
    private Client client;

    public Invoice() {
    }

    public Invoice(String description, Long total) {
        this.description = description;
        this.total = total;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Long getTotal() {
        return total;
    }
    
    public void setTotal(Long total) {
        this.total = total;
    }
}
```



## **@OneToOne**

- **Descripción**: Representa una relación en la que una instancia de una entidad está relacionada con una única instancia de otra entidad.
- **Uso**: Se usa para definir una relación uno a uno en una entidad.

```java
@Entity
public class Persona {
    @OneToOne
    @JoinColumn(name = "direccion_id")
    private Direccion direccion;
} 
```

## Asociacion @ManyToMany (Llaves compuestas)

1. Descargue el proyecto base https://github.com/trainingLeader/app-relationship.git

2. Cree dos nuevas entidades Product

   ```java
   package com.asociacionesapp.app_relationship.entities;
      
      import jakarta.persistence.Entity;
      import jakarta.persistence.GeneratedValue;
      import jakarta.persistence.GenerationType;
      import jakarta.persistence.Id;
      import jakarta.persistence.Table;
      
      @Entity
      @Table(name="products")
      public class Product {
      
          @Id
          @GeneratedValue(strategy = GenerationType.IDENTITY)
          private Long id;
      
          private String name;
          private double price;
          private int stock;
          private int stockmin;
          private int stockmax;
          public Product() {
          }
          public Product(String name, double price, int stock, int stockmin, int stockmax) {
              this.name = name;
              this.price = price;
              this.stock = stock;
              this.stockmin = stockmin;
              this.stockmax = stockmax;
          }
          public Long getId() {
              return id;
          }
          public void setId(Long id) {
              this.id = id;
          }
          public String getName() {
              return name;
          }
          public void setName(String name) {
              this.name = name;
          }
          public double getPrice() {
              return price;
          }
          public void setPrice(double price) {
              this.price = price;
          }
          public int getStock() {
              return stock;
          }
          public void setStock(int stock) {
              this.stock = stock;
          }
          public int getStockmin() {
              return stockmin;
          }
          public void setStockmin(int stockmin) {
              this.stockmin = stockmin;
          }
          public int getStockmax() {
              return stockmax;
          }
          public void setStockmax(int stockmax) {
              this.stockmax = stockmax;
          }
          
          
      }
   ```

   

3. Cree la Clase DetailProduct : Esta cllase tiene dos atributos compuestos uno de la entidad product y otro de [invoice.]()

   

   ```java
   package com.asociacionesapp.app_relationship.entities;
   
   import jakarta.persistence.EmbeddedId;
   import jakarta.persistence.Entity;
   import jakarta.persistence.JoinColumn;
   import jakarta.persistence.ManyToOne;
   import jakarta.persistence.Table;
   
   @Entity
   @Table(name = "detail_products")
   public class DetailProduct {
   
       @EmbeddedId
       ProductInvoicePk id;
       
       private Integer quatity;
       private Double price;
       
       @ManyToOne
       @JoinColumn(name = "id_invoice", insertable = false, updatable = false)
       private Invoice invoice;
       
       @ManyToOne
       @JoinColumn(name = "id_product", insertable = false, updatable = false)
       private Product products;
   
   
       public ProductInvoicePk getId() {
           return id;
       }
       public void setId(ProductInvoicePk id) {
           this.id = id;
       }
       public Integer getQuatity() {
           return quatity;
       }
       public void setQuatity(Integer quatity) {
           this.quatity = quatity;
       }
       public Double getPrice() {
           return price;
       }
       public void setPrice(Double price) {
           this.price = price;
       }
       public ProductInvoicePk getId() {
       return id;
       }
       public void setId(ProductInvoicePk id) {
           this.id = id;
       }
       public Integer getQuatity() {
           return quatity;
       }
       public void setQuatity(Integer quatity) {
           this.quatity = quatity;
       }
       public Double getPrice() {
           return price;
       }
       public void setPrice(Double price) {
           this.price = price;
       }
   }
   ```

   


   Para implementar esta asociación se debe crear una nueva clase que vincule las llaves compuestas. Para nombrar esta clase se recomienda que sea un identificador compuesto entre las dos tablas para este ejemplo Product e Invoice  terminado en Pk - (ProductInvoicePk)

   ```java
   package com.asociacionesapp.app_relationship.entities;
   
   import java.io.Serializable;
   
   import jakarta.persistence.Column;
   import jakarta.persistence.Embeddable;
   
   @Embeddable
   public class ProductInvoicePk implements Serializable {
   
       @Column(name ="id_product")
       private Long idproduct;
       @Column(name = "id_invoice")
       private Long idinvoice;
       public Long getIdproduct() {
           return idproduct;
       }
       public void setIdproduct(Long idproduct) {
           this.idproduct = idproduct;
       }
       public Long getIdinvoice() {
           return idinvoice;
       }
       public void setIdinvoice(Long idinvoice) {
           this.idinvoice = idinvoice;
       }
   }

   ```
```java
java
import javax.persistence.*;
import java.util.List;

@Entity
public class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
```

    private String name;
    
    @OneToMany
    @JoinTable(
        name = "employee_phone",
        joinColumns = @JoinColumn(name = "employee_id"),
        inverseJoinColumns = @JoinColumn(name = "phone_id")
    )
    private List<Phone> phones;
    
    // Getters y setters
}
```

```java
import javax.persistence.*;

@Entity
public class Phone {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String number;

    // Getters y setters
}
```

## **Asociacion @ManyToMany  usando  @EmbeddedId y Clave Compuesta con `@Embeddable`**

Para este ejemplo se tienen dos entidades una llamada estudiante y otra curso. El estudiante puede tomar muchos cursos y el curso puede ser tomado por muchos estudiantes. En este caso se debe generar una tabla intermedia EstudianteCurso.

entidad Estudiante

```java
@Entity
@Table(name = "estudiantes")
public class Estudiante {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nombre;

    @OneToMany(mappedBy = "estudiante", cascade = CascadeType.ALL, orphanRemoval = true)
    private Set<EstudianteCurso> estudianteCursos = new HashSet<>();

    // Constructor, getters y setters
}
```

Entidad Curso

```java
@Entity
@Table(name = "cursos")
public class Curso {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nombre;

    @OneToMany(mappedBy = "curso", cascade = CascadeType.ALL, orphanRemoval = true)
    private Set<EstudianteCurso> estudianteCursos = new HashSet<>();

    // Constructor, getters y setters
}
```

**Clase EstudianteCursoId** : Dado quese esta  usando una entidad intermedia con una clave compuesta (las claves foráneas de `Estudiante` y `Curso`), se debe crear una nueva clase que represente esta clave compuesta.

```java
@Embeddable
public class EstudianteCursoId implements Serializable {

    private Long estudianteId;
    private Long cursoId;

    // Constructor, getters, setters, hashCode y equals

    public EstudianteCursoId() {}

    public EstudianteCursoId(Long estudianteId, Long cursoId) {
        this.estudianteId = estudianteId;
        this.cursoId = cursoId;
    }

    // Getters y Setters

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        EstudianteCursoId that = (EstudianteCursoId) o;
        return Objects.equals(estudianteId, that.estudianteId) &&
               Objects.equals(cursoId, that.cursoId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(estudianteId, cursoId);
    }
}

```

### **`@Embeddable`**:

La anotación `@Embeddable` indica que esta clase puede ser **incrustada** en otra entidad como parte de su clave primaria. Es decir, esta clase será utilizada como una **clave compuesta** en una entidad que involucra una relación Many-to-Many entre `Estudiante` y `Curso`.

En este caso, `EstudianteCursoId` representa una clave compuesta con los atributos `estudianteId` y `cursoId`, que combinados, identifican de manera única un registro en la tabla intermedia que vincula `Estudiante` y `Curso`.

### **Implementación de `Serializable`**:

La clase `EstudianteCursoId` implementa la interfaz `Serializable`. Esto es necesario porque JPA requiere que las clases que representan claves compuestas sean serializables. La serialización permite convertir un objeto en una secuencia de bytes, que puede ser almacenada o transmitida y luego reconstruida.

- **`estudianteId`**: La clave primaria de la entidad `Estudiante`.
- **`cursoId`**: La clave primaria de la entidad `Curso`.

**JPA usará estos dos campos para generar la clave compuesta en la entidad que los use como clave primaria.**

### **Métodos `equals` y `hashCode`**:

Estos dos métodos son fundamentales en cualquier clase que represente una clave compuesta, ya que JPA utiliza estos métodos para comprobar la igualdad y gestionar correctamente las entidades en un contexto de persistencia.

`Objects.equals` compara los valores de `estudianteId` y `cursoId` entre dos instancias de `EstudianteCursoId`.

#### **`hashCode`**:

El método `hashCode` genera un código hash para la instancia de `EstudianteCursoId`, basado en `estudianteId` y `cursoId`. JPA utiliza este código hash para optimizar operaciones de almacenamiento en caché y búsqueda.



Entidad Intermedia EstudianteCurso

```java
@Entity
@Table(name = "estudiantes_cursos")
public class EstudianteCurso {

    @EmbeddedId
    private EstudianteCursoId id = new EstudianteCursoId(); // Clave compuesta

    @ManyToOne
    @MapsId("estudianteId") // Mapea la parte de estudiante en la clave compuesta
    @JoinColumn(name = "estudiante_id")
    private Estudiante estudiante;

    @ManyToOne
    @MapsId("cursoId") // Mapea la parte de curso en la clave compuesta
    @JoinColumn(name = "curso_id")
    private Curso curso;

    // Columnas adicionales
    @Column(name = "fecha_inicio")
    private LocalDate fechaInicio;

    @Column(name = "fecha_finalizacion")
    private LocalDate fechaFinalizacion;

    // Constructor, getters y setters

    public EstudianteCurso() {}

    public EstudianteCurso(Estudiante estudiante, Curso curso, LocalDate fechaInicio, LocalDate fechaFinalizacion) {
        this.estudiante = estudiante;
        this.curso = curso;
        this.fechaInicio = fechaInicio;
        this.fechaFinalizacion = fechaFinalizacion;
        this.id = new EstudianteCursoId(estudiante.getId(), curso.getId());
    }

    // Getters y Setters
}
```





# Usando @JoinTable

La anotación `@JoinTable` en JPA se utiliza para definir la tabla de unión que se emplea en relaciones muchos a muchos (Many-to-Many) o en relaciones uno a muchos (One-to-Many) donde se desea personalizar la tabla intermedia y las columnas de la relación. Esta anotación proporciona un control detallado sobre cómo se gestionan las uniones entre las tablas en una base de datos relacional.

## Uso de `@JoinTable` en Relaciones Muchos a Muchos

En una relación muchos a muchos, se necesita una tabla de unión para conectar las entidades. La anotación `@JoinTable` permite especificar el nombre de esta tabla de unión y las columnas que se usarán para establecer la relación.



## Uso de `@JoinTable` en Relaciones Uno a Muchos

Aunque `@JoinTable` se usa principalmente en relaciones muchos a muchos, también se puede utilizar en relaciones uno a muchos si se desea un mayor control sobre la tabla de unión.

### Ejemplo de Relaciones Uno a Muchos con `@JoinTable`

Supongamos que tenemos una entidad `Employee` y una entidad `Phone`, donde un empleado puede tener múltiples teléfonos.



### Explicación Adicional de `@JoinTable` en Uno a Muchos

En este caso, `@JoinTable` crea una tabla de unión `employee_phone` que tiene columnas `employee_id` y `phone_id`. Esto permite que la relación uno a muchos se gestione a través de una tabla intermedia.

#### Beneficios de Usar `@JoinTable`

1. **Control Detallado**: Permite un control detallado sobre la estructura de la tabla de unión, incluyendo nombres de tablas y columnas.
2. **Flexibilidad**: Facilita la gestión de relaciones complejas y personalizadas entre entidades.
3. **Normalización**: Ayuda en la normalización de la base de datos al separar las relaciones en tablas dedicadas.

Implementacion en client

```java
package com.asociacionesapp.app_relationship.entities;

import java.util.*;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.JoinTable;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
import jakarta.persistence.UniqueConstraint;

@Entity
@Table(name = "clients")
public class Client {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private String lastname;

    // @JoinColumn(name = "client_id_address")
    @OneToMany(cascade = CascadeType.ALL, orphanRemoval = true)
    @JoinTable(
        name = "address_clients",
        joinColumns = @JoinColumn(name = "client_id"),
        inverseJoinColumns = @JoinColumn(name = "address_id"),
        uniqueConstraints = @UniqueConstraint(columnNames = {"address_id"})
    )
    private List<Address> addresses = new ArrayList<>();

    public Client() {}

    public Client(String name, String lastname) {
        this.name = name;
        this.lastname = lastname;
    }
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getLastname() {
        return lastname;
    }
    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    @Override
    public String toString() {
        return "{id=" + id +
                ", name=" + name +
                ", lastname=" + lastname +
                "}";
    }
    public void setAddresses(List<Address> addresses) {
        this.addresses = addresses;
    }
    public List<Address> getAddresses() {
        return addresses;
    }

}
```

**Explicación**

**@JoinTable**:

- Esta anotación se usa para definir la tabla de unión que se utilizará en una relación de muchos a muchos (Many-to-Many) o uno a muchos (One-to-Many) cuando se necesita una tabla intermedia personalizada.

**name = "address_clients"**:

- `name` especifica el nombre de la tabla de unión en la base de datos. En este caso, la tabla se llama `address_clients`.

**joinColumns = @JoinColumn(name = "client_id")**:

- `joinColumns` define la columna en la tabla de unión que referencia a la entidad propietaria de la relación (la entidad donde se define la anotación `@JoinTable`).
- `@JoinColumn(name = "client_id")` especifica que la columna `client_id` en la tabla de unión se usará para referenciar la entidad `Client`.

**inverseJoinColumns = @JoinColumn(name = "address_id")**:

- `inverseJoinColumns` define la columna en la tabla de unión que referencia a la entidad inversa de la relación (la otra entidad de la relación).
- `@JoinColumn(name = "address_id")` especifica que la columna `address_id` en la tabla de unión se usará para referenciar la entidad `Address`.

**uniqueConstraints = @UniqueConstraint(columnNames = {"address_id"})**:

- `uniqueConstraints` se usa para definir restricciones únicas en la tabla de unión.
- `@UniqueConstraint(columnNames = {"address_id"})` crea una restricción única en la columna `address_id` de la tabla `address_clients`. Esto significa que cada dirección (`address_id`) solo puede estar asociada con un único cliente en esta tabla de unión.

## Uso de `@JoinTable` en Relaciones **@ManyToMany**

- **Descripción**: Representa una relación en la que muchas instancias de una entidad están relacionadas con muchas instancias de otra entidad.
- **Uso**: Se usa para definir una relación de muchos a muchos en una entidad.

```java
@Entity
public class Estudiante {
    @ManyToMany
    @JoinTable(
        name = "estudiante_curso",
        joinColumns = @JoinColumn(name = "estudiante_id"),
        inverseJoinColumns = @JoinColumn(name = "curso_id"),
        uniqueConstraints = @UniqueConstraint(columnNames = {"estudiante_id", "curso_id"})
    )
    private List<Curso> cursos;
}

@Entity
public class Curso {
    @ManyToMany(mappedBy = "cursos")
    private List<Estudiante> estudiantes;
}
```

```java

```

# Manejo Excepciones

## RuntimeException

`RuntimeException` es una clase en Java que extiende `Exception` y se utiliza para representar excepciones que pueden ocurrir durante la ejecución del programa y que no necesariamente necesitan ser declaradas en una cláusula `throws` de un método. Estas excepciones son conocidas como "unchecked exceptions" (excepciones no comprobadas), ya que no son verificadas por el compilador en tiempo de compilación, a diferencia de las "checked exceptions" (excepciones comprobadas).

### Características de `RuntimeException`

1. **Unchecked Exception**: Las excepciones que heredan de `RuntimeException` no necesitan ser declaradas en la firma del método con `throws`.
2. **Errores en Tiempo de Ejecución**: Representa errores que típicamente ocurren debido a problemas del programa que son detectados en tiempo de ejecución, como acceso a una posición fuera de los límites de un array, divisiones por cero, o errores de conversión de tipos.
3. **Manejo Opcional**: Debido a que no necesitan ser declaradas, el manejo de estas excepciones es opcional. Los desarrolladores pueden optar por capturarlas y manejarlas, o dejarlas sin manejar para ser capturadas por el gestor de excepciones predeterminado de la JVM.

### Uso Común

Algunos ejemplos comunes de excepciones que extienden `RuntimeException` incluyen:

- `NullPointerException`
- `ArrayIndexOutOfBoundsException`
- `IllegalArgumentException`
- `IllegalStateException`

## @PathVariable(Repaso)

La anotación `@PathVariable` en Spring se utiliza para extraer valores de la URL de la solicitud y asignarlos a parámetros de método en los controladores. Esta anotación es especialmente útil cuando se desea trabajar con datos que forman parte de la estructura de la URL en lugar de parámetros de consulta o el cuerpo de la solicitud.

## @RestControllerAdvice

La anotación `@RestControllerAdvice` en Spring se utiliza para manejar excepciones globalmente y aplicar lógica transversal a todos los controladores REST dentro de una aplicación Spring Boot. Esta anotación combina las funcionalidades de `@ControllerAdvice` y `@ResponseBody`, permitiendo el manejo centralizado de excepciones y respuestas JSON.

### ¿Qué es `@RestControllerAdvice`?

`@RestControllerAdvice` es una especialización de `@ControllerAdvice` que automáticamente incluye la anotación `@ResponseBody`, lo que significa que todos los métodos en una clase anotada con `@RestControllerAdvice` retornarán sus resultados directamente como respuestas JSON. Es una forma conveniente de manejar excepciones y otros aspectos transversales (como configuración global de validaciones) en aplicaciones que exponen APIs RESTful.

```java
@ResponseStatus(HttpStatus.NOT_FOUND)
public class UserNotFoundException extends RuntimeException {
    public UserNotFoundException(Long id) {
        super("Usuario con ID " + id + " no encontrado.");
    }
}
```

> La anotación `@ResponseStatus` se puede omitir si vas a manejar el código HTTP en `@ControllerAdvice`

**`@ControllerAdvice` para manejo global**

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<Map<String, String>> handleUserNotFound(UserNotFoundException ex) {
        Map<String, String> error = new HashMap<>();
        error.put("error", "Usuario no encontrado");
        error.put("detalle", ex.getMessage());
        return new ResponseEntity<>(error, HttpStatus.NOT_FOUND);
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getFieldErrors().forEach(err ->
            errors.put(err.getField(), err.getDefaultMessage()));
        return new ResponseEntity<>(errors, HttpStatus.BAD_REQUEST);
    }

    // Puedes agregar más handlers: ConstraintViolationException, IllegalArgumentException, etc.
}
```

**Usar la excepción en el controlador**

```java
@GetMapping("/{id}")
public ResponseEntity<User> getUserById(@PathVariable Long id) {
    User user = userRepository.findById(id)
        .orElseThrow(() -> new UserNotFoundException(id));
    return ResponseEntity.ok(user);
}
```



## @ExceptionHandler

La anotación `@ExceptionHandler` en Spring se utiliza para manejar excepciones específicas que pueden ocurrir durante la ejecución de un controlador en una aplicación web. Esta anotación se coloca sobre un método en una clase de controlador y le indica a Spring que, cuando se lanza una excepción de un tipo especificado, el método anotado debe ser invocado para manejar dicha excepción.

## ResponseEntity

`ResponseEntity` es una clase en Spring que representa la respuesta HTTP completa. Se utiliza principalmente en controladores RESTful para personalizar la respuesta HTTP en términos de estado, cabeceras y cuerpo de la respuesta. Aquí hay un desglose de para qué se usa `ResponseEntity`:

1. **Personalización del Estado HTTP**: Permite especificar el estado HTTP (como 200 OK, 404 Not Found, etc.) que se devolverá al cliente.
2. **Incluir Cabeceras HTTP**: Se pueden agregar cabeceras HTTP personalizadas a la respuesta.
3. **Definir el Cuerpo de la Respuesta**: Permite especificar el cuerpo de la respuesta, que puede ser cualquier objeto que luego se convierte a JSON o XML según la configuración de Spring.

## @ResponseStatus

La anotación `@ResponseStatus` en Spring se utiliza para marcar una clase de excepción con un código de estado HTTP específico. Esto permite que cuando se lance esa excepción, el servidor devuelva automáticamente el código de estado HTTP configurado sin necesidad de manejarlo explícitamente en cada controlador.

> `HttpStatus` en Spring es una enumeración (`enum`) que forma parte del paquete `org.springframework.http`. Representa los **códigos de estado HTTP** (como `200 OK`, `404 Not Found`, `500 Internal Server Error`, etc.) que puedes usar para controlar las respuestas HTTP en controladores REST.

### Códigos de Estado Comunes

- `HttpStatus.OK` (200): Solicitud exitosa.
- `HttpStatus.CREATED` (201): Recurso creado exitosamente.
- `HttpStatus.NO_CONTENT` (204): Solicitud exitosa pero sin contenido en la respuesta.
- `HttpStatus.BAD_REQUEST` (400): Solicitud inválida.
- `HttpStatus.UNAUTHORIZED` (401): No autorizado.
- `HttpStatus.FORBIDDEN` (403): Prohibido.
- `HttpStatus.NOT_FOUND` (404): Recurso no encontrado.
- `HttpStatus.METHOD_NOT_ALLOWED` (405): Método no permitido.
- `HttpStatus.CONFLICT` (409): Conflicto en la solicitud.
- `HttpStatus.INTERNAL_SERVER_ERROR` (500): Error interno del servidor.
- `HttpStatus.NOT_IMPLEMENTED` (501): No implementado.
- `HttpStatus.BAD_GATEWAY` (502): Puerta de enlace incorrecta.
- `HttpStatus.SERVICE_UNAVAILABLE` (503): Servicio no disponible.

Ejemplo

```java
@RestController
@RequestMapping("/api/users")
public class UserController {

    @Autowired
    private UserRepository userRepository;

    @GetMapping("/{id}")
    public ResponseEntity<User> getUserById(@PathVariable Long id) {
        Optional<User> user = userRepository.findById(id);

        if (user.isPresent()) {
            return new ResponseEntity<>(user.get(), HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
}
```



## HttpMessageNotWritableException

La excepción `HttpMessageNotWritableException` en Spring Framework se lanza cuando el framework no puede escribir un cuerpo de mensaje HTTP para una respuesta. Esto puede suceder por varias razones, como problemas con la serialización de objetos a JSON o XML, configuraciones incorrectas del convertidor de mensajes HTTP, o restricciones en los tipos de datos.

### Posibles Causas de `HttpMessageNotWritableException`

1. **Problemas de Serialización**: Si un objeto no puede ser serializado correctamente a JSON o XML. Por ejemplo, si hay un ciclo en las referencias de los objetos que Jackson no puede resolver.
2. **Configuración Incorrecta del Convertidor de Mensajes**: Si no hay un convertidor adecuado configurado para el tipo de contenido (por ejemplo, Jackson no está en el classpath para JSON).
3. **Accesibilidad del Objeto**: Si el objeto a serializar contiene propiedades privadas sin métodos getter públicos.
4. **Errores en los Datos**: Si los datos del objeto contienen valores no válidos o inesperados que el convertidor no puede manejar.

## NullPointerException

`NullPointerException` es una excepción en Java que se lanza cuando se intenta utilizar una referencia que apunta a `null` en lugar de una instancia válida de un objeto. Esta excepción es una de las más comunes y puede ocurrir en varias situaciones, como al intentar acceder a métodos o propiedades de un objeto no inicializado.



## Ejercicio

1. Clone el repo https://github.com/trainingLeader/hexagonal-app.git

2. Cree una clase controller llamada AppController

   ```java
   package com.hexagonal.hexagonal_app.infrastructure.controllers;
   
   import org.springframework.web.bind.annotation.RestController;
   import org.springframework.web.bind.annotation.GetMapping;
   
   @RestController
   public class AppController {
   
       @GetMapping("/app")
       public String index(){
           return "Ok 200";
       }
   }
   
   ```

   Agregue al endPoint int valor = 100/0;

   ```java
   package com.hexagonal.hexagonal_app.infrastructure.controllers;
   
   import org.springframework.web.bind.annotation.RestController;
   import org.springframework.web.bind.annotation.GetMapping;
   
   @RestController
   public class AppController {
   
       @GetMapping("/app")
       public String index(){
           int valor = 100/0;
           return "Ok 200";
       }
   }
   ```

   > 		"timestamp": "2024-08-27T13:35:03.993+00:00",
   > 		"status": 500,
   > 		"error": "Internal Server Error",
   > 		"trace": "java.lang.ArithmeticException: / by zero\r\n\tat com.hexagonal.hexagonal_app.infrastructure.controllers.AppController.index(AppController.java:11)\r\n\tat java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)\r\n\tat java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77)\r\n\tat java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)\r\n\tat java.base/java.lang.reflect.Method.invoke(Method.java:568)\r\n\tat org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:255)\r\n\tat 

3. Cree paquete models en el paquete infrastructure

4. En models cree una clase llamada ErrorCustom y genere los metodos Getter y Setter

   ```java
   public class ErrorCustom {
       private String message;
       private String error;
       private int status;
       private Date date;
       public String getMessage() {
           return message;
       }
       public void setMessage(String message) {
           this.message = message;
       }
       public String getError() {
           return error;
       }
       public void setError(String error) {
           this.error = error;
       }
       public int getStatus() {
           return status;
       }
       public void setStatus(int status) {
           this.status = status;
       }
       public Date getDate() {
           return date;
       }
       public void setDate(Date date) {
           this.date = date;
       }
   }
   ```

   

5. Cree un nuevo controller llamada HandleExceptionController y agregue la anotacion @RestControllerAdvice

6. Agregue el siguiente método en el HandlerExceptionController

   ```java
       @ExceptionHandler({ArithmeticException.class})
       public ResponseEntity<ErrorCustom> divisionByZero(Exception ex) {
   
           ErrorCustom error = new ErrorCustom();
           error.setDate(new Date());
           error.setError("Error division por cero!");
           error.setMessage(ex.getMessage());
           error.setStatus(HttpStatus.INTERNAL_SERVER_ERROR.value());
   
           // return ResponseEntity.internalServerError().body(error);
           return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR.value()).body(error);
       }
   ```

   > import java.util.Date;
   >
   > import java.util.HashMap;
   >
   > import java.util.Map;
   >
   > import org.springframework.http.HttpStatus;
   >
   > import org.springframework.http.ResponseEntity;
   >
   > import org.springframework.http.converter.HttpMessageNotWritableException;
   >
   > import org.springframework.web.bind.annotation.ExceptionHandler;
   >
   > import org.springframework.web.bind.annotation.ResponseStatus;
   >
   > import org.springframework.web.bind.annotation.RestControllerAdvice;
   >
   > import org.springframework.web.servlet.NoHandlerFoundException;

   **Explicación**

   Anotación `@ExceptionHandler`: Esta anotación indica que el método `divisionByZero` se utilizará para manejar excepciones del tipo `ArithmeticException`. Spring llamará automáticamente a este método cuando ocurra una excepción de este tipo en cualquier parte del controlador donde esté definido.

   Definición del método `divisionByZero`: Este método recibe como parámetro una excepción (`Exception ex`) y devuelve un objeto `ResponseEntity<ErrorCustom>`. `ResponseEntity` es una clase que representa una respuesta HTTP completa, incluyendo el cuerpo, el estado y los encabezados.

   Creación de un objeto `ErrorCustom`: Aquí se crea una instancia de la clase `ErrorCustom` (que se asume es una clase personalizada para representar detalles de errores). Se configuran varios atributos del error:

   - `date`: la fecha y hora actual.
   - `error`: un mensaje genérico indicando que ocurrió un error de división por cero.
   - `message`: el mensaje de la excepción original, que proporciona más detalles sobre lo que salió mal.
   - `status`: el código de estado HTTP `500` (Internal Server Error).

   **return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR.value()).body(error)**;  Finalmente, el método devuelve un `ResponseEntity` con el código de estado HTTP `500` y el cuerpo de la respuesta que contiene el objeto `ErrorCustom` con los detalles del error.

   > {
   > 	"message": "/ by zero",
   > 	"error": "Error division por cero!",
   > 	"status": 500,
   > 	"date": "2024-08-27T13:54:21.597+00:00"
   > }

 7. Error 404 : Agregue el siguiente método

    ```java
    @ExceptionHandler(NoHandlerFoundException.class)
    public ResponseEntity<ErrorCustom> notFoundEx(NoHandlerFoundException e) { 
            ErrorCustom error = new ErrorCustom();
            error.setDate(new Date());
            error.setError("Api rest no encontrado");
            error.setMessage(e.getMessage());
    
            error.setStatus(HttpStatus.NOT_FOUND.value());
            
            return ResponseEntity.status(HttpStatus.NOT_FOUND.value()).body(error);
    }
    ```

    8. En el archivo de properties agregue **spring.web.resources.add-mappings=false**

    ## Excepciones personalizadas

    1. Cree una nueva clase llamada Use y Role en domain>entities

       ```java
       public class Role {
           private String name;
       
           public String getName() {
               return name;
           }
       
           public void setName(String name) {
               this.name = name;
           }
       }
       ```

       ```java
       public class User {
           private Long id;
           private String name;
           private String lastname;
       
           private Role role;
           
           public User(Long id, String name, String lastname) {
               this.id = id;
               this.name = name;
               this.lastname = lastname;
           }
           public User() {
           }
           public Long getId() {
               return id;
           }
           public void setId(Long id) {
               this.id = id;
           }
           public String getName() {
               return name;
           }
           public void setName(String name) {
               this.name = name;
           }
           public String getLastname() {
               return lastname;
           }
           public void setLastname(String lastname) {
               this.lastname = lastname;
           }
           public Role getRole() {
               return role;
           }
           // public String getRoleName() {
           //     return role.getName();
           // }
           public void setRole(Role role) {
               this.role = role;
           }
       }
       ```

    2. Cree un interface llamada IUserService

       ```java
       import java.util.List;
       import java.util.Optional;
       
       public interface IUserService {
           List<User> findAll();
           Optional<User> findById(Long id);
       }
       ```

    3. Implemente el IUserService. Cree una nueva clase en Infrastructure>repository

       ```java
       import org.springframework.beans.factory.annotation.Autowired;
       import org.springframework.stereotype.Service;
       
       import com.hexagonal.hexagonal_app.application.service.product.IUserService;
       import com.hexagonal.hexagonal_app.domain.entities.User;
       
       import java.util.List;
       import java.util.Optional;
       
       @Service
       public class UserImpl implements IUserService {
       
           @Autowired
           private List<User> users;
       
           @Override
           public List<User> findAll() {
               return users;
           }
       
           @Override
           public Optional<User> findById(Long id) {
               return users.stream().filter( usr -> usr.getId().equals(id) ).findFirst();
           }
       }
       ```

       Cree un archivo de configuración llamado AppConfig. Recuerde que este archivo se crea a nivel del paquete principal.

       ```java
       import java.util.ArrayList;
       import java.util.List;
       
       import org.springframework.context.annotation.Bean;
       import org.springframework.context.annotation.Configuration;
       
       import com.hexagonal.hexagonal_app.domain.entities.User;
       
       @Configuration
       public class AppConfig {
       
           @Bean
           List<User> users(){
               List<User> users = new ArrayList<>();
                    users.add(new User(1L,"Carlos","Patiño"));
                    return users;
           }
       }
       ```
    
       En la clase **HandlerExceptionController** incorpore el siguiente codigo sino se encuentra implementado:
    
       ```java
       @ExceptionHandler(NoHandlerFoundException.class)
       public ResponseEntity<ErrorCustom> notFoundEx(NoHandlerFoundException e) { 
               ErrorCustom error = new ErrorCustom();
               error.setDate(new Date());
               error.setError("Api rest no encontrado");
               error.setMessage(e.getMessage());
       
               error.setStatus(HttpStatus.NOT_FOUND.value());
               
               return ResponseEntity.status(HttpStatus.NOT_FOUND.value()).body(error);
       }
       ```

       

       ## Excepciones Usando Api Optional Java 8
    
       
    
    4. el siguiente método en HandlerExceptionController
    
       ```java
           @ExceptionHandler({NullPointerException.class, HttpMessageNotWritableException.class,UserNotFoundException.class})
           @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
           public Map<String, Object> userNotFoundException(Exception ex){
       
               Map<String, Object> error = new HashMap<>();
               error.put("date", new Date());
               error.put("error", "el usuario o role no existe!");
               error.put("message", ex.getMessage());
               error.put("status", HttpStatus.INTERNAL_SERVER_ERROR.value());
       
               return error;
           }
       ```
    
    5. En el paquete Infrastructure cree un nuevo paquete llamado exception y Cree una nueva clase llamada UserNotFoundException y agregue el siguiente codigo a la clase.
    
       ```java
       package com.hexagonal.hexagonal_app.infrastructure.models.exception;
       
       public class UserNotFoundException extends RuntimeException {
           public UserNotFoundException(String message) {
               super(message);
           } 
       }
       ```



# Validación datos (Validation)

## Explicación de las Anotaciones

- `@NotBlank`: Asegura que la propiedad no sea `null` y que la cadena no esté vacía ni compuesta solo por espacios en blanco.
- `@Size(min =, max =)`: Restringe el tamaño de la cadena a un rango específico.
- `@Email`: Valida que la propiedad sea una dirección de correo electrónico válida.
- `@Pattern`: Valida que la cadena coincida con la expresión regular proporcionada.
- `@Valid`: Se usa en el controlador para validar el objeto entrante basado en las anotaciones de validación presentes en la clase.

Ejemplo

```java
package com.asociacionesapp.app_relationship.entities;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotNull;
import java.util.Set;

@Entity
@Table(name="clients")
public class Client {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotNull(message = "El nombre no puede ser nulo")
    private String name;

    @NotNull(message = "El correo electrónico no puede ser nulo")
    @Email(message = "Debe proporcionar un correo electrónico válido")
    private String email;

    @NotNull(message = "El número de teléfono no puede ser nulo")
    @Pattern(regexp = "^\\+?[0-9. ()-]{7,25}$", message = "Debe proporcionar un número de teléfono válido")
    private String phoneNumber;

    @OneToMany(mappedBy = "client")
    private Set<Invoice> invoices;

    // Getters y setters
}

```

## Taller de validaciones

1. Instalar la dependencia  validation

   ![93](Manuales\imgspring\news\93.png)

   ![94](Manuales\imgspring\news\94.png)

   2. Agregar la anotación @Valid en el qRequestBody del controlador.

      ![95](Manuales\imgspring\news\95.png)

     3. Agregue anotaciones de validacion en los atributos de la Entidad relacionada con el controlador.

        ![96](Manuales\imgspring\news\96.png)

        

## Personalizando respuesta con mensaje de error (BindingResult)

`BindingResult` es una interfaz en Spring que representa los resultados de la validación de un objeto. Se utiliza en los controladores para capturar y manejar errores de validación cuando se procesan formularios o solicitudes que contienen datos del cliente.

### Función de `BindingResult`

- **Captura de errores de validación**: `BindingResult` almacena los errores de validación que ocurren cuando se intenta vincular los datos del cliente a un objeto de dominio o DTO.
- **Proporciona detalles de errores**: Permite acceder a detalles específicos de los errores, como qué campos tienen errores y qué mensajes de error están asociados con esos campos.
- **Facilita el manejo de errores en el controlador**: Permite al controlador manejar errores de validación de manera programática, proporcionando retroalimentación útil al cliente.

### Beneficios de `BindingResult`

- **Manejo eficiente de errores**: Proporciona una manera clara y estructurada de manejar errores de validación en los controladores.
- **Detalles de errores**: Permite acceder a mensajes de error específicos y relevantes, lo que facilita la retroalimentación al usuario.
- **Integración con Spring**: Se integra perfectamente con el sistema de validación de Spring, facilitando la configuración y el uso.

Aplicando validacion en el Controller

```java
package com.breakline.survey.app_survey.web.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.breakline.survey.app_survey.domain.service.catalog.ICatalog;
import com.breakline.survey.app_survey.persistence.entity.Catalog;

import jakarta.validation.Valid;

import java.util.*;

@RestController
@RequestMapping("/catalogs")
public class CatalogController {

    @Autowired
    private ICatalog service;

    @GetMapping
    public List<Catalog> listCatalog(){
        return service.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Catalog> view(@PathVariable Long id){
        Optional<Catalog> catalogOpt = service.findById(id);
        if(catalogOpt.isPresent()){
            return ResponseEntity.ok(catalogOpt.orElseThrow());
        }
        return ResponseEntity.notFound().build();
    }

    @PostMapping
    public ResponseEntity<?> create(@Valid @RequestBody Catalog catalog, BindingResult result){
        if (result.hasFieldErrors()) {
            return validation(result);
        }
        return ResponseEntity.status(HttpStatus.CREATED).body(service.save(catalog));
    }

    @PutMapping("/{id}")
    public ResponseEntity<?> update(@Valid @RequestBody Catalog catalog,BindingResult result,@PathVariable Long id){
        if (result.hasFieldErrors()) {
            return validation(result);
        }
        Optional<Catalog> catalogOpt = service.update(id, catalog);
        if (catalogOpt.isPresent()){
           return ResponseEntity.status(HttpStatus.CREATED).body(catalogOpt.orElseThrow());  
        }
        return ResponseEntity.notFound().build();
    }
    @DeleteMapping("/{id}")
    public ResponseEntity<Catalog> delete(@PathVariable Long id){
        Catalog catalog = new Catalog();
        catalog.setId(id);
        Optional<Catalog> catalogOpt = service.delete(id);
        if(catalogOpt.isPresent()){
            return ResponseEntity.ok(catalogOpt.orElseThrow());
        }
        return ResponseEntity.notFound().build();
    }
    private ResponseEntity<?> validation(BindingResult result) {
        Map<String, String> errors = new HashMap<>();

        result.getFieldErrors().forEach(err -> {
            errors.put(err.getField(), "El campo " + err.getField() + " " + err.getDefaultMessage());
        });
        return ResponseEntity.badRequest().body(errors);
    }
}
```

# Mensajes de errores personalizados usando properties

1. Cree un nuevo archivo properties; para el ejemplo message.properties

2. En el paquete principal aplique la anotacion PropertySource para importar el archivo de propiedades creado.

   ![97](Manuales\imgspring\news\97.png)

3. En las propiedades de la entidad aplique la valor de la propiedad.

   ![98](Manuales\imgspring\news\98.png)

# Validacion personalizada usando la clase validation

Cree una nueva clase llamada ProductValidation e implemente Validator de springboot. La clase se crea a nivel de paquete principal.

```java
import org.springframework.stereotype.Component;
import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;
import org.springframework.validation.Validator;

import com.andres.curso.springboot.app.springbootcrud.entities.Product;

@Component
public class ProductValidation implements Validator {

    @Override
    public boolean supports(Class<?> clazz) {
        return Product.class.isAssignableFrom(clazz);
    }

    @Override
    public void validate(Object target, Errors errors) {
        Product product = (Product) target;
        ValidationUtils.rejectIfEmptyOrWhitespace(errors, "name", null, "es requerido!");
        // ValidationUtils.rejectIfEmptyOrWhitespace(errors, "description", "NotBlank.product.description");
        if (product.getDescription() == null || product.getDescription().isBlank()) {
            errors.rejectValue("description", null, "es requerido, por favor");
        }

        if (product.getPrice() == null) {
            errors.rejectValue("price", null, "no puede ser nulo, ok!");
        } else if (product.getPrice() < 500) {
            errors.rejectValue("price", null, "debe ser un valor numerico mayor o igual que 500!");
        }

    }
}
```

Aplique la validacion al controlador especifico; para el ejemplo a productcontroller. Agregue **validation.validate(product, result);** a el metodo post y put.

```java
@PostMapping
public ResponseEntity<?> create(@Valid @RequestBody Product product, BindingResult result) {
  validation.validate(product, result);
  if (result.hasFieldErrors()) {
            return validation(result);
  }
  return ResponseEntity.status(HttpStatus.CREATED).body(service.save(product));
}

@PutMapping("/{id}")
public ResponseEntity<?> update(@Valid @RequestBody Product product, BindingResult result, @PathVariable Long id) {
   validation.validate(product, result);
   if (result.hasFieldErrors()) {
       return validation(result);
   }
   Optional<Product> productOptional = service.update(id, product);
   if (productOptional.isPresent()) {
            return ResponseEntity.status(HttpStatus.CREATED).body(productOptional.orElseThrow());
   }
   return ResponseEntity.notFound().build();
}
```

# Validacion personalizada usando anotaciones

Comente o elimine las lineas de codigo usadas en la validación por clases y cree un nuevo paquete llamado **validations** en infrastructure.

Cree una nueva interface llamada isRequired.

```java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.lang.annotation.ElementType;

@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.FIELD, ElementType.METHOD })
public @interface isRequired {

}
```

Agregue el siguiente codigo a la interface

```java
	String message() default "El atributo es requerido y no puede se vacio";

	Class<?>[] groups() default { };

	Class<? extends Payload>[] payload() default { };
```

```java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.lang.annotation.ElementType;

@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.FIELD, ElementType.METHOD })
public @interface isRequired {
	String message() default "El atributo es requerido y no puede se vacio";

	Class<?>[] groups() default { };

	Class<? extends Payload>[] payload() default { };
}
```

Cree una nueva clase llamada **RequiredValidation** para enlazar la anotacion isRequired

```java
import org.springframework.util.StringUtils;

import jakarta.validation.ConstraintValidator;
import jakarta.validation.ConstraintValidatorContext;

public class RequiredValidation implements ConstraintValidator<isRequired, String>{

    @Override
    public boolean isValid(String value, ConstraintValidatorContext context) {
        // return (value != null && !value.isEmpty() && !value.isBlank());
        return StringUtils.hasText(value);
    }

}
```

**Imports:**

- `import org.springframework.util.StringUtils;`: Importa utilidades de Spring, en este caso, el método `hasText()` que se utiliza para verificar si un `String` no está vacío, no es nulo y contiene caracteres visibles.
- `import jakarta.validation.ConstraintValidator;`: Importa la interfaz `ConstraintValidator`, que se utiliza para crear validadores personalizados en el contexto de validaciones de Java Bean.
- `import jakarta.validation.ConstraintValidatorContext;`: Importa el contexto de validación, que permite personalizar el mensaje de error o interactuar con el proceso de validación.

**Clase `RequiredValidation`:**

- Esta clase implementa `ConstraintValidator`, especificando que va a validar campos de tipo `String` anotados con la anotación `@isRequired`.

**Métodos:**

- `isValid(String value, ConstraintValidatorContext context)`: Este método es la implementación del validador. Se invoca durante la validación del campo.

Enlace la interface de tipo anotación con la clase RequiredValidation. Para realizar este proceso use la instrucción @Constraint(validatedBy = RequiredValidation.class)

```java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

import jakarta.validation.Constraint;
import jakarta.validation.Payload;

import java.lang.annotation.ElementType;

@Constraint(validatedBy = RequiredValidation.class)
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.FIELD, ElementType.METHOD })
public @interface isRequired {
	String message() default "El atributo es requerido y no puede se vacio";

	Class<?>[] groups() default { };

	Class<? extends Payload>[] payload() default { };
}

```

Ahora ya puede implementar la anotación de validacion personaliza en los atributos de la clase.

```java
    @isRequired(message = "{isRequired.product.name}")
    @Size(min=3, max=20)
    private String name;
    
    @isRequired
    private String description;
```



# ORM

Un ORM (Object-Relational Mapping, por sus siglas en inglés) es una técnica de programación que permite convertir datos entre sistemas incompatibles usando lenguajes de programación orientados a objetos. En términos más simples, un ORM permite mapear objetos en el código a tablas en una base de datos relacional, lo que facilita el trabajo con bases de datos utilizando conceptos de programación orientada a objetos.

## Características de un ORM

1. **Mapeo de clases a tablas**: Las clases de la aplicación se mapean a tablas de la base de datos.
2. **Mapeo de atributos a columnas**: Los atributos de las clases se mapean a columnas de las tablas.
3. **Automatización de operaciones CRUD**: Proporciona métodos para crear, leer, actualizar y eliminar (CRUD) registros en la base de datos sin escribir consultas SQL explícitas.
4. **Gestión de relaciones**: Facilita la gestión de relaciones entre entidades (uno a uno, uno a muchos, muchos a uno, muchos a muchos).
5. **Abstracción de la base de datos**: Permite cambiar de una base de datos a otra con mínimas modificaciones en el código de la aplicación.

## Ventajas de usar un ORM

1. **Productividad**: Reduce la cantidad de código que los desarrolladores necesitan escribir para interactuar con la base de datos.
2. **Mantenimiento**: Facilita el mantenimiento del código al evitar SQL embebido en el código de la aplicación.
3. **Portabilidad**: Habilita la portabilidad del código entre diferentes sistemas de gestión de bases de datos.
4. **Seguridad**: Ayuda a prevenir ataques de inyección SQL al permitir la manipulación de datos a través de métodos seguros.
5. **Abstracción**: Proporciona una capa de abstracción que permite trabajar con datos en términos de objetos y relaciones, en lugar de tablas y columnas.

## Ejemplos de ORM populares

- **Hibernate**: Un ORM para Java que implementa la especificación JPA (Java Persistence API).
- **Entity Framework**: Un ORM para .NET que facilita la manipulación de datos en aplicaciones basadas en C#.
- **Django ORM**: Un ORM integrado en el framework Django para aplicaciones Python.
- **SQLAlchemy**: Un ORM para Python que proporciona una API flexible para interactuar con bases de datos.

# JPA (https://spring.io/projects/spring-data)

JPA (Java Persistence API) es una especificación de Java que estandariza el mapeo de objetos Java a tablas en bases de datos relacionales. JPA proporciona un marco común para el acceso y la gestión de datos persistentes en aplicaciones Java, definiendo una API para realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) y consultas en bases de datos de manera uniforme.

## Características de JPA

1. **Mapeo de Entidades**: Define cómo mapear las clases Java a tablas en la base de datos utilizando anotaciones.
2. **Consultas**: Proporciona JPQL (Java Persistence Query Language) para escribir consultas orientadas a objetos.
3. **Gestión del Ciclo de Vida de Entidades**: Gestiona el ciclo de vida de las entidades (persistencia, fusión, eliminación).
4. **Relaciones entre Entidades**: Facilita la definición de relaciones entre entidades (uno a uno, uno a muchos, muchos a uno, muchos a muchos).
5. **Transacciones**: Maneja transacciones para asegurar la integridad y consistencia de los datos.

## Componentes Principales de JPA

1. **Entidades**: Clases Java que representan las tablas en la base de datos.
2. **Entity Manager**: La interfaz principal de JPA que gestiona las operaciones de persistencia.
3. **Persistencia**: El contexto de persistencia define el entorno en el que se gestionan las entidades.
4. **Consultas**: JPQL permite realizar consultas a la base de datos de manera similar a SQL, pero con un enfoque orientado a objetos.

# JPA Query Methods(https://docs.spring.io/spring-data/jpa/reference/jpa/query-methods.html)

## Qué son los JPA Query Methods?

Los JPA Query Methods son métodos de consulta definidos en los repositorios de Spring Data JPA. Estos métodos permiten realizar consultas a la base de datos sin necesidad de escribir consultas SQL explícitas. Spring Data JPA genera automáticamente las consultas basadas en los nombres de los métodos siguiendo ciertas convenciones.

## Convenciones de Nombres en JPA Query Methods

Los nombres de los métodos de consulta siguen ciertas convenciones para que Spring Data JPA pueda derivar la consulta. Aquí hay algunos ejemplos y una lista de las convenciones más comunes:

```java
package com.example.demo.domain.repository;

import com.example.demo.domain.model.ExampleEntity;
import org.springframework.data.repository.CrudRepository;

import java.util.List;
import java.util.Optional;

public interface ExampleRepository extends CrudRepository<ExampleEntity, Long> {

    // Búsqueda por un campo específico
    Optional<ExampleEntity> findByName(String name);

    // Búsqueda por múltiples campos
    List<ExampleEntity> findByAgeAndAddress_City(int age, String city);

    // Búsqueda con ordenación
    List<ExampleEntity> findByAgeOrderByAddress_CityAsc(int age);

    // Búsqueda con clausula "Like"
    List<ExampleEntity> findByNameContaining(String keyword);

    // Búsqueda con clausula "Between"
    List<ExampleEntity> findByAgeBetween(int startAge, int endAge);

    // Búsqueda con clausula "In"
    List<ExampleEntity> findByNameIn(List<String> names);

    // Búsqueda con clausula "GreaterThan" y "LessThan"
    List<ExampleEntity> findByAgeGreaterThan(int age);
    List<ExampleEntity> findByAgeLessThan(int age);

    // Búsqueda con clausula "IsNull" y "IsNotNull"
    List<ExampleEntity> findByAddress_IsNull();
    List<ExampleEntity> findByAddress_IsNotNull();
}

```

## Lista de Convenciones de Nombres en JPA Query Methods

Aquí hay una lista de las convenciones de nombres más comunes que puedes usar en tus métodos de consulta:

- ### **Simple Keyword**:

  - `findBy`: Encuentra por un campo específico.
  - `readBy`: Lee por un campo específico.
  - `queryBy`: Consulta por un campo específico.
  - `countBy`: Cuenta por un campo específico.
  - `getBy`: Obtiene por un campo específico.

- ### **Palabras Clave Lógicas**:

  - `And`: Conjunción lógica (y).
  - `Or`: Conjunción lógica (o).

- ### **Palabras Clave de Comparación**:

  - `Is`, `Equals`: Igual a.
  - `Between`: Entre dos valores.
  - `LessThan`, `LessThanEqual`: Menor que, menor o igual que.
  - `GreaterThan`, `GreaterThanEqual`: Mayor que, mayor o igual que.
  - `After`, `Before`: Después de, antes de (normalmente utilizado con fechas).
  - `IsNull`, `IsNotNull`, `NotNull`: Nulo, no nulo.
  - `Like`: Similar a (uso de comodines `%` y `_`).
  - `NotLike`: No similar a.
  - `StartingWith`: Comienza con.
  - `EndingWith`: Termina con.
  - `Containing`: Contiene.
  - `OrderBy`: Ordenado por.

- ### **Palabras Clave de Colección**:

  - `In`: En una colección.
  - `NotIn`: No en una colección.

  ## Taller JPA

  1. Cree un nuevo proyecto

  2. Agregue las dependencias JPA, MysqlDriver y Devtools

     ![78](Manuales\imgspring\news\78.png)

       3. Cree paquete entities.

          <img src="Manuales\imgspring\news\79.png" alt="79" style="zoom: 67%;" />

          4. En la clase principal del proyecto implemente la interfaz CommandLineRunner

          <img src="Manuales\imgspring\news\80.png" alt="80" style="zoom:67%;" />

          5. Cree la clase person en entities

          ```java
          package com.appjpa.app_jpa.entities;
          
          import jakarta.persistence.Column;
          import jakarta.persistence.Entity;
          import jakarta.persistence.GeneratedValue;
          import jakarta.persistence.GenerationType;
          import jakarta.persistence.Id;
          import jakarta.persistence.Table;
          
          @Entity
          @Table(name="persons")
          public class Person {
          
              @Id
              @GeneratedValue(strategy = GenerationType.IDENTITY)
              private Long id;
          
              private String name;
              private String lastname;
          
              @Column(name = "programming_language")
              private String programmingLanguage;
          
              public Person() {
              }
          
              public Person(Long id, String name, String lastname, String programmingLanguage) {
                  this.id = id;
                  this.name = name;
                  this.lastname = lastname;
                  this.programmingLanguage = programmingLanguage;
              }
          
              public Long getId() {
                  return id;
              }
              public void setId(Long id) {
                  this.id = id;
              }
              public String getName() {
                  return name;
              }
              public void setName(String name) {
                  this.name = name;
              }
              public String getLastname() {
                  return lastname;
              }
              public void setLastname(String lastname) {
                  this.lastname = lastname;
              }
              public String getProgrammingLanguage() {
                  return programmingLanguage;
              }
              public void setProgrammingLanguage(String programmingLanguage) {
                  this.programmingLanguage = programmingLanguage;
              }
          
              @Override
              public String toString() {
                  return "[id=" + id + ", name=" + name + ", lastname=" + lastname + ", programmingLanguage="
                          + programmingLanguage + "]";
              }
          
              
          }
          ```

          6. Establezca la configuracion de conexion a la base de datos en el archivo properties

             ```
             spring.application.name=app-jpa
             spring.datasource.url=jdbc:mysql://localhost:3306/db_jpademo
             spring.datasource.username=root
             spring.datasource.password=123456
             spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
             spring.jpa.database-platform=org.hibernate.dialect.MySQLDialect
             spring.jpa.show-sql=true
             spring.jpa.hibernate.ddl-auto=create
             ```

          7. Cree el paquete repositories y cree una interface llamada PersonRepository

             ```java
             package com.appjpa.app_jpa.repositories;
             
             import org.springframework.data.repository.CrudRepository;
             
             import com.appjpa.app_jpa.entities.Person;
             
             public interface PersonRepository extends CrudRepository<Person,Long> {
             
             }
             ```

            8. Inyecte el repositorio PersonRepository en la clase principal.

               <img src="Manuales\imgspring\news\81.png" alt="81" style="zoom:67%;" />

             9. Cree el archivo import.sql en resources

                ![82](Manuales\imgspring\news\82.png)

                En el archivo creado agregue insert de prueba por ejemplo:

                ```sql
                INSERT INTO persons (name, lastname, programming_language) VALUES ('Johlver', 'Pardo', 'Java');
                INSERT INTO persons (name, lastname, programming_language) VALUES ('Miguel', 'Catro', 'JavaScript');
                INSERT INTO persons (name, lastname, programming_language) VALUES ('Jose', 'Manuel', 'React Native');
                ```


​				

## @Transactional

### ¿Qué es `@Transactional`?

`@Transactional` es una anotación proporcionada por Spring que se utiliza para demarcar los límites de una transacción. Cuando un método anotado con `@Transactional` es ejecutado, Spring gestiona automáticamente el inicio, la confirmación (commit) y la reversión (rollback) de la transacción. Esto simplifica la gestión de transacciones en la aplicación y asegura que todas las operaciones dentro del método se realicen de manera atómica.

### ¿Para qué se usa `@Transactional`?

1. **Garantizar Atomicidad**: Asegura que todas las operaciones dentro de una transacción se completen exitosamente o ninguna de ellas se complete en caso de error.
2. **Manejo de Errores**: Facilita la reversión automática de cambios en caso de que se produzca una excepción.
3. **Consistencia de Datos**: Mantiene la consistencia de los datos al asegurarse de que todas las operaciones relacionadas con una transacción se realicen en un único contexto transaccional.
4. **Simplificación de Código**: Reduce la cantidad de código necesario para manejar transacciones explícitamente.

### Configuración de Transacciones

Spring permite configurar el comportamiento de las transacciones mediante varios atributos de la anotación `@Transactional`:

- **propagation**: Define el comportamiento de propagación de la transacción. Por ejemplo, `REQUIRED` (valor por defecto) indica que el método debe ejecutarse dentro de una transacción existente o iniciar una nueva si no hay ninguna.

- **isolation**: Define el nivel de aislamiento de la transacción, como `READ_COMMITTED`, `REPEATABLE_READ`, `SERIALIZABLE`.

- **timeout**: Especifica el tiempo máximo que la transacción puede ejecutarse antes de ser revertida automáticamente.

- **readOnly**: Indica si la transacción es solo de lectura, lo cual puede ayudar a optimizar el rendimiento.

  **¿Qué es `@Transactional(readOnly = true)`?**

  `@Transactional(readOnly = true)` es una configuración de transacción en la cual se indica que la transacción no realizará ninguna operación de escritura en la base de datos. Esta configuración es útil para consultas y operaciones que no modifican los datos, asegurando que el contexto de persistencia de Hibernate (o el ORM utilizado) se optimice para operaciones de lectura.

  **¿Para qué se usa `@Transactional(readOnly = true)`?**

  1. **Optimización del Rendimiento**: Las operaciones de lectura pueden ser optimizadas por el gestor de la base de datos y el ORM, ya que no se necesita gestionar la sincronización de cambios en el contexto de persistencia.
  2. **Bloqueos Menores**: Reduce el nivel de bloqueo en la base de datos, permitiendo un mayor nivel de concurrencia. Las transacciones de solo lectura no requieren los mismos niveles de bloqueo que las de escritura.
  3. **Consistencia**: Asegura que las operaciones de consulta no alteren el estado de la base de datos, proporcionando una garantía adicional de consistencia.

- **rollbackFor**: Define las excepciones que provocarán la reversión de la transacción.

```java
@Transactional(propagation = Propagation.REQUIRED, isolation = Isolation.READ_COMMITTED, timeout = 30, rollbackFor = Exception.class)
public void realizarOperacionCompleja() {
    // Operaciones de la transacción
}
```

Explicación:

La transacción tiene un nivel de propagación `REQUIRED`.

El nivel de aislamiento es `READ_COMMITTED`.

El tiempo máximo de ejecución es de 30 segundos.

La transacción se revertirá en caso de cualquier excepción.

# Hibérnate eventos y ciclo de vida

En el contexto de JPA y Hibernate, los eventos y el ciclo de vida de una entidad se refieren a los distintos estados por los que pasa una entidad desde su creación hasta su eliminación, y los eventos que pueden ser interceptados para ejecutar lógica personalizada en esos puntos del ciclo de vida.

## Ciclo de Vida de una Entidad JPA

El ciclo de vida de una entidad JPA comprende los siguientes estados:

1. **New (Transiente)**: La entidad ha sido creada pero no está asociada a un contexto de persistencia. No tiene representación en la base de datos.
2. **Managed (Persistente)**: La entidad está asociada a un contexto de persistencia (EntityManager) y cualquier cambio en la entidad se sincroniza con la base de datos.
3. **Detached (Desasociada)**: La entidad ha estado en un contexto de persistencia, pero ahora está fuera de él. Las modificaciones en esta entidad no serán sincronizadas con la base de datos.
4. **Removed (Eliminada)**: La entidad está marcada para eliminación en el contexto de persistencia, pero aún no ha sido eliminada de la base de datos.

## Eventos del Ciclo de Vida

JPA proporciona anotaciones para interceptar eventos del ciclo de vida de una entidad. Estas anotaciones se pueden usar para ejecutar lógica personalizada en puntos específicos del ciclo de vida.

## Anotaciones de Eventos del Ciclo de Vida

- **@PrePersist**: Método anotado se ejecuta antes de que una nueva entidad se persista (INSERT) en la base de datos.
- **@PostPersist**: Método anotado se ejecuta después de que una nueva entidad se haya persistido (INSERT) en la base de datos.
- **@PreUpdate**: Método anotado se ejecuta antes de que una entidad existente se actualice (UPDATE) en la base de datos.
- **@PostUpdate**: Método anotado se ejecuta después de que una entidad existente se haya actualizado (UPDATE) en la base de datos.
- **@PreRemove**: Método anotado se ejecuta antes de que una entidad se elimine (DELETE) de la base de datos.
- **@PostRemove**: Método anotado se ejecuta después de que una entidad se haya eliminado (DELETE) de la base de datos.
- **@PostLoad**: Método anotado se ejecuta después de que una entidad se haya cargado desde la base de datos.

## Aplicando Ciclo de vida en el entity Person

```java
package com.appjpa.app_jpa.entities;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.PrePersist;
import jakarta.persistence.PreUpdate;
import jakarta.persistence.Table;

import java.time.*;

@Entity
@Table(name="persons")
public class Person {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private String lastname;

    @Column(name = "programming_language")
    private String programmingLanguage;

    @Column(name = "create_at")
    private LocalDateTime createdAt;
    @Column(name = "updated_at")
    private LocalDateTime updatedAt;

    public Person() {
    }

    public Person(Long id, String name, String lastname, String programmingLanguage) {
        this.id = id;
        this.name = name;
        this.lastname = lastname;
        this.programmingLanguage = programmingLanguage;
    }

    @PrePersist
    public void prePersistAudit() {
        createdAt = LocalDateTime.now();
    }

    @PreUpdate
    public void preUpdateAudit() {
        updatedAt = LocalDateTime.now();
    }

    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getLastname() {
        return lastname;
    }
    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getProgrammingLanguage() {
        return programmingLanguage;
    }
    public void setProgrammingLanguage(String programmingLanguage) {
        this.programmingLanguage = programmingLanguage;
    }

    @Override
    public String toString() {
        return "[id=" + id + ", name=" + name + ", lastname=" + lastname + ", programmingLanguage="
                + programmingLanguage + "]";
    }

    
}
```

```
mysql> describe persons;
+----------------------+--------------+------+-----+---------+----------------+
| Field                | Type         | Null | Key | Default | Extra          |
+----------------------+--------------+------+-----+---------+----------------+
| id                   | bigint       | NO   | PRI | NULL    | auto_increment |
| lastname             | varchar(255) | YES  |     | NULL    |                |
| name                 | varchar(255) | YES  |     | NULL    |                |
| programming_language | varchar(255) | YES  |     | NULL    |                |
| create_at            | datetime(6)  | YES  |     | NULL    |                |
| updated_at           | datetime(6)  | YES  |     | NULL    |                |
+----------------------+--------------+------+-----+---------+----------------+
6 rows in set (0.00 sec)
```

Importante en el metodo main llamar el metodo create

<img src="Manuales\imgspring\news\83.png" alt="83" style="zoom:67%;" />

```
+----+----------+----------+----------------------+----------------------------+------------+
| id | lastname | name     | programming_language | create_at                  | updated_at |
+----+----------+----------+----------------------+----------------------------+------------+
|  1 | Pardo    | Johlver  | Java                 | NULL                       | NULL       |
|  2 | Catro    | Miguel   | JavaScript           | NULL                       | NULL       |
|  3 | Manuel   | Jose     | React Native         | NULL                       | NULL       |
|  4 | Acu¤a    | Martha   | PHP                  | NULL                       | NULL       |
|  5 | Luzardo  | Consuelo | Dart                 | 2024-07-25 10:55:31.672913 | NULL       |
+----+----------+----------+----------------------+----------------------------+------------+
5 rows in set (0.00 sec)
```

Ahora llame el metodo Update

<img src="Manuales\imgspring\news\84.png" alt="84" style="zoom:67%;" />

```
+----+----------+----------+----------------------+----------------------------+---------------------------+
| id | lastname | name     | programming_language | create_at                  | updated_at                 |
+----+----------+----------+----------------------+----------------------------+---------------------------+
|  1 | Pardo    | Johlver  | Java                 | NULL                       | NULL                       
|  2 | Catro    | Miguel   | JavaScript           | NULL                       | NULL                       
|  3 | Manuel   | Jose     | React Native         | NULL                       | NULL                       
|  4 | Acu¤a    | Martha   | PHP                  | NULL                       | NULL                       
|  5 | Luzardo  | Consuelo | Kotlin               | 2024-07-25 10:55:31.672913 | 2024-07-25 11:03:00.891343 
+----+----------+----------+----------------------+----------------------------+---------------------------+
5 rows in set (0.00 sec)
```

# @Embedded y @Embeddable

Las anotaciones `@Embedded` y `@Embeddable` en JPA (Java Persistence API) se utilizan para definir y manejar objetos compuestos en una entidad. Esto permite descomponer una entidad en componentes reutilizables, lo que mejora la modularidad y la reutilización del código.

## `@Embeddable`

La anotación `@Embeddable` se usa para marcar una clase como un objeto embebible. Un objeto embebible es una clase cuyos atributos se mapean a las columnas de una tabla de una entidad contenedora.

```java
import javax.persistence.Embeddable;

@Embeddable
public class Direccion {
    private String calle;
    private String ciudad;
    private String estado;
    private String codigoPostal;

    // Getters y setters
}
```

## `@Embedded`

La anotación `@Embedded` se usa en una entidad para indicar que una instancia de una clase embebible se debe incluir en la entidad. Los atributos de la clase embebible se mapean a las columnas de la tabla de la entidad contenedora.

```java
import javax.persistence.*;

@Entity
public class Empleado {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nombre;

    @Embedded
    private Direccion direccion;

    // Getters y setters
}
```

## Aplicando @Embedded y @Embeddable

1. Cree una nueva clase llamada Audit.

2. Mueva los atributos de fecha y los eventos  creados en person a audit y agregue la anotacio @Embeddable

   ```java
   @Column(name = "create_at")
   private LocalDateTime createdAt;
   @Column(name = "updated_at")
   private LocalDateTime updatedAt;
   @PrePersist
   public void prePersistAudit() {
           createdAt = LocalDateTime.now();
   }
   @PreUpdate
   public void preUpdateAudit() {
           updatedAt = LocalDateTime.now();
   }
   //Clase completa
   package com.appjpa.app_jpa.entities;
   
   import jakarta.persistence.Column;
   import jakarta.persistence.Embeddable;
   import jakarta.persistence.PrePersist;
   import jakarta.persistence.PreUpdate;
   import java.time.*;
   
   @Embeddable
   public class Audit {
       @Column(name = "create_at")
       private LocalDateTime createdAt;
       @Column(name = "updated_at")
       private LocalDateTime updatedAt;
       @PrePersist
   
       public void prePersistAudit() {
           createdAt = LocalDateTime.now();
       }
       @PreUpdate
       public void preUpdateAudit() {
           updatedAt = LocalDateTime.now();
       }
       public LocalDateTime getCreatedAt() {
           return createdAt;
       }
       public void setCreatedAt(LocalDateTime createdAt) {
           this.createdAt = createdAt;
       }
       public LocalDateTime getUpdatedAt() {
           return updatedAt;
       }
       public void setUpdatedAt(LocalDateTime updatedAt) {
           this.updatedAt = updatedAt;
       } 
   }
   ```

3. Genere los metodos getter y setter en la clase Audit y agregue la anotación @Embeddable

   <img src="Manuales\imgspring\news\85.png" alt="85" style="zoom:67%;" />

   ```java
   package com.appjpa.app_jpa.entities;
   
   import jakarta.persistence.Column;
   import jakarta.persistence.Embeddable;
   import jakarta.persistence.PrePersist;
   import jakarta.persistence.PreUpdate;
   import java.time.*;
   
   @Embeddable
   public class Audit {
       @Column(name = "create_at")
       private LocalDateTime createdAt;
       @Column(name = "updated_at")
       private LocalDateTime updatedAt;
       @PrePersist
   
       public void prePersistAudit() {
           createdAt = LocalDateTime.now();
       }
       @PreUpdate
       public void preUpdateAudit() {
           updatedAt = LocalDateTime.now();
       }
       public LocalDateTime getCreatedAt() {
           return createdAt;
       }
       public void setCreatedAt(LocalDateTime createdAt) {
           this.createdAt = createdAt;
       }
       public LocalDateTime getUpdatedAt() {
           return updatedAt;
       }
       public void setUpdatedAt(LocalDateTime updatedAt) {
           this.updatedAt = updatedAt;
       }
   
       
   }
   ```

4. En la clase Person cree un atributo que referencie a la clase Audit y agregue la anotación @Embedded

   

   ```java
   package com.appjpa.app_jpa.entities;
   
   import jakarta.persistence.Column;
   import jakarta.persistence.Embedded;
   import jakarta.persistence.Entity;
   import jakarta.persistence.GeneratedValue;
   import jakarta.persistence.GenerationType;
   import jakarta.persistence.Id;
   import jakarta.persistence.Table;
   
   @Entity
   @Table(name="persons")
   public class Person {
   
       @Id
       @GeneratedValue(strategy = GenerationType.IDENTITY)
       private Long id;
   
       private String name;
       private String lastname;
   
       @Column(name = "programming_language")
       private String programmingLanguage;
   
       @Embedded
       Audit audit;
   
       public Person() {
       }
   
       public Person(Long id, String name, String lastname, String programmingLanguage) {
           this.id = id;
           this.name = name;
           this.lastname = lastname;
           this.programmingLanguage = programmingLanguage;
       }
   
       public Long getId() {
           return id;
       }
       public void setId(Long id) {
           this.id = id;
       }
       public String getName() {
           return name;
       }
       public void setName(String name) {
           this.name = name;
       }
       public String getLastname() {
           return lastname;
       }
       public void setLastname(String lastname) {
           this.lastname = lastname;
       }
       public String getProgrammingLanguage() {
           return programmingLanguage;
       }
       public void setProgrammingLanguage(String programmingLanguage) {
           this.programmingLanguage = programmingLanguage;
       }
   
       @Override
       public String toString() {
           return "[id=" + id + ", name=" + name + ", lastname=" + lastname + ", programmingLanguage="
                   + programmingLanguage + " create_at= "+ audit.getCreatedAt() +"]";
       }
   }
   ```

   Invoque el metodo create y ejecute nuevamente el programa. Si obtiene el siguiente error:

   > java.lang.NullPointerException: Cannot invoke "com.appjpa.app_jpa.entities.Audit.getCreatedAt()" because "this.audit" is null
   >         at com.appjpa.app_jpa.entities.Person.toString(Person.java:66) ~[classes/:na]      
   >         at java.base/java.lang.String.valueOf(String.java:4220) ~[na:na]
   >         at java.base/java.io.PrintStream.println(PrintStream.java:1047) ~[na:na]
   >         at com.appjpa.app_jpa.AppJpaApplication.create(AppJpaApplication.java:49) ~[classes/:na]
   >         at com.appjpa.app_jpa.AppJpaApplication.run(AppJpaApplication.java:31) ~[classes/:na]
   >         at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method) ~[na:na]
   >         at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77) ~[na:na]

​	Instancie la clase audit en el atributo embedded

​	<img src="Manuales\imgspring\news\86.png" alt="86" style="zoom:67%;" />

​	

```
+----+----------+----------+----------------------+----------------------------+----------------------------
| id | lastname | name     | programming_language | create_at                  | updated_at                 
+----+----------+----------+----------------------+----------------------------+----------------------------
|  1 | Pardo    | Johlver  | Java                 | NULL                       | NULL                       
|  2 | Catro    | Miguel   | JavaScript           | NULL                       | NULL                       
|  3 | Manuel   | Jose     | React Native         | NULL                       | NULL                       
|  4 | Acu¤a    | Martha   | PHP                  | NULL                       | NULL                       
|  5 | Luzardo  | Consuelo | Kotlin               | 2024-07-25 10:55:31.672913 | 2024-07-25 11:03:00.891343 
|  6 | Bond     | James    | C++                  | NULL                       | NULL                       
|  7 | Bond     | James    | C++                  | 2024-07-25 11:56:30.267976 | NULL                       
+----+----------+----------+----------------------+----------------------------+----------------------------
```



**Resultado:**

![87](Manuales\imgspring\news\87.png)

## Relación OneToMany Bidireccional

Una relación bidireccional OneToMany (Uno a Muchos) en JPA (Java Persistence API) es una relación en la que una entidad tiene una colección de otra entidad, y esa otra entidad tiene una referencia de vuelta a la primera entidad. En otras palabras, ambas entidades están conscientes de la relación y pueden navegar a través de ella en ambas direcciones.

```java
package com.asociacionesapp.app_relationship.entities;

import java.util.*;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.JoinTable;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
import jakarta.persistence.UniqueConstraint;

@Entity
@Table(name = "clients")
public class Client {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private String lastname;

    // @JoinColumn(name = "client_id_address")
    @OneToMany(cascade = CascadeType.ALL, orphanRemoval = true)
    @JoinTable(
        name = "address_clients",
        joinColumns = @JoinColumn(name = "client_id"),
        inverseJoinColumns = @JoinColumn(name = "address_id"),
        uniqueConstraints = @UniqueConstraint(columnNames = {"address_id"})
    )
    private List<Address> addresses = new ArrayList<>();

    //Aplicacion relacion bidireccional
    @OneToMany(cascade = CascadeType.ALL, orphanRemoval = true, mappedBy="client")
    private Set<Invoice> invoices;

    public Client() {}

    public Client(String name, String lastname) {
        this.name = name;
        this.lastname = lastname;
    }
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getLastname() {
        return lastname;
    }
    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public void setAddresses(List<Address> addresses) {
        this.addresses = addresses;
    }
    public List<Address> getAddresses() {
        return addresses;
    }

    public Set<Invoice> getInvoices() {
        return invoices;
    }

    public void setInvoices(Set<Invoice> invoices) {
        this.invoices = invoices;
    }
    @Override
    public String toString() {
        return "{id=" + id +
                ", name=" + name +
                ", lastname=" + lastname +
                "}";
    }
}
```

```java
package com.asociacionesapp.app_relationship.entities;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name="invoices")
public class Invoice {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String description;
    private Long total;

     // @JoinColumn(name = "client_id")
    @ManyToOne
    private Client client;

    public Invoice() {
    }
    public Invoice(String description, Long total) {
        this.description = description;
        this.total = total;
    }
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }
    public void setDescription(String description) {
        this.description = description;
    }
    public Long getTotal() {
        return total;
    }
    public void setTotal(Long total) {
        this.total = total;
    }
    public Client getClient() {
        return client;
    }
    public void setClient(Client client) {
        this.client = client;
    }
    @Override
    public String toString() {
        return "{id=" + id + ", description=" + description + ", total=" + total + ", client=" + client + "}";
    }
}
```

# Taller Asociaciones

- Cree un nuevo proyecto
- Agregue las dependencia JPA, Mysql Driver, Devtools
- Cree los paquetes entities y  repositories
- En el paquete entities cree la clase Client e Invoice

​	Clase Client (ManyToOne)

```java
package com.asociacionesapp.app_relationship.entities;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "clients")
public class Client {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private String lastname;
    public Client() {
    }
    public Client(Long id, String name, String lastname) {
        this.id = id;
        this.name = name;
        this.lastname = lastname;
    }
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getLastname() {
        return lastname;
    }
    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

```

```java
package com.asociacionesapp.app_relationship.entities;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name="invoices")
public class Invoice {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String description;
    private Long total;
    public Invoice() {
    }
    public Invoice(String description, Long total) {
        this.description = description;
        this.total = total;
    }
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }
    public void setDescription(String description) {
        this.description = description;
    }
    public Long getTotal() {
        return total;
    }
    public void setTotal(Long total) {
        this.total = total;
    }

}
```

- Aplicando asociaciones OneToMany - ManyToOne

  Clase Client

  ```java
  package com.asociacionesapp.app_relationship.entities;
  
  import java.util.List;
  
  import org.springframework.boot.autoconfigure.amqp.RabbitConnectionDetails.Address;
  
  import jakarta.persistence.CascadeType;
  import jakarta.persistence.Entity;
  import jakarta.persistence.GeneratedValue;
  import jakarta.persistence.GenerationType;
  import jakarta.persistence.Id;
  import jakarta.persistence.JoinColumn;
  import jakarta.persistence.OneToMany;
  import jakarta.persistence.Table;
  
  @Entity
  @Table(name = "clients")
  public class Client {
      @Id
      @GeneratedValue(strategy = GenerationType.IDENTITY)
      private Long id;
  
      private String name;
      private String lastname;
  
      public Client() {
      }
      public Client(String name, String lastname) {
          this.name = name;
          this.lastname = lastname;
      }
      public Long getId() {
          return id;
      }
      public void setId(Long id) {
          this.id = id;
      }
      public String getName() {
          return name;
      }
      public void setName(String name) {
          this.name = name;
      }
      public String getLastname() {
          return lastname;
      }
      public void setLastname(String lastname) {
          this.lastname = lastname;
      }
      @Override
      public String toString() {
          return "{id=" + id +
                  ", name=" + name +
                  ", lastname=" + lastname +
                  ", addresses=" + addresses + "}";
      }
  
  }
  ```

  Clase Invoice

  ```java
  package com.asociacionesapp.app_relationship.entities;
  
  import jakarta.persistence.Entity;
  import jakarta.persistence.GeneratedValue;
  import jakarta.persistence.GenerationType;
  import jakarta.persistence.Id;
  import jakarta.persistence.ManyToOne;
  import jakarta.persistence.Table;
  
  @Entity
  @Table(name="invoices")
  public class Invoice {
      
      @Id
      @GeneratedValue(strategy = GenerationType.IDENTITY)
      private Long id;
      private String description;
      private Long total;
  
       // @JoinColumn(name = "client_id")
      @ManyToOne
      private Client client;
  
      public Invoice() {
      }
      public Invoice(String description, Long total) {
          this.description = description;
          this.total = total;
      }
      public Long getId() {
          return id;
      }
      public void setId(Long id) {
          this.id = id;
      }
      public String getDescription() {
          return description;
      }
      public void setDescription(String description) {
          this.description = description;
      }
      public Long getTotal() {
          return total;
      }
      public void setTotal(Long total) {
          this.total = total;
      }
  
      @Override
      public String toString() {
          return "{id=" + id + 
              "description=" + description + 
              ", total=" + total + 
              ", client=" + client + "}";
      }
  
  }
  ```

  Cree los repositorios (ClientRepository y InvoiceRepository)

  Relaciones OneToMany

  1. Cree una Entity llamada Address

     ```java
     package com.asociacionesapp.app_relationship.entities;
     
     import jakarta.persistence.Entity;
     import jakarta.persistence.GeneratedValue;
     import jakarta.persistence.GenerationType;
     import jakarta.persistence.Id;
     import jakarta.persistence.Table;
     
     @Entity
     @Table(name="addresses")
     public class Address {
         
         @Id
         @GeneratedValue(strategy = GenerationType.IDENTITY)
         private Long id;
     
         private String street;
         private Integer number;
     
         public Address() {
         }
     
         public Address(String street, Integer number) {
             this.street = street;
             this.number = number;
         }
         public Long getId() {
             return id;
         }
         public void setId(Long id) {
             this.id = id;
         }
         public String getStreet() {
             return street;
         }
         public void setStreet(String street) {
             this.street = street;
         }
         public Integer getNumber() {
             return number;
         }
         public void setNumber(Integer number) {
             this.number = number;
         }
     
         @Override
         public String toString() {
             return "{id=" + id + ", street=" + street + ", number=" + number + "}";
         }
     
     }
     ```

  2. Modifique la tabla client

     ```java
     package com.asociacionesapp.app_relationship.entities;
     
     import java.util.List;
     import java.util.*;
     
     import jakarta.persistence.CascadeType;
     import jakarta.persistence.Entity;
     import jakarta.persistence.GeneratedValue;
     import jakarta.persistence.GenerationType;
     import jakarta.persistence.Id;
     import jakarta.persistence.JoinColumn;
     import jakarta.persistence.OneToMany;
     import jakarta.persistence.Table;
     
     @Entity
     @Table(name = "clients")
     public class Client {
         @Id
         @GeneratedValue(strategy = GenerationType.IDENTITY)
         private Long id;
     
         private String name;
         private String lastname;
     
         @OneToMany(cascade = CascadeType.ALL, orphanRemoval = true)
         @JoinColumn(name = "client_id_address")
         private List<Address> addresses = new ArrayList<>();
     
         public Client() {
         }
         public Client(String name, String lastname) {
             this.name = name;
             this.lastname = lastname;
         }
         public Long getId() {
             return id;
         }
         public void setId(Long id) {
             this.id = id;
         }
         public String getName() {
             return name;
         }
         public void setName(String name) {
             this.name = name;
         }
         public String getLastname() {
             return lastname;
         }
         public void setLastname(String lastname) {
             this.lastname = lastname;
         }
     
         @Override
         public String toString() {
             return "{id=" + id +
                     ", name=" + name +
                     ", lastname=" + lastname +
                     "}";
         }
     
     }
     ```

> **Nota : Recordar generar los métodos getter y setter de las clases.**

```java
	@Transactional
	public void oneToManyFindById() {
		Optional<Client> optionalClient = clientRepository.findById(2L);
		optionalClient.ifPresent(client -> {
			Address address1 = new Address("Direccion cliente A", 1234);
			Address address2 = new Address("Direccion cliente B", 9875);
	
			client.setAddresses(Arrays.asList(address1, address2));
	
			clientRepository.save(client);
	
			System.out.println(client);
		});
		
	}
```

## 

# Arquitectura orientada al dominio

![88](Manuales\imgspring\news\88.png)

```
.
├── .mvn
├── .vscode
├── src
│   └── main
│       └── java
│           └── com
│               └── skeleton
│                   └── skeleton_app
│                       ├── domain
│                       │   ├── dto
│                       │   ├── repository
│                       │   ├── service
│                       ├── persistence
│                       │   ├── crud
│                       │   ├── entity
│                       └── web
│                           └── controllers
│       └── resources
├── test
├── target
├── .gitignore
├── HELP.md
├── mvnw
├── mvnw.cmd
└── pom.xml

```



## Dominio

La sección superior del gráfico está etiquetada como "Dominio". Esta es la capa central y más importante en DDD. Aquí es donde reside la lógica de negocio y las reglas del dominio. En esta capa se encuentran los siguientes elementos:

- **DTO & Objetos de Dominio**: Los Data Transfer Objects (DTOs) y las entidades del dominio que representan los conceptos centrales del negocio. Estos son objetos que encapsulan los datos y la lógica de negocio.
- **Servicios**: Servicios de dominio que contienen lógica que no encaja bien en una sola entidad. Los servicios de dominio suelen encargarse de operaciones que involucran múltiples entidades.

## Web

La sección "Web" se encuentra en la parte inferior izquierda del gráfico. Esta capa se ocupa de la interacción con el mundo exterior, principalmente a través de controladores que manejan solicitudes HTTP. Los componentes en esta capa incluyen:

- **Controladores de API Rest**: Estos son los controladores que exponen las API RESTful. Son responsables de recibir solicitudes HTTP, procesarlas y devolver respuestas HTTP. Los controladores utilizan los servicios de la capa de dominio para realizar las operaciones de negocio necesarias.

## Persistencia

La sección "Persistencia" se encuentra en la parte inferior derecha del gráfico. Esta capa se encarga de la comunicación con la base de datos y otros sistemas de almacenamiento. Incluye:

- **Repositorios**: Los repositorios son responsables de recuperar y almacenar las entidades del dominio. Proporcionan una abstracción sobre el acceso a los datos y permiten que la lógica de negocio no dependa de los detalles de la implementación de la persistencia.
- **Entities**: Las entidades que son mapeadas a tablas de la base de datos. Estas entidades son gestionadas por los repositorios para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

## Resumen del Flujo de Trabajo

![89](Manuales\imgspring\news\89.png)

1. **Interacción del Usuario**: Un usuario realiza una solicitud a través de la interfaz de usuario, que puede ser una aplicación web o móvil.
2. **Controladores de API REST**: La solicitud llega a un controlador de API REST en la capa web, que se encarga de procesar la solicitud y convertirla en una operación de negocio.
3. **Servicios de Dominio**: El controlador llama a un servicio de dominio para realizar la operación de negocio. El servicio de dominio puede involucrar lógica compleja y reglas de negocio.
4. **Repositorios**: Si la operación de negocio requiere acceso a datos, el servicio de dominio interactúa con los repositorios para recuperar o almacenar entidades.
5. **Persistencia**: Los repositorios manejan la comunicación con la base de datos para realizar las operaciones necesarias.
6. **Respuesta**: El resultado de la operación de negocio se devuelve al controlador, que a su vez devuelve una respuesta HTTP al usuario.

## Beneficios de Esta Arquitectura

1. **Claridad y Separación de Preocupaciones**: La lógica de negocio se mantiene separada de la lógica de presentación y de persistencia, facilitando el mantenimiento y la comprensión del código.
2. **Flexibilidad**: Cambios en la lógica de negocio o en la persistencia no afectan a la capa de presentación y viceversa.
3. **Reutilización del Código**: Los servicios de dominio y los repositorios pueden ser reutilizados en diferentes partes de la aplicación.
4. **Testabilidad**: Las diferentes capas pueden ser testeadas de manera independiente, facilitando la escritura de pruebas unitarias y de integración.

## Ejemplo estructura base

```
├── .mvn
├── .vscode
├── src
│   └── main
│       └── java
│           └── com
│               └── skeleton
│                   └── skeleton_app
│                       ├── domain
│                       │   ├── dto
│                       │   ├── repository
│                       │   ├── service
│                       ├── persistence
│                       │   ├── crud
│                       │   ├── entity
│                       └── web
│                           └── controllers
│       └── resources
├── test
├── target
├── .gitignore
├── HELP.md
├── mvnw
├── mvnw.cmd
└── pom.xml
```

# Arquitectura Hexagonal

## Estructura inicial

```
.mvn/
.vscode/
src/
├── main/
│   ├── java/
│   │   └── com/
│   │       └── hexagonal/
│   │           └── hexagonal_app/
│   │               ├── application/
│   │               ├── domain/
│   │               ├── infrastructure/
│   │               └── HexagonalAppApplication.java
│   ├── resources/
├── test/
target/
.gitignore
HELP.md
mvnw
mvnw.cmd
pom.xml
```



## Creacion de entities (persistence>entity)

```java
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name="products")
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private double price;
    private int stock;
    private int stockmin;
    private int stockmax;
    public Product() {
    }
    public Product(String name, double price, int stock, int stockmin, int stockmax) {
        this.name = name;
        this.price = price;
        this.stock = stock;
        this.stockmin = stockmin;
        this.stockmax = stockmax;
    }
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public double getPrice() {
        return price;
    }
    public void setPrice(double price) {
        this.price = price;
    }
    public int getStock() {
        return stock;
    }
    public void setStock(int stock) {
        this.stock = stock;
    }
    public int getStockmin() {
        return stockmin;
    }
    public void setStockmin(int stockmin) {
        this.stockmin = stockmin;
    }
    public int getStockmax() {
        return stockmax;
    }
    public void setStockmax(int stockmax) {
        this.stockmax = stockmax;
    } 
}
```

```java
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name="invoices")
public class Invoice {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String description;
    private Long total;

     // @JoinColumn(name = "client_id")
    @ManyToOne
    private Client client;

    public Invoice() {
    }
    public Invoice(String description, Long total) {
        this.description = description;
        this.total = total;
    }
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }
    public void setDescription(String description) {
        this.description = description;
    }
    public Long getTotal() {
        return total;
    }
    public void setTotal(Long total) {
        this.total = total;
    }
    public Client getClient() {
        return client;
    }
    public void setClient(Client client) {
        this.client = client;
    }
}
```

```java
import jakarta.persistence.EmbeddedId;
import jakarta.persistence.Entity;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;


@Entity
@Table(name = "detail_products")
public class DetailProduct {

    @EmbeddedId
    ProductInvoicePk id;

    private Integer quatity;
    private Double price;
    
    @ManyToOne
    @JoinColumn(name = "id_invoice", insertable = false, updatable = false)
    private Invoice invoice;
    
    @ManyToOne
    @JoinColumn(name = "id_product", insertable = false, updatable = false)
    private Product products;


    public ProductInvoicePk getId() {
        return id;
    }
    public void setId(ProductInvoicePk id) {
        this.id = id;
    }
    public Integer getQuatity() {
        return quatity;
    }
    public void setQuatity(Integer quatity) {
        this.quatity = quatity;
    }
    public Double getPrice() {
        return price;
    }
    public void setPrice(Double price) {
        this.price = price;
    }
}
```



## Creación de Repositorios

Cree una clase de tipo interface  y extienda CrudRepository.

Ejemplo:

![92](Manuales\imgspring\news\92.png)

```java
package com.breakline.survey.app_survey.domain.repository;

import org.springframework.data.repository.CrudRepository;
import com.breakline.survey.app_survey.persistence.entity.ResponseOption;

public interface ResponseOptionRepository extends CrudRepository<ResponseOption,Long> {
}
```

Cree las clases de tipo interface para los servicios.

Código ejemplo de un servicio:

```java
package com.breakline.survey.app_survey.domain.service;

import java.util.List;
import java.util.Optional;

import com.breakline.survey.app_survey.persistence.entity.Catalog;


public interface CatalogService {
    List<Catalog> findAll();
    Optional<Catalog> findById(Long id);
    Catalog save(Catalog catalog);
    Catalog update(Long id);
    Optional<Catalog> delete(Long id);
}
```

Implemente las interfaces de Service. Para cada Service genere una nieva clase que implemente cada uno de los servicios.

Codigo ejemplo:

```java
package com.breakline.survey.app_survey.domain.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.breakline.survey.app_survey.domain.repository.CatalogRepository;
import com.breakline.survey.app_survey.persistence.entity.Catalog;

@Service
public class CatalogImpl implements CatalogService {

    @Autowired
    private CatalogRepository  repository;

    @Transactional
    @Override
    public List<Catalog> findAll() {
        return (List<Catalog>) repository.findAll();
    }
    
    @Transactional
    @Override
    public Optional<Catalog> findById(Long id) {
        return repository.findById(id);
    }
    @Transactional
    @Override
    public Catalog save(Catalog catalog) {
        return repository.save(catalog);
    }
    @Transactional
    @Override
    public Optional<Catalog> delete(Long id) {
        Optional<Catalog> catalogOpt = repository.findById(id);
        catalogOpt.ifPresent(catalogItem ->{
            repository.delete(catalogItem);
        });
        return catalogOpt;
    }

    @Override
    public Optional<Catalog> update(Long id, Catalog catalog) {
        Optional<Catalog> catalogOpt = repository.findById(id);
        if (catalogOpt.isPresent()){
            Catalog catalogItem = catalogOpt.orElseThrow();
            catalogItem.setName(catalog.getName());
            catalogItem.setResponseCatalogs(catalog.getResponseCatalogs());
            return Optional.of(repository.save(catalogItem));
        }
        return catalogOpt;
    }
}
```

Cree los controladores. web.controller

```java
package com.breakline.survey.app_survey.web.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.breakline.survey.app_survey.domain.service.CatalogService;
import com.breakline.survey.app_survey.persistence.entity.Catalog;

import java.util.*;

@RestController
@RequestMapping("/api/catalogs")
public class CatalogController {

    @Autowired
    private CatalogService service;

    @GetMapping
    public List<Catalog> listCatalog(){
        return service.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Catalog> view(@PathVariable Long id){
        Optional<Catalog> catalogOpt = service.findById(id);
        if(catalogOpt.isPresent()){
            return ResponseEntity.ok(catalogOpt.orElseThrow());
        }
        return ResponseEntity.notFound().build();
    }

    @PostMapping
    public ResponseEntity<Catalog> create(@RequestBody Catalog catalog){
        Catalog catalogNew = service.save(catalog);
        return ResponseEntity.status(HttpStatus.CREATED).body(catalogNew);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Catalog> update(@PathVariable Long id,@RequestBody Catalog catalog){
        Optional<Catalog> catalogOpt = service.update(id, catalog);
        if (catalogOpt.isPresent()){
           return ResponseEntity.status(HttpStatus.CREATED).body(catalogOpt.orElseThrow());  
        }
        return ResponseEntity.notFound().build();
    }
    @DeleteMapping("/{id}")
    public ResponseEntity<Catalog> delete(@PathVariable Long id){
        Catalog catalog = new Catalog();
        catalog.setId(id);
        Optional<Catalog> catalogOpt = service.delete(id);
        if(catalogOpt.isPresent()){
            return ResponseEntity.ok(catalogOpt.orElseThrow());
        }
        return ResponseEntity.notFound().build();
    }
}

```



# Spring security 6  

Spring Security es un módulo del ecosistema de Spring diseñado para proteger aplicaciones web y APIs mediante la implementación de mecanismos robustos de autenticación y autorización. Este módulo se integra estrechamente con el marco de trabajo de Spring, proporcionando una solución integral para gestionar la seguridad de las aplicaciones sin necesidad de abordar detalles complicados.

## Puntos Clave de Spring Security

1. **Autenticación**: Verifica la identidad del usuario. ¿Quién es?
2. **Autorización**: Determina los permisos del usuario autenticado. ¿Qué puede hacer?
3. **Protección de Recursos**: Define qué recursos están protegidos y cuáles son públicos.
4. **Integración con Diferentes Mecanismos de Autenticación**: Soporte para diversos métodos como autenticación basada en formularios, HTTP Basic, OAuth2, JWT, etc.

## Componentes Principales

1. **FilterChainProxy**: Componente central que maneja la cadena de filtros de seguridad, coordinando el flujo de trabajo de la seguridad.
2. **DelegatingFilterProxy**: Actúa como un delegado para un filtro definido en el contexto de la aplicación, integrando los filtros de seguridad de Spring con la configuración de filtros de una aplicación web.
3. **SecurityFilterChain**: Interfaz que representa una cadena de filtros de seguridad aplicada a las solicitudes HTTP.

## Tipos de Aplicaciones

- **Stateful (Basada en Sesiones)**: Mantiene un estado en el servidor para cada usuario. Es eficaz para mantener información del usuario, pero puede presentar problemas de escalabilidad y rendimiento con muchos usuarios concurrentes.
- **Stateless (Basada en Tokens de Autenticación)**: No mantiene estado en el servidor. Cada solicitud del cliente contiene toda la información necesaria para procesar la solicitud. Es altamente escalable y eficiente, pero requiere que los tokens se protejan adecuadamente.

## Arquitectura

### FilterChain

​						Obtenido : https://docs.spring.io/spring-security/reference/servlet/architecture.html

<img src="C:\Breakline\Manuales\springSecurity\Screenshot_1.png" alt="Screenshot_1" style="zoom:67%;" />



FilterChain) en una arquitectura de aplicaciones web utilizando Spring Security. Vamos a desglosar cada parte del gráfico:

#### Componentes

1. **Client**:
   - Representa al cliente que realiza una solicitud HTTP hacia la aplicación web.
2. **FilterChain**:
   - Es una estructura que encadena varios filtros que procesan la solicitud HTTP antes de llegar al servlet final.
   - Los filtros son responsables de diversas tareas relacionadas con la seguridad y otros aspectos de la gestión de la solicitud.
3. **Filter0, Filter1, Filter2**:
   - Representan los diferentes filtros en la cadena.
   - Cada filtro tiene la oportunidad de inspeccionar, modificar, o rechazar la solicitud antes de pasarla al siguiente filtro en la cadena.
   - Los filtros se aplican en el orden en que están configurados.
4. **Servlet**:
   - El componente final que maneja la solicitud HTTP una vez que ha pasado a través de todos los filtros de la cadena.
   - Aquí es donde se ejecuta la lógica de negocio de la aplicación web.

### Flujo del Proceso

1. **Cliente realiza una solicitud HTTP**:
   - El cliente envía una solicitud HTTP a la aplicación web.
2. **La solicitud pasa a través del FilterChain**:
   - La solicitud entra en el `FilterChain`, donde se aplican una serie de filtros secuencialmente.
3. **Filtro 0 (Filter0)**:
   - El primer filtro en la cadena (`Filter0`) procesa la solicitud. Puede autenticar al usuario, realizar registros, o aplicar cualquier lógica específica de seguridad.
   - Luego, la solicitud se pasa al siguiente filtro (`Filter1`).
4. **Filtro 1 (Filter1)**:
   - El segundo filtro (`Filter1`) aplica su propia lógica de procesamiento.
   - Después de esto, la solicitud se pasa al siguiente filtro (`Filter2`).
5. **Filtro 2 (Filter2)**:
   - El tercer filtro (`Filter2`) realiza su procesamiento.
   - Una vez completado, la solicitud es pasada al servlet.
6. **Servlet**:
   - Finalmente, la solicitud llega al `Servlet` donde se maneja la lógica de negocio específica de la aplicación.
   - El servlet genera una respuesta basada en la solicitud procesada y esta respuesta sigue el camino inverso de regreso al cliente, pasando nuevamente por los filtros si es necesario.

### Aplicación en Spring Security

En el contexto de Spring Security, los filtros dentro del `FilterChain` pueden incluir:

- **Authentication Filters**: Para autenticar las credenciales del usuario.
- **Authorization Filters**: Para verificar los permisos del usuario y determinar si tiene acceso al recurso solicitado.
- **Logging Filters**: Para registrar detalles de la solicitud.
- **CORS Filters**: Para manejar las políticas de intercambio de recursos de origen cruzado.

Estos filtros trabajan juntos para asegurar que solo las solicitudes autorizadas y autenticadas accedan a los recursos protegidos de la aplicación, proporcionando una capa robusta de seguridad.

### DelegatingFilterProxy

Es una clase de Spring Framework que crea la instancia del delegado de un filtro declarado en el contexto de la aplicación. Se utiliza normalmente en Spring Security para unir la cadena de filtros de seguridad de Spring Security con la configuración del filtro de una aplicación web de Servlet.

> Spring ofrece una implementación de filtro llamada `DelegatingFilterProxy` que permite establecer un puente entre el ciclo de vida del contenedor Servlet y el `ApplicationContext` de Spring. El contenedor Servlet permite registrar instancias de `Filter` utilizando sus propios estándares, pero no reconoce los Beans definidos por Spring. Puedes registrar `DelegatingFilterProxy` a través de los mecanismos estándar del contenedor Servlet, pero delegar todo el trabajo a un Bean de Spring que implementa.

<img src="C:\Breakline\Manuales\springSecurity\Screenshot_2.png" alt="Screenshot_2" style="zoom:67%;" />

El `DelegatingFilterProxy` es crucial en el contexto de aplicaciones Spring, ya que permite integrar los filtros definidos como beans dentro del contexto de la aplicación Spring con la cadena de filtros de una aplicación web basada en Servlets. Esto proporciona una manera flexible y poderosa de aplicar lógica de seguridad y otras operaciones personalizadas en las solicitudes HTTP.

### FilterChainProxy

Es el componente central de Spring Security que maneja la coordinación de la cadena de filtros de seguridad para proteger una aplicación web.

<img src="C:\Breakline\Manuales\springSecurity\Screenshot_3.png" alt="Screenshot_3" style="zoom:67%;" />

> El soporte de Servlet de Spring Security se encuentra dentro de `FilterChainProxy`. `FilterChainProxy` es un filtro especial proporcionado por Spring Security que permite delegar en muchas instancias de `Filter` a través de `SecurityFilterChain`. Dado que `FilterChainProxy` es un Bean, generalmente se envuelve en un `DelegatingFilterProxy`.

El componente **SecurityFilterChain** en Spring Security es una pieza clave para la configuración de la seguridad en aplicaciones web basadas en Spring. A continuación se explica en detalle su rol y funcionamiento:

#### SecurityFilterChain

<img src="C:\Breakline\Manuales\springSecurity\Screenshot_4.png" alt="Screenshot_4" style="zoom:67%;" />

> Los filtros de seguridad en `SecurityFilterChain` son típicamente Beans, pero se registran con `FilterChainProxy` en lugar de con `DelegatingFilterProxy`. `FilterChainProxy` ofrece varias ventajas en comparación con el registro directo en el contenedor Servlet o con `DelegatingFilterProxy`. En primer lugar, proporciona un punto de partida para todo el soporte de Servlet de Spring Security. Por esta razón, si intentas solucionar problemas con el soporte de Servlet de Spring Security, agregar un punto de depuración en `FilterChainProxy` es un excelente punto de partida.
>
> En segundo lugar, dado que `FilterChainProxy` es central en el uso de Spring Security, puede realizar tareas que no se consideran opcionales. Por ejemplo, borra el `SecurityContext` para evitar fugas de memoria. También aplica el `HttpFirewall` de Spring Security para proteger las aplicaciones contra ciertos tipos de ataques.
>
> Además, proporciona mayor flexibilidad para determinar cuándo se debe invocar un `SecurityFilterChain`. En un contenedor Servlet, las instancias de `Filter` se invocan basándose únicamente en la URL. Sin embargo, `FilterChainProxy` puede determinar la invocación basándose en cualquier cosa dentro del `HttpServletRequest` utilizando la interfaz `RequestMatcher`. (https://docs.spring.io/spring-security/reference/servlet/architecture.html)

**SecurityFilterChain** es una interfaz en Spring Security que define una cadena de filtros de seguridad que se aplican a las solicitudes HTTP en una aplicación web. Estos filtros manejan diversas responsabilidades relacionadas con la seguridad, como autenticación, autorización, manejo de sesiones, y protección contra ataques comunes (e.g., CSRF).

<img src="C:\Breakline\Manuales\springSecurity\Screenshot_5.png" alt="Screenshot_5" style="zoom:67%;" />

> En el esquema de múltiples `SecurityFilterChain`, `FilterChainProxy` determina cuál `SecurityFilterChain` debe emplearse. Solo se ejecuta la primera `SecurityFilterChain` que coincida. Por ejemplo, si se solicita la URL `/api/messages/`, coincide primero con el patrón `/api/**` de `SecurityFilterChain0`, por lo que únicamente se invoca `SecurityFilterChain0`, aunque también podría coincidir con `SecurityFilterChainn`. Si se solicita la URL `/messages/`, no coincide con el patrón `/api/**` de `SecurityFilterChain0`, por lo que `FilterChainProxy` continúa verificando cada `SecurityFilterChain`. Suponiendo que ninguna otra instancia de `SecurityFilterChain` coincida, se invoca `SecurityFilterChainn`.
>
> Cabe destacar que `SecurityFilterChain0` tiene solo tres filtros de seguridad configurados, mientras que `SecurityFilterChainn` tiene cuatro. Es importante mencionar que cada `SecurityFilterChain` puede ser única y configurarse de manera independiente. De hecho, una `SecurityFilterChain` puede no tener filtros de seguridad si la aplicación requiere que Spring Security ignore ciertas solicitudes.



#### Funciones Clave de SecurityFilterChain

1. **Definición de Filtros**:
   - **SecurityFilterChain** permite especificar una serie de filtros que procesarán las solicitudes HTTP. Cada filtro tiene una función específica dentro del proceso de seguridad.
2. **Coordinación de Filtros**:
   - Gestiona el orden en el que se aplican los filtros. Esto es crucial, ya que ciertos filtros deben ejecutarse antes que otros para garantizar un correcto flujo de seguridad.
3. **Aplicación Condicional**:
   - **SecurityFilterChain** puede configurarse para que se aplique a ciertas rutas o patrones de URL específicos. Esto permite definir reglas de seguridad diferenciadas para distintas partes de la aplicación.

## ¿Por qué es importante Spring Security?  

La seguridad es primordial en cualquier API o aplicación web. Spring Security es la fuerte y confiable infraestructura de autenticación y autorización para darnos las herramientas de seguridad suficientes sin ocuparnos de la preparación tediosa.

#### **En el contexto de la seguridad web y Spring Security, es crucial entender las diferencias entre las aplicaciones stateless y stateful. Ambas tienen diferentes enfoques y ventajas en términos de gestión de sesiones y autenticación de usuarios.**

<img src="C:\Breakline\Manuales\springSecurity\Screenshot_6.png" alt="Screenshot_6" style="zoom:67%;" />

| Característica        | Stateful                                    | Stateless                              |
| --------------------- | ------------------------------------------- | -------------------------------------- |
| **Mantenimiento**     | Sesiones gestionadas en el servidor         | No se mantiene estado en el servidor   |
| **Autenticación**     | Basada en sesiones (Session ID)             | Basada en tokens (JWT)                 |
| **Escalabilidad**     | Puede presentar problemas de escalabilidad  | Altamente escalable                    |
| **Balanceo de Carga** | Requiere afinidad de sesión                 | No requiere afinidad de sesión         |
| **Almacenamiento**    | Información almacenada en el servidor       | Información incluida en cada solicitud |
| **Seguridad**         | Sesiones pueden ser vulnerables a secuestro | Tokens deben protegerse adecuadamente  |

### Aplicaciones Stateful

<img src="C:\Breakline\Manuales\springSecurity\Screenshot_7.png" alt="Screenshot_7" style="zoom:67%;" />

Las aplicaciones stateful son aquellas en las que se mantiene un estado persistente en el servidor durante la interacción del usuario con la aplicación. Esto significa que el servidor guarda información sobre la sesión del usuario, permitiendo que las solicitudes sucesivas sean tratadas en el contexto de esa sesión.

#### Características Principales

1. **Mantenimiento de Sesiones en el Servidor**:
   - Las aplicaciones stateful mantienen un estado en el servidor para cada usuario. Esto generalmente se logra a través de sesiones HTTP.
   - La información de la sesión se almacena en el servidor, y cada usuario tiene una sesión única identificada por un identificador de sesión (session ID).
2. **Gestión de Sesiones**:
   - El servidor es responsable de gestionar y almacenar la información de la sesión. Esto incluye detalles como la identidad del usuario, permisos, y otros datos necesarios durante la interacción del usuario con la aplicación.
   - La gestión de sesiones puede incluir el almacenamiento en memoria, bases de datos, o almacenes de sesiones dedicados como Redis.
3. **Escalabilidad**:
   - Mantener sesiones en el servidor puede generar problemas de escalabilidad, especialmente cuando se manejan muchos usuarios concurrentes.
   - Requiere un balanceo de carga que gestione la "afinidad de sesión" o "pegajosa" para asegurar que las solicitudes de un usuario específico siempre se dirijan al mismo servidor.

## Aplicaciones  **stateless**

<img src="C:\Breakline\Manuales\springSecurity\Screenshot_8.png" alt="Screenshot_8" style="zoom:67%;" />

Las aplicaciones stateless, en contraste con las aplicaciones stateful, no mantienen el estado del usuario en el servidor entre las solicitudes. En su lugar, cada solicitud del cliente contiene toda la información necesaria para que el servidor la procese de manera independiente.

### Características de las Aplicaciones Stateless

1. **Sin Mantenimiento de Sesiones en el Servidor**:
   - No se guarda el estado de la sesión en el servidor. Cada solicitud se procesa de manera independiente.
   - Los datos necesarios para la autenticación y la autorización se envían con cada solicitud, típicamente en forma de tokens.
2. **Uso de Tokens**:
   - Las aplicaciones stateless utilizan tokens, como JSON Web Tokens (JWT), para transmitir la información de seguridad.
   - Un token JWT contiene toda la información necesaria (como identidad del usuario y roles) en su propia estructura y es enviado en cada solicitud.
3. **Escalabilidad**:
   - Las aplicaciones stateless son altamente escalables porque no dependen del estado de la sesión del servidor.
   - Los servidores pueden manejar solicitudes de manera independiente, lo que facilita la distribución de la carga y mejora el rendimiento.
4. **Seguridad**:
   - Los tokens deben ser protegidos adecuadamente para prevenir accesos no autorizados y manipulaciones.
   - La autenticidad e integridad de los tokens se asegura mediante firmas criptográficas.
5. **Balanceo de Carga**:
   - No requiere afinidad de sesión, ya que cualquier servidor puede procesar cualquier solicitud sin necesidad de mantener información de sesión específica del usuario.

# JWT: Json Web Token

JSON Web Token (JWT) es un estándar abierto (RFC 7519) que define una forma compacta y autónoma de transmitir información de manera segura entre dos partes como un objeto JSON. Esta información puede ser verificada y confiable porque está firmada digitalmente. Los JWTs se utilizan comúnmente para la autenticación y autorización en aplicaciones web y APIs.

<img src="C:\Breakline\Manuales\springSecurity\Screenshot_9.png" alt="Screenshot_9" style="zoom:67%;" />

​			Obtenido : https://jwt.io/

## Estructura de un JWT

Un JWT consta de tres partes separadas por puntos (`.`):

1. **Header (Encabezado)**
2. **Payload (Carga útil)**
3. **Signature (Firma)**

### 1. Header (Encabezado)

El encabezado típicamente consta de dos partes: el tipo de token (JWT) y el algoritmo de firma que se está utilizando, como HMAC SHA256 o RSA.

### 2. Payload (Carga útil)

La carga útil es la parte del token que contiene las declaraciones (claims). Las declaraciones son afirmaciones sobre una entidad (generalmente, el usuario) y datos adicionales. Hay tres tipos de declaraciones:

- **Registered Claims**: Son un conjunto de declaraciones predefinidas no obligatorias pero recomendadas, como `iss` (emisor), `exp` (expiración), `sub` (asunto), `aud` (audiencia).
- **Public Claims**: Pueden definirse libremente por aquellos que usen JWTs. Pueden incluir información como el nombre del usuario, roles, etc.
- **Private Claims**: Son declaraciones personalizadas que se crean para compartir información entre partes que acuerdan utilizarla.

```java
{
  "sub": "1234567890",
  "name": "xxxxx xxxx",
  "admin": true
}
```

### 3. Signature (Firma)

Para crear la firma, se toma el encabezado codificado, el payload codificado, un secreto (en el caso de HMAC) o una clave privada (en el caso de RSA), y el algoritmo especificado en el encabezado, y se firma.

La firma se usa para verificar que el emisor del JWT sea quien dice ser y para asegurar que el mensaje no haya sido cambiado a lo largo del camino.

<img src="C:\Breakline\Manuales\springSecurity\Screenshot_10.png" alt="Screenshot_10" style="zoom:67%;" />

<img src="C:\Breakline\Manuales\springSecurity\Screenshot_11.png" alt="Screenshot_11" style="zoom:67%;" />

# Taller Practico

1. Descargue proyecto base https://github.com/trainingLeader/app-security-app.git

2. Configure el archivo properties para la conexion con la base de datos.

   ```java
   spring.datasource.url=jdbc:mysql://localhost:3306/db?createDatabaseIfNotExist=true
   spring.datasource.username=xxxxxxxx
   spring.datasource.password=xxxxxxxx
   spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
   spring.jpa.database-platform=org.hibernate.dialect.MySQLDialect
   spring.jpa.show-sql=true
   spring.jpa.hibernate.ddl-auto=create-drop
   ```

3. Cree las entidades User(users) y Role(roles)

   ```java
   import java.util.ArrayList;
   import java.util.List;
   
   import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
   
   import jakarta.persistence.Column;
   import jakarta.persistence.Entity;
   import jakarta.persistence.GeneratedValue;
   import jakarta.persistence.GenerationType;
   import jakarta.persistence.Id;
   import jakarta.persistence.ManyToMany;
   import jakarta.persistence.Table;
   
   @Entity
   @Table(name="roles")
   public class Role {
       
       @Id
       @GeneratedValue(strategy = GenerationType.IDENTITY)
       private Long id;
   
       @Column(unique = true)
       private String name;
   
       @JsonIgnoreProperties({"roles", "handler", "hibernateLazyInitializer"})
       @ManyToMany(mappedBy = "roles")
       private List<User> users;
   
       public Role() {
           this.users = new ArrayList<>();
       }
   
       public Long getId() {
           return id;
       }
   
       public void setId(Long id) {
           this.id = id;
       }
   
       public String getName() {
           return name;
       }
   
       public void setName(String name) {
           this.name = name;
       }
   
       public List<User> getUsers() {
           return users;
       }
   
       public void setUsers(List<User> users) {
           this.users = users;
       }
   }
   
   ```

   ```java
   import java.util.ArrayList;
   import java.util.List;
   
   import com.fasterxml.jackson.annotation.JsonProperty;
   
   import jakarta.persistence.Entity;
   import jakarta.persistence.GeneratedValue;
   import jakarta.persistence.GenerationType;
   import jakarta.persistence.Id;
   import jakarta.persistence.JoinColumn;
   import jakarta.persistence.JoinTable;
   import jakarta.persistence.ManyToMany;
   import jakarta.persistence.PrePersist;
   import jakarta.persistence.Table;
   import jakarta.persistence.Transient;
   import jakarta.persistence.UniqueConstraint;
   
   @Entity
   @Table(name = "users")
   public class User {
   
       @Id
       @GeneratedValue(strategy = GenerationType.IDENTITY)
       private Long id;
   
       private String username;
   
       private String password;
   
       @ManyToMany
       @JoinTable(
           name = "users_roles",
           joinColumns = @JoinColumn(name="user_id"),
           inverseJoinColumns = @JoinColumn(name="role_id"),
           uniqueConstraints = { @UniqueConstraint(columnNames = {"user_id", "role_id"})}
       )
       private List<Role> roles;
   
       
       public User() {
           roles = new ArrayList<>();
       }
   
       public Long getId() {
           return id;
       }
   
       public void setId(Long id) {
           this.id = id;
       }
   
       public String getUsername() {
           return username;
       }
   
       public void setUsername(String username) {
           this.username = username;
       }
   
       public String getPassword() {
           return password;
       }
   
       public void setPassword(String password) {
           this.password = password;
       }
   
       public List<Role> getRoles() {
           return roles;
       }
   
       public void setRoles(List<Role> roles) {
           this.roles = roles;
       }
   
   }
   
   ```

4. Cree los repositories para user y role de tipo **CrudRepository**

   ```java
   import java.util.Optional;
   import org.springframework.data.repository.CrudRepository;
   
   import com.uissurvey.uissurvey_app.domain.entities.Role;
   
   public interface RoleRepository extends CrudRepository<Role,Long> {
       Optional<Role> findByName(String name);
   }
   
   //-------------------------------------------------------------------------
   import java.util.Optional;
   import org.springframework.data.repository.CrudRepository;
   import org.springframework.stereotype.Repository;
   
   import com.uissurvey.uissurvey_app.domain.entities.User;
   
   @Repository
   public interface UserRepository extends CrudRepository<User,Long> {
       boolean existsByUsername(String username);
       Optional<User> findByUsername(String username);
   }
   ```

   

5. Cree los servicios para user e implemente el servicio

   ```java
   import java.util.List;
   
   import com.crudsec.app_security_app.domain.entity.User;
   
   public interface IUserService {
       List<User> findAll();
       User save(User user);
   }
   ```

6. Agregue el siguiente atributo a la clase User

   ```java
   @Transient
   @JsonProperty(access = JsonProperty.Access.WRITE_ONLY)
   private boolean admin;
   
   ---------------- Y -----------------
   public boolean isAdmin() {
           return admin;
   }
   
   public void setAdmin(boolean admin) {
           this.admin = admin;
   }
   ```

7. Cree un método personalizado en el Repositorio de RoleRepository para buscar el rol por nombre.

   ```java
   Optional<Role> findByName(String name);
   ```

8. Cree el archivo message.properties

   ```
   NotEmpty.product.name=es requerido!
   NotBlank.product.description=es requerido, por favor
   NotNull.product.price=no puede ser nulo, ok!
   Min.product.price=debe ser un valor numerico mayor o igual que 500!
   IsRequired.product.name=es requerido usando anotaciones, mensaje en properties!
   ```

9. Cree el archivo de configuración para la aplicacion y para security

   ```
   import org.springframework.context.annotation.Configuration;
   import org.springframework.context.annotation.PropertySource;
   
   @Configuration
   @PropertySource("classpath:messages.properties")
   public class AppConfig {
       
   }
   ```

10. Agregue la dependencia de Spring Security

    ```java
    <dependency>
    	<groupId>org.springframework.boot</groupId>
    	<artifactId>spring-boot-starter-security</artifactId>
    </dependency>
    ```

    > ​    <dependency>
    >
    > ​      <groupId>org.springframework.boot</groupId>
    >
    > ​      <artifactId>spring-boot-starter-security</artifactId>
    >
    > ​    </dependency>

11. Cree la clase SpringSecurityConfig. Esta clase se coloca en un paquete llamado security

    ```java
    import org.springframework.context.annotation.Bean;
    import org.springframework.context.annotation.Configuration;
    import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
    import org.springframework.security.crypto.password.PasswordEncoder;
    
    @Configuration
    public class SpringSecurityConfig {
    
        @Bean
        PasswordEncoder passwordEncoder() {
            return new BCryptPasswordEncoder();
        }
    }
    ```

    **@Bean**:

    - La anotación `@Bean` indica que el método produce un bean que debe ser administrado por el contenedor de Spring. Los beans en Spring son objetos que son instanciados, ensamblados y administrados por Spring IoC Container.
    - Cuando el contenedor de Spring encuentra este método anotado, llamará al método y registrará el valor devuelto como un bean dentro del contexto de la aplicación de Spring.

    **PasswordEncoder**:

    - `PasswordEncoder` es una interfaz de Spring Security que define métodos para codificar contraseñas y verificar contraseñas codificadas.
    - Es una interfaz fundamental para la seguridad, ya que permite manejar las contraseñas de manera segura, utilizando técnicas de hashing en lugar de almacenarlas en texto plano.

    **BCryptPasswordEncoder**:

    - `BCryptPasswordEncoder` es una implementación de `PasswordEncoder` que utiliza el algoritmo BCrypt para el hashing de contraseñas. BCrypt es un algoritmo de hashing que incluye un factor de costo ajustable, lo que significa que la cantidad de tiempo que toma codificar una contraseña puede incrementarse a medida que el hardware mejora, haciendo que el hash sea más seguro frente a ataques de fuerza bruta.
    - Al devolver una instancia de `BCryptPasswordEncoder`, se asegura que las contraseñas en la aplicación se codifiquen utilizando BCrypt.

    > ### ¿Por qué es importante?
    >
    > El uso de un `PasswordEncoder` como `BCryptPasswordEncoder` es crucial para proteger las contraseñas de los usuarios. Cuando una contraseña es codificada con BCrypt, se convierte en un hash seguro que es difícil de revertir. Esto significa que incluso si un atacante obtiene acceso a la base de datos, no podría obtener fácilmente las contraseñas originales.

12. En la implementación del servicio inyecte RoleRepository y PasswordEncoder

    ```java
    @Autowired
    private RoleRepository roleRepository;
    
    @Autowired
    private PasswordEncoder passwordEncoder;
    ```

13. Agregue los roles ROLE_USER Y ROLE_ADMIN en la tabla roles de la base de datos.

14. Modifique el metodo save de la implementacion del servicio.

    ```java
    @Override
    @Transactional
    public User save(User user) {
            Optional<Role> optionalRoleUser = roleRepository.findByName("ROLE_USER");
            List<Role> roles = new ArrayList<>();
    
            optionalRoleUser.ifPresent(roles::add);
    
            if (user.isAdmin()) {
                Optional<Role> optionalRoleAdmin = roleRepository.findByName("ROLE_ADMIN");
                optionalRoleAdmin.ifPresent(roles::add);
            }
    
            user.setRoles(roles);
            user.setPassword(passwordEncoder.encode(user.getPassword()));
            return repository.save(user);
    }
    ```

15. Agregue el UserController

    ```java
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.http.HttpStatus;
    import org.springframework.http.ResponseEntity;
    import org.springframework.validation.BindingResult;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.PostMapping;
    import org.springframework.web.bind.annotation.RequestBody;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RestController;
    import java.util.*;
    import com.crudsec.app_security_app.application.services.IUserService;
    import com.crudsec.app_security_app.domain.entity.User;
    
    import jakarta.validation.Valid;
    
    @RestController
    @RequestMapping("/users")
    public class UserController {
        @Autowired
        private IUserService service;
    
        @GetMapping
        public List<User> list() {
            return service.findAll();
        }
        
        @PostMapping
        public ResponseEntity<?> create(@Valid @RequestBody User user, BindingResult result) {
            if (result.hasFieldErrors()) {
                return validation(result);
            }
            return ResponseEntity.status(HttpStatus.CREATED).body(service.save(user));
        }
        
        private ResponseEntity<?> validation(BindingResult result) {
            Map<String, String> errors = new HashMap<>();
    
            result.getFieldErrors().forEach(err -> {
                errors.put(err.getField(), "El campo " + err.getField() + " " + err.getDefaultMessage());
            });
            return ResponseEntity.badRequest().body(errors);
        }
    }
    ```

    **@RestController**:

    - Esta anotación indica que la clase `UserController` es un controlador de Spring que gestiona solicitudes HTTP. Combina las anotaciones `@Controller` y `@ResponseBody`, lo que significa que los métodos de la clase devolverán directamente los datos (en formato JSON, XML, etc.) en lugar de una vista.

    **@RequestMapping("/users")**:

    - Define la ruta base para este controlador. Todas las rutas de los métodos de esta clase comenzarán con `/users`. Por ejemplo, `/users` para listar todos los usuarios.

    **IUserService**:

    - `IUserService` es una interfaz de servicio que contiene la lógica de negocio relacionada con los usuarios. Esta interfaz se inyecta en el controlador usando la anotación `@Autowired`, lo que indica a Spring que debe proporcionar una instancia del servicio automáticamente.

    **@GetMapping**:

    - Asocia este método con solicitudes HTTP GET. Cuando un cliente realiza una solicitud GET a `/users`, se invocará este método.

    **list()**:

    - Este método llama al servicio para obtener una lista de todos los usuarios (`service.findAll()`) y la devuelve. El resultado se convierte automáticamente en JSON debido a `@RestController`.

    **@PostMapping**:

    - Este método está asociado con solicitudes HTTP POST. Se utilizará cuando un cliente envíe datos para crear un nuevo usuario a la ruta `/users`.

    **@Valid @RequestBody User user**:

    - `@RequestBody` indica que el cuerpo de la solicitud HTTP debe ser convertido en un objeto `User`.
    - `@Valid` activa la validación automática del objeto `User` basado en las anotaciones de validación que pueda tener, como `@NotNull`, `@Size`, etc.

    **BindingResult result**:

    - Este parámetro captura los resultados de la validación. Si hay errores en los datos enviados, se guardan en `result`.

    **if (result.hasFieldErrors())**:

    - Este bloque verifica si hubo errores de validación. Si los hay, llama al método `validation(result)` para manejar los errores.

    **service.save(user)**:

    - Si no hay errores, se llama al método `save` del servicio para guardar el nuevo usuario en la base de datos. Luego, se devuelve una respuesta HTTP con el estado `201 Created` y el objeto usuario recién creado.

    **validation(BindingResult result)**:

    - Este método privado se encarga de manejar los errores de validación. Crea un `Map` de errores donde la clave es el nombre del campo y el valor es un mensaje de error personalizado.

    **result.getFieldErrors()**:

    - Obtiene una lista de errores de campo que se produjo durante la validación.

    **forEach(err -> { ... })**:

    - Recorre todos los errores de campo y los agrega al mapa de errores con un mensaje descriptivo.

    **ResponseEntity.badRequest().body(errors)**:

    - Devuelve una respuesta HTTP con el estado `400 Bad Request` y el cuerpo de la respuesta contiene el mapa de errores.

## Configuración reglas de seguridad

En la clase SpringSecurity agregue el siguiente metodo

```java
@Bean
SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        return http.authorizeHttpRequests((authz) -> authz
                .requestMatchers("/users").permitAll()
                .anyRequest().authenticated())
                .csrf(config -> config.disable())
                .sessionManagement(management -> management.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
                .build();
}
```

A la clase User agreguele el atributo private boolean enabled;

Cree una nueva interface llamada **ExistsByUsername** y la clase de implementacion **ExistsByUsernameValidation**  para validar la existencia del usuario.

```java
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

import jakarta.validation.Payload;

@Target(ElementType.FIELD)
@Retention(RetentionPolicy.RUNTIME)
public @interface ExistsByUsername {
    String message() default "ya existe en la base de datos!, escoja otro username!";

    Class<?>[] groups() default {};

    Class<? extends Payload>[] payload() default {};
}
//--------------------------------------------------------------
import jakarta.validation.ConstraintValidator;
import jakarta.validation.ConstraintValidatorContext;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.crudsec.app_security_app.application.services.IUserService;

@Component
public class ExistsByUsernameValidation implements ConstraintValidator<ExistsByUsername, String> {

    @Autowired
    private IUserService service;

    @Override
    public boolean isValid(String username, ConstraintValidatorContext context) {
        if (service == null) {
            return true;
        }
        return !service.existsByUsername(username);
    }
}
```

Modifique el Service, CrudRepository y Repository de User

```java
import java.util.List;

import com.crudsec.app_security_app.domain.entity.User;

public interface IUserService {
    List<User> findAll();
    User save(User user);
    boolean existsByUsername(String username); //<-- Add this code
}
//------------------------------------------------------------------
import java.util.Optional;
import org.springframework.data.repository.CrudRepository;

import com.crudsec.app_security_app.domain.entity.User;

public interface UserRepository extends CrudRepository<User,Long> {
    boolean existsByUsername(String username); //<-- Add this code

    Optional<User> findByUsername(String username); //<-- Add this code
}
// -----------------------------------------------------------------
import java.util.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.crudsec.app_security_app.application.services.IUserService;
import com.crudsec.app_security_app.domain.entity.Role;
import com.crudsec.app_security_app.domain.entity.User;
import com.crudsec.app_security_app.infrastructure.repositories.RoleRepository;

@Service
public class UserAdapter implements IUserService {
    @Autowired
    private UserRepository repository;

    @Autowired
    private RoleRepository roleRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Override
    @Transactional(readOnly = true)
    public List<User> findAll() {
        return (List<User>) repository.findAll();
    }

    @Override
    @Transactional
    public User save(User user) {
        Optional<Role> optionalRoleUser = roleRepository.findByName("ROLE_USER");
        List<Role> roles = new ArrayList<>();

        optionalRoleUser.ifPresent(roles::add);

        if (user.isAdmin()) {
            Optional<Role> optionalRoleAdmin = roleRepository.findByName("ROLE_ADMIN");
            optionalRoleAdmin.ifPresent(roles::add);
        }

        user.setRoles(roles);
        user.setPassword(passwordEncoder.encode(user.getPassword()));
        return repository.save(user);
    }
    @Override
    public boolean existsByUsername(String username) {
        return repository.existsByUsername(username);   //<-- Add this method
    }

}
```

Implemente el UserDetailsService

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.crudsec.app_security_app.domain.entity.User;
import com.crudsec.app_security_app.infrastructure.repositories.user.UserRepository;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;


import org.springframework.transaction.annotation.Transactional;

@Service
public class JpaUserDetailsService implements UserDetailsService{

     @Autowired
    private UserRepository repository;

    @Transactional(readOnly = true)
    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {

        Optional<User> userOptional = repository.findByUsername(username);

        if (userOptional.isEmpty()) {
            throw new UsernameNotFoundException(String.format("Username %s no existe en el sistema!", username));
        }

        User user = userOptional.orElseThrow();

        List<GrantedAuthority> authorities = user.getRoles().stream()
                .map(role -> new SimpleGrantedAuthority(role.getName()))
                .collect(Collectors.toList());

        return new org.springframework.security.core.userdetails.User(user.getUsername(), 
        user.getPassword(), 
        user.isEnabled(),
    	true, // la cuenta no ha expirado
    	true, // las credenciales no han expirado
    	true, // la cuenta no está bloqueada
    	authorities); // los roles del usuario      
    }
}
```

### Anotaciones y Clases:

- `@Service`: Marca la clase como un *Spring Service* que puede ser inyectado y gestionado por el *Spring container*.
- `UserDetailsService`: Es una interfaz de Spring Security que se usa para cargar detalles específicos de un usuario con base en su nombre de usuario, especialmente durante la autenticación.

### Dependencias:

- `@Autowired UserRepository repository`: Inyecta una instancia de `UserRepository`, que es la interfaz que permite interactuar con la base de datos de usuarios.

### Método `loadUserByUsername`:

Este método es crucial para la autenticación. Spring Security lo usa para cargar el usuario por su nombre de usuario y devolver un objeto `UserDetails`, que contiene la información necesaria para la autenticación y autorización.

1. **Entrada**:

   - Recibe el nombre de usuario (`username`) y lanza una excepción `UsernameNotFoundException` si no lo encuentra.

2. **Búsqueda del usuario**:

   - `repository.findByUsername(username)`: Llama al repositorio para buscar un usuario por su nombre. El repositorio devuelve un `Optional<User>`.

3. **Validación**:

   - Si el `Optional` está vacío, se lanza `UsernameNotFoundException` con un mensaje de error personalizado.
   - En caso de que no esté vacío, se obtiene el usuario de `Optional` con `orElseThrow()`.

4. **Asignación de roles (Authorities)**:

   - Se convierten los roles del usuario en instancias de `GrantedAuthority`, una interfaz de Spring Security que define permisos.
   - Cada rol del usuario (`user.getRoles()`) se transforma en una instancia de `SimpleGrantedAuthority`, usando el nombre del rol como argumento.

5. **Creación del objeto `UserDetails`**:

   - Se retorna una instancia de 

     ```
     User
     ```

      de Spring Security (

     ```
     org.springframework.security.core.userdetails.User
     ```

     ), que contiene:

     - El nombre de usuario (`user.getUsername()`).
     - La contraseña (`user.getPassword()`).
     - Tres atributos booleanos (`user.isEnabled()`, `true`, `true`, `true`) que representan si el usuario está activo, si la cuenta no está expirada, y si las credenciales no han expirado.
     - La lista de `authorities`, que son los roles asociados.

> return new org.springframework.security.core.userdetails.User(
>     user.getUsername(), 
>     user.getPassword(), 
>     user.isEnabled(), // true si el usuario está habilitado
>     true, // la cuenta no ha expirado
>     true, // las credenciales no han expirado
>     true, // la cuenta no está bloqueada
>     authorities // los roles del usuario
> );



Añadiendo JwtAuthenticationFilter. Cree un nuevo paquete llamado filter; este paquete debe ser creado en security.

```java
import java.io.IOException;

import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

import com.fasterxml.jackson.core.exc.StreamReadException;
import com.fasterxml.jackson.databind.DatabindException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.uissurvey.uissurvey_app.domain.entities.User;

import org.springframework.security.core.Authentication;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import org.springframework.security.core.AuthenticationException;

public class JwtAuthenticationFilter extends UsernamePasswordAuthenticationFilter{
   private AuthenticationManager authenticationManager;

    public JwtAuthenticationFilter(AuthenticationManager authenticationManager) {
        this.authenticationManager = authenticationManager;
    }

    @Override
    public Authentication attemptAuthentication(HttpServletRequest request, HttpServletResponse response)
            throws AuthenticationException {

        User user = null;
        String username = null;
        String password = null;

        try {
            user = new ObjectMapper().readValue(request.getInputStream(), User.class);
            username = user.getUsername();
            password = user.getPassword();
        } catch (StreamReadException e) {
            e.printStackTrace();
        } catch (DatabindException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(username,
                password);

        return authenticationManager.authenticate(authenticationToken);
    }
}

```

### **Clase `JwtAuthenticationFilter`**:

Esta clase extiende `UsernamePasswordAuthenticationFilter` para manejar la autenticación de usuarios en la aplicación. Se utiliza para interceptar y procesar solicitudes de autenticación, normalmente al inicio de sesión.

### **Dependencias y Objetos:**

- **`AuthenticationManager`**: Se utiliza para gestionar el proceso de autenticación. Recibe un *token* de autenticación con las credenciales (nombre de usuario y contraseña) y devuelve un objeto de autenticación si las credenciales son válidas.
- **`ObjectMapper`**: De la librería *Jackson*, es usado para leer y convertir los datos de entrada de la solicitud (en formato JSON) a un objeto de la clase `User`.

### Constructor

El constructor recibe el `AuthenticationManager` para autenticar al usuario. Esto permite inyectar el *manager* desde la configuración de seguridad.

### **Método `attemptAuthentication`**:

Este método es el corazón del filtro. Se ejecuta cuando el usuario intenta autenticarse (por ejemplo, al enviar un formulario de inicio de sesión). Aquí, se extraen las credenciales (nombre de usuario y contraseña) de la solicitud HTTP y se intenta autenticar al usuario.

- **Entrada**:
  - `HttpServletRequest request`: Representa la solicitud HTTP que contiene los datos de autenticación.
  - `HttpServletResponse response`: Representa la respuesta HTTP, aunque aquí no se usa directamente.
  - Este método lanza una `AuthenticationException` si ocurre algún problema durante la autenticación.

- **Cuerpo del método**:

1. **Leer los datos del usuario**:

   ```java
   user = new ObjectMapper().readValue(request.getInputStream(), User.class);
   ```

   Utiliza `ObjectMapper` para leer el *input stream* de la solicitud (que se espera esté en formato JSON) y lo convierte en un objeto `User`. Este JSON debe incluir el nombre de usuario y la contraseña.

2. **Obtener el nombre de usuario y la contraseña**:

   ```java
   username = user.getUsername();
   password = user.getPassword();
   ```

   Una vez que el `User` ha sido deserializado, extrae el nombre de usuario y la contraseña.

3. **Manejo de excepciones**: Se incluyen varios bloques `catch` para manejar las posibles excepciones que pueden surgir al leer el JSON:

   - `StreamReadException`: Error al leer el flujo de datos.
   - `DatabindException`: Error al enlazar los datos al objeto `User`.
   - `IOException`: Cualquier error general de entrada/salida.

4. **Crear el token de autenticación**:

   ```java
   UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(username, password);
   ```

   Se crea un objeto `UsernamePasswordAuthenticationToken` usando el nombre de usuario y la contraseña. Este token se utiliza para realizar la autenticación real.

5. **Autenticación**:

   ```java
   return authenticationManager.authenticate(authenticationToken);
   ```

   Finalmente, el `authenticationManager` procesa el token de autenticación para verificar si las credenciales son correctas. Si lo son, devuelve un objeto `Authentication` que representa al usuario autenticado.

## Importar dependencias JWT

1. Ingresar a la pagina oficial de JWT

2. Seleccionar la opcion de Librerias.

   <img src="C:\Users\developer\AppData\Roaming\Typora\typora-user-images\image-20241007211756842.png" alt="image-20241007211756842" style="zoom:80%;" />

3. En el filtro buscar por Java

   <img src="C:\Users\developer\AppData\Roaming\Typora\typora-user-images\image-20241007211905268.png" alt="image-20241007211905268" style="zoom:80%;" />



4. Se recomienda seleccionar la librería con mas popularidad.

   <img src="C:\Users\developer\AppData\Roaming\Typora\typora-user-images\image-20241007212050403.png" alt="image-20241007212050403" style="zoom:80%;" />



5. Cuando ingrese al repo navegar hasta la seccion de Instalación>Maven

   <img src="C:\Users\developer\AppData\Roaming\Typora\typora-user-images\image-20241007212244511.png" alt="image-20241007212244511" style="zoom:80%;" />



6. Copiar las dependencias en el pom del proyecto.

En el paquete Securitycree una clase llamada TokenJwtConfig

```java
import javax.crypto.SecretKey;

import io.jsonwebtoken.Jwts;

public class TokenJwtConfig {
    public static final SecretKey SECRET_KEY = Jwts.SIG.HS256.key().build();
    public static final String PREFIX_TOKEN = "Bearer ";
    public static final String HEADER_AUTHORIZATION = "Authorization";
    public static final String CONTENT_TYPE = "application/json";
}
```

En la clase JwtAuthenticationFilter agregue el metodo successfulAuthentication

```java
    @Override
    protected void successfulAuthentication(HttpServletRequest request, HttpServletResponse response, FilterChain chain,
            Authentication authResult) throws IOException, ServletException {

        org.springframework.security.core.userdetails.User user = (org.springframework.security.core.userdetails.User) authResult.getPrincipal();
        String username = user.getUsername();
        Collection<? extends GrantedAuthority> roles = authResult.getAuthorities();

        Claims claims = Jwts.claims()
                .add("authorities", new ObjectMapper().writeValueAsString(roles))
                .add("username", username)
        .build();


        String token = Jwts.builder()
                .subject(username)
                .claims(claims)
                .expiration(new Date(System.currentTimeMillis() + 3600000))
                .issuedAt(new Date())
                .signWith(SECRET_KEY)
                .compact();

        response.addHeader(HEADER_AUTHORIZATION, PREFIX_TOKEN + token);

        Map<String, String> body = new HashMap<>();
        body.put("token", token);
        body.put("username", username);
        body.put("message", String.format("Hola %s ha iniciado sesion con exito!", username));

        response.getWriter().write(new ObjectMapper().writeValueAsString(body));
        response.setContentType(CONTENT_TYPE);
        response.setStatus(200);
    }
```

Agregue el metodo unsuccessfulAuthentication en la clase JwtAuthenticationFilter

```java
    @Override
    protected void unsuccessfulAuthentication(HttpServletRequest request, HttpServletResponse response,
            AuthenticationException failed) throws IOException, ServletException {
        Map<String, String> body = new HashMap<>();
        body.put("message", "Error en la autenticacion username o password incorrectos!");
        body.put("error", failed.getMessage());

        response.getWriter().write(new ObjectMapper().writeValueAsString(body));
        response.setStatus(401);
        response.setContentType(CONTENT_TYPE);
    }
```

Agregue el siguiente codigo en la clase SpringSecurityConfig

```java
    @Autowired
    private AuthenticationConfiguration authenticationConfiguration;

    @Bean
    AuthenticationManager authenticationManager() throws Exception {
        return authenticationConfiguration.getAuthenticationManager();
    }
```

Agregue el filtro de JwtAuthenticationFilter en el metodo filterchain

```java
.addFilter(new JwtAuthenticationFilter(authenticationManager()))
```

Clase completa

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
public class SpringSecurityConfig {
    @Autowired
    private AuthenticationConfiguration authenticationConfiguration;

    @Bean
    AuthenticationManager authenticationManager() throws Exception {
        return authenticationConfiguration.getAuthenticationManager();
    }
    @Bean
    PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        return http.authorizeHttpRequests((authz) -> authz
                .requestMatchers(HttpMethod.GET,"/api/users").permitAll()
                .requestMatchers(HttpMethod.POST,"/api/users/register").permitAll()
                .requestMatchers("/api/surveyanswer").permitAll()
                .anyRequest().authenticated())
            	.addFilter(new JwtAuthenticationFilter(authenticationManager()))
                .csrf(config -> config.disable())
                .sessionManagement(management -> management.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
                .build();
    }
}
```



# Rate Limiting

El rate limiting (limitación de tasa) es una técnica utilizada para controlar la frecuencia con la que un recurso puede ser accedido o una acción puede ser realizada en un sistema durante un período de tiempo específico. Esta técnica es ampliamente utilizada en servicios web y APIs para prevenir el abuso, garantizar la calidad del servicio, y proteger los recursos del sistema contra sobrecargas.

## Objetivos del Rate Limiting

1. **Prevenir Abuso**:
   - Protege contra el uso excesivo o malicioso de los recursos, evitando que un usuario o un conjunto de usuarios puedan monopolizar el servicio.
2. **Mantener Estabilidad del Sistema**:
   - Asegura que los recursos del sistema no se sobrecarguen, manteniendo la estabilidad y el rendimiento del sistema.
3. **Garantizar Equidad**:
   - Garantiza que todos los usuarios tengan acceso equitativo a los recursos del sistema.
4. **Proteger Contra Ataques**:
   - Mitiga ataques como DDoS (Distributed Denial of Service) limitando la cantidad de solicitudes que pueden ser procesadas.

## Cómo Funciona el Rate Limiting

El rate limiting funciona estableciendo un límite en el número de acciones (como solicitudes HTTP) que un usuario puede realizar en un intervalo de tiempo determinado. Si el usuario excede este límite, se bloquean sus solicitudes adicionales hasta que el intervalo de tiempo se renueve.

## Estrategias Comunes de Rate Limiting

1. **Token Bucket**:
   - Un enfoque popular donde se utiliza un "cubo" que contiene tokens. Cada acción consume un token. Los tokens se recargan a una tasa fija. Si no hay suficientes tokens, la acción se bloquea.
2. **Leaky Bucket**:
   - Similar al token bucket, pero con un enfoque en el "goteo" constante de tokens para mantener el flujo constante de solicitudes procesadas. Las solicitudes que llegan cuando el bucket está lleno se descartan.
3. **Fixed Window Counter**:
   - Cuenta las solicitudes en intervalos de tiempo fijos. Si el número de solicitudes en un intervalo supera el límite, las solicitudes adicionales se bloquean hasta el siguiente intervalo.
4. **Sliding Window Log**:
   - Mantiene un registro de las solicitudes en una ventana de tiempo deslizante. Permite una tasa más granular al registrar cada solicitud individualmente.
5. **Sliding Window Counter**:
   - Similar al Fixed Window Counter, pero con una ventana de tiempo deslizante que proporciona una limitación de tasa más suave.

## Aplicar RateLimit SpringBoot

Importe la dependencia **bucket4j**

```
<!-- https://mvnrepository.com/artifact/com.bucket4j/bucket4j-core -->
<dependency>
    <groupId>com.bucket4j</groupId>
    <artifactId>bucket4j-core</artifactId>
    <version>8.10.1</version>
</dependency>
```

Cree un filtro que interceptará las solicitudes y aplicará la lógica de rate limiting:

> Cree el filtro en el paquete principal del proyecto.
