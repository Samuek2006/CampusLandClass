[TOC]



# git-flow

# Instalacion

Antes de comezar es Necesitarás wget y util-linux para instalar git-flow. con el siguiente comando

## macOS 

### Homebrew

```bash
brew install git-flow-avh
```

### Macports

```bash
port install git-flow-avh
```

## Linux

```bash
apt-get install git-flow
```

## Windows (Cygwin)

```bash
wget -q -O - --no-check-certificate https://raw.github.com/petervanderdoes/gitflow-avh/develop/contrib/gitflow-installer.sh install stable | bash

```



# Inicialización

Comience a usar git-flow inicializándolo desde dentro de un repositorio git existente:

```bash
git flow init
```

![](https://i.ibb.co/r6Jfvdv/image.png)

Deberá contestar algunas preguntas relacionadas con las convenciones de nombres para las ramas.
Se recomienda utilizar los valores predeterminados. dando enter en todas las opciones

![](https://i.ibb.co/b5Q3WT5/image.png)

**Nota:** Se recomienda sincronizar el repositorio con la rama `master` en este punto para minimizar los conflictos de ramas en el futuro y evitar la necesidad de resolver conflictos en la medida de lo posible.

# Características

- Desarrollar características para futuras versiones
- Es típico que sólo se use en los repositorios para desarrollo

## Comenzar una nueva característica

El desarrollo de nuevas características parte de la rama `develop`. Comienze una nueva característica usando

```bash
git flow feature start DOCUMENTACION
```

![](https://i.ibb.co/ssc2bk5/image.png)

Esta acción crea una nueva rama derivada de **`develop`** y cambia a esta, estableciéndola como rama de trabajo actual.

**Nota:** Ten en cuenta que `feature/DOCUMENTACION` es una rama dedicada a la característica que deseas desarrollar en el proyecto. Para mantener un mejor orden, se recomienda que cada commit siga el estándar de `Conventional Commits`, ya que al finalizar la característica y realizar el `merge`, esto facilitará la identificación del trabajo realizado.

- En este ejemplo, realizaremos dos commits: uno para el título y otro para la descripción, utilizando la convención de `commits convencional.`

![](https://i.ibb.co/5s6JPH5/image.png)

![](https://i.ibb.co/pd3BW8F/image.png)



## Publicar una característica

Publica una característica a un servidor remoto para que así pueda ser vista por otros.

```bash
git flow feature publish DOCUMENTACION
```

![](https://i.ibb.co/ZSKbDQh/image.png)



## Obteniendo características publicadas

Obtén una característica publicada por otro.

```bash
git flow feature pull origin WEB
```

![](https://i.ibb.co/gzsqL0F/image.png)

Puedes mantener un seguimiento de sus cambios usando.

```bash
git flow feature track WEB
```



## Finalizar una característica

Finaliza el desarrollo de una característica. Esta acción realiza lo siguiente:

- Fusiona DOCUMENTACION en `develop`
- Borra la rama DOCUMENTACION
- Cambia a la rama `develop`, estableciéndola como rama de trabajo actual

**Nota:** Este comando debe ejecutarse una vez que se haya finalizado la característica, ya que eliminará la rama `feature/DOCUMENTACION` y realizará un merge en la rama `develop`. Además, la característica no podrá publicarse en el servidor, ya que ha sido eliminada. Los desarrolladores que necesiten acceder a esta funcionalidad deberán tener una copia local de la misma.

```bash
git flow feature finish DOCUMENTACION
```

![](https://i.ibb.co/qMDnbmq/image.png)



# Publicar una versión

- Prepara una versión para producción

- Permite arreglos menores y la preparación de los metadatos para la publicación

  

## Comenzar una publicación

Para comenzar una publicación, usa el comando git flow release. Creará una rama de publicación derivada de la rama `develop.`

```bash
git flow release start v1.0.0
```

Opcionalmente, puede usar `[BASE]` indicando el código sha-1 del cambio desde el cual comenzar la versión de publicación. El cambio debe ser parte de la rama `develop`.

![](https://i.ibb.co/8B2Dd4b/image.png)

Es apropiado publicar remotamente la rama de publicación después de crearla para permitir que otros desarrolladores envíen cambios para esta versión. Hazlo de forma similar a publicar características:

```bash
git flow release publish v1.0.0
```

![](https://i.ibb.co/8z2d62w/image.png)

(Puede establecer el seguimiento de los cambios de la publicación remota utilizando el siguiente comando)

```bash
git flow release track v1.0.0
```

## Concluir una publicación

Dar cierre a una publicación es un gran paso. Realiza varias acciones:

- Fusiona la rama de la publicación con la rama `master`
- Etiqueta el cambio con su nombre
- Vuelve a fusionar la publicación con la rama `develop`
- Borra la rama de la publicación

```bash
git flow release finish v1.0.0
```

![](https://i.ibb.co/SBkPY2P/image.png)

![](https://i.ibb.co/93kRYXh/image.png)

No olvides añadir las tags con 

```bash
git push --tags
```

# Revisiones

Las revisiones surgen de la necesidad de actuar inmediatamente cuando la versión ejecutándose en producción se encuentra en un estado que no deseamos

Puede ramificarse desde la versión correspondiente etiquetada en la rama `master` que corresponda a la versión en producción.

## git flow hotfix start

Como otros comandos de git flow, una revisión se abre con

```bash
git flow hotfix start VERSION v1.1.0
```

![](https://i.ibb.co/8MnwQcR/image.png)

El argumento de la versión determina el nombre de la revisión. Opcionalmente, puede agregar un nombre para la base desde la cual comenzar.

![](https://i.ibb.co/JQZgkmY/image.png)

## Cierra una revisión

Al cerrar una revisión, esta se fusiona en las ramas `develop` y `master`. Luego, el cambio en 'master' es etiquetado con el nombre de la revisión.

```bash
git flow hotfix finish v1.1.0
```

![](https://i.ibb.co/dJk2tBL/image.png)

 

<iframe width="560" height="315" src="https://www.youtube.com/embed/ppiARvOnP6M?si=oE_4xmGFlVyiPEq0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

![image-20250503132431790](C:\Users\developer\AppData\Roaming\Typora\typora-user-images\image-20250503132431790.png)