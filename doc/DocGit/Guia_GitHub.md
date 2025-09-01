# Guía para Configuración de Git y GitHub

Este documento describe los pasos esenciales para configurar credenciales en Git, crear repositorios, realizar commits y subir
cambios a GitHub.

------------------------------------------------------------------------

## 1. Instalación de Git

Antes de comenzar, asegúrate de tener instalado Git.

Descarga el instalador desde: <https://git-scm.com/downloads/win>

Para verificar la instalación:

``` bash
git --version
```

Recuerda tambien tener instalado Visual Studio Code, Python e instalar la extensión Python de Microsoft en Visual Studio Code para poder ejecutar los programas correctamente.

------------------------------------------------------------------------

## 2. Configuración de Credenciales

1.  Abrir la terminal de Visual Studio Code.
2.  Verificar si ya existen credenciales configuradas:

``` bash
git config --global -e
```

3.  Configurar nombre de usuario de GitHub:

``` bash
git config --global user.name "TuNombreDeGitHub"
```

4.  Configurar correo electrónico asociado a tu cuenta de GitHub:

``` bash
git config --global user.email "tu_correo@github.com"
```

5. Verificar que las credenciales fueron configuradas con:

``` bash
git config --global -e
```

------------------------------------------------------------------------

## 3. Creación de un Repositorio Local y Envío a GitHub

### Paso 1. Crear una carpeta y abrirla en Visual Studio Code

### Paso 2. Inicializar Git en la carpeta

``` bash
git init
```

### Paso 3. Crear un archivo inicial (ejemplo: README.md) o mediante la interfaz de Visual

``` bash
echo "# Mi Proyecto" >> README.md
```

### Paso 4. Subir archivo(s) al stage

``` bash
git add .
```

### Paso 5. Realizar un commit

``` bash
git commit -m "first commit"
```

### Paso 6. Definir rama principal

``` bash
git branch -M main
```

### Paso 7. Crear repositorio remoto en GitHub

Ir a www.github.com → **New Repository** → *Public* (sin README para ver los comandos).

### Paso 8. Enlazar el repositorio local con el remoto

``` bash
git remote add origin https://github.com/usuario/repositorio.git
```

### Paso 9. Verifica que el repositorio remoto quedo vinculado

``` bash
git remote -v
```

Deberas ver una salida como:

```bash
PS C:\Users\user_name\example> git remote -v
origin  https://github.com/user_GitHub/name_repository.git (fetch)
origin  https://github.com/user_GitHub/name_repository.git (push)
```

### Paso 10. Subir los cambios al remoto

``` bash
git push -u origin main
```

------------------------------------------------------------------------

## 4. Nuevos Cambios y Commits

Cada vez que hagas un cambio:

``` bash
git add .
git commit -m "mensaje del commit"
git push
```

------------------------------------------------------------------------

## 5. Clonar un Repositorio

Si deseas trabajar con un repositorio existente en GitHub:

1.  Crear una carpeta vacía en tu equipo.
2.  Copiar la URL del repositorio en GitHub (HTTPS o SSH).
3.  Ejecutar en terminal:

``` bash
git clone URL_DEL_REPOSITORIO
```

------------------------------------------------------------------------

## 6. Solución de Problemas

Si tu archivo de configuración está dañado, edítalo con:

Para Linux

``` bash
nano ~/.gitconfig
```

Para Windows

```bash
code $HOME\.gitconfig
```

o con Visual Studio Code:

``` bash
git config --global -e
```

Si tienes un repositorio remoto diferente lo puedes eliminar usando:

```bash
git remote remove origin
```

------------------------------------------------------------------------

## 7. Flujo rápido con Visual Studio Code

1. Ir a www.github.com → **New Repository** → *Public* (sin README para ver los comandos).

2. Abrir una nueva ventana de Visual Studio Code.

3. Crear una carpeta nueva y vacía.

4. Configurar credenciales si es necesario.

   - Configurar el editor de Git en VSCode:

   ``` bash
   git config --global core.editor "code --wait"
   ```

   - Abre el archivo config desde el editor de VSCode:

   ```bash
       git config --global -e
   ```

   - Configuración recomendada adicional en `~/.gitconfig`:

   ``` ini
   [init]
       defaultBranch = main
   [core]
       editor = code --wait
       autocrlf = input
   [user]
       name = nombre_GitHub
       email = correo_GitHub
   ```

   - Cierra el archivo para guardar los cambios.
   - Verifica que las credenciales fueron configuradas correctamente

   ```bash
   git config --global -e
   ```

5. Inicializar Git:

``` bash
git init
git remote add origin URL_DEL_REPOSITORIO
```

6. Crear los archivos necesarios para el proyecto.

7. Usar el menú de **Control de versiones** en el sidebar izquierdo de VSCode para subir los cambios al remoto:

   -   Escribir mensaje del commit.

   -   Hacer clic en **Commit**.

   -   Confirmar **Si** para agregar cambios al *stage*.

   -   Publicar rama **Publish branch** en el primer commit o **Sync changes** para los siguientes commits.

Nota: Recuerda eliminar tus credenciales al finalizar tu trabajo.

------------------------------------------------------------------------

✅ Con estos pasos ya puedes trabajar de forma fluida con Git y GitHub para crear repositorios locales y remotos y conservar tu información y las respectivas actualizaciones.
