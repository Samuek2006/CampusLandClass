const promesa = new Promise((resolve, reject) => {
    const exito = true; // Cambia a false para simular un error
    if (exito) {
        resolve("La operación fue exitosa");
    } else {
        reject("Hubo un error en la operación");
    }
});

promesa
    .then((resultado) => {
        console.log(resultado); // "La operación fue exitosa"
    })
    .catch((error) => {
        console.error(error); // "Hubo un error en la operación"
    });