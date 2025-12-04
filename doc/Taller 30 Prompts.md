## Documento 1: `var`, `let` y `const` (alcance básico)

**Instrucción:**
 Actúa como docente de programación para estudiantes de 17-24 años que están empezando con JavaScript. Explica de forma sencilla la diferencia básica entre `var`, `let` y `const`.

**Contexto:**
 Soy un estudiante que ya ha visto variables en otros lenguajes, pero me confunde por qué en JavaScript existen tres formas distintas de declarar: `var`, `let` y `const`.

**Entrada:**
 Te haré preguntas directas sobre cuándo usar `var`, cuándo `let` y cuándo `const`.

**Salida:**
 Responde con:

1. Explicación corta de cada palabra clave.
2. Una tabla sencilla (en texto) comparando alcance y posibilidad de reasignar.
3. Un ejemplo de código corto.
4. Una pregunta final para practicar.

**Ejemplo:**

```
let nombre = "Ana";
const edad = 20;
var ciudad = "Bogotá";

console.log(nombre, edad, ciudad);
```

**Pregunta #1:**
 ¿Cómo describirías en una frase cuándo usarías `const` en tu código?

------

## Documento 2: Tipos de datos primitivos

**Instrucción:**
 Actúa como docente y explica los tipos de datos primitivos en JavaScript a un estudiante principiante.

**Contexto:**
 Conozco la palabra “variable”, pero no tengo claro qué significa que algo sea `string`, `number`, `boolean`, `null`, `undefined` o `bigint`.

**Entrada:**
 Te pediré que me expliques qué es cada tipo primitivo con ejemplos sencillos.

**Salida:**

1. Lista de tipos primitivos con una frase de explicación.
2. Un ejemplo de código donde se declaren al menos 4 tipos diferentes.
3. Explicación breve del ejemplo.
4. Una pregunta para identificar el tipo de un valor.

**Ejemplo:**

```
let nombre = "Carlos";  // string
let edad = 18;          // number
let esMayor = false;    // boolean
let nada = null;        // null
```

**Pregunta #1:**
 ¿Qué tipo de dato es el valor `true` en JavaScript?

------

## Documento 3: Operadores aritméticos básicos

**Instrucción:**
 Explica cómo funcionan los operadores aritméticos básicos en JavaScript: suma, resta, multiplicación, división y módulo.

**Contexto:**
 Estoy iniciando en programación y quiero usar JavaScript para hacer operaciones matemáticas simples.

**Entrada:**
 Te pediré ejemplos con números pequeños para entender `+`, `-`, `*`, `/` y `%`.

**Salida:**

1. Definición corta de cada operador.
2. Ejemplo de código que use todos los operadores.
3. Explicación línea por línea.
4. Un ejercicio para que yo calcule un resultado.

**Ejemplo:**

```
let a = 10;
let b = 3;

console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);
```

**Pregunta #1:**
 ¿Qué mostraría `console.log(9 % 4);` en la consola?

------

## Documento 4: Operadores de comparación

**Instrucción:**
 Enseña a un estudiante básico la diferencia entre `==`, `===`, `!=` y `!==` en JavaScript.

**Contexto:**
 Ya sé hacer operaciones con números, pero no entiendo bien cómo comparar valores y por qué hay dos tipos de igualdad.

**Entrada:**
 Te haré preguntas sobre cómo comparar números y textos.

**Salida:**

1. Explicación simple de cada operador.
2. Ejemplo de código comparando un número y un string.
3. Explicación del resultado.
4. Una pregunta para que el estudiante prediga el resultado de una comparación.

**Ejemplo:**

```
let x = 5;
let y = "5";

console.log(x == y);   // ?
console.log(x === y);  // ?
```

**Pregunta #1:**
 ¿Qué crees que mostrará `console.log(3 === "3");` y por qué?

------

## Documento 5: ¡Errorcito leve! Operadores lógicos

**Instrucción:**
 Explica el uso básico de los operadores lógicos `&&` (y), `||` (o) y `!` (no) en JavaScript.

**Contexto:**
 Quiero combinar varias condiciones en un `if`, pero me confundo cuando uso más de una comparación.

**Entrada:**
 Te pediré ejemplos simples con edades y permisos.

**Salida:**

1. Explicación corta de cada operador lógico.
2. Un ejemplo de código con un `if` que combine al menos dos operadores.
3. Explicación del flujo lógico.
4. Una pregunta para que adivine si una condición es verdadera o falsa.

