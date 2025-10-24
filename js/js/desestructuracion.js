// Objeto
const persona = { nombre: 'Juan', edad: 25, ciudad: 'Madrid' };

// Destructuración de objetos
const { nombre, edad, ciudad } = persona;

// Uso de las variables extraídas
console.log(nombre); // 'Juan'
console.log(edad);
console.log(ciudad); // 'Madrid'

const persona2 = { nombre: 'Juan', edad: 25, ciudad: 'Madrid', pais: 'España' };

// Rest en la destructuración para recoger el resto de propiedades en un objeto
const { nombre2, ... resto } = persona;
console.log(resto);
console.log(nombre);