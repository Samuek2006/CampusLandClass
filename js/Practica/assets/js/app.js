window.calculaIMC = async function calculaIMC() {
    const { value: formValues } = await Swal.fire({
        title: "Calcular IMC",
        html: `
        <div style="text-align:left">
            <label for="swal-input-nombre">Nombre</label>
            <input id="swal-input-nombre" class="swal2-input" placeholder="Ej: Ana Pérez" />
            <label for="swal-input-edad">Edad (años)</label>
            <input id="swal-input-edad" type="number" min="0" class="swal2-input" placeholder="Ej: 30" />
            <label for="swal-input-estatura">Estatura (m)</label>
            <input id="swal-input-estatura" type="number" step="0.01" min="0.3" class="swal2-input" placeholder="Ej: 1.70" />
            <label for="swal-input-peso">Peso (kg)</label>
            <input id="swal-input-peso" type="number" step="0.1" min="1" class="swal2-input" placeholder="Ej: 68.5" />
        </div>
    `,
        focusConfirm: false,
        showCancelButton: true,
        confirmButtonText: "Calcular",
        cancelButtonText: "Cancelar",
        preConfirm: () => {
            const nombre = document.getElementById("swal-input-nombre").value.trim();
            const edadStr = document.getElementById("swal-input-edad").value.trim();
            const estaturaStr = document.getElementById("swal-input-estatura").value.trim();
            const pesoStr = document.getElementById("swal-input-peso").value.trim();

            const edad = Number(edadStr);
            const estatura = Number(estaturaStr);
            const peso = Number(pesoStr);

            if (!nombre) {
                Swal.showValidationMessage("Por favor ingresa el nombre.");
                return;
            }
            if (!Number.isFinite(edad) || edad < 0) {
                Swal.showValidationMessage("Ingresa una edad válida (0 o mayor).");
                return;
            }
            if (!Number.isFinite(estatura) || estatura <= 0) {
                Swal.showValidationMessage("Ingresa una estatura válida en metros (ej: 1.70).");
                return;
            }
            if (!Number.isFinite(peso) || peso <= 0) {
                Swal.showValidationMessage("Ingresa un peso válido en kg (ej: 68.5).");
                return;
            }

            return { nombre, edad, estatura, peso };
        },
        didOpen: () => {
            const nombreEl = document.getElementById("swal-input-nombre");
            if (nombreEl) nombreEl.focus();
        },
    });

    if (!formValues) return; // Cancelado

    const { nombre, edad, estatura, peso } = formValues;
    const imc = peso / (estatura * estatura);

    // Clasificación básica del IMC
    let categoria = "";
    if (imc < 18.5) categoria = "Bajo peso";
    else if (imc < 25) categoria = "Normal";
    else if (imc < 30) categoria = "Sobrepeso";
    else categoria = "Obesidad";

    // Actualizar el valor en el HTML
    const imcSpan = document.getElementById("calculo-IMC");
    if (imcSpan) imcSpan.innerText = imc.toFixed(2);

    await Swal.fire({
        icon: "info",
        title: "Resultado IMC",
        html: `
        <p><strong>Nombre:</strong> ${nombre}</p>
        <p><strong>Edad:</strong> ${edad} años</p>
        <p><strong>IMC:</strong> ${imc.toFixed(2)} (${categoria})</p>
    `,
        confirmButtonText: "Aceptar",
    });
};
