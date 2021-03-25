function ocultarDiv() {
    let div = document.getElementById("agregarDireccion");
    div.hide()
}

let div = document.querySelector('#agregarDireccion');
let botton = document.querySelector('#btnAgregarDireccion');
let botton1 = document.querySelector('#btnAgregarUna');
botton.onclick(div.show())
botton1.onclick(div.hide()