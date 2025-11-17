class HelloWorld extends HTMLElement {
    constructor() {
        super(); // Siempre llamar a super()

        // Creamos Shadow DOM en modo "open" (se puede acceder con JS)
        const shadow = this.attachShadow({ mode: 'open' });

        // Crear contenido del componente
        const wrapper = document.createElement('div');
        wrapper.textContent = 'Hola, Johlver 👋';

        // Agregar estilo aislado
        const style = document.createElement('style');
        style.textContent = `
        div {
            padding: 10px;
            background: #f0f0f0;
            color: #333;
            font-weight: bold;
            border-radius: 8px;
            font-family: sans-serif;
        }
        `;

        // Añadir estilo y contenido al Shadow DOM
        shadow.appendChild(style);
        shadow.appendChild(wrapper);
    }
}

// Registrar el componente personalizado
customElements.define('hello-world', HelloWorld);