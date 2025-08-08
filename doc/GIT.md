[TOC]



# GIT

Un Sistema de control de versiones es una herramienta que permite hacer seguimiento (rastrear) los cambios que se han realizado en conjunto de archivos de un proyecto de software.

# GitHub

Servicio de hosting que nos permite almacenar proyectos de desarrollo de software y control de versiones usando git.

# Instalación y Configuración

1. Ejecutar comando **sudo apt update**

2. Ejecutar comando **sudo apt install git**

3. Ejecutar **git --version**

   ![](https://i.ibb.co/TtN6Sss/image.png)

4. Configure credenciales de git localmente

   ```
   git config --global user.name "tra"
   git config --global user.email "131613955+trainingLeader@users.noreply.github.com"
   ```

   ![](https://i.ibb.co/z4t9T9z/image.png)

![](https://i.ibb.co/BVPct6S/image.png)

## Configurando rama Main

```
git config --global init.defaultBranch main
nano ~/.gitconfig
git config --global -e
```

![](https://i.ibb.co/7Smwv4B/image.png)

![](https://i.ibb.co/6DxRDMF/image.png)

## Configuracion editor por defecto

```
git config --global core.editor "Editor"
```

**Visual Studio Code**

```
git config --global core.editor "code --wait"
```

**Vim**

```
git config --global core.editor "vim"
```

![](https://i.ibb.co/9ZPym20/image.png)

![](https://i.ibb.co/xmhbnkS/image.png)

## Resumen Comandos Conf. Inicial

```less
git --version
213225665+johlverpardo@users.noreply.github.com

git config --global user.name "xxxxxxx"
git config --global user.email xxxxxx@gmail.com

git config --global init.defaultBranch main
# muestra todas las configuraciones de Git activas en tu sistema. 
git config --list
# asignando visual studio code como editor de configuración de git
git config --global core.editor "code --wait"
#abre el archivo de configuración global de Git (~/.gitconfig en Linux/macOS o C:\Users\TuUsuario\.gitconfig en Windows) en el #editor de texto predeterminado de Git.
git config --global -e
# para estandarizar los saltos de línea en windows
git config --global core.autocrlf true
# para estandarizar los saltos de línea en linux/mac
git config --global core.autocrlf input
# ver todas las opciones de la configuración en la terminal
git config -h
# ver todas las opciones de la configuración en el navegador
git help config
```



# Conceptos Básicos

## Control de versiones

El control de versiones es un sistema que permite gestionar y realizar un seguimiento de los cambios en el código o en cualquier conjunto de archivos a lo largo del tiempo. Su función principal es guardar distintas versiones o estados de un proyecto, facilitando la colaboración entre desarrolladores y permitiendo volver a versiones anteriores si es necesario.

Algunas de las características clave del control de versiones son:

1. **Historial de cambios**: Almacena cada modificación realizada, lo que permite ver qué cambios se hicieron, quién los hizo y cuándo.
2. **Colaboración**: Facilita que varios desarrolladores trabajen en el mismo proyecto sin pisarse el trabajo, incluso si están modificando los mismos archivos.
3. **Deshacer cambios**: Permite revertir el proyecto a un estado anterior si se cometió un error o si un cambio no resulta como se esperaba.
4. **Ramas (branches)**: Ofrece la capacidad de crear versiones paralelas del proyecto, llamadas "ramas," para experimentar o desarrollar nuevas características sin afectar la versión principal.

Las herramientas de control de versiones más populares incluyen Git, Subversion (SVN), y Mercurial, aunque Git es la más común, especialmente en proyectos de software libre y desarrollo colaborativo.



## Repositorio

![](https://i.ibb.co/wYvvrch/image.png)

Un repositorio es un espacio o almacenamiento en el que se guarda y organiza el código de un proyecto, junto con su historial de cambios y configuraciones. Es como una "biblioteca" de archivos y datos del proyecto, que permite gestionar el control de versiones y la colaboración entre desarrolladores. Los repositorios pueden estar en tu máquina local (repositorio local) o en un servidor en la nube (repositorio remoto) al que pueden acceder varios usuarios.

**Características principales de un repositorio:**

1. **Almacenamiento de código**: Guarda los archivos del proyecto, desde el código fuente hasta los documentos relacionados.
2. **Historial de cambios**: Lleva un registro de todas las modificaciones realizadas, permitiendo a los desarrolladores revisar y restaurar versiones anteriores del proyecto.
3. **Colaboración**: Permite que varios desarrolladores contribuyan al mismo proyecto. Los cambios de cada colaborador se integran al repositorio, facilitando la cooperación.
4. **Ramas**: Permite crear ramas (branches) o versiones paralelas del proyecto para desarrollar nuevas características o probar cambios sin afectar la versión principal.
5. **Acceso remoto**: Un repositorio remoto, como los de plataformas como GitHub, GitLab o Bitbucket, facilita la colaboración al permitir que los desarrolladores trabajen en el mismo proyecto desde diferentes ubicaciones.

## Commit

Un **commit** en el contexto del control de versiones (como Git) es una acción que permite guardar un "punto de control" de los cambios realizados en el proyecto. Es como tomar una "foto" del estado actual del proyecto en un momento específico. Cada commit registra el conjunto de cambios que se han hecho desde el último commit, incluyendo un mensaje que describe esos cambios, lo cual ayuda a mantener un historial claro y detallado de la evolución del proyecto.

![](https://i.ibb.co/GF151V8/image.png)

![](https://i.ibb.co/ThPrmRw/image.png)



### Características de un commit:

1. **Historial de cambios**: Un commit guarda un registro permanente de los cambios en el proyecto, facilitando el seguimiento de lo que se hizo en cada etapa.
2. **Deshacer o revertir cambios**: Gracias al historial de commits, es posible volver a un estado anterior del proyecto si algún cambio resultó en un error o problema.
3. **Colaboración**: Cada commit indica quién hizo el cambio, cuándo, y con qué propósito, ayudando a que los miembros del equipo comprendan el flujo de trabajo y el avance de otros colaboradores.
4. **Mensajes descriptivos**: Al hacer un commit, se recomienda escribir un mensaje que describa brevemente los cambios realizados (como "Corrige error en el cálculo de impuestos" o "Agrega nueva función de búsqueda"). Esto facilita la revisión del historial.

# Áreas en Git

![](https://i.ibb.co/h7SqPT6/image.png)

En Git, las áreas representan diferentes etapas del ciclo de vida de los cambios en los archivos dentro de un repositorio. Estas áreas son esenciales para gestionar versiones y organizar cambios de manera eficiente. Aquí están las principales áreas en Git:

### **Working Directory (Directorio de trabajo)**

Es el área correspondiente al estado ***modified\*** y es la carpeta local de tu computadora donde almacenas los archivos de tu proyecto.

- **Estado:** Los archivos están **modificados** pero no rastreados o preparados para un commit.
- **Acción clave:** Si haces cambios en tus archivos, puedes moverlos al área de preparación con

```
git add archivo
```

### **Staging Area (Área de preparación o index)**

Es el área correspondiente al estado ***staged\*** también se le llama ***index\*** por que es el área donde *git* indexa y agrega los cambios realizados en los archivos previos a comprometerlos en su registro.

- **Estado:** Los archivos están **preparados**.

- **Acción clave:** Para añadir archivos o cambios al área de preparación, usa:

  ```
  git add archivo
  ```

- **Ver archivos preparados**

  ```
  git status
  ```

### **Repository (Repositorio local o commit area)**

Es el área correspondiente al estado ***remote\*** y es el directorio remoto donde almacenamos los archivos del proyecto en alguna plataforma *web* como *GitHub*, *GitLab*, *BitBucket*. *Git* denomina ***origin\*** al repositorio remoto.

- **Estado:** Los archivos están **confirmados**.
- **Acción clave:** Para confirmar cambios desde el área de preparación

```
git commit -m "Mensaje del commit"
```

```
git log — Muestra el historial de commits en el repositorio.
```

### Remote Repository (Repositorio remoto)

Es una copia del repositorio local almacenada en un servidor remoto, como GitHub, GitLab o Bitbucket. Permite colaborar con otros desarrolladores.

- **Estado:** Los cambios están **enviados** al remoto.
- **Acción clave:** Para subir cambios al repositorio remoto:

```
git push origin rama
```

- **Sincronización:** Puedes obtener cambios desde el remoto con

```
git pull origin rama
```

### Ciclo de flujo típico en Git:

1. **Editar archivos** en el directorio de trabajo.
2. **Preparar cambios** en el área de preparación con `git add`.
3. **Confirmar cambios** al repositorio local con `git commit`.
4. **Subir cambios** al repositorio remoto con `git push`.

![](https://i.ibb.co/kKs17QB/image.png)

```
# agregar los cambios de un archivo al staged
git add archivo/directorio
# agregar todos los cambios de todos los archivos al staged
git add .

# los cambios son comprometidos en el repositorio
# debes escribir el mensaje del cambio
# cuando se abra el archivo de configuración
# al terminar guarda y cierra el archivo
# para que los cambios tengan efecto
git commit
# es un shortcut del comando anterior
# escribes y confirmas el mensaje del cambio en un sólo paso
git commit -m "mensaje descriptivo del cambio"


# se agrega el origen remoto de tu repositorio de GitHub
git remote add origin https://github.com/usuario/repositorio.git
# la primera vez que vinculamos el repositorio remoto con el local
git push -u origin main
# para las subsecuentes actualizaciones, sino cambias de rama
git push


#para descargar los cambios del repositorio remoto al local
git pull
```

## De *master* a *main*

Con los desafortunados acontecimientos del 25 de mayo de 2020 en los Estados Unidos que culminaron con el asesinato del afroamericano [*George Floyd*](https://es.wikipedia.org/wiki/Muerte_de_George_Floyd) a manos de policias de la ciudad de *Mineápolis*, se intensificó de manera global el movimiento [*#BlackLivesMatter*](https://es.wikipedia.org/wiki/Black_Lives_Matter).

Con dicho movimiento muchas industrias y empresas comenzaron a tomar acciones para erradicar el racismo.

En la industria de la tecnología por años se han empleado palabras como *master*, *slave*, *whitelist*, *blacklist* entre otras que actualmente no son bien vistas por el contexto y la semántica que implican.

Al respecto *Microsoft* empresa propietaria de *GitHub* decidió comenzar una campaña para reemplazar el nombre de la rama principal de los repositorios de *master* a *main*

### Para repositorios nuevos

```
git init
git add .
git commit -m "Primer commit"
git branch -M main
git remote add origin https://github.com/usuario/repositorio.git
git push -u origin main
```

### Para repositorios existentes

```
git branch -M main
git remote add origin https://github.com/usuario/repositorio.git
git push -u origin main
```

### Para reemplazar la rama *master* por *main* en *GitHub*

```
# Paso 1
# Crea la rama local main y pásale el historial de la rama master
git branch -m master main


# Paso 2
# Haz un push de la nueva rama local main en el repositorio remoto de GitHub
git push -u origin main


# Paso 3
# Cambia el HEAD actual a la rama main
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main

Paso 4
Cambia la rama default de master a main en tu repositorio de GitHub .

# Paso 5
# Elimina la rama master del repositorio remoto
git push origin --delete master



```



## Estado de los archivos en git

![](https://i.ibb.co/6cK5K3z/image.png)

En Git, los archivos pasan por diferentes **estados** durante su ciclo de vida en el repositorio. Estos estados indican cómo Git percibe un archivo en relación con su historial y el área de preparación. Aquí están los principales estados de los archivos en Git:

### **Untracked (No rastreado)**

El archivo existe en el directorio de trabajo, pero Git no lo está rastreando.

- **Características:**
  - Git no lo incluye en el repositorio.
  - Necesita ser añadido explícitamente para que Git comience a rastrearlo.
- **Acción para rastrear el archivo:**

```
git add archivo
```

### **Tracked (Rastreado)**

El archivo ya está siendo gestionado por Git. Este estado tiene subcategorías:

#### a) **Unmodified (No modificado):**

El archivo está sincronizado con el último commit. No se han realizado cambios.

- **Acción:** Si lo editas, su estado cambiará a **modified**.

#### b) **Modified (Modificado):**

El archivo ha sido editado, pero los cambios aún no se han añadido al área de preparación.

- Acción para preparar los cambios:

  ```
  git add archivo
  ```

#### c) **Staged (Preparado):**

El archivo ha sido modificado y añadido al área de preparación. Está listo para ser confirmado (commit).

- **Acción para confirmar los cambios**

```
git commit -m "Mensaje del commit"
```

### **Deleted (Eliminado)**

El archivo ha sido eliminado del directorio de trabajo.

Si desea incluir la eliminación en el próximo commit

```
git rm archivo
git commit -m "Eliminado archivo"
```

Si quiere restaurarlo desde el último commit:

```
git checkout -- archivo
```



## Ayuda

```
# ayuda en la terminal
git comando -
# ayuda en el navegador
git help comando
```

![](https://i.ibb.co/KzNXbMG/image.png)



# Taller Aplicando Comandos Git

1. Cree una nueva carpeta llamada projectsDev **mkdir projectsDev**

2. Acceda a la carpeta **cd projectsDev/**

3. Cree un archivo llamado README.md  **touch README.md**

4. Cree el archivo .gitignore **touch .gitignore**

   > El archivo `.gitignore` es una herramienta que permite a Git ignorar ciertos archivos o directorios en un repositorio. Esto es útil para excluir archivos generados automáticamente, configuraciones locales, claves privadas o cualquier archivo que no desees rastrear ni incluir en el repositorio.

```
tree -a
.
├── .gitignore
└── README.md
```

5. Inicialice el repositorio local  **git init**

```
trainer@johlver-virtual-machine:~/projectsDev$ tree -a -L 2
.
├── .git
│   ├── branches
│   ├── config
│   ├── description
│   ├── HEAD
│   ├── hooks
│   ├── info
│   ├── objects
│   └── refs
├── .gitignore
└── README.md

6 directories, 5 files

```

6. Abrir el proyecto en visual studio code **code .**

![](https://i.ibb.co/KVtdSwf/image.png)

7. Pasar los archivos de Working Directory a Staging **git add**

   ![](https://i.ibb.co/SN5Xkf0/image.png)

   > El comando `git add` es fundamental en Git y se utiliza para **añadir cambios al área de preparación** (staging area). Esto significa que los archivos o cambios seleccionados estarán listos para ser incluidos en el próximo commit. Sin usar `git add`, los cambios no se guardarán en el historial del repositorio.
   >
   > Añadir un archivo específico : **git add archivo.txt**
   >
   > Añadir todos los archivos en el directorio actual: **git add .**
   >
   > Añadir todos los archivos modificados (excluyendo no rastreados):  **git add -u**
   >
   > Añadir todos los archivos con un patrón específico: **git add *.txt**
   >
   > Añadir un directorio completo : **git add directorio/**

8. Verifica los archivos que han pasado a staging **git status**

   > El comando `git status` se utiliza en Git para mostrar el estado actual del repositorio. Este comando es clave para entender qué cambios han ocurrido en tu proyecto y en qué etapa del ciclo de vida de Git se encuentran tus archivos.

![](https://i.ibb.co/vkvrWX5/image.png)



9. Realizar commit para pasar a HEAD **git commit**

   > El comando `git commit` es fundamental en Git y se utiliza para guardar los cambios en el repositorio local. Los commits actúan como puntos de control en el historial del proyecto, permitiéndote regresar a versiones anteriores si es necesario.
   >
   > ### **Qué hace `git commit`?**
   >
   > - Confirma (guarda) los cambios del área de preparación (staging area) al historial del repositorio.
   > - Crea un mensaje descriptivo que documenta qué cambios se realizaron.
   > - No afecta el repositorio remoto; solo modifica el repositorio local.
   >
   > Sintaxis : **git commit -m "Mensaje del commit"**

   ![](https://i.ibb.co/gr6BnPp/image.png)

![](https://i.ibb.co/w6hVgT6/image.png)

Modifica el archivo README y crea un nuevo commit usando **git commit -m**

![](https://i.ibb.co/dtVNCL8/image.png)

10. Cree un nuevo repositorio en git. Use url amigables

    > Una **URL amigable** es una dirección web diseñada para ser fácil de leer y comprender tanto para los usuarios como para los motores de búsqueda. Estas URLs suelen ser cortas, descriptivas y están estructuradas de manera lógica para proporcionar información clara sobre el contenido de la página.
    >
    > ### **Características de una URL amigable**
    >
    > 1. **Claridad:** Describe el contenido de la página de forma precisa.
    > 2. **Longitud adecuada:** Es corta, pero contiene la información esencial.
    > 3. **Uso de palabras clave:** Incluye términos relevantes para mejorar el SEO.
    > 4. **Separadores claros:** Usa guiones `-` para separar palabras (no espacios ni subrayados `_`).
    > 5. **Sin caracteres especiales:** Evita caracteres como `%`, `&`, `?`, `=`, o `#` innecesarios.
    > 6. **Sin extensiones visibles:** No incluye `.html`, `.php`, etc.
    >
    > ### **Ejemplo de transformación de URL**
    >
    > | **URL no amigable**                | **URL amigable**                             |
    > | ---------------------------------- | -------------------------------------------- |
    > | `https://tienda.com/prod?id=1234`  | `https://tienda.com/productos/zapatos-rojos` |
    > | `https://blog.com/?p=456`          | `https://blog.com/como-mejorar-tu-sitio-web` |
    > | `https://web.com/cat=42&sort=desc` | `https://web.com/categoria/tecnologia`       |

![](https://i.ibb.co/RyVcKHc/image.png)

![](https://i.ibb.co/yn7L05T/image.png)

11. Agregue el repositorio remoto a el local **git remote add origin NombreDelRepositorio**

    ```
    git remote add origin https://github.com/trainingLeader/taller-git.git
    ```

12. Suba los cambios del repositorio local al remoto con el comando

    > Recuerde que debe autorizar el uso de Visual Studio Code para acceder al git
    >
    > El comando `git push -u origin main` se utiliza para subir los cambios confirmados en la rama local `main` al repositorio remoto configurado como `origin` y establecer una relación de seguimiento entre la rama local y la rama remota. Esto simplifica los futuros envíos de cambios, ya que no tendrás que especificar el nombre del remoto ni de la rama cada vez

![](https://i.ibb.co/8DngjdM/image.png)

![](https://i.ibb.co/BG3SbPW/image.png)

## Pull

El comando `git pull` se utiliza en Git para **descargar cambios del repositorio remoto** e integrarlos con tu rama local. Es una combinación de dos comandos en uno:

1. **`git fetch`**: Descarga los cambios del remoto al repositorio local, pero no los integra.
2. **`git merge`**: Integra los cambios descargados en la rama actual.

Para el ejemplo del taller se agregara un archivo de licencia

1. Agregue un nuevo archivo desde git

![](https://i.ibb.co/8B71JWM/image.png)

2. Agregue el nombre del archivo como license.txt y seleccione una plantilla de licencia

   ![](https://i.ibb.co/4gQd5vt/image.png)

![](https://i.ibb.co/0nNTzjf/image.png)

3. Genere el commit desde git

   ![](https://i.ibb.co/NxJsRvG/image.png)

![](https://i.ibb.co/x1XwpYv/image.png)

4. Desde la terminal ejecute el comando **git pull**

   ![](https://i.ibb.co/hKQx9Pb/image.png)

![](https://i.ibb.co/JKLnjGr/image.png)

# .gitIgnore

El archivo **`.gitignore`** en Git se utiliza para especificar archivos o directorios que deseas que Git ignore, es decir, que no se incluyan en el control de versiones. Es útil para evitar que subas archivos temporales, configuraciones locales o archivos sensibles al repositorio.

### ¿Cómo funciona `.gitignore`?

1. **Ubicación:**

   - Se coloca generalmente en la raíz del proyecto.
   - Puedes tener múltiples archivos `.gitignore` en diferentes subdirectorios, y cada uno aplicará reglas específicas para su ubicación.

2. **Reglas básicas:**

   - Las líneas en `.gitignore` indican patrones que Git debe ignorar.

   ```
   # Ignorar archivos temporales
   *.log
   
   # Ignorar una carpeta específica
   /build/
   
   # Ignorar todos los archivos en una carpeta excepto uno
   /config/*
   !/config/config.example.json
   ```

   **Importante:**
   Si un archivo ya está siendo rastreado por Git, no será ignorado automáticamente, incluso si agregas una regla en `.gitignore`. Debes deshacer el seguimiento de esos archivos con:

   ```
   git rm --cached archivo
   ```

   ### Ejemplo básico de un archivo `.gitignore`

   Supongamos que tienes un proyecto Node.js. Un `.gitignore` típico sería:

   ```
   # Dependencias de Node.js
   node_modules/
   
   # Archivos de entorno
   .env
   
   # Archivos de logs
   *.log
   logs/
   npm-debug.log*
   yarn-debug.log*
   yarn-error.log*
   
   # Sistemas operativos
   .DS_Store      # macOS
   Thumbs.db      # Windows
   
   # Directorios de compilación
   /build/
   /dist/
   ```

   

# Ramas

Las **ramas en Git** son una característica poderosa que permite trabajar en diferentes líneas de desarrollo dentro de un repositorio. Una rama es esencialmente un puntero a un commit específico, lo que facilita trabajar en funcionalidades nuevas, corregir errores o experimentar sin afectar el código principal.

## Conceptos clave

1. **Rama principal (main o master):**
   - Es la rama por defecto que se crea al iniciar un repositorio. Normalmente contiene la versión estable del proyecto.
2. **Ramas secundarias:**
   - Estas se crean para desarrollar nuevas funcionalidades, corregir errores, o probar ideas antes de fusionarlas con la rama principal.
3. **Fusionar (merge):**
   - Es el proceso de integrar cambios de una rama a otra. Esto puede ser con o sin conflictos.
4. **Conflictos:**
   - Ocurren cuando los mismos archivos han sido modificados en ambas ramas. Git requerirá que resuelvas manualmente estas diferencias.

## Comandos básicos relacionados con ramas en Git

```
# crear rama
git branch nombre-rama

# cambiar de rama
git checkout nombre-rama

# crear una rama y cambiarte a ella
git checkout -b rama

# eliminar rama
git branch -d nombre-rama

# eliminar ramas remotas
git push origin --delete nombre-rama

#eliminar rama (forzado)
git branch -D nombre-rama

# listar todas las ramas del repositorio
git branch

# lista ramas no fusionadas a la rama actual
git branch --no-merged

# lista ramas fusionadas a la rama actual
git branch --merged

# rebasar ramas
git checkout rama-secundaria
git rebase rama-principal
```

## Taller Ramas

1. Abrir en visual studio code el folder **projectsDev** que se trabajo en el taller de aplicación de comandos de git.

2. Visualizar las ramas creadas con el comando **git branch**

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git branch
   * main
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

3. Cree una nueva rama llamada html y ejecute el comando para visualizar las ramas existentes.

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git branch html
   trainer@johlver-virtual-machine:~/projectsDev$ git branch
     html
   * main
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

4. Selecciona la rama html con el comando **git checkout**

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git checkout html
   Switched to branch 'html'
   trainer@johlver-virtual-machine:~/projectsDev$ git branch
   * html
     main
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

   Como se puede observar html tiene un (*) esto indica que ha sido seleccionada la rama

5. Cree una nueva rama llamada js y usa el comando **git checkout** para seleccionar la rama creada.

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git checkout -b js
   Switched to a new branch 'js'
   trainer@johlver-virtual-machine:~/projectsDev$ git branch
     html
   * js
     main
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

6. Elimine las ramas creadas anteriormente con el comando **git branch** 

   > Tenga en cuenta que no se debe estas ubicado en la rama a borrar

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git checkout main
   Switched to branch 'main'
   Your branch is up to date with 'origin/main'.
   trainer@johlver-virtual-machine:~/projectsDev$ git branch
     html
     js
   * main
   trainer@johlver-virtual-machine:~/projectsDev$ git branch -d html
   Deleted branch html (was 3465c76).
   trainer@johlver-virtual-machine:~/projectsDev$ git branch -d js
   Deleted branch js (was 3465c76).
   trainer@johlver-virtual-machine:~/projectsDev$ git branch
   * main
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

7. Cree nuevamente la rama html

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git checkout -b html
   Switched to a new branch 'html'
   trainer@johlver-virtual-machine:~/projectsDev$ git branch
   * html
     main
   ```

8. Cree un archivo llamado index.html y use el comando git para trakear los archivos creados.

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git add .
   trainer@johlver-virtual-machine:~/projectsDev$ git status
   On branch html
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)
           new file:   index.html
   ```

9. Cree un commit usando el comando **git commit**

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git commit -m "Creacion documento html"
   [html d5cf366] Creacion documento html
    1 file changed, 11 insertions(+)
    create mode 100644 index.html
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

   Ejecuta el comando **git push**

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git push
   fatal: The current branch html has no upstream branch.
   To push the current branch and set the remote as upstream, use
   
       git push --set-upstream origin html
   ```

   Nota. Cuando se ejecuta el comando se notifica un error ya que la rama html no se encuentra en el remoto. Para solucionar el error ejecute el comando git push -u origin Nombre-de-la-rama

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git push -u origin html
   Enumerating objects: 4, done.
   Counting objects: 100% (4/4), done.
   Delta compression using up to 4 threads
   Compressing objects: 100% (3/3), done.
   Writing objects: 100% (3/3), 478 bytes | 478.00 KiB/s, done.
   Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
   remote: Resolving deltas: 100% (1/1), completed with 1 local object.
   remote: 
   remote: Create a pull request for 'html' on GitHub by visiting:
   remote:      https://github.com/trainingLeader/taller-git/pull/new/html
   remote: 
   To https://github.com/trainingLeader/taller-git.git
    * [new branch]      html -> html
   Branch 'html' set up to track remote branch 'html' from 'origin'.
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

   Resultado en git

   ![](https://i.ibb.co/yVhsZpf/image.png)

10. Cree otra rama llamada css y ubicate en la rama, crea el archivo style.css y realiza commit

    ```
    trainer@johlver-virtual-machine:~/projectsDev$ git checkout -b css
    Switched to a new branch 'css'
    trainer@johlver-virtual-machine:~/projectsDev$ git add .
    trainer@johlver-virtual-machine:~/projectsDev$ git status
    On branch css
    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            new file:   style.css
    
    trainer@johlver-virtual-machine:~/projectsDev$ git commit -m "Add css file style"
    [css 853b093] Add css file style
     1 file changed, 3 insertions(+)
     create mode 100644 style.css
    trainer@johlver-virtual-machine:~/projectsDev$ git push -u origin css
    Enumerating objects: 4, done.
    Counting objects: 100% (4/4), done.
    Delta compression using up to 4 threads
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (3/3), 336 bytes | 336.00 KiB/s, done.
    Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
    remote: Resolving deltas: 100% (1/1), completed with 1 local object.
    remote: 
    remote: Create a pull request for 'css' on GitHub by visiting:
    remote:      https://github.com/trainingLeader/taller-git/pull/new/css
    remote: 
    To https://github.com/trainingLeader/taller-git.git
     * [new branch]      css -> css
    Branch 'css' set up to track remote branch 'css' from 'origin'.
    trainer@johlver-virtual-machine:~/projectsDev$ 
    ```

11. Repita los pasos anteriores y cree la rama js. No olvidar ubicarse en la rama principal

    ```
    trainer@johlver-virtual-machine:~/projectsDev$ git checkout -b js
    Switched to a new branch 'js'
    trainer@johlver-virtual-machine:~/projectsDev$ git add .
    trainer@johlver-virtual-machine:~/projectsDev$ git status
    On branch js
    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            new file:   app.js
    
    trainer@johlver-virtual-machine:~/projectsDev$ git commit -m "Add file Js"
    [js e54d648] Add file Js
     1 file changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 app.js
    trainer@johlver-virtual-machine:~/projectsDev$ git push -u origin js
    Enumerating objects: 3, done.
    Counting objects: 100% (3/3), done.
    Delta compression using up to 4 threads
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (2/2), 256 bytes | 256.00 KiB/s, done.
    Total 2 (delta 1), reused 0 (delta 0), pack-reused 0
    remote: Resolving deltas: 100% (1/1), completed with 1 local object.
    remote: 
    remote: Create a pull request for 'js' on GitHub by visiting:
    remote:      https://github.com/trainingLeader/taller-git/pull/new/js
    remote: 
    To https://github.com/trainingLeader/taller-git.git
     * [new branch]      js -> js
    Branch 'js' set up to track remote branch 'js' from 'origin'.
    trainer@johlver-virtual-machine:~/projectsDev$ 
    ```

12. Visualice el historial de los commit con el comando **git log**

    ```
    trainer@johlver-virtual-machine:~/projectsDev$ git log
    commit e54d648bafaacc7f4dae1ad553558464e2ed5be9 (HEAD -> js, origin/js)
    Author: trainingLeader <131613955+trainingLeader@users.noreply.github.com>
    Date:   Sun Nov 24 20:15:00 2024 -0500
    
        Add file Js
    
    commit 3465c76440b1a307c4ba6de49e4c75374a65bf70 (origin/main, main)
    Author: trainingLeader <131613955+trainingLeader@users.noreply.github.com>
    Date:   Mon Nov 18 19:37:29 2024 -0500
    
        Create LICENSE
        
        Add license file to repository
    
    commit c42e973ece2eaba14ac1a8921c1e10735b3c12c2
    Author: trainingLeader <131613955+trainingLeader@users.noreply.github.com>
    Date:   Mon Nov 18 18:58:42 2024 -0500
    
        Agregando titulo
    
    commit 419c95d9809410127e0e91accdb483043284e92f
    Author: trainingLeader <131613955+trainingLeader@users.noreply.github.com>
    Date:   Mon Nov 18 18:50:07 2024 -0500
    
        Primer commit
    trainer@johlver-virtual-machine:~/projectsDev$ 
    ```

    

# Registro del historial

**`git log`** nos permite conocer todo el historial de un proyecto, con la información de la fecha, el autor y id de cada cambio.

```less
git log

# muestra en una sola línea por cambio
git log --oneline

# guarda el log en la ruta y archivo que especifiquemos
git log > commits.txt

# muestra el historial con el formato que indicamos
git log --pretty=format:"%h - %an, %ar : %s"

# cambiamos la n por cualquier número entero y mostrará los n cambios recientes
git log -n

# muestra los cambios realizados después de la fecha especificada
git log --after="2024-07-07 00:00:00"

# muestra los cambios realizados antes de la fecha especificada
git log --before="2024-07-08 00:00:00"

# muestra los cambios realizados en el rango de fecha especificado
git log --after="2024-07-07 00:00:00" --before="2024-07-08 00:00:00"

# muestra una gráfica del historial de cambios, rama y fusiones
git log --oneline --graph --all

# muestra todo el registro de acciones del log
# incluyendo inserciones, cambios, eliminaciones, fusiones, etc.
git reflog

# diferencias entre el Working Directory y el Staging Area
git diff
```

# Reseteo del historial

```less
#nos muestra el listado de archivos nuevos (untracked), borrados o editados
git status

# borra HEAD
git reset --soft

# borra HEAD y Staging
git reset --mixed

# borra todo: HEAD, Staging y Working Directory
git reset --hard

# deshace todos los cambios después del commit indicado, preservando los cambios localmente
git reset id-commit

# desecha todo el historial y regresa al commit especificado
git reset --hard id-commit
```



# Conventional commit

**Conventional Commit** es una especificación de formato para los mensajes de confirmación (commits) en sistemas de control de versiones como Git. Su objetivo principal es proporcionar una manera estructurada y semántica de describir los cambios realizados en un proyecto, facilitando la colaboración, la automatización y la comprensión del historial del proyecto.

### **Estructura de un mensaje de commit convencional**

Un mensaje de commit convencional sigue esta estructura básica:

```less
<tipo>[alcance opcional]: <descripción corta>

[cuerpo opcional]

[pie de mensaje opcional con referencias y notas]
```

#### **Elementos principales**

1. **Tipo (`<tipo>`):** Indica la categoría del cambio. Ejemplos comunes incluyen:
   - `feat`: Una nueva funcionalidad.
   - `fix`: Corrección de un error.
   - `docs`: Cambios en la documentación.
   - `style`: Cambios que no afectan la lógica del código (formato, espacios, etc.).
   - `refactor`: Cambios en el código que no corrigen errores ni agregan funcionalidades.
   - `test`: Adición o modificación de pruebas.
   - `chore`: Cambios en herramientas o configuraciones sin afectar el código fuente.
2. **Alcance (`[alcance opcional]`):** Una descripción opcional que especifica qué parte del proyecto se ve afectada (e.g., `UI`, `API`, `auth`).
3. **Descripción corta (`<descripción corta>`):** Un resumen breve y claro del cambio realizado.
4. **Cuerpo (`[cuerpo opcional]`):** Proporciona más detalles sobre el cambio, incluyendo razones y contexto.
5. **Pie de mensaje (`[pie de mensaje opcional]`):** Incluye información como referencias a issues cerrados o notas adicionales:
   - `BREAKING CHANGE`: Indica un cambio que rompe la compatibilidad con versiones anteriores.
   - Referencias a issues: `Closes #123`.

```
feat(auth): add login functionality

Added login functionality using OAuth2.0. Updated the authentication flow to use the new token endpoint.

BREAKING CHANGE: The old login endpoint `/login-basic` is now replaced by `/login-oauth`.

```

### Tipos de commits

Los tipos de commits son los siguientes:

- **feat**: Una nueva característica o funcionalidad. Tendría correlación con una versión MINOR siguiendo *SemVer*.
- **fix**: Un error corregido. Tendría correlación con una versión PATCH siguiendo *SemVer*.
- **BREAKING CHANGE**: Un cambio que contenga esta palabra en el `footer` del mensaje o un signo `!` despues del tipo o scope, rompe la compatibilidad con versiones anteriores. Tendría correlación con una versión MAJOR siguiendo *SemVer*.

Se permiten también los siguientes tipos:

- **build**: Cambios que afectan el sistema de compilación o dependencias externas (ej. cambios en el `package.json`).
- **ci**: Cambios en nuestros archivos y scripts de configuración de integración continua.
- **docs**: Cambios en la documentación.
- **chore**: Otros cambios que no afectan el código fuente.
- **perf**: Un cambio de código que mejora el rendimiento.
- **refactor**: Un cambio de código que no corrige un error ni agrega una característica.
- **style**: Cambios que no afectan el significado del código (espacios en blanco, formato, puntos y comas faltantes, etc).
- **test**: Agregar pruebas faltantes o corregir pruebas existentes.

### **Ventajas de usar Conventional Commit**

1. **Estandarización:** Los mensajes son consistentes, lo que facilita la colaboración entre equipos.
2. **Automatización:** Permite herramientas como `commitlint` o `semantic-release` para generar automáticamente changelogs, versiones semánticas y más.
3. **Claridad:** Hace que el historial de commits sea más fácil de entender.
4. **Integración con CI/CD:** Es más fácil automatizar procesos basados en tipos de cambios.

Ejemplos

```less
fix(ui): bugfix on Button component

```

```less
Commit que rompe la compatibilidad con versiones anteriores, aunque no añade características nuevas ni corrige bugs.

chore!: drop support for Node 6

BREAKING CHANGE: use JavaScript features not available in Node 6.
```

```less
Commit que agrega pruebas faltantes
test(ui): add missing tests for Button component

```

### Gitemoji

**Gitemoji** es una convención que utiliza emojis para representar de forma visual el propósito o el tipo de cambio realizado en un commit dentro de un sistema de control de versiones como Git. Es una forma creativa y efectiva de mejorar la legibilidad y comprensión del historial de commits.

### **Cómo funciona Gitemoji**

Cada emoji representa un tipo específico de cambio. Los emojis se colocan al inicio del mensaje de commit, seguidos de una breve descripción del cambio.

Ejemplo

```less
✨ feat: add user authentication module
🐛 fix: resolve null pointer exception in login form
📝 docs: update README with installation instructions
```

### **Emojis comunes**

| Emoji                            | Propósito                           | Tipo sugerido (Conventional Commit) |
| -------------------------------- | ----------------------------------- | ----------------------------------- |
| ✨ (`:sparkles:`)                 | Añadir una nueva funcionalidad      | `feat`                              |
| 🐛 (`:bug:`)                      | Corrección de errores               | `fix`                               |
| 📝 (`:memo:`)                     | Actualizar documentación            | `docs`                              |
| 🎨 (`:art:`)                      | Mejoras de formato o estilo         | `style`                             |
| 🔥 (`:fire:`)                     | Eliminar código o archivos          | `refactor`                          |
| 🚑️ (`:ambulance:`)                | Hotfix (corrección urgente)         | `fix`                               |
| ♻️ (`:recycle:`)                  | Refactorización de código           | `refactor`                          |
| ✅ (`:white_check_mark:`)         | Añadir o modificar pruebas          | `test`                              |
| 🔧 (`:wrench:`)                   | Cambios en configuración            | `chore`                             |
| 🚀 (`:rocket:`)                   | Implementar algo en producción      | `chore`                             |
| ⚡ (`:zap:`)                      | Mejoras de rendimiento              | `perf`                              |
| 🐳 (`:whale:`)                    | Cambios relacionados con Docker     | `chore`                             |
| 📦️ (`:package:`)                  | Añadir o actualizar dependencias    | `chore`                             |
| 💄 (`:lipstick:`)                 | Cambios en el diseño o UI           | `style`                             |
| 🚨 (`:rotating_light:`)           | Solución de advertencias de linting | `fix`                               |
| 🔒 (`:lock:`)                     | Solución de problemas de seguridad  | `fix`                               |
| 🚧 (`:construction:`)             | Trabajo en progreso (WIP)           | `chore`                             |
| 🗑️ (`:wastebasket:`)              | Borrar archivos o código            | `chore`                             |
| 🌱 (`:seedling:`)                 | Inicialización de proyecto          | `chore`                             |
| 📈 (`:chart_with_upwards_trend:`) | Mejorar análisis o seguimiento      | `feat`                              |
| 🐿️ (`:chipmunk:`)                 | Cambios experimentales              | `feat`                              |

### **Ventajas de usar Gitemoji**

1. **Visualización rápida:** Los emojis son intuitivos y facilitan identificar rápidamente el propósito de cada commit.
2. **Estandarización:** Mejora la consistencia en equipos al usar un lenguaje visual común.
3. **Mejora en la comunicación:** Hace que los mensajes de commit sean más atractivos y claros.



### Taller

1. Abra el proyecto creado en los apartados anteriores

2. Instale la herramienta gitmoji-cli use el comando **npm install -g gitmoji-cli** En caso de tener errores instalar el nvm ver url https://gndx.dev/blog/instalar-nvm-en-ubuntu-20-04/

3. Ejecute nuevamente el comando **npm install -g gitmoji-cli**

4. Realice actualización del README

5. Agrega el cambio al staging con **git add .**

6. Inicialice el gitmoji-cli : **gitmoji -i**

   ```less
   trainer@johlver-virtual-machine:~/projectsDev$ gitmoji -i
   ✔ Gitmoji commit hook created successfully
   ```

7. Ejecute el comando **gitmoji -c** y seleccione el emoji que se ajuste al commit para el caso seleccionar Add or Update documentation

   ![](https://i.ibb.co/0hHSfvY/image.png)

8. Agregue el titulo del commit

   ![](https://i.ibb.co/pQLND5X/image.png)

9. Ingrese el mensaje largo del commit

   ![](https://i.ibb.co/7KHfxrq/image.png)

10. Hacer push

En caso de tener problemas revise el siguiente resumen:

```less
trainer@johlver-virtual-machine:~/apoloJ1$ git add .
trainer@johlver-virtual-machine:~/apoloJ1$ gitmoji -i
✔ Gitmoji commit hook created successfully
trainer@johlver-virtual-machine:~/apoloJ1$ gitmoji -c
? Choose a gitmoji: 🔨  - Add or update development scripts.
? Enter the commit title [18/48]: Add code html file
? Enter the commit message: Add structure to file html blablalbla

Error: Seems that you're trying to commit with the cli but you have the hook created.
If you want to use the `gitmoji -c` command you have to remove the hook with the command `gitmoji -r`. 
The hook must be used only when you want to commit with the instruction `git commit`

trainer@johlver-virtual-machine:~/apoloJ1$ gitmoji -r
✔ Gitmoji commit hook removed successfully
trainer@johlver-virtual-machine:~/apoloJ1$ gitmoji -c
? Choose a gitmoji: ✨  - Introduce new features.
? Enter the commit title [12/48]: Ad structure
? Enter the commit message: demo
[main a011f57] ✨ Ad structure
 1 file changed, 11 insertions(+)
trainer@johlver-virtual-machine:~/apoloJ1$ git log --oneline
a011f57 (HEAD -> main) ✨ Ad structure
366fd2d (origin/main) docs: :memo: Add new line
6c8afac Create LICENSE
dbfd3f4 Add title README
ec17259 Start Project Web
trainer@johlver-virtual-machine:~/apoloJ1$ 
```



# Taller interactuando con el ultimo commit

1. Realice una modificación al archivo html. Para el caso practico agregue una lista ordenada con las estaciones climaticas.

   ```
       <ol>
           <li>Primavera</li>
           <li>Verano</li>
           <li>Invierno</li>
       </ol>
   ```

2. Agregue los cambios y realice un commit

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git add .
   trainer@johlver-virtual-machine:~/projectsDev$ git commit -m "Agregando estaciones"
   [main 78c2fbb] Agregando estaciones
    1 file changed, 5 insertions(+)
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

3. Liste el historial de los commits realizados **git log --oneline**

   ```
   78c2fbb (HEAD -> main) Agregando estaciones
   b8589d7 (origin/main) Resolviendo los conflictos de forma manual
   a4c9706 (html) Importacion archivo JS
   0799721 Agregando hoja de estilos al html
   6fcd14f Merge branch 'js'
   e54d648 (origin/js, js) Add file Js
   853b093 (origin/css, css) Add css file style
   d5cf366 (origin/html) Creacion documento html
   3465c76 Create LICENSE
   c42e973 Agregando titulo
   419c95d Primer commit
   ```

4. Agregue la estación Otoño  para modificar el ultimo commit realizado y vincular los cambios. Ejecute primero el comando **git add .** y posteriormente **git commit --amend --no-edit**

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git add .
   trainer@johlver-virtual-machine:~/projectsDev$ git commit --amend --no-edit
   [main 36cebe3] Agregando estaciones
    Date: Mon Nov 25 15:30:22 2024 -0500
    1 file changed, 6 insertions(+)
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

### Modificar el mensaje del ultimo commit

1. Realice cambios al documento html

   ```html
   <ol>
       <li>Primavera que buena estacion</li>
       <li>Verano hace mucha calor</li>
       <li>Invierno que frio tan horrible</li>
       <li>Otoño que calido el clima</li>
   </ol>
   ```

2. Agregue los cambios al stagging con **git add .**  ejecute el comando **git commit --amend -m "Nuevo mensaje"**

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git add .
   trainer@johlver-virtual-machine:~/projectsDev$ git commit --amend -m "Se agregaron descripciones a las estaciones"
   [main 9718733] Se agregaron descripciones a las estaciones
    Date: Mon Nov 25 15:30:22 2024 -0500
    1 file changed, 6 insertions(+)
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git log --oneline
   9718733 (HEAD -> main) Se agregaron descripciones a las estaciones
   b8589d7 Resolviendo los conflictos de forma manual
   a4c9706 (html) Importacion archivo JS
   0799721 Agregando hoja de estilos al html
   6fcd14f Merge branch 'js'
   e54d648 (origin/js, js) Add file Js
   853b093 (origin/css, css) Add css file style
   d5cf366 (origin/html) Creacion documento html
   3465c76 Create LICENSE
   c42e973 Agregando titulo
   419c95d Primer commit
   ```

3. Ejecute  el comando **git push**

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git push
   To https://github.com/trainingLeader/taller-git.git
    ! [rejected]        main -> main (non-fast-forward)
   error: failed to push some refs to 'https://github.com/trainingLeader/taller-git.git'
   hint: Updates were rejected because the tip of your current branch is behind
   hint: its remote counterpart. Integrate the remote changes (e.g.
   hint: 'git pull ...') before pushing again.
   hint: See the 'Note about fast-forwards' in 'git push --help' for details.
   ```

   COMO SE PUEDE OBSERVAR OBTENEMOS UN ERROR YA QUE REALIZAMOS CAMBIOS A UN COMMIT QUE YA ESTA CARGADO EN EL REPOSITORIO REMOTO. PARA SOLUCIONAR EL PROBLEMA SE DEBE REALIZAR UN **git pull origin **. En caso de salir un error de ramas divergentes ejecutar primero el comando **git config pull.rebase true** y posteriormente ejecutar **git pull**. Cuando se ejecuta el comando se debe resolver los conflictos.

   ![](https://i.ibb.co/Hz2sqyr/image.png)

​	En esta ocasión se utilizara el menú interactivo de resolucion de conflictos mostrado por visual studio code

​	![](https://i.ibb.co/gd6gb6S/image.png)

> 1. **Accept Current Change (Aceptar cambio actual):**
>    - Al elegir esta opción, se conserva el cambio que ya existe en tu rama local. Es decir, los cambios provenientes de la rama remota (incoming changes) serán descartados.
> 2. **Accept Incoming Change (Aceptar cambio entrante):**
>    - Esta opción acepta únicamente los cambios provenientes de la rama remota (incoming changes). Los cambios locales serán descartados.
> 3. **Accept Both Changes (Aceptar ambos cambios):**
>    - Se combinan tanto los cambios locales como los entrantes. Esto puede resultar en que ambos conjuntos de cambios aparezcan juntos en el archivo final, lo que podría necesitar edición adicional para que funcione correctamente.
> 4. **Compare Changes (Comparar cambios):**
>    - Muestra una comparación detallada entre los cambios locales y los entrantes. Es útil si necesitas analizar las diferencias antes de decidir cuál aceptar o cómo fusionarlos manualmente.
>
> ### ¿Cómo decidir qué opción usar?
>
> - **Usa "Accept Current Change"** si prefieres mantener tus cambios locales intactos.
> - **Usa "Accept Incoming Change"** si los cambios remotos son correctos y quieres sobrescribir los locales.
> - **Usa "Accept Both Changes"** si ambos conjuntos de cambios son relevantes y pueden coexistir.
> - **Usa "Compare Changes"** si necesitas analizar cuidadosamente las diferencias antes de tomar una decisión.

Para el caso practico dar clic en **Accept Incoming Change**

CUANDO SE PRESENTA UN CONFLICTO SIEMPRE SE DEBE GENERAR UN NUEVO COMMIT. PARA EL CASO PRACTICO AGREGUE LOS CAMBIOS A EL STAGGING **git add .** y por ultimo cree el nuevo commit.

```
trainer@johlver-virtual-machine:~/projectsDev$ git add .
trainer@johlver-virtual-machine:~/projectsDev$ git commit -m "Agregando descripcion a estaciones con solucion de conflictos"
[detached HEAD 001b0a7] Agregando descripcion a estaciones con solucion de conflictos
 1 file changed, 4 insertions(+), 4 deletions(-)
trainer@johlver-virtual-machine:~/projectsDev$ 
```

```
trainer@johlver-virtual-machine:~/projectsDev$ git push
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 592 bytes | 592.00 KiB/s, done.
Total 4 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 2 local objects.
To https://github.com/trainingLeader/taller-git.git
   36cebe3..182d34b  main -> main
trainer@johlver-virtual-machine:~/projectsDev$
```

> En caso de querer eliminar el ultimo commit puede ejecutar el comando 
>
> git reset --hard HEAD~1



# Git Rebase

Si existe un rebase pendiente se debe abortar. 

```less
git rebase --abort
```



## ¿Qué es git rebase?

El comando `git rebase` en Git se utiliza para **reaplicar commits en una nueva base**, reorganizando la historia de commits de manera más limpia y lineal. Esto lo hace moviendo una rama o conjunto de commits para que se apliquen "encima" de otro punto de la historia.

```
# Rebase 9718733 onto 0b07462 (9 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
#                    commit's log message, unless -C is used, in which case
#                    keep only this commit's message; -c is same as -C but
#                    opens the editor
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
# .       create a merge commit using the original merge commit's
# .       message (or the oneline, if no original merge commit was
# .       specified); use -c <commit> to reword the commit message
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
```




## ¿Qué hace en términos simples?

`git rebase` toma un conjunto de commits de una rama (o una parte de la historia) y los "recoloca" como si se hubieran creado directamente sobre otro punto en el historial de Git.

El comando `git rebase -i --root` se utiliza en Git para reescribir la historia del repositorio desde su raíz (el primer commit) de manera interactiva. Este comando permite modificar, reordenar, combinar o eliminar commits desde el inicio del repositorio.

![](https://i.ibb.co/TcNw6j3/image.png)

## Detalle de la funcionalidad:

1. **`-i` (interactivo):**
   - Abre un editor de texto donde puedes ver y modificar la lista de commits a partir de la raíz.
   - En esta lista puedes:
     - Cambiar el mensaje de un commit.
     - Reordenar commits.
     - Combinar varios commits (squash).
     - Eliminar commits.
2. **`--root`:**
   - Aplica el rebase desde el primer commit del repositorio (la raíz).
   - Esto es útil si necesitas modificar el primer commit, algo que normalmente no se podría hacer sin este flag.

## Casos de uso:

- **Modificar el primer commit:** Si el mensaje o contenido del primer commit es incorrecto, puedes usar `git rebase -i --root` para editarlo.
- **Limpiar la historia:** Puedes combinar varios commits iniciales en uno solo (squash) para simplificar la historia del repositorio.
- **Reescribir toda la historia:** Ideal si necesitas aplicar cambios masivos a la estructura o mensajes de los commits iniciales.



# Cambiar el nombre de un commit

En la imagen se muestra el uso de un **rebase interactivo** iniciado con el comando:

```bash
git rebase -i --root
```

Esto indica que estás intentando reescribir la historia de **todos los commits del repositorio**, comenzando desde el **primer commit (raíz)**.

En el archivo `git-rebase-todo`, puedes observar una lista de commits de tu proyecto. Cada línea comienza con el comando `pick`, que indica que, por defecto, esos commits se aplicarán tal cual están.

Ahora, en el caso del commit `331274d` con el mensaje **"Dejar de rastrear archivos ignorados"**, has cambiado la acción de `pick` a `reword`. Esto indica que quieres **modificar el mensaje** de ese commit.
![](https://i.ibb.co/p3pdTMF/image.png)

### Lo que ocurrirá:

1. Git pausará el rebase en el commit `331274d` y abrirá un editor de texto para que cambies el mensaje del commit.

2. Cuando el editor se abra, deberás escribir el nuevo mensaje deseado. Por ejemplo:

   ```bash
   Actualización: Dejar de rastrear archivos ignorados correctamente
   ```

3. Una vez guardes y cierres el editor, Git aplicará el nuevo mensaje al commit y continuará con el rebase.

![](https://i.ibb.co/Nx7VH21/image.png)

### Flujo general del proceso:

1. **Lista de commits:** El rebase interactivo muestra la lista de commits desde el primero hasta el último. Puedes decidir qué hacer con cada uno (e.g., `pick`, `reword`, `squash`, etc.).
2. **Editar el mensaje:** Cambiar `pick` a `reword` te permite editar solo el mensaje de un commit sin alterar su contenido.
3. **Continuar el rebase:** Una vez editado el mensaje y cerrado el editor, el rebase continuará automáticamente. Si no hay conflictos, finalizará correctamente.

### Resultado:

Después de completar este proceso, el commit `331274d` tendrá el mensaje actualizado y el resto de los commits se mantendrán tal cual, salvo que hayas hecho otros cambios en el archivo `git-rebase-todo`.

### Nota importante:

Si esta rama ya ha sido enviada a un remoto (usaste `git push` anteriormente), necesitarás usar:

```
git push origin -f
```

Esto es necesario porque el hash del commit cambiará debido a la reescritura de la historia.

# Fusiones (merge)

El comando **`git merge`** se utiliza para combinar los cambios de una rama en otra, fusionando el historial de ambas ramas en un solo punto. Es una herramienta esencial para integrar nuevas características, solucionar errores o finalizar el desarrollo de una rama secundaria.

## Tipos de Merge en Git

1. **Fast-Forward Merge**
   Ocurre cuando no hay nuevos commits en la rama de destino desde que la rama secundaria se creó. Git simplemente mueve el puntero de la rama destino al último commit de la rama secundaria.

```
git checkout main
git merge feature/nueva-funcionalidad
```

## Taller de fusiones

1. Ubiquese en la rama principal

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git checkout main
   Switched to branch 'main'
   Your branch is up to date with 'origin/main'.
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

2. Ejecute el comando git merge Nombre-Rama-Fusionar

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git merge css
   Updating 3465c76..853b093
   Fast-forward
    index.html | 11 +++++++++++
    style.css  |  3 +++
    2 files changed, 14 insertions(+)
    create mode 100644 index.html
    create mode 100644 style.css
   ```

3. Haga push de origin a main

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git push origin main
   Enumerating objects: 4, done.
   Counting objects: 100% (4/4), done.
   Delta compression using up to 4 threads
   Compressing objects: 100% (2/2), done.
   Writing objects: 100% (2/2), 287 bytes | 287.00 KiB/s, done.
   Total 2 (delta 1), reused 0 (delta 0), pack-reused 0
   remote: Resolving deltas: 100% (1/1), completed with 1 local object.
   To https://github.com/trainingLeader/taller-git.git
      3465c76..6fcd14f  main -> main
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```


## Merge Manual

### Conflictos en un Merge 

Un **conflicto de fusión** ocurre cuando los mismos archivos han sido modificados en ambas ramas, y Git no puede decidir automáticamente cómo fusionarlos.

### Taller Conflictos

1. Ingresar a la carpeta del proyecto creado en los puntos anteriores **projectsDev**

2. Seleccione la rama principal. Importe la hoja de estilo creada en los puntos anteriores <link rel="stylesheet" href="style.css">

   > Puede usar el atajo : ul>li{Elemento $}*5 para agregar una lista no ordenada y 5 list item
   >
   >     <ul>
   >         <li>Elemento 1</li>
   >         <li>Elemento 2</li>
   >         <li>Elemento 3</li>
   >         <li>Elemento 4</li>
   >         <li>Elemento 5</li>
   >     </ul>

​	Modifique el archivo index.html de la siguiente forma

​	

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Intro Web</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Introduccion a control de versiones/Ramas. Mis primeros pasos desde la rama principal</h1>
    <ul>
        <li>Elemento 1</li>
        <li>Elemento 2</li>
        <li>Elemento 3</li>
        <li>Elemento 4</li>
        <li>Elemento 5</li>
    </ul>
</body>
</html>
```

3. Agregue el cambio y realice commit

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git add  .
   trainer@johlver-virtual-machine:~/projectsDev$ git commit -m "Agregando hoja de estilos al html"
   [main 0799721] Agregando hoja de estilos al html
    1 file changed, 9 insertions(+), 1 deletion(-)
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

4. Seleccione la rama html **git checkout**

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git checkout html
   Switched to branch 'html'
   Your branch is up to date with 'origin/html'.
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

5. En el documento html agregue la importación del archivo app.js, agregue una lista ordenada con 5 li

   ```
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Intro Web</title>
   </head>
   <body>
       <h1>Introduccion a control de versiones/Ramas, Texto escrito desde la rama html web</h1>
       <ol>
           <li>Elemento 1</li>
           <li>Elemento 2</li>
           <li>Elemento 3</li>
           <li>Elemento 4</li>
           <li>Elemento 5</li>
       </ol>
       <script src="app.js"></script>
   </body>
   </html>
   ```

6. Agregue los cambios de la rama y realice commit

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git add .
   trainer@johlver-virtual-machine:~/projectsDev$ git commit -m "Importacion archivo JS"
   [html a4c9706] Importacion archivo JS
    1 file changed, 9 insertions(+), 1 deletion(-)
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

7. Regrese a la rama principal y realice merge a la rama html

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git merge html
   Auto-merging index.html
   CONFLICT (content): Merge conflict in index.html
   Automatic merge failed; fix conflicts and then commit the result.
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

   Cuando se realiza merge notifica conflicto en la rama el cual debe resolverse

   ![](https://i.ibb.co/3NmXJn4/image.png)

> Modifique de forma manual la información que desea conservar.

Cuando finalicemos los cambios ejecutamos el git merge nuevamente

```
trainer@johlver-virtual-machine:~/projectsDev$ git merge html
error: Merging is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.
trainer@johlver-virtual-machine:~/projectsDev$ 
```

PODEMOS NOTAR QUE NOS APARECE UN ERROR DE MERGE YA ES ESTAMOS RESOLVIENDO CONFILCTOS DE FORMA MANUAL. EN ESTE PUNTO SE DEBE AGREGAR LOS NUEVOS CAMBIOS CON **git add .** y hacer commit nuevamente.

```
trainer@johlver-virtual-machine:~/projectsDev$ git add .
trainer@johlver-virtual-machine:~/projectsDev$ git commit -m "Resolviendo los conflictos de forma manual"
[main b8589d7] Resolviendo los conflictos de forma manual
trainer@johlver-virtual-machine:~/projectsDev$ 
```

Ejecute push **git push**

![](https://i.ibb.co/nrYkfC9/image.png)

### Cherry-pick

El comando `git cherry-pick` se utiliza para **aplicar un commit específico de otra rama** en la rama actual. Es una herramienta útil cuando necesitas incorporar un cambio puntual sin fusionar toda la rama de origen. Básicamente, copia un commit identificado por su hash a tu rama activa.

#### ¿Cuándo usar `git cherry-pick`?

- **Incorporar un bugfix**: Si un error se corrigió en una rama y necesitas esa corrección en otra rama sin incorporar otros cambios.
- **Tomar características específicas**: Para traer un commit en particular de una rama de desarrollo a producción.
- **Integrar commits aislados**: Si quieres agregar algunos cambios de otra rama sin afectar el historial general.



#### Sintaxis básica

```bash
git cherry-pick <hash-commit>
```

#### Ejemplo práctico

Supongamos que tienes dos ramas:

- `main`
- `html`

En la rama `html`, hiciste un commit con el hash `abc123`, y ahora necesitas aplicarlo a la rama `main` sin fusionar la rama completa.

1. Cambia a la rama `main`:

   ```bash
   git checkout main
   ```

2. Aplica el commit específico de `html`:

   ```bash
   git cherry-pick abc123
   ```

Ahora, el commit `abc123` se aplica en la rama `main`.

#### Otras opciones útiles

- **Aplicar múltiples commits**:

  ```bash
  git cherry-pick <hash1> <hash2> <hash3>
  ```

- **Aplicar un rango de commits**:

  ```bash
  git cherry-pick <hash-inicial>..<hash-final>
  ```

- **Resolver conflictos manualmente**: Si hay conflictos, `git cherry-pick` te pedirá resolverlos antes de continuar.

  Después de resolverlos:

  ```bash
  git add .
  git cherry-pick --continue
  ```

#### Taller

1. Acceda al proyecto generado en los pasos anteriores

2. Acceda a la rama a la cual quiere traer el commit de otra rama. Para el ejemplo se usara html y main.

   ```less
   trainer@johlver-virtual-machine:~/projectsDev$ git checkout html
   Switched to branch 'html'
   Your branch is ahead of 'origin/html' by 1 commit.
     (use "git push" to publish your local commits)
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

3. Liste los commit que ha realizado en la rama que contiene los commit que desea copiar. Para esto se debe cambiar a la rama main usando el comando especifico de git.

   ```less
   trainer@johlver-virtual-machine:~/projectsDev$ git checkout main
   Switched to branch 'main'
   Your branch is up to date with 'origin/main'.
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

   ```less
   trainer@johlver-virtual-machine:~/projectsDev$ git log --oneline
   882713b (HEAD -> main, origin/main) Se agregaron descripciones a las estaciones
   a31e3a9 Importacion archivo JS
   2b2cf6a Agregando hoja de estilos al html
   6543844 Add file Js
   a30737d feat: :sparkles: Add css file style
   d5cf366 (origin/html) Creacion documento html
   3465c76 Create LICENSE
   c42e973 Agregando titulo
   419c95d Primer commit
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

4. Revisar el contenido del commit que desea copia usando el comando **diff** de git : git diff HasCode del commit a revisar

   ```
   git diff 6543844
   ```

   ![](https://i.ibb.co/d0wfrT6/image.png)

5. Se realiza la selección a la rama que se le copiara la información, para el caso practico será la rama html. Para esto se ejecuta el comando **git cherry-pick  6543844 **, lo cual producira un conflicto que se deberá solucionar como se menciono en el punto 4; una vez se ha solucionado el conflicto se dara continuacion a la ejecución del copia del commit a la rama html usando el comando **git cherry-pick --continue** si desea cambiar el mensaje del commit se podrá realizar.

   ```less
   trainer@johlver-virtual-machine:~/projectsDev$ git cherry-pick  6543844
   [html c310b35] Add file Js
    Date: Sun Nov 24 20:15:00 2024 -0500
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 app.js
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

   En este ejemplo no se genero conflicto ya que git reviso los commit y los fusiono ya que comprometia la integridad de los archivos.

   > En caso de querer realizar cambios adicionales antes de copiar el commit puede usar el comando git cherry-pick  6543844 -n el cual envia el flujo a el stage area y se prepara para realizar el commit.

   ```less
   trainer@johlver-virtual-machine:~/projectsDev$ git cherry-pick  6543844 -n
   trainer@johlver-virtual-machine:~/projectsDev$ git status
   On branch html
   Your branch is ahead of 'origin/html' by 1 commit.
     (use "git push" to publish your local commits)
   
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)
           new file:   app.js
   
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

   ```less
   trainer@johlver-virtual-machine:~/projectsDev$ git commit -m "Haciendo copia del commit"
   [html 75b88e6] Haciendo copia del commit
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 app.js
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

   ![](https://i.ibb.co/DY6qLD7/image.png)

## Fusion entre commits (Squash)

### ¿Que es squash?

En **Git**, el término **squash** se refiere al proceso de combinar múltiples confirmaciones (**commits**) en una sola. Esto es especialmente útil para mantener un historial de commits limpio y legible, reduciendo la cantidad de confirmaciones innecesarias o intermedias en un proyecto.

### ¿Cuándo usar squash?

- **Limpieza del historial de commits:** Por ejemplo, cuando trabajas en una rama de características (feature branch) y realizas muchos commits pequeños para pruebas o ajustes menores.
- **Preparación antes de fusionar:** Cuando se desea combinar todos los commits relacionados con una característica en uno solo antes de integrarlos en la rama principal (ej. `main` o `develop`).

Si estás trabajando en un proyecto e intentando implementar una nueva característica, es posible que hagas varios `commit` para probar cómo funciona. Esto te permite ver cómo se comporta o cómo luce el código.

Al hacer esto, las cosas pueden volverse un poco desordenadas porque ahora tienes varios `commit`, incluso para cosas que no son necesarias.

Por esta razón, es posible que quieras combinar todos esos `commit` en un único `commit`. Este proceso se llama **commit squashing**.

En este artículo, te mostraré cómo funciona el commit squashing en Git, para que puedas combinar varios `commit` desordenados o innecesarios en uno solo sin perder tus cambios.

### Cómo combinar commits en Git con rebase interactivo

En este proceso, tomarás todos los `commit` con el comando `git rebase` utilizando el flag `i` y los unirás con `squash`. Además de combinar `commit`, este comando también te permite eliminar `commit`, reescribir mensajes de `commit` y añadir nuevos archivos.

Tengo estos `commit` que me gustaría combinar en uno solo:

![](https://i.ibb.co/JqVYgdr/image.png)

Nota se tienen dos ramas: `html` y `css`. Quiero combinar todos los commits de la rama `css` en un solo commit.

Puedo ver esos commits porque ejecuté el comando `git log --oneline`. También están ya en GitHub:

![](https://i.ibb.co/VgqQXxL/image.png)

Lo primero que necesitas hacer es indicarle a Git cuántos commits hacia atrás quieres hacer el rebase. Así que, si deseas combinar todos esos commits en la rama `css`, necesitas retroceder todos los commits.

Para hacerlo, ejecuta este comando:

```bash
git rebase -i --root
```

Esto abrirá tu editor preferido para Git. El predeterminado es Vim, pero en mi caso, es VS Code. Así es como se ve el editor:

![](https://i.ibb.co/sWj3n9n/image.png)

Ahora, se necesita reemplazar todos los`pick` con `squash` (o simplemente `s`), excepto el primero.

**Nota:** `pick` o `p` solo utilizarán esos commits, pero `squash` o `s` los usará y los combinará todos juntos.

El primer commit es aquel en el que los combinará sin perder los cambios.

![](https://i.ibb.co/CKdtm8B/image.png)

![](https://i.ibb.co/nr20H0S/image.png)

Después de hacer esto, guarde el archivo y cierre la pestaña. Git abrirá otro editor donde se podra ver el nuevo mensaje de commit que se gerara:

![](https://i.ibb.co/1sN7TQ8/image.png)

![](https://i.ibb.co/xftMc4K/image.png)

En la terminal se puede observar el siguiente resultado:

```less
trainer@johlver-virtual-machine:~/projectsDev$ git rebase -i --root
[detached HEAD 662603a] Primer commit
 Date: Mon Nov 18 18:50:07 2024 -0500
 5 files changed, 36 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 LICENSE
 create mode 100644 README.md
 create mode 100644 index.html
 create mode 100644 style.css
Successfully rebased and updated refs/heads/css.
trainer@johlver-virtual-machine:~/projectsDev$ 
```

Después de ejecutar los comandos, deberías ver un mensaje de éxito en la terminal.

Revisa tu registro de Git nuevamente ejecutando `git log --oneline` y deberías ver que todos los commits se han combinado:

```less
trainer@johlver-virtual-machine:~/projectsDev$ git log --oneline
662603a (HEAD -> css) Primer commit
trainer@johlver-virtual-machine:~/projectsDev$ 
```

Recuerda que el nuevo mensaje de commit es "Primer commit". Si haces un **push** de tu rama a Git, también verás un mensaje de commit:

```less
trainer@johlver-virtual-machine:~/projectsDev$ git push origin -f
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (7/7), 1.26 KiB | 1.26 MiB/s, done.
Total 7 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/trainingLeader/taller-git.git
 + 853b093...662603a css -> css (forced update)
trainer@johlver-virtual-machine:~/projectsDev$ 
```

![](https://i.ibb.co/kSYV9rK/image.png)

# Guía de Ejercicios Físicos

**Guía de Ejercicios Físicos** es un proyecto que tiene como objetivo crear una colección de ejercicios físicos clasificados por tipo. Cada tipo de ejercicio se desarrolla en una rama independiente, donde los usuarios pueden realizar múltiples `commits` documentando diferentes aspectos del ejercicio. Al final, todas las ramas se fusionan en la rama principal para formar una guía completa y coherente.

## Problemática

El desafío principal de este proyecto es la gestión eficaz de ramas y `commits` en Git. Los usuarios deben asegurarse de que cada rama represente adecuadamente un tipo de ejercicio y que los cambios realizados sean significativos y bien documentados. Durante el proceso de fusión de ramas, pueden surgir conflictos que requieren resolución. Esta experiencia no solo fortalece las habilidades en el uso de Git, sino que también ilustra la importancia de una buena documentación al organizar información.

En este ejercicio, practicarás la creación de hasta **10 ramas** en tu proyecto **Guía de Ejercicios Físicos**, cada una dedicada a un tipo diferente de ejercicio. Cada rama deberá contener al menos **`5 commits`** relacionados con el ejercicio correspondiente, y al final se realizará una fusión de todas las ramas en la rama principal (`main`), integrando todos los ejercicios en un solo documento final.

## Instrucciones

1. **Crear la Carpeta y la Estructura del Proyecto**
   - Crea una carpeta llamada `ejercicios/` en la raíz del proyecto donde se guardarán los archivos para cada tipo de ejercicio. La carpeta raíz se llamará `GuiaDeEjercicios`.
2. **Crear Hasta 10 Ramas para los Tipos de Ejercicio**
   - Los tipos de ejercicio pueden incluir: `Cardio`, `Fuerza`, `Flexibilidad`, `Entrenamiento Funcional`, `Yoga`, `Pilates`, `Ciclismo`, `Natación`, `Boxeo`, y `CrossFit`.
   - Pista: Utiliza un comando para crear una nueva rama y cambiarte a ella al mismo tiempo.
3. **Agregar una Entrada para Cada Ejercicio con Múltiples Commits**
   - En cada rama, crea un archivo `Markdown` para el tipo de ejercicio correspondiente.
   - Realiza al menos `5 commits` en la rama, añadiendo cambios incrementales al archivo. Por ejemplo:
     - Primer `commit`: Agregar el título del ejercicio.
     - Segundo `commit`: Descripción del ejercicio.
     - Tercer `commit`: Beneficios del ejercicio.
     - Cuarto `commit`: Instrucciones de cómo realizarlo.
     - Quinto `commit`: Consejos y precauciones.
   - Pista: Realiza los cambios en el archivo y utiliza los comandos para agregar y registrar los cambios en el historial.
   - **Nota**: recuerda que cada `commit` se realizará siguiendo el formato de **`conventional commits.`**
4. **Repetir para Cada Tipo de Ejercicio**
   - Cambia de rama y repite los pasos para cada uno de los 10 tipos de ejercicio, asegurándote de hacer al menos **5 `commits`** incrementales en cada rama.
5. **Fusionar Cada Rama a la Rama Principal (`main`)**
   - Cambia a la rama principal (`main`) y realiza la fusión de cada rama de ejercicio.
   - Pista: Asegúrate de estar en la rama principal antes de realizar la fusión.
   - Si se producen conflictos, resuélvelos manualmente y confirma los cambios.
6. **Subir los Cambios al Repositorio Remoto**
   - Sube la rama principal y las demás ramas al repositorio remoto para consolidar todos los cambios.
   - Asegúrate de que el repositorio esté público y compartido.

# Contenido del `cardio.md` de la Rama `cardio`:

```markdown
# Ejercicio Cardio

## Descripción
Los ejercicios de cardio son actividades que aumentan tu frecuencia cardíaca y mejoran la resistencia.

## Beneficios
- Aumenta la capacidad cardiovascular.
- Ayuda a quemar calorías.
- Mejora el estado de ánimo.

## Instrucciones
1. Comienza con un calentamiento de 5-10 minutos.
2. Realiza la actividad (correr, nadar, andar en bicicleta) durante al menos 30 minutos.
3. Termina con un enfriamiento y estiramientos.

## Consejos
- Mantén una hidratación adecuada.
- Escoge un ritmo que puedas mantener.
```

## Instrucciones Visuales

### Rama `cardio`

```bash
GuiaDeEjercicios/
├── ejercicios/
│   ├── cardio.md  # Commit 1: Crea el archivo y agrega el título.
└── README.md

GuiaDeEjercicios/
├── ejercicios/
│   ├── cardio.md  # Commit 2: Agrega la descripción del ejercicio.
└── README.md

GuiaDeEjercicios/
├── ejercicios/
│   ├── cardio.md  # Commit 3: Añade los beneficios del ejercicio.
└── README.md

GuiaDeEjercicios/
├── ejercicios/
│   ├── cardio.md  # Commit 4: Incluye las instrucciones para realizar el ejercicio.
└── README.md

GuiaDeEjercicios/
├── ejercicios/
│   ├── cardio.md  # Commit 5: Agrega consejos y precauciones.
└── README.md
```

### Rama `fuerza`

```bash
GuiaDeEjercicios/
├── ejercicios/
│   ├── fuerza.md  # Commit 1: Crea el archivo y agrega el título.
└── README.md
```

(El proceso de `commits` incrementales se repite para los otros tipos de ejercicio.)

### Rama `main`

Después de fusionar todas las ramas (`cardio`, `fuerza`, `flexibilidad`, etc.) en la rama `main`, la estructura del proyecto se verá así:

```bash
GuiaDeEjercicios/
├── ejercicios/
│   ├── cardio.md        # Contenido final fusionado desde la rama `cardio`.
│   ├── fuerza.md        # Contenido final fusionado desde la rama `fuerza`.
│   ├── flexibilidad.md   # Contenido final fusionado desde la rama `flexibilidad`.
│   ├── entrenamiento_funcional.md
│   ├── yoga.md
│   ├── pilates.md
│   ├── ciclismo.md
│   ├── natacion.md
│   ├── boxeo.md
│   └── crossfit.md
└── README.md
```

Cada archivo en la carpeta `ejercicios/` contendrá la versión final de cada tipo de ejercicio, resultado de los `commits` en las ramas correspondientes. La fusión en `main` integrará todos los cambios, consolidando el proyecto.

# Contenido del `README.md` de la Rama `main`

El `README.md` en la rama `main` podría tener un contenido que vincule a los archivos de cada ejercicio, con un enfoque especial en los ejercicios de cardio. Aquí tienes un ejemplo de cómo podría ser el contenido:

```markdown
# Guía de Ejercicios Físicos

Bienvenido a nuestra guía de ejercicios físicos, donde compartimos descripciones y beneficios de diferentes tipos de ejercicios.

## Tipos de Ejercicio

- [Ejercicio Cardio](ejercicios/cardio.md): Mejora tu resistencia y salud cardiovascular.
- [Ejercicio de Fuerza](ejercicios/fuerza.md): Aumenta la masa muscular y la fuerza.
- [Ejercicio de Flexibilidad](ejercicios/flexibilidad.md): Mejora la movilidad y reduce el riesgo de lesiones.
- [Ejercicio de Entrenamiento Funcional](ejercicios/entrenamiento_funcional.md): Mejora la fuerza en movimientos cotidianos.
- [Ejercicio de Yoga](ejercicios/yoga.md): Fomenta la relajación y la flexibilidad.
- [Ejercicio de Pilates](ejercicios/pilates.md): Fortalece el núcleo y mejora la postura.
- [Ejercicio de Ciclismo](ejercicios/ciclismo.md): Gran ejercicio cardiovascular de bajo impacto.
- [Ejercicio de Natación](ejercicios/natacion.md): Trabaja todos los grupos musculares de manera suave.
- [Ejercicio de Boxeo](ejercicios/boxeo.md): Mejora la coordinación y la resistencia.
- [Ejercicio de CrossFit](ejercicios/crossfit.md): Entrenamiento intensivo y funcional.

¡Esperamos que encuentres útiles estos ejercicios y te inspires para mantenerte activo y saludable!
```



## Etiquetas

Las **etiquetas en Git** (tags) son referencias que apuntan a puntos específicos en el historial de commits. Se usan comúnmente para marcar versiones importantes del proyecto, como lanzamientos de software (`v1.0`, `v2.0`, etc.).

### Tipos de Etiquetas

**Etiquetas ligeras (Lightweight Tags):**

- Son básicamente un puntero a un commit.
- No contienen metadatos adicionales (como nombre o fecha del creador).
- Útiles para usos temporales o referencias rápidas.

```
git tag <nombre-del-tag>
```

**Etiquetas anotadas (Annotated Tags):**

- Contienen información adicional, como un mensaje, el nombre del autor, y la fecha.
- Se almacenan como objetos en la base de datos de Git.
- Útiles para versiones oficiales o referencias permanentes.

```
git tag -a <nombre-del-tag> -m "Mensaje del tag"
```

> Nomeclatura de versionado : https://semver.org/lang/es/

### Taller Creación de etiquetas

1. Ingrese al proyecto creado en los pasos anteriores

2. Verifique el listado de etiquetas creadas con el comando **git tag**

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git tag
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

3. Modifique el achivo README para generar cambios en el proyecto.

4. Agregue los cambios al staging **git add .**

5. Cree la nueva etiqueta con el comando **git tag v1.0.0**

6. Realice el commit apuntando a la etiqueta con el comando **git commit -m "v1.0.0"**

   Resumen

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git tag
   trainer@johlver-virtual-machine:~/projectsDev$ git add .
   trainer@johlver-virtual-machine:~/projectsDev$ git tag v1.0.0
   trainer@johlver-virtual-machine:~/projectsDev$ git commit -m "v1.0.0"
   [main 8da20a6] v1.0.0
    1 file changed, 2 insertions(+), 1 deletion(-)
   ```

7. Haga push hacia el repositorio remoto con el comando **git push origin numero-version**

   ```
   trainer@johlver-virtual-machine:~/projectsDev$ git push origin v1.0.0
   Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
   To https://github.com/trainingLeader/taller-git.git
    * [new tag]         v1.0.0 -> v1.0.0
   trainer@johlver-virtual-machine:~/projectsDev$ 
   ```

   ![](https://i.ibb.co/h13vkKf/image.png)

# Github Pages

GitHub Pages es un servicio gratuito que te permite alojar sitios web estáticos directamente desde un repositorio de GitHub. Es ideal para proyectos personales, blogs o sitios de documentación.

**Acceder a la Url**

- *URL* del sitio: **https://usuario.github.io/repositorio**

### **Características principales:**

- **Alojamiento de sitios estáticos:** Sirve archivos HTML, CSS y JavaScript directamente desde tu repositorio.
- **Integración con Jekyll:** Compatible con Jekyll, un generador de sitios estáticos que permite contenido dinámico.
- **Dominios personalizados:** Permite el uso de dominios personalizados para tu sitio.
- **Soporte HTTPS:** Proporciona cifrado HTTPS para conexiones seguras

### Comandos útiles

```
git branch gh-pages
git checkout gh-pages

git remote add origin https://github.com/usuario/repositorio.git
git push origin gh-pages

# para descargar los cambios del repositorio remoto al local
git pull origin gh-pages
```

### Taller

1. Ingrese al proyecto y asegurese que exista el archivo index.html

2. Cree la rama gh-pages. **git branch gh-pages** e ingrese a la rama **git checkout gh-pages** o utilice el comando **git checkout -b gh-pages**

3. ```
   trainer@johlver-virtual-machine:~/projectsDev$ git checkout -b gh-pages
   Switched to a new branch 'gh-pages'
   trainer@johlver-virtual-machine:~/projectsDev$ git push origin gh-pages
   ```

# GitFlow 

Gitflow es un modelo alternativo de creación de ramas en Git en el que se utilizan ramas de función y varias ramas principales. Fue [Vincent Driessen en nvie](http://nvie.com/posts/a-successful-git-branching-model/) quien lo publicó por primera vez y quien lo popularizó. En comparación con el desarrollo basado en troncos, Gitflow tiene diversas ramas de más duración y mayores confirmaciones. Según este modelo, los desarrolladores crean una rama de función y retrasan su fusión con la rama principal del tronco hasta que la función está completa. Estas ramas de función de larga duración requieren más colaboración para la fusión y tienen mayor riesgo de desviarse de la rama troncal. También pueden introducir actualizaciones conflictivas(https://www.atlassian.com/es/git/tutorials/comparing-workflows/gitflow-workflow).

https://danielkummer.github.io/git-flow-cheatsheet/index.es_ES.html

## Ramas en Git Flow

![](https://i.ibb.co/MDnBCDj/image.png)

En cuanto a la política de ramas, Git Flow propone:

- *main* como rama principal del proyecto. Contiene el código de producción. NUNCA trabajaremos sobre ella. De esta rama no nace ninguna excepto los **hotfix**.
- *Develop* como rama de desarrollo. NUNCA trabajaremos sobre ella. De esta rama nacen todas las ramas de **feature**. La rama develop se mergeará con master cuando vayamos a desplegar el proyecto a través de las **releases**.
- *Feature* serán las ramas sobre las que trabajaremos normalmente. Llevan por defecto el prefijo *feature/* seguido del nombre de la rama (ej: *feature/add-event-cpt*). Nacen SIEMPRE desde la rama develop y mueren cuando son mergeadas.
- *Hotfix* son las ramas que utilizaremos para corregir errores críticos encontrados en producción. Llevan el prefijo *hotfix/* seguido del nombre de la rama (ej: *hotfix/fix-form-submit*). Nacen SIEMPRE desde la rama **main** y se mergean contra **main** y **develop**, con el objetivo de poner el hotfix en producción y que también esté disponible para nuevos evolutivos en la rama de desarrollo.
- *Release* son las ramas que utilizaremos para crear nuevas versiones para desplegar a producción. Llevan el prefijo *release/* seguido del número de versión. Es el mecanismo a través del cual mergeamos los nuevos desarrollos que tenemos en **develop** contra **main**. Es recomendable utilizar [SemVer](https://semver.org/lang/es/) para los números de versión.
- *Bugfix* son ramas que se utilizan para corregir errores que aún no han llegado a producción. Llevan el prefijo *bugfix/* seguido del nombre de la rama (ej: *bugfix/fix-wrong-logout-link*). Nacen SIEMPRE desde la rama **develop**.



Instalar git flow **sudo apt-get install git-flow**  

## Taller

1. Cree un proyecto llamado invapp

   ```less
   trainer@johlver-virtual-machine:~$ mkdir invapp
   trainer@johlver-virtual-machine:~$ 
   ```

2. Cree los siguientes archivos

   ![](https://i.ibb.co/YhHMcs0/image.png)

3. A cada archivo creado agregue el siguiente codigo

   ```css
   body {
       font-family: Arial, sans-serif;
       text-align: center;
       margin-top: 50px;
   }
   
   h1 {
       color: #333;
   }
   
   h2 {
       color: #333;
   }
   
   h3 {
       color: #333;
   }
   
   
   button {
       padding: 10px 20px;
       font-size: 16px;
       cursor: pointer;
   }
   
   #output {
       margin-top: 20px;
       font-size: 18px;
       color: #555;
   }
   
   form {
       margin-top: 20px;
       display: inline-block;
       text-align: left;
   }
   
   label {
       display: block;
       margin-top: 10px;
   }
   
   input[type="text"], input[type="email"] {
       width: 100%;
       padding: 5px;
       margin-top: 5px;
   }
   
   input[type="submit"] {
       margin-top: 10px;
       padding: 10px 20px;
       cursor: pointer;
   }
   
   #formOutput {
       margin-top: 20px;
       font-size: 18px;
       color: #555;
   }
   ```

   ```html
   <!DOCTYPE html>
   <html lang="es">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Mi App Web Básica</title>
       <link rel="stylesheet" href="styles.css">
   </head>
   <body>
       <h1>Hola Camper</h1>
       <h1>Welcome to CampusLands</h1>
   </body>
   </html>
   ```

   ```javascript
   document.getElementById('btnClick').addEventListener('click', function() {
       document.getElementById('output').textContent = '¡Botón clicado!';
   });
   
   ```

4. Inicialice git con **git init**

5. Agregue los cambios de los archivos al staging **git add .**

6. Cree un commit basico **git commit -m "Start Project"**

7. Cree un repositorio remoto  git remote add origin [Repositorio remoto]

8. ejecute el comando **git push -u origin main**

9. Inicialice git flow con el comando **git flow init**

   ![](https://i.ibb.co/ZJchfSV/image.png)

10. Por defecto se crean las siguientes rama

    ```less
    trainer@johlver-virtual-machine:~/invapp$ git branch
    * develop
      main
    trainer@johlver-virtual-machine:~/invapp$ 
    ```

11. Agregue nuevas funcionalidades a los archivos index.html, app.js

    ```javascript
    document.getElementById('contactForm').addEventListener('submit', function(event) {
        event.preventDefault();
        var name = document.getElementById('name').value;
        var email = document.getElementById('email').value;
        document.getElementById('formOutput').textContent = 'Nombre: ' + name + ', Email: ' + email;
    });
    ```

    ```html
        <h1>Aprende DevOps</h1>
        <button id="btnClick">Haz clic aquí</button>
        <p id="output"></p>
        <form id="contactForm">
            <label for="name">Nombre:</label>
            <input type="text" id="name" name="name">
            <br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email">
            <br>
            <input type="submit" value="Enviar">
        </form>
        <p id="formOutput"></p>
        <script src="script.js"></script>
    ```

12. Cree un nuevo feature(Rama) con el comando **git flow feature start NombreFeature**

    ```less
    trainer@johlver-virtual-machine:~/invapp$ git flow feature start contact-form
    M       app.js
    M       index.html
    Switched to a new branch 'feature/contact-form'
    
    Summary of actions:
    - A new branch 'feature/contact-form' was created, based on 'develop'
    - You are now on branch 'feature/contact-form'
    
    Now, start committing on your feature. When done, use:
    
         git flow feature finish contact-form
    
    trainer@johlver-virtual-machine:~/invapp$
    ```

    ```less
    trainer@johlver-virtual-machine:~/invapp$ git branch
      develop
    * feature/contact-form
      main
    trainer@johlver-virtual-machine:~/invapp$ 
    ```

    

13. Realice un cambio en cualquiera de los archivos para integrarlos a develop

14. Agregue los cambio realizado al staging y realice un commit

    ```less
    trainer@johlver-virtual-machine:~/invapp$ git add .
    trainer@johlver-virtual-machine:~/invapp$ git commit -m "Add new features to JS and Html"
    [feature/contact-form af917ae] Add new features to JS and Html
     2 files changed, 22 insertions(+), 1 deletion(-)
    trainer@johlver-virtual-machine:~/invapp$ 
    ```

15. Integre los cambios de la rama **feature/contact-form** a la rama **develop** para esto ejecute el comando **git flow feature finish NombreRama**

    ```less
    trainer@johlver-virtual-machine:~/invapp$ git flow feature finish contact-form
    Switched to branch 'develop'
    Updating 4389745..af917ae
    Fast-forward
     app.js     |  7 +++++++
     index.html | 16 +++++++++++++++-
     2 files changed, 22 insertions(+), 1 deletion(-)
    Deleted branch feature/contact-form (was af917ae).
    
    Summary of actions:
    - The feature branch 'feature/contact-form' was merged into 'develop'
    - Feature branch 'feature/contact-form' has been locally deleted
    - You are now on branch 'develop'
    ```

16. Realice push a develop

    ```less
    trainer@johlver-virtual-machine:~/invapp$ git push origin develop
    Enumerating objects: 7, done.
    Counting objects: 100% (7/7), done.
    Delta compression using up to 4 threads
    Compressing objects: 100% (4/4), done.
    Writing objects: 100% (4/4), 1022 bytes | 1022.00 KiB/s, done.
    Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
    remote: 
    remote: Create a pull request for 'develop' on GitHub by visiting:
    remote:      https://github.com/trainingLeader/gitflow-app/pull/new/develop
    remote: 
    To https://github.com/trainingLeader/gitflow-app.git
     * [new branch]      develop -> develop
    trainer@johlver-virtual-machine:~/invapp$ 
    ```

17. Cree un release con el comando **git flow release start Version**

    ```less
    trainer@johlver-virtual-machine:~/invapp$ git flow release start v1.0.0
    Switched to a new branch 'release/v1.0.0'
    
    Summary of actions:
    - A new branch 'release/v1.0.0' was created, based on 'develop'
    - You are now on branch 'release/v1.0.0'
    
    Follow-up actions:
    - Bump the version number now!
    - Start committing last-minute fixes in preparing your release
    - When done, run:
    
         git flow release finish 'v1.0.0'
    
    trainer@johlver-virtual-machine:~/invapp$ 
    ```

    Realice cualquier cambio en los archivos

18. Agregue los cambios al staging y realice un commit

    ```less
    trainer@johlver-virtual-machine:~/invapp$ git add .
    trainer@johlver-virtual-machine:~/invapp$ git commit -m "New features"
    [release/v1.0.0 34ef008] New features
     2 files changed, 2 insertions(+), 1 deletion(-)
    trainer@johlver-virtual-machine:~/invapp$ 
    ```

19. Realice la integración de la version release a develop y main con el comando **git flow release finish Version** Cuando se ejecuta el comando se abre una ventana del editor para agregar un mensaje al proceso.

    ![](https://i.ibb.co/C6rJtJv/image.png)

Cierre la ventana o agregue un mensaje y cierre la ventana. Cuando se cierra la ventana se abre otra ventana en la cual agregaremos un mensaje para el tag.

![](https://i.ibb.co/TWQVbmG/image.png)

Resumen del proceso:

```less
trainer@johlver-virtual-machine:~/invapp$ git flow release finish v1.0.0
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
Merge made by the 'ort' strategy.
 app.js     |  7 +++++++
 index.html | 17 ++++++++++++++++-
 2 files changed, 23 insertions(+), 1 deletion(-)
Already on 'main'
Your branch is ahead of 'origin/main' by 3 commits.
  (use "git push" to publish your local commits)
Switched to branch 'develop'
Merge made by the 'ort' strategy.
 app.js     | 2 +-
 index.html | 1 +
 2 files changed, 2 insertions(+), 1 deletion(-)
Deleted branch release/v1.0.0 (was 34ef008).

Summary of actions:
- Release branch 'release/v1.0.0' has been merged into 'main'
- The release was tagged 'v1.0.0'
- Release tag 'v1.0.0' has been back-merged into 'develop'
- Release branch 'release/v1.0.0' has been locally deleted
- You are now on branch 'develop'

trainer@johlver-virtual-machine:~/invapp$ 
```

20. Realice push a develop y main

    ```less
    trainer@johlver-virtual-machine:~/invapp$ git push origin develop
    Enumerating objects: 12, done.
    Counting objects: 100% (12/12), done.
    Delta compression using up to 4 threads
    Compressing objects: 100% (6/6), done.
    Writing objects: 100% (6/6), 716 bytes | 716.00 KiB/s, done.
    Total 6 (delta 4), reused 0 (delta 0), pack-reused 0
    remote: Resolving deltas: 100% (4/4), completed with 2 local objects.
    To https://github.com/trainingLeader/gitflow-app.git
       af917ae..555d812  develop -> develop
       
    trainer@johlver-virtual-machine:~/invapp$ git push origin main --tags
    Enumerating objects: 1, done.
    Counting objects: 100% (1/1), done.
    Writing objects: 100% (1/1), 183 bytes | 183.00 KiB/s, done.
    Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
    To https://github.com/trainingLeader/gitflow-app.git
       4389745..973adda  main -> main
     * [new tag]         v1.0.0 -> v1.0.0
    trainer@johlver-virtual-machine:~/invapp$ 
    ```

21. Creacion de la rama hotfix. Se debe ubicar en la rama main y ejecute el comando **git flow hotfix start Version**

    ```less
    trainer@johlver-virtual-machine:~/invapp$ git flow hotfix start V1.0.1
    Switched to a new branch 'hotfix/V1.0.1'
    
    Summary of actions:
    - A new branch 'hotfix/V1.0.1' was created, based on 'main'
    - You are now on branch 'hotfix/V1.0.1'
    
    Follow-up actions:
    - Start committing your hot fixes
    - Bump the version number now!
    - When done, run:
    
         git flow hotfix finish 'V1.0.1'
    
    trainer@johlver-virtual-machine:~/invapp$ 
    ```

22. Realice cambios en el proyecto. Y agregue los cambios al staging y haga un commit

    ```less
    trainer@johlver-virtual-machine:~/invapp$ git add .
    trainer@johlver-virtual-machine:~/invapp$ git commit -m "Fix critical bugs"
    [hotfix/V1.0.1 099d837] Fix critical bugs
     2 files changed, 5 insertions(+)
    trainer@johlver-virtual-machine:~/invapp$ 
    ```

23. Ejecute el comando git flow hotfix finish Version

    ![](https://i.ibb.co/LhBMYyq/image.png)

    ```less
    trainer@johlver-virtual-machine:~/invapp$ git flow hotfix finish V1.0.1
    Switched to branch 'main'
    Your branch is up to date with 'origin/main'.
    Merge made by the 'ort' strategy.
     index.html | 1 +
     style.css  | 4 ++++
     2 files changed, 5 insertions(+)
    Switched to branch 'develop'
    Merge made by the 'ort' strategy.
     index.html | 1 +
     style.css  | 4 ++++
     2 files changed, 5 insertions(+)
    Deleted branch hotfix/V1.0.1 (was 099d837).
    
    Summary of actions:
    - Hotfix branch 'hotfix/V1.0.1' has been merged into 'main'
    - The hotfix was tagged 'V1.0.1'
    - Hotfix tag 'V1.0.1' has been back-merged into 'develop'
    - Hotfix branch 'hotfix/V1.0.1' has been locally deleted
    - You are now on branch 'develop'
    
    trainer@johlver-virtual-machine:~/invapp$ 
    ```

    24. Realice push a develop y a main

        ```less
        trainer@johlver-virtual-machine:~/invapp$ git push origin develop
        Enumerating objects: 9, done.
        Counting objects: 100% (9/9), done.
        Delta compression using up to 4 threads
        Compressing objects: 100% (6/6), done.
        Writing objects: 100% (6/6), 674 bytes | 674.00 KiB/s, done.
        Total 6 (delta 4), reused 0 (delta 0), pack-reused 0
        remote: Resolving deltas: 100% (4/4), completed with 2 local objects.
        To https://github.com/trainingLeader/gitflow-app.git
           555d812..953c5ec  develop -> develop
        trainer@johlver-virtual-machine:~/invapp$ git push origin main --tags
        Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
        To https://github.com/trainingLeader/gitflow-app.git
           973adda..f38c2ac  main -> main
        trainer@johlver-virtual-machine:~/invapp$ 
        ```

        ![](https://i.ibb.co/ZLVnyDW/image.png)