**Ejemplo (con un pequeño detalle a corregir):**

```
let edad = 17;
let tienePermiso = true;

if (edad >= 18 && tienePermiso == true || false) {
  console.log("Puede entrar al concierto");
} else {
  console.log("No puede entrar");
}
```

> *Nota: hay una condición innecesaria en el `if` que hace el código un poco confuso.*

**Pregunta #1:**
 ¿Cómo simplificarías la condición del `if` anterior para que sea más clara?

------

## Documento 6: Strings y concatenación

**Instrucción:**
 Enseña cómo crear strings y concatenarlos usando el operador `+`.

**Contexto:**
 Quiero mostrar mensajes combinando nombre y apellido de un usuario.

**Entrada:**
 Te haré preguntas sobre cómo unir textos y variables en un solo mensaje.

**Salida:**

1. Explicación de qué es un string.
2. Ejemplo de concatenación con `+`.
3. Explicación de cada línea.
4. Una pregunta para que el estudiante construya su propio mensaje.

**Ejemplo:**

```
let nombre = "Laura";
let apellido = "Gómez";

let mensaje = "Hola " + nombre + " " + apellido;
console.log(mensaje);
```

**Pregunta #1:**
 ¿Cómo concatenarías un saludo que diga: `"Hola, soy Pedro"` usando dos variables?

------

## Documento 7: Template literals (cadenas con backticks)

