let str = "123";
console.log(typeof str);
let num = Number(str);
console.log(typeof num);
console.log(`The value of str is: ${str}`);

let age = prompt("Ingresa tu edad");
console.log(`Tienes ${age} años`);

let confirmacion = confirm('Deseas confirmar')
if (confirmacion){
    console.log('Confirmacion Exitosa')
} else {
    console.log('Abortada')
}