// Array para almacenar los nombres de amigos
let listaDeAmigos = [];

// Elementos del DOM
const listaVisual = document.getElementById("listaAmigos");
const inputAmigo = document.getElementById("amigo");
const resultadoSorteo = document.getElementById("resultado");

// Función para formatear un nombre (primera letra mayúscula, resto minúsculas)
function formatearNombre(nombre) {
    return nombre.charAt(0).toUpperCase() + nombre.slice(1).toLowerCase();
}

// Función para agregar un amigo a la lista
function agregarAmigo() {
    let nombre = inputAmigo.value.trim(); // Eliminar espacios innecesarios

    if (nombre) {
        nombre = formatearNombre(nombre);

        listaDeAmigos.push(nombre);
        actualizarLista();
        limpiarInput();
    } else {
        alert("Por favor, ingrese un nombre válido.");
    }
}

// Función para actualizar la lista en la interfaz
function actualizarLista() {
    listaVisual.innerHTML = ""; // Limpiar lista antes de actualizar

    listaDeAmigos.forEach((amigo, index) => {
        let elemento = document.createElement("li");
        elemento.textContent = `${index + 1}. ${amigo}`; // Agregar numeración a la lista
        listaVisual.appendChild(elemento);
    });
}

// Función para realizar el sorteo de un amigo aleatorio
function sortearAmigo() {
    if (listaDeAmigos.length === 0) {
        alert("No hay amigos en la lista para sortear.");
        return;
    }

    let seleccionado = listaDeAmigos[Math.floor(Math.random() * listaDeAmigos.length)];
    resultadoSorteo.textContent = `Tu amigo secreto es: ${seleccionado} `;
}

// Función para limpiar el campo de entrada
function limpiarInput() {
    inputAmigo.value = "";
}
