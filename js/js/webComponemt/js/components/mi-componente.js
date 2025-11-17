class MiComponente extends HTMLElement {
    constructor() {
        super();
        // Creamos el shadow DOM
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = `
        <style>
            p { color: blue; }
        </style>
        <p>Hola, soy un componente personalizado</p>
        `;
    }

    // Se ejecuta cuando el componente se agrega al DOM
    connectedCallback() {
        console.log('MiComponente fue agregado al DOM.');
        // Puedes inicializar datos, eventos, etc.
        this.shadowRoot.querySelector('p').textContent += ' (Ahora estoy conectado)';
    }

    // Opcional: Limpia eventos o recursos si se elimina del DOM
    disconnectedCallback() {
        console.log('MiComponente fue eliminado del DOM.');
    }
}

// Definir el elemento personalizado
customElements.define('mi-componente', MiComponente);

// Usar el componente en el DOM
document.body.innerHTML = `<mi-componente></mi-componente>`;