**Instrucción:**
 Explica cómo usar template literals con backticks (```) y `${}`.

**Contexto:**
 Ya sé concatenar con `+`, pero me cuesta leer el código cuando hay muchos textos.

**Entrada:**
 Te pediré un ejemplo de interpolación de variables dentro de una cadena.

**Salida:**

1. Explicación de qué es un template literal.
2. Ejemplo de uso con al menos dos variables.
3. Explicación de la sintaxis `${}`.
4. Una pregunta para reescribir un ejemplo con template literals.

**Ejemplo:**

```
let producto = "Computador";
let precio = 1500;

let mensaje = `El ${producto} cuesta ${precio} dólares`;
console.log(mensaje);
```

**Pregunta #1:**
 Convierte una concatenación con `+` a template literal usando backticks.

------

## Documento 8: Estructura básica de un `if`

**Instrucción:**
 Enseña a usar un `if` simple en JavaScript.

**Contexto:**
 Soy nuevo en programación y quiero ejecutar código solo si se cumple una condición.

**Entrada:**
 Te haré preguntas sobre cuándo se ejecuta el bloque `if`.

**Salida:**

1. Explicación de la sintaxis de `if`.
2. Ejemplo con una condición verdadera.
3. Explicación del flujo.
4. Una pregunta donde yo tenga que decidir si el `if` se ejecuta o no.

**Ejemplo:**

```
let edad = 20;

if (edad >= 18) {
  console.log("Eres mayor de edad");
}
```

**Pregunta #1:**
 ¿Qué pasaría si `edad` fuera 15 en el ejemplo anterior?

------

## Documento 9: `if...else`

**Instrucción:**
 Explica cómo usar `if...else` para tomar dos caminos posibles en el código.

**Contexto:**
 Quiero mostrar un mensaje si un usuario está logueado y otro si no lo está.

**Entrada:**
 Te preguntaré cómo decidir entre dos opciones con un `if` y un `else`.

**Salida:**

1. Explicación de `if` y `else`.
2. Ejemplo con una condición falsa.
3. Explicación de cada rama.
4. Una pregunta de predicción del resultado.

**Ejemplo:**

```
let estaLogueado = false;

if (estaLogueado) {
  console.log("Bienvenido de nuevo");
} else {
  console.log("Por favor inicia sesión");
}
```

**Pregunta #1:**
 ¿Qué mensaje se muestra si `estaLogueado` vale `true`?

------

## Documento 10: `if...else if...else`

**Instrucción:**
 Enseña a encadenar varias condiciones usando `if`, `else if` y `else`.

**Contexto:**
 Quiero mostrar diferentes mensajes según la nota de un estudiante: malo, regular o bueno.

**Entrada:**
 Te pediré un ejemplo donde se evalúe una nota numérica.

**Salida:**

1. Explicación del orden en que se revisan las condiciones.
2. Ejemplo con tres rangos de notas.
3. Explicación del flujo.
4. Una pregunta para crear un nuevo rango.

**Ejemplo:**

```
let nota = 85;

if (nota >= 90) {
  console.log("Excelente");
} else if (nota >= 60) {
  console.log("Aprobado");
} else {
  console.log("Reprobado");
}
```

**Pregunta #1:**
 ¿En qué casos se ejecuta el bloque `else`?

------

## Documento 11: `switch` básico

**Instrucción:**
 Explica cómo usar la estructura `switch` para elegir entre varias opciones.

**Contexto:**
 Tengo muchos `if` seguidos comparando la misma variable y quiero una forma más ordenada.

**Entrada:**
 Te pediré ejemplos con días de la semana.

**Salida:**

1. Explicación del `switch`.
2. Ejemplo con al menos 3 `case`.
3. Explicación del uso de `break` y `default`.
4. Una pregunta para agregar un nuevo caso.

**Ejemplo:**

```
let dia = "lunes";

switch (dia) {
  case "lunes":
    console.log("Inicio de semana");
    break;
  case "viernes":
    console.log("Casi fin de semana");
    break;
  default:
    console.log("Día cualquiera");
}
```

**Pregunta #1:**
 ¿Qué mensaje se mostraría si `dia` fuera `"viernes"`?

------

## Documento 12: ¡Errorcito leve! Ciclo `while`

**Instrucción:**
 Enseña a usar un ciclo `while` para repetir código mientras se cumpla una condición.

**Contexto:**
 Quiero contar números del 1 al 5 con un bucle, pero me preocupa hacer un bucle infinito.

**Entrada:**
 Te preguntaré cómo controlar la condición y la actualización de la variable.

**Salida:**

1. Explicación de la estructura `while`.
2. Ejemplo contando del 1 al 3.
3. Explicación de por qué el ciclo termina.
4. Una pregunta para modificar el rango.

**Ejemplo (con un pequeño descuido):**

```
let i = 1;

while (i <= 3) {
  console.log(i);
  // falta incrementar i aquí
}
```

> *Nota: el ejemplo está incompleto, el estudiante debe notar qué falta para evitar un bucle infinito.*

**Pregunta #1:**
 ¿Qué línea agregarías dentro del `while` para que el ciclo termine correctamente?

------

## Documento 13: Ciclo `do...while`

**Instrucción:**
 Explica cómo funciona el ciclo `do...while` y en qué se diferencia de `while`.

**Contexto:**
 Quiero que cierto código se ejecute al menos una vez, aunque la condición sea falsa.

**Entrada:**
 Te pediré un ejemplo de `do...while` con un contador.

**Salida:**

1. Explicación de la estructura `do...while`.
2. Ejemplo simple con un contador.
3. Explicación del orden de ejecución.
4. Una pregunta para comparar con `while`.

**Ejemplo:**

```
let numero = 5;

do {
  console.log(numero);
  numero++;
} while (numero < 5);
```

**Pregunta #1:**
 ¿Por qué el ejemplo anterior imprime al menos un número?

------

## Documento 14: Ciclo `for` clásico

**Instrucción:**
 Enseña a usar el ciclo `for` tradicional con inicialización, condición y actualización.

**Contexto:**
 Quiero recorrer números del 1 al 5 haciendo algo con cada uno.

**Entrada:**
 Te haré preguntas sobre el orden de las partes del `for`.

**Salida:**

1. Explicación de la sintaxis del `for`.
2. Ejemplo que imprima del 1 al 5.
3. Explicación breve línea por línea.
4. Una pregunta para cambiar el rango.

**Ejemplo:**

```
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
```

**Pregunta #1:**
 ¿Cómo cambiarías el `for` para contar solo números pares del 2 al 10?

------

## Documento 15: Arreglos (arrays) básicos

**Instrucción:**
 Explica qué es un array en JavaScript y cómo acceder a sus elementos por índice.

**Contexto:**
 Quiero guardar varios nombres en una sola variable y recorrerlos.

**Entrada:**
 Te pediré ejemplos con un array de 3 o 4 elementos.

**Salida:**

1. Definición sencilla de array.
2. Ejemplo de creación y acceso por índices.
3. Explicación de índices empezando en 0.
4. Una pregunta para que el estudiante obtenga un elemento concreto.

**Ejemplo:**

```
let frutas = ["Manzana", "Banano", "Pera"];

console.log(frutas[0]);
console.log(frutas[2]);
```

**Pregunta #1:**
 ¿Qué mostrará `console.log(frutas[1]);` en el ejemplo anterior?

------

## Documento 16: Recorrer arrays con `for`

**Instrucción:**
 Enseña a recorrer un array usando un ciclo `for`.

**Contexto:**
 Ya sé crear arrays, pero quiero imprimir todos sus elementos sin repetir código.

**Entrada:**
 Te pediré un ejemplo con un array de números.

**Salida:**

1. Explicación de cómo usar la propiedad `.length`.
2. Ejemplo de `for` para recorrer el array.
3. Explicación del papel del índice.
4. Una pregunta para modificar el código.

**Ejemplo:**

```
let numeros = [10, 20, 30];

for (let i = 0; i < numeros.length; i++) {
  console.log(numeros[i]);
}
```

**Pregunta #1:**
 ¿Cómo harías para sumar todos los elementos del array dentro del mismo `for`?

------

## Documento 17: Métodos de array: `push` y `pop`

**Instrucción:**
 Explica los métodos `push` y `pop` para agregar y eliminar elementos al final de un array.

**Contexto:**
 Quiero construir una lista dinámica donde pueda añadir y quitar elementos fácilmente.

**Entrada:**
 Te haré preguntas sobre cómo cambia el tamaño del array al usar estos métodos.

**Salida:**

1. Definición de `push` y `pop`.
2. Ejemplo de uso paso a paso.
3. Explicación de los cambios en el array.
4. Una pregunta sobre el resultado final del array.

**Ejemplo:**

```
let numeros = [1, 2];

numeros.push(3);
numeros.push(4);
numeros.pop();

console.log(numeros);
```

**Pregunta #1:**
 ¿Qué elementos quedan en el array `numeros` al final del ejemplo?

------

## Documento 18: Funciones básicas (declaración)

**Instrucción:**
 Enseña a declarar y llamar una función simple en JavaScript.

**Contexto:**
 Quiero agrupar código que se repite para no escribirlo varias veces.

**Entrada:**
 Te pediré un ejemplo de función que reciba un nombre y muestre un saludo.

**Salida:**

1. Explicación de qué es una función.
2. Ejemplo con parámetros.
3. Explicación de la llamada a la función.
4. Una pregunta para que el estudiante cree otra función similar.

**Ejemplo:**

```
function saludar(nombre) {
  console.log("Hola " + nombre);
}

saludar("Juan");
```

**Pregunta #1:**
 ¿Cómo llamarías a la función `saludar` para que salude a “María”?

------

## Documento 19: ¡Errorcito leve! Funciones flecha (`=>`)

**Instrucción:**
 Explica qué es una función flecha (arrow function) y cómo se escribe.

**Contexto:**
 Ya he visto funciones normales, pero la sintaxis de `=>` me parece rara.

**Entrada:**
 Te pediré un ejemplo que sume dos números.

**Salida:**

1. Explicación de la sintaxis básica.
2. Ejemplo de función flecha.
3. Explicación de cada parte.
4. Una pregunta para convertir una función tradicional a flecha.

**Ejemplo (con un detalle mínimo):**

```
const sumar = (a, b) => {
  return a + b
}

console.log(suma(2, 3));
```

> *Nota: hay un pequeño error en el nombre usado en `console.log`, que el estudiante puede detectar.*

**Pregunta #1:**
 ¿Qué tendrías que corregir en el ejemplo para que funcione correctamente?

------

## Documento 20: Parámetros y valores de retorno

**Instrucción:**
 Enseña la diferencia entre pasar parámetros a una función y devolver un valor con `return`.

**Contexto:**
 Quiero que mi función calcule algo y me entregue el resultado para usarlo después.

**Entrada:**
 Te pediré un ejemplo que calcule el área de un rectángulo.

**Salida:**

1. Explicación de parámetros y retorno.
2. Ejemplo de función que devuelva un número.
3. Explicación del uso de `return`.
4. Una pregunta para que el estudiante use el valor retornado.

**Ejemplo:**

```
function areaRectangulo(base, altura) {
  return base * altura;
}

let resultado = areaRectangulo(5, 3);
console.log(resultado);
```

**Pregunta #1:**
 ¿Qué pasaría si llamas a `areaRectangulo(2, 10);`?

------

## Documento 21: Alcance de variables (scope) simple

**Instrucción:**
 Explica el alcance de variables declaradas dentro y fuera de una función.

**Contexto:**
 No sé por qué algunas variables “no existen” fuera de ciertos bloques.

**Entrada:**
 Te pediré un ejemplo con una variable global y una local.

**Salida:**

1. Explicación de variable global vs local.
2. Ejemplo de función que use ambas.
3. Explicación de dónde se puede usar cada variable.
4. Una pregunta para predecir un error de referencia.

**Ejemplo:**

```
let mensajeGlobal = "Hola";

function mostrarMensaje() {
  let mensajeLocal = "Mundo";
  console.log(mensajeGlobal + " " + mensajeLocal);
}

mostrarMensaje();
// console.log(mensajeLocal); // ¿qué pasaría aquí?
```

**Pregunta #1:**
 ¿Por qué la última línea comentada generaría un error si se ejecutara?

------

## Documento 22: Objetos literales básicos

**Instrucción:**
 Enseña qué es un objeto literal en JavaScript y cómo definirlo.

**Contexto:**
 Quiero agrupar varios datos relacionados de una persona en una sola estructura.

**Entrada:**
 Te pediré un ejemplo de objeto `persona` con nombre, edad y ciudad.

**Salida:**

1. Explicación de objeto literal.
2. Ejemplo de creación del objeto.
3. Explicación de cada propiedad.
4. Una pregunta para agregar una nueva propiedad.

**Ejemplo:**

```
let persona = {
  nombre: "Ana",
  edad: 25,
  ciudad: "Medellín"
};
```

**Pregunta #1:**
 ¿Cómo agregarías la propiedad `profesion` al objeto `persona`?

------

## Documento 23: Acceso a propiedades de un objeto

**Instrucción:**
 Explica cómo acceder a las propiedades de un objeto usando notación punto y notación corchetes.

**Contexto:**
 Tengo un objeto `persona` pero no sé bien cómo leer sus datos.

**Entrada:**
 Te preguntaré la diferencia entre `persona.nombre` y `persona["nombre"]`.

**Salida:**

1. Explicación de ambas notaciones.
2. Ejemplo que use las dos.
3. Explicación de cuándo usar cada una.
4. Una pregunta donde el estudiante deba obtener una propiedad.

**Ejemplo:**

```
let persona = {
  nombre: "Luis",
  edad: 30
};

console.log(persona.nombre);
console.log(persona["edad"]);
```

**Pregunta #1:**
 ¿Cómo accederías a la propiedad `nombre` usando corchetes?

------

## Documento 24: ¡Errorcito leve! Métodos dentro de un objeto

**Instrucción:**
 Enseña cómo definir un método (función) dentro de un objeto.

**Contexto:**
 Quiero que mi objeto `persona` pueda “presentarse” mostrando un mensaje con su nombre.

**Entrada:**
 Te pediré un ejemplo de objeto con un método.

**Salida:**

1. Explicación de qué es un método.
2. Ejemplo con `this`.
3. Explicación del uso de `this`.
4. Una pregunta para modificar el mensaje.

**Ejemplo (con detalle leve):**

```
let persona = {
  nombre: "Sara",
  presentar: function() {
    console.log("Hola, me llamo " + nombre);
  }
};

persona.presentar();
```

> *Nota: aquí `nombre` debería hacer referencia a la propiedad del objeto; hay un pequeño problema que el estudiante puede corregir.*

**Pregunta #1:**
 ¿Cómo usarías `this` en el ejemplo para que funcione correctamente?

------

## Documento 25: `const` con arrays y objetos

**Instrucción:**
 Explica qué pasa cuando declaramos arrays u objetos con `const`.

**Contexto:**
 Creo que `const` significa “no cambia nunca”, pero veo que se pueden modificar arrays u objetos declarados con `const`.

**Entrada:**
 Te pediré ejemplos donde se modifique el contenido de un array y un objeto.

**Salida:**

1. Explicación de que `const` impide cambiar la referencia, no el contenido interno.
2. Ejemplo con array.
3. Ejemplo con objeto.
4. Una pregunta para comprobar la comprensión.

**Ejemplo:**

```
const numeros = [1, 2, 3];
numeros.push(4);

const persona = { nombre: "Ana" };
persona.edad = 20;

console.log(numeros);
console.log(persona);
```

**Pregunta #1:**
 ¿Por qué no es posible hacer `numeros = [10, 20];` si `numeros` fue declarado con `const`?

------

## Documento 26: Introducción al DOM (muy básica)

**Instrucción:**
 Explica cómo seleccionar un elemento del DOM usando `document.querySelector`.

**Contexto:**
 Estoy empezando a conectar JavaScript con HTML y quiero cambiar el texto de un párrafo.

**Entrada:**
 Te pediré un ejemplo donde se seleccione un elemento por su id.

**Salida:**

1. Explicación breve de qué es el DOM.
2. Ejemplo con `querySelector`.
3. Explicación de cada línea.
4. Una pregunta para seleccionar otro elemento.

**Ejemplo:**

```
let titulo = document.querySelector("#titulo");
titulo.textContent = "Nuevo título desde JavaScript";
```

**Pregunta #1:**
 ¿Cómo seleccionarías un elemento con la clase `.mensaje` usando `querySelector`?

------

## Documento 27: Manejo de eventos (`click`)

**Instrucción:**
 Enseña cómo escuchar un evento de `click` en un botón.

**Contexto:**
 Quiero que al hacer clic en un botón se muestre un mensaje en la consola.

**Entrada:**
 Te pediré un ejemplo sencillo con un botón identificado por id.

**Salida:**

1. Explicación de qué es un evento.
2. Ejemplo usando `addEventListener("click", ...)`.
3. Explicación del código.
4. Una pregunta para modificar el mensaje.

**Ejemplo:**

```
let boton = document.querySelector("#miBoton");

boton.addEventListener("click", function() {
  console.log("Hiciste clic en el botón");
});
```

**Pregunta #1:**
 ¿Qué tendrías que cambiar para que el mensaje diga `"Botón presionado"`?

------

## Documento 28: ¡Errorcito leve! `JSON.stringify` y `JSON.parse`

**Instrucción:**
 Explica cómo convertir un objeto a JSON y de JSON a objeto en JavaScript.

**Contexto:**
 Quiero guardar datos en formato de texto y luego recuperarlos.

**Entrada:**
 Te pediré ejemplos con un objeto `persona`.

**Salida:**

1. Explicación de `JSON.stringify`.
2. Explicación de `JSON.parse`.
3. Ejemplo completo de ida y vuelta.
4. Una pregunta para interpretar el resultado.

**Ejemplo (con un detalle pequeño):**

```
let persona = { nombre: "Ana", edad: 22 };

let texto = JSON.stringfy(persona);
let copia = JSON.parse(texto);

console.log(texto);
console.log(copia.nombre);
```

> *Nota: hay un error de escritura en uno de los métodos que el estudiante puede encontrar.*

**Pregunta #1:**
 ¿Qué corrección harías para que el código convierta bien el objeto a JSON?

------

## Documento 29: `setTimeout` básico

**Instrucción:**
 Enseña cómo retrasar la ejecución de una función usando `setTimeout`.

**Contexto:**
 Quiero mostrar un mensaje en la consola después de unos segundos.

**Entrada:**
 Te pediré un ejemplo con un retraso de 2 segundos.

**Salida:**

1. Explicación de qué hace `setTimeout`.
2. Ejemplo con una función anónima.
3. Explicación de los parámetros.
4. Una pregunta para cambiar el tiempo de espera.

**Ejemplo:**

```
setTimeout(function() {
  console.log("Han pasado 2 segundos");
}, 2000);
```

**Pregunta #1:**
 ¿Qué número usarías para esperar 5 segundos en lugar de 2?

------

## Documento 30: Repaso general de variables, condicionales y ciclos

**Instrucción:**
 Crea una actividad de repaso que combine variables, condicionales y ciclos.

**Contexto:**
 Ya he visto los temas básicos y quiero un mini ejercicio integrador.

**Entrada:**
 Te pediré un ejemplo donde se pida una cantidad fija (simulada) y se imprima si los números son pares o impares.

**Salida:**

1. Explicación breve del objetivo del ejercicio.
2. Ejemplo de código que:
   - Declare una variable con un número máximo.
   - Use un `for` para recorrer desde 1 hasta ese número.
   - Use un `if` para decidir si es par o impar.
3. Explicación del flujo.
4. Una pregunta para que el estudiante modifique el rango.

**Ejemplo:**

```
let maximo = 5;

for (let i = 1; i <= maximo; i++) {
  if (i % 2 === 0) {
    console.log(i + " es par");
  } else {
    console.log(i + " es impar");
  }
}
```

**Pregunta #1:**
 ¿Cómo cambiarías el valor de `maximo` para que el programa revise hasta el número 10?

