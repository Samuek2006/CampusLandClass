function cambiarUno() {
    const primerMensaje = document.querySelector(".mensaje");
    primerMensaje.textContent = "Texto cambiado solo en el primero";
}

function enumerarTodos() {
    const items = document.querySelectorAll(".item");
    items.forEach((item, index) => {
        item.textContent = '${index + 1}. ${ item.textContent }';
    });
}

const boton = document.querySelector('#boton-importante');
const botond = document.querySelector('#boton-demo');

boton.addEventListener('click', () => {
    boton.textContent = '¡Aplicado!';
    boton.classList.add('aplicado');
    boton.disabled = true;           // deshabilita interacciones
}, { once: true });                 // se ejecuta una sola vez

botond.addEventListener('click', function () {
    botond.textContent = '¡Aplicado!'
    botond.style.backgroundColor = '#df0fd4ff'
    botond.style.color = 'white'
    botond.style.border = 'none'
    botond.style.cursor = 'not-allowed'
})