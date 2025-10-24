const miobjeto = {
    nombre: "Ejemplo Objeto",
    version: 1.0,
    descripcion: "Un objeto de ejemplo con una función",
    mostrarInformacion: function (p1, p2) {
        console.log("Nombre: " + this.nombre);
        console.log("Version: " + this.version);
        console.log("Descripción: " + this.descripcion);
        console.log("Parámetro 1: " + p1);
        console.log("Parámetro 2: " + p2);
    }
};

// Llamada a la función dentro del objeto
miobjeto.mostrarInformacion("Valor 1", "Valor 2");