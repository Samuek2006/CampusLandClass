# Grid, Responsive

## ¿Qué es la propiedad Grid?

Uno de los procesos más desafiantes y frustrantes en CSS, especialmente para aquellos que son nuevos en ello, es la colocación y distribución de elementos en una página. Mecanismos como el posicionamiento, los floats o la diferenciación entre elementos en bloque o en línea a menudo resultan insuficientes o demasiado complejos para crear diseños o estructuras de páginas web modernas.

A pesar de las mejoras que ofrece el sistema de elementos flexibles Flex, está diseñado para estructuras de una sola dimensión y puede resultar complicado crear estructuras web más complejas. Por lo tanto, todavía se necesita una solución más potente para crear rápidamente estructuras web multidimensionales. Con el tiempo, surgieron muchos frameworks CSS y bibliotecas que adoptaron un enfoque basado en una cuadrícula. Estos frameworks permitían definir una cuadrícula y ajustar su tamaño, posición o disposición al cambiar las clases asociadas.

﻿👀﻿Para comprender mejor Grid CSS, es recomendable familiarizarse previamente con el sistema de maquetación basado en Flex, ya que Grid incorpora muchos de los principios y conceptos utilizados en Flex.﻿👀﻿

## ¿Qué es la propiedad Grid? - Conceptos

Para crear diseños basados en Grid CSS necesitaremos tener en cuenta una serie de conceptos que utilizaremos a partir de ahora y que definiremos a continuación:

**Elementos generales a tener en cuenta cuando se implementa Grid. Tomado de:** [**Fuente**](https://lenguajecss.com/css/maquetacion-y-colocacion/grid-css/)

![img](https://khc-sistema-v2.s3.amazonaws.com/editor/1718891487127a8b310b4f54fb8/attachment-1.png.png)



- **Contenedor**: El elemento padre contenedor que definirá la cuadrícula o rejilla.
- **Ítem**: Cada uno de los hijos que contiene la cuadrícula (*elemento contenedor*).
- **Celda (grid cell):** Cada uno de los cuadritos (*unidad mínima*) de la cuadrícula.
- **Area (grid area):** Región o conjunto de celdas de la cuadrícula.
- **Banda (grid track)**: Banda horizontal o vertical de celdas de la cuadrícula.
- **Línea (grid line):** Separador horizontal o vertical de las celdas de la cuadrícula.



### **Modalidades de grid**

Para utilizar cuadriculas Grid CSS, trabajaremos bajo el siguiente escenario:

```
<div class="grid"><!-- contenedor -->
  <div class="item item-1">Item 1</div> <!-- cada uno de los ítems del grid -->
  <div class="item item-2">Item 2</div>
	<div class="item item-3">Item 3</div>
	<div class="item item-4">Item 4</div>
</div>
```

Para activar la cuadrícula grid hay que utilizar sobre el elemento contenedor la propiedad display y especificar uno de los dos valores que queramos utilizar: grid o inline-grid.



### **Tipo de elemento**

inline-grid

### **Descripción**

Establece una cuadrícula con ítems en línea, de forma equivalente a inline-block.

### **Tipo de elemento**

grid

### **Descripción**

Establece una cuadrícula con ítems en bloque, de forma equivalente a block.

Este valor afecta al comportamiento de la cuadrícula en relación con el contenido que la rodea. El primero de ellos hace que la cuadrícula se superponga o esté debajo del contenido circundante (en bloque), mientras que el segundo hace que la cuadrícula se coloque a la izquierda o a la derecha (en línea) del contenido circundante (es importante notar que esto se aplica a la cuadrícula en su conjunto, no a cada uno de sus elementos):

Una vez que hayas seleccionado uno de estos dos valores y configurado la propiedad display en el elemento contenedor, existen diversas formas de configurar tu cuadrícula grid. Al igual que con Flex, muchas de las propiedades se aplican al contenedor principal, pero también hay algunas que se aplican a los elementos hijos. A continuación, exploraremos detalladamente todas estas propiedades.﻿

## ¿Qué es la propiedad Grid? - Definir filas y columnas

### **Filas y columnas fijas**

En Grid CSS, la forma principal de definir una cuadrícula es indicar el tamaño de sus filas y sus columnas de forma explícita. Para ello, sólo tenemos que usar las propiedades CSS grid-template-columns y grid-template-rows:

### **Propiedad**

grid-template-columns

### **Valor**

### [*col1*] [*col2*] ...

### **Descripción**

Establece el de cada columna (*col 1, col 2...*).

### **Propiedad**

grid-template-rows

### **Valor**

### [*fila1*] [*fila2*] ...

### **Descripción**

Establece el de cada fila (*fila 1, fila 2...*).

Conociendo estas dos propiedades, asumamos el siguiente código CSS:

```
.grid {
  display: grid;
  grid-template-columns: 50px 300px;
  grid-template-rows: 200px 75px;
}
```

Al utilizar la propiedad display: grid, establecemos que deseamos crear un grid, y luego, mediante las propiedades grid-template-columns y grid-template-rows, definimos los tamaños de las columnas y las filas. Esto implica que inicialmente tendríamos un grid con un total de 4 celdas:

**Diferencia en la generación de filas y columnas con Grid. Tomado de:** [**Fuente**](https://lenguajecss.com/css/maquetacion-y-colocacion/grid-css/)

<img src="https://khc-sistema-v2.s3.amazonaws.com/editor/171889317431301e368812a384/attachment-1.png.png" alt="img" style="zoom: 33%;" />

Es importante tener en cuenta que es nuestra responsabilidad garantizar que el número de elementos hijos en el grid sea el correcto. Dependiendo del número de elementos hijos definidos en el contenedor grid en el HTML, obtendremos una cuadrícula de 2x2 elementos (4 ítems), 2x3 elementos (6 ítems), 2x4 elementos (8 ítems), y así sucesivamente. Incluso, si el número de ítems es impar, como en el caso de 5 ítems, la última celda de la cuadrícula quedará vacía.

A medida que fueramos incluyendo más ítems en el grid, podríamos aumentar también el número de parámetros de la propiedad grid-template-columns y/o la propiedad grid-template-rows. En caso de tener más ítems de lo que se indica en la propiedad, los ítems restantes se incluirían sin formato. De tener menos, simplemente se ocuparían los ítems implicados.

### **Unidad fracción restante (fr)**

En el ejemplo anterior, he utilizado píxeles como unidades para las celdas de la cuadrícula. No obstante, también podemos emplear otras unidades, como porcentajes, la palabra clave "auto" (que adquiere el tamaño restante) o la unidad especial de grid fr (fracción restante), que se detallarán a continuación.

Supongamos el siguiente fragmento de código, donde utilizamos las unidades fr:

```
.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 2fr 1fr;
}
```

Este nuevo ejemplo, también crea una cuadrícula de 2x2, donde el tamaño de la cuadrícula se divide en:

- **Dos columnas:** Mismo tamaño de ancho para cada una.
- **Dos filas:** La primera fila ocupará el doble (*2fr*) que la segunda fila (*1fr*).

**Representación gráfica de las medidas relativas en grillas. Tomado de:** [**Fuente**](https://lenguajecss.com/css/maquetacion-y-colocacion/grid-css/)



<img src="https://khc-sistema-v2.s3.amazonaws.com/editor/171889317431301e368812a384/attachment-2.png.png" alt="img" style="zoom:33%;" />



De esta forma, es muy fácil predecir el espacio que va a ocupar la cuadrícula, ya que sólo tenemos que sumar todas las unidades para saber el tamaño total, y comparar con cada columna o fila para saber como de grande o pequeña es respecto al total. Así tendremos un mejor control del espacio restante de la cuadrícula, y resultará más intuitivo calcularlo.

Se pueden combinar varias unidades diferentes, como por ejemplo píxeles (px), fracciones restantes (fr), porcentajes (%) y otras combinaciones similares.

### **Filas y columnas repetitivas**

En ocasiones, en las propiedades grid-template-columns y grid-template-rows, es necesario especificar las mismas cantidades múltiples veces, lo que puede resultar repetitivo y tedioso. Para simplificar este proceso, podemos emplear la función repeat(), que nos permite indicar cuántas veces se repiten los valores y su tamaño correspondiente.

La expresión a utilizar sería la siguiente: repeat(número de veces, tamaño):



```
.grid {
  display: grid;

  grid-template-columns: 100px repeat(4, 50px) 200px;
  grid-template-rows: repeat(2, 1fr 2fr);

  /* Equivalente a... */
  grid-template-columns: 100px 50px 50px 50px 50px 200px;
  grid-template-rows: 1fr 2fr 1fr 2fr;
}
```

Asumiendo que tuviéramos un contenedor grid con 24 ítems hijos en el HTML, el ejemplo anterior crearía una cuadrícula con 6 columnas y 4 filas. Recuerda que, en el caso de tener más ítems, hijos, el patrón se seguiría repitiendo.

### **Función minmax()**

La función minmax() se puede utilizar como valor para definir rangos flexibles de celda. Funciona de la siguiente forma:

### **Función**

minmax(min, max)

### **Descripción**

Define un rango entre min y max.

Si definimos un rango, por ejemplo, grid-template-column: minmax(200px, 500px) estamos especificando que la columna correspondiente tendrá un tamaño de 500px, a menos que redimensionemos la ventana del navegador y la reduzcamos, en cuyo caso el tamaño de la columna podría disminuir hasta un mínimo de 200px.

Prueba con este ejemplo, y prueba a redimensionar la ventana del navegador:

```
<div class="container">
	<div class="item item-1">Item 1</div>
	<div class="item item-2">Item 2</div>
	<div class="item item-3">Item 3</div>
	<div class="item item-4">Item 4</div>
</div>
<style>
.container {
  display: grid;
  grid-template-columns: repeat(2, minmax(400px, 600px));
  grid-template-rows: repeat(2, 1fr);
  gap: 5px;
}

.item {
  background: black;
  color: white;
  padding: 1em;
}
</style>
```

Comprobarás que las celdas se hacen más pequeñas hasta un punto en el que se alcanza el mínimo.

### **Auto-fill y Auto-fit**

En la función repeat(), podemos emplear las palabras clave auto-fill o auto-fit para instruir al navegador a rellenar o ajustar el contenedor grid con múltiples elementos hijos según el tamaño del viewport (la región visible del navegador). Por ejemplo, si usamos repeat(auto-fill, minmax(300px, 1fr)), el navegador se encargará de acomodar los elementos hijos con tamaño mínimo en la primera fila y, en caso de que no quepan, los distribuirá en las siguientes filas del grid. Esto garantiza una óptima utilización del contenedor, logrando un efecto similar al de las media queries pero de manera más directa y con menos código.

Imagina el siguiente ejemplo, con un grid con 10 ítems:

```
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  background: grey;
  gap: 10px;
}

.item {
  background: blue;
  color: #fff;
  font-size: 2rem;
}
```

Si cambiamos el ejemplo anterior a auto-fit no veremos ninguna diferencia. Sin embargo, si por ejemplo cambiamos el valor mínimo de 300px a 50px **(\*de modo que no llegue a cubrir la primera fila completamente\*),** comprobaremos que mientras auto-fill va rellenando la fila del grid y deja el resto del espacio libre, auto-fit ajusta el tamaño de los ítems para que cubran el tamaño máximo de la fila.

### **Atajo: La propiedad grid-template**

Si sueles utilizar estas propiedades con regularidad, puedes aprovechar la propiedad grid-template, que funciona como un atajo para simplificar múltiples configuraciones. Una de sus ventajas es la capacidad de resumir en una sola propiedad los valores que normalmente definirías en grid-template-columns y grid-template-rows.

### **Propiedad**

grid-template

### **Valores**

none | *grid-template-rows* / *grid-template-columns*

### **Descripción**

Atajo para definir dimensiones del grid.

Esta propiedad simplifica considerablemente la creación de grids con dimensiones específicas. Si utilizas el valor "none", las propiedades grid-template-rows, grid-template-columns, y la propiedad grid-template-areas (que exploraremos más adelante en el tema de Grid por áreas) se restablecerán a sus valores por defecto, desactivando su funcionamiento.

﻿﻿En el caso de utilizar unos valores definidos, la propiedad grid-template-areas se establecerá a none.

## ¿Qué es la propiedad Grid? - Huecos en grid

De forma predeterminada, todas las celdas de la cuadrícula están adyacentes entre sí. Aunque podríamos aplicar un margen a las celdas dentro del contenedor, existe una opción más adecuada: los espacios (gutters).

Para especificar los **huecos (\*espacio entre celdas\*)** podemos utilizar las propiedades column-gap y/o row-gap. En ellas indicaremos el tamaño de dichos huecos:

### ﻿﻿﻿﻿**Propiedad**

column-gap

### **Descripción**

Establece el de los huecos entre columnas **(\*líneas verticales\*).**

### ﻿﻿**Propiedad**

row-gap

### **Descripción**

Establece el de los huecos entre filas **(\*líneas horizontales\*)**.

Observa el siguiente grid irregular de ejemplo. No te preocupes por la estructura, más adelante veremos como hacerla. En él, le indicamos estas dos propiedades para colocar huecos entre las celdas de la cuadrícula.

El código sería el siguiente:

```
.grid {
  column-gap: 100px;
  row-gap: 10px;
}
```

Con la primera propiedad column-gap, establecemos un hueco de 100px entre celda y celda que se encuentre en columna, mientras que con la propiedad row-gap establecemos un hueco de 10px entre celda y celda que se encuentre en fila. Nos quedaría algo similar a esto:

**Representación visual de la separación entre elementos con Grid. Tomado de:** [**Fuente**](https://lenguajecss.com/css/maquetacion-y-colocacion/grid-css/)

<img src="https://khc-sistema-v2.s3.amazonaws.com/editor/17188973770314da5cd6b9bd1b/attachment-1.png.png" alt="img" style="zoom:33%;" />



### **Atajo: Grid con huecos**

De manera similar a lo que has visto en flex, existe una propiedad de atajo para las propiedades column-gap y row-gap, lo que nos permite evitar tener que definir estas propiedades por separado. Esta propiedad se llama gap y se utiliza de la siguiente manera:

```
.grid {
  /* gap: <row-gap> <column-gap> */
  gap: 20px 80px;
  /* Equivalente a... */
  row-gap: 20px;
  column-gap: 80px;

  gap: 40px;
  /* Equivalente a... */
  row-gap: 40px;
  column-gap: 40px;
}
```



﻿﻿﻿👀﻿﻿﻿En el pasado, las propiedades column-gap, row-gap y gap se conocían como grid-column-gap, grid-row-gap y grid-gap, por lo que es posible que todavía encuentres información desactualizada que haga referencia a estas últimas. En la actualidad, se recomienda utilizar las primeras tres propiedades en su lugar.﻿﻿﻿👀﻿﻿﻿

### **Grid por áreas**

### **Propiedad**

grid-template-areas

### **Descripción**

Indica la disposición de las áreas en el grid. Cada texto entre comillas simboliza una fila.

### **Propiedad**

grid-area

### **Descripción**

Indica el nombre del área. Se usa sobre ítems hijos del grid.

﻿﻿﻿De esta forma, es muy sencillo crear una cuadrícula altamente personalizada en apenas unas cuantas líneas de CSS, con mucha flexibilidad en la disposición y posición de cada área. Veamos un ejemplo:

```
<div class="container">
	<div class="item item-1"></div>
	<div class="item item-2"></div>
	<div class="item item-3"></div>
	<div class="item item-4"></div>
</div>
<style>
.container {
  display: grid;
  grid-template-areas: "head head"
                       "menu main"
                       "foot foot";
}

.item-1 { grid-area: head; background: blue; }
.item-2 { grid-area: menu; background: red; }
.item-3 { grid-area: main; background: green; }
.item-4 { grid-area: foot; background: orange; }
</style>
```

﻿﻿👀﻿﻿Recuerda que área y nombre de clase son cosas independientes y diferentes. Es muy importante no confundirlas.﻿﻿👀﻿﻿

- **El Item 1** sería nuestra cabecera **(\*head\*)**, que ocuparía la primera fila **(\*toda la parte superior\*).**
- El **Item 2** sería nuestro menú lateral (*menu*), que ocuparía el área izquierda del grid **(\*debajo de la cabecera\*).**
- El **Item 3** sería nuestro contenido (*main*), que ocuparía el área derecha del grid **(\*debajo de la cabecera\*).**
- El **Item 4** sería nuestro pie de cuadrícula (*foot*), que ocuparía la última fila **(\*área inferior del grid\*).**

**Representación visual del uso del contenedor con ítems insertados. Tomado de:** [**Fuente**](https://lenguajecss.com/css/maquetacion-y-colocacion/grid-css-areas/)

![img](https://khc-sistema-v2.s3.amazonaws.com/editor/17188973770314da5cd6b9bd1b/attachment-3.png.png)

Asegúrate de agregar contenido de texto en cada celda de la cuadrícula, ya que si no hay contenido y no has especificado un tamaño para las filas/columnas, la cuadrícula se ajustará automáticamente a su contenido vacío, lo que podría dar la impresión de que no existe. Además, ten en cuenta que puedes combinar esto con propiedades como grid-template-columns y/o grid-template-rows para definir tamaños o dimensiones específicas.

### **La propiedad grid-template-areas**

### **Propiedad**

grid-template-areas

### **Valores**

none | *fila1*, *fila2*, ...

### **Descripción**

Define cada fila del grid, indicando el nombre del área a colocar.

Cada una de estas filas se definen como un identificador donde indicaremos el nombre de un área que posteriormente definiremos en nuestro código CSS. Cada fila puede tener ninguna o varias áreas que habría que separar por espacio. A continuación veremos algunos ejemplos de los valores que podemos indicar en esta propiedad y su significado:

### ﻿﻿**Valores**

none

### **Descripción**

Indica que no se creará ninguna plantilla de áreas.

### ﻿﻿**Valores**

"head"

### **Descripción**

Indica que se creará una fila de una columna con el área head.

### ﻿﻿**Valores**

"head menu"

### **Descripción**

Indica que se creará una fila de 2 columnas con el área head en una y el área menú en otra.

### ﻿﻿**Valores**

"head head"

### **Descripción**

Indica que se creará una fila de 2 columnas con el área head ocupando ambas.

### ﻿﻿**Valores**

### "."

### **Descripción**

Indica que se colocará una celda sin nombre **(\*nula\*)** en esta posición.

﻿👀﻿Recuerda que las áreas deben existir y estar definidas con la propiedad grid-area, de lo contrario, se anulará la propiedad.﻿👀﻿

### **La propiedad grid-area**

Por otro lado, al utilizar la propiedad grid-template-areas y nombrar varias áreas en sus valores, es necesario que dichas áreas estén definidas mediante la propiedad grid-area en sus elementos hijos. Recuerda no confundir nombre de área, con nombre de clase, puesto que no es lo mismo.

### **Propiedad**

grid-area

### **Valores**

auto | *nombre*

### **Descripción**

Da un nombre de área al elemento indicado.

Esta propiedad permite nombrar un elemento del HTML con un nombre de área. Mucho cuidado, ya que este nombre no es un string, y, por lo tanto, no debe definirse entre comillas ". Estos nombres se utilizarán en la propiedad grid-template-areas para definir dónde irán ubicados.

Los valores que puede tomar la propiedad grid-area son los siguientes:

### **Valores**

### auto

### **Descripción**

Coloca la celda en la próxima área vacía que se encuentre disponible.

### **Valores**

### ﻿*nombre*

### **Descripción**

Le da un nombre de área al elemento en cuestión.

# Responsive

En la actualidad, el uso de una amplia variedad de dispositivos móviles ha experimentado un aumento significativo, incluyendo no solo smartphones, sino también tablets, smartwatches, lectores de ebooks y diversos dispositivos con conectividad a Internet.

En la actualidad, es cada vez más común el acceso a Internet a través de una variedad de dispositivos con pantallas y resoluciones diversas, que presentan tamaños y formas distintas. Esto conlleva a que las páginas web se visualicen de manera variada y plantea diferentes desafíos, necesidades y soluciones.

**Ejemplo de una web responsive. Tomado de:** [**Fuente**](https://lenguajecss.com/css/maquetacion-y-colocacion/grid-css-areas/)

![img](https://khc-sistema-v2.s3.amazonaws.com/editor/1718902526393c1290e86ad2038/attachment-1.png.png)

En la actualidad, al diseñar un sitio web, es esencial garantizar su correcta visualización en diversas resoluciones, lo que puede ser un desafío. En el pasado, se solía crear versiones separadas de un sitio web para adaptarse a dispositivos o navegadores específicos, pero esta práctica resultó poco práctica y se abandonó en favor de enfoques más flexibles.

Por suerte, esos tiempos han quedado atrás, y la máxima que se sigue hoy es diseñar una sola web, que se adapte visualmente al dispositivo utilizado.

Actualmente, se utiliza el término "Diseño Web Responsivo" (Responsive Web Design o RWD) para describir aquellos diseños web que pueden ajustarse al tamaño y formato de la pantalla en la que se visualizan, en contraposición a los diseños tradicionales que estaban destinados a tamaños o formatos específicos sin la capacidad de adaptación correspondiente.

Aunque en principio el concepto de web adaptativa es muy sencillo de comprender, aplicarlo puede ser todo un quebradero de cabeza si no se conocen bien las bases y se adquiere experiencia. En [MediaQueri.es](http://mediaqueri.es/) puedes encontrar algunos ejemplos de páginas que utilizan Responsive Web Design para tener clara la idea.



**Responsive vs Adaptativo. Tomado de:** [**Fuente**](https://lenguajecss.com/css/responsive-web-design/que-es/)



![img](https://khc-sistema-v2.s3.amazonaws.com/editor/1718902526393c1290e86ad2038/attachment-2.png.png)

## Responsive - Conceptos básicos

En el artículo "9 principios básicos del diseño web responsivo" de Froont, encontrarás una excelente descripción visual de algunos conceptos fundamentales que son esenciales para comprender adecuadamente el Diseño Web Responsivo. Además, el artículo incluye animaciones ilustrativas que facilitan la comprensión de estos conceptos. Estos principios son los siguientes:

### **Responsive vs Adaptative**

El primer concepto a comprender es la distinción entre el "diseño responsivo" y el "diseño adaptativo". La imagen que se muestra a continuación ilustra esta diferencia: un diseño responsivo se ajusta constantemente a las dimensiones del dispositivo, mientras que un diseño adaptativo se adapta, pero no necesariamente responde de manera continua:

﻿👀﻿Exploraremos cómo aplicar adecuadamente conceptos como media queries, porcentajes y propiedades de ancho máximo y mínimo en los próximos apartados, ya que estos elementos marcan la diferencia en esta distinción.﻿👀﻿

### **Unidades relativas vs estáticas**



Por otro lado, para trabajar correctamente en diseños responsive hay que tener en cuenta que debemos trabajar con unidades relativas e intentar evitar las unidades fijas o estáticas, las cuales no responden a la adaptación de nuestros diseños flexibles:

**Unidades relativas vs Unidades estáticas. Tomado de:** [**Fuente**](https://lenguajecss.com/css/responsive-web-design/que-es/)

![img](https://khc-sistema-v2.s3.amazonaws.com/editor/1718903499512a00c2b918e5c/attachment-1.png.png)



### **Con máximos y sin máximos**

Una estrategia interesante para lograr diseños responsivos es emplear propiedades como min-width o max-width, las cuales establecen tamaños mínimos o máximos para permitir que los elementos de la página se ajusten de manera adecuada según las dimensiones de la pantalla del dispositivo en uso.

Con estas propiedades podemos crear diseños que aprovechen al máximo toda la pantalla de dispositivos pequeños (*como móviles o tablets*), mientras que establecemos unos máximos en pantallas de dispositivos grandes, para crear unos espacios visuales que hacen que el diseño sea más agradable:

### **Flujo vs Estático**

Otro concepto importante y atractivo en nuestros diseños responsivos es mantener el flujo de los elementos, evitando que se superpongan al cambiar de tamaño.



Si estamos habituados a trabajar en diseños más estáticos que no están preparados para móviles, suele ser duro hacer ese cambio. Sin embargo, una vez lo conseguimos, todo resulta mucho más fácil y conseguiremos transmitir una buena respuesta y fluidez visual:



### **Con breakpoints vs sin breakpoints**

Esto último va muy de la mano del sistema habitual de recolocación de elementos que se suele seguir en los diseños Responsive Design. Como se puede ver en la siguiente imagen, en un diseño responsive se utilizan ciertos «puntos de control».

Por ejemplo, se suele pensar que en una resolución de escritorio queremos mostrar la información dentro de una cuadrícula (*grid*) de 4 ó 5 celdas de ancho, mientras que en la versión de tablet será solo de 3 celdas de ancho (*el resto se desplazará a la siguiente fila*) y en móviles será una sola celda de ancho, mostrándose el resto de celdas haciendo scroll hacia abajo:

Esta forma de trabajar nos proporciona múltiples ventajas:

- Es mucho más sencillo mostrar la misma información desde diseños de pantalla grande.
- Ayuda a evitar la mala práctica de ocultar bloques de información en dispositivos móviles.
- Incentiva a diseñar siguiendo buenas prácticas para facilitar la creación responsive.

## Responsive - Preparación previa

Antes de comenzar a crear un diseño web preparado para móviles, es importante tener claro ciertos detalles:



- A priori, ¿Cuál es tu público objetivo? ¿móvil o escritorio? ¿ambos?
- Debes conocer las resoluciones más utilizadas por tu público potencial.
- Debes elegir una estrategia acorde a los datos anteriores.



En primer lugar, es importante conocer los formatos de pantalla más comunes con los cuales nos vamos a encontrar. Podemos consultar páginas como [MyDevices](https://www.mydevice.io/), la cuál tiene un apartado de [comparación de dispositivos](https://www.mydevice.io/#compare-devices), donde se nos muestra un listado de dispositivos categorizados en smartphones, tablets u otros dispositivos con las características de cada uno: dimensiones de ancho, alto, radio de píxels, etc...

Una vez estés familiarizado con estos detalles, es importante conocer el público de tu sitio web. ¿Acceden más usuarios desde móvil o desde escritorio? ¿Predominan las tablets o los móviles? ¿Tu objetivo es tener más usuarios de móvil o de escritorio?

Consulta con algún sistema de estadísticas como [Google Analytics](https://marketingplatform.google.com/about/analytics/) para comprobar qué tipo de público tienes actualmente. También es aconsejable echar un vistazo a información externa como las que nos proporcionan estadísticas globales anónimas de [Global StatCounter](https://gs.statcounter.com/screen-resolution-stats), para hacernos una idea de los atributos más comunes.

## Responsive - Estrategias de diseño

Por último, es aconsejable decidirse por una estrategia de diseño antes de comenzar. Aunque existen otras estrategias, las dos vertientes principales más populares son las siguientes:

### **Estrategia**

Mobile first

### **Descripción**

Primero nos enfocamos en dispositivos móviles y luego pensamos en otros.

### **Estrategia**

Desktop first

### **Descripción**

Primero nos enfocamos en dispositivos de escritorio, y luego pensamos en otros.

### **Mobile-first**

La estrategia "Mobile-first" es empleada por los diseñadores de sitios web cuando su audiencia principal son usuarios de dispositivos móviles. Ejemplos como una web para comprar boletos de transporte, la página de un juego o aplicación móvil, o un sitio para reservar una mesa en un restaurante podrían ser opciones adecuadas para adoptar la estrategia "Mobile-first".

﻿﻿👀﻿﻿Esta estrategia hace que el desarrollo en escritorio sea muy sencillo, ya que se reduce a tener un diseño de móvil en escritorio e ir añadiendo nuevas secciones o partes para «completar» el diseño en resoluciones grandes.﻿﻿👀﻿﻿

### **Desktop-first**

Por otro lado, la estrategia Desktop-first suele interesar más a los diseñadores de sitios webs en los que el público objetivo son usuarios de escritorio. Por ejemplo, una página de una aplicación para PC/Mac o similares, podría ser una buena opción para la estrategia Desktop-first.

En ella, hacemos justo lo contrario que en la anterior. Lo primero que diseñamos es la versión de escritorio, y luego vamos descargando detalles o recolocando información hasta tener la versión para dispositivos móviles.

# ¿Qué es Media Query?

![img](https://khc-sistema-v2.s3.amazonaws.com/editor/1718907779518b437490a5cd27/attachment-1.png.png)El *media query* es un concepto el cual permite hacer excepciones de estilos de acuerdo a una condicionalidad establecida, permitiendo realizar cambios en los estilos que una página de acuerdo a la necesidad del usuario.

Esto permite que, si la pantalla cambia en su ancho o alto, o en alguna propiedad, *media query* intervenga y haga los cambios pertinentes en la hoja de estilos establecida en la página a mostrar.

Veamos a continuación la sintaxis de dicha aplicación:

**Sintaxis general de la implementación de** **@media****. Tomado de:**[**enlace**](https://lenguajecss.com/css/responsive-web-design/media-queries/)**.** 

```
@media (*condición*) {
  .container {
    background: green;
  }
}

@media not (*condición*) {
  .container {
    background: red;
  }
}
```



En el ejemplo anterior, si se cumple la condición establecida, se aplicará un color verde. Sin embargo, si no se cumple, se aplicará un color rojo. Esto es similar al funcionamiento de una estructura if / else en programación.

No debe olvidarse que al escribir una regla @media, es posible que se estén sobrescribiendo los estilos CSS en otro fragmento posterior. Una buena práctica para empezar a escribir consultas de medios (media queries) es colocar las reglas @media siempre al final del documento, tratándolas como excepciones al código anterior.

El número de bloques de reglas @media a utilizar depende del criterio del desarrollador web, ya que no existe una obligación o norma que imponga un número concreto. Se pueden utilizar desde una sola consulta de medios hasta múltiples a lo largo de todo el documento CSS.

Si se desea, es posible establecer múltiples condiciones en las reglas @media. Esto permite manejar situaciones mucho más específicas y flexibles, pues es crucial tener cuidado al aplicar el operador not en las condiciones, para no negar de manera incorrecta los casos deseados.

# 📚 Resumen con Recursos Externos

## 📦 Grid CSS

- **Conceptos:** contenedor, ítems, celdas, áreas, tracks y líneas.
- **Propiedades clave:**
  - `grid-template-columns / rows`
  - `fr` (fracciones), `repeat()`, `minmax()`
  - `auto-fit` / `auto-fill`
  - `gap`, `grid-template-areas`, `grid-area`

🔗 Recursos:

- MDN – Guía de Grid CSS
- CSS Tricks – Complete Guide to Grid
- [LenguajeCSS – Grid CSS](https://lenguajecss.com/css/maquetacion-y-colocacion/grid-css/)

📺 Videos YouTube:

- [Kevin Powell – CSS Grid Tutorial](https://www.youtube.com/watch?v=rg7Fvvl3taU)
- [Fazt Code – CSS Grid desde cero](https://www.youtube.com/watch?v=0xMQfnTU6oo)

------

## 📱 Responsive Design

- **Bases:** usar unidades relativas (`%`, `em`, `rem`, `fr`) en lugar de px.
- **Media queries:** `@media (max-width: 768px)` para breakpoints.
- **Estrategias:**
  - *Mobile First*: estilos base para móvil, luego ampliar a escritorio.
  - *Desktop First*: estilos base para escritorio, luego adaptar a móvil.
- **Buenas prácticas:** `min-width`, `max-width`, fluidez con `auto-fit` y `minmax`.

🔗 Recursos:

- MDN – Responsive Design
- [MediaQueri.es – Galería de sitios responsive](http://mediaqueri.es/)
- [StatCounter – Resoluciones de pantallas globales](https://gs.statcounter.com/screen-resolution-stats)

📺 Videos YouTube:

- [Traversy Media – Responsive Web Design Crash Course](https://www.youtube.com/watch?v=srvUrASNj0s)
- [HolaMundo – Diseño Responsive con CSS Grid y Flexbox](https://www.youtube.com/watch?v=rnhoY5Cdmy0)

------

# 🧑‍💻 Ejercicios Prácticos con Solución

### 🔹 Ejercicio 1: Grid Básico

👉 Crea un grid de 2 columnas y 2 filas usando fracciones.

```
<div class="grid">
  <div>1</div><div>2</div>
  <div>3</div><div>4</div>
</div>

<style>
.grid {
  display: grid;
  grid-template-columns: 1fr 2fr;
  grid-template-rows: 100px 50px;
  gap: 10px;
}
.grid div {
  background: steelblue;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
```

✅ **Solución:** Dos columnas, la segunda ocupa el doble de espacio que la primera.

------

### 🔹 Ejercicio 2: Auto-fit con minmax()

👉 Crea una galería responsiva que se adapte al ancho.

```
<div class="gallery">
  <div>A</div><div>B</div><div>C</div><div>D</div>
</div>

<style>
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
}
.gallery div {
  background: tomato;
  color: white;
  text-align: center;
  padding: 2rem;
}
</style>
```

✅ **Solución:** Se crean tantas columnas como quepan, mínimo 150px cada una.

------

### 🔹 Ejercicio 3: Grid por Áreas

👉 Define un layout con header, sidebar, main y footer.

```
<div class="container">
  <header class="head">Header</header>
  <aside class="menu">Menu</aside>
  <main class="main">Contenido</main>
  <footer class="foot">Footer</footer>
</div>

<style>
.container {
  display: grid;
  grid-template-areas:
    "head head"
    "menu main"
    "foot foot";
  grid-template-columns: 200px 1fr;
  grid-template-rows: auto 1fr auto;
  height: 100vh;
}
.head  { grid-area: head;  background: steelblue; color: #fff; }
.menu  { grid-area: menu;  background: lightgray; }
.main  { grid-area: main;  background: white; }
.foot  { grid-area: foot;  background: darkslategray; color: #fff; }
</style>
```

✅ **Solución:** Distribución clara con `grid-template-areas`.

------

### 🔹 Ejercicio 4: Responsive con Media Query

👉 Haz que en pantallas menores de 600px el grid pase a 1 columna.

```
<div class="responsive">
  <div>Box 1</div>
  <div>Box 2</div>
  <div>Box 3</div>
</div>

<style>
.responsive {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}
.responsive div {
  background: lightseagreen;
  color: white;
  text-align: center;
  padding: 2rem;
}
@media (max-width: 600px) {
  .responsive {
    grid-template-columns: 1fr;
  }
}
</style>
```

✅ **Solución:** En escritorio, 3 columnas. En móvil, se apila en 1.

------

### 🔹 Ejercicio 5: Layout Completo Responsive

👉 Crea un sitio con **header, navbar, content y footer**, que se reorganice en móvil.

```
<div class="page">
  <header>Header</header>
  <nav>Nav</nav>
  <main>Main</main>
  <footer>Footer</footer>
</div>

<style>
.page {
  display: grid;
  grid-template-areas:
    "header header"
    "nav main"
    "footer footer";
  grid-template-columns: 200px 1fr;
  min-height: 100vh;
}
header { grid-area: header; background: steelblue; color: #fff; padding: 1rem; }
nav    { grid-area: nav;    background: lightgray; padding: 1rem; }
main   { grid-area: main;   background: white; padding: 1rem; }
footer { grid-area: footer; background: darkslategray; color: #fff; padding: 1rem; }

@media (max-width: 700px) {
  .page {
    grid-template-areas:
      "header"
      "nav"
      "main"
      "footer";
    grid-template-columns: 1fr;
  }
}
</style>
```

✅ **Solución:**

- Escritorio → nav a la izquierda y main a la derecha.
- Móvil → se apila todo verticalmente.