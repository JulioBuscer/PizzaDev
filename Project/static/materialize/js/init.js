(function ($) {
  $(function () {
    $('.modal').modal();
    $('.parallax').parallax();
    $('.sidenav').sidenav();
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space

$('#textarea').val();
M.textareaAutoResize($('#textarea'));

document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.datepicker');
  var options = {}
  var instances = M.Datepicker.init(elems, options);
});

// Or with jQuery

$(document).ready(function () {
  $('.datepicker').datepicker();
});

document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('select');
  var options = {}
  var instances = M.FormSelect.init(elems, options);
});

// Or with jQuery

$(document).ready(function () {
  $('select').formSelect();
});

document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.dropdown-trigger');
  var options = {}
  var instances = M.Dropdown.init(elems, options);
});

//  ---------------------- MATERIA PRIMA -----------------------------

document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.modal');
  var options = {}
  var instances = M.modal.init(elems, options);
});

$(document).ready(function () {
  $('ul.tabs').tabs();
});

function modalMatPrim(idMateriaPrima, nombre, descripcion, categoria, precio, cantidad, proveedor_empresa, unidad) {
  $('#idMateriaPrima1').val(idMateriaPrima);
  $('#nombreMateria').val(nombre);
  $('#descMatPrim').val(descripcion);
  $('#categoria1').val(categoria);
  $('#precio1').val(precio);
  $('#cantidadMat').val(cantidad);
  $('#unidadMat').val(unidad);

  $("#updateBtn").click(function () {
    swal({
      title: "¿Quieres actualizar el producto?",
      text: "No se podrá deshacer esta acción",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then((willDelete) => {
      if (willDelete) {
        idMateriaPrimas = $('#idMateriaPrima1').val();
        nombres = $('#nombreMateria').val();
        descripcions = $('#descMatPrim').val();
        categorias = $('#categoria1').val();
        precios = $('#precio1').val();
        cantidads = $('#cantidadMat').val();
        unidads = $('#unidadM').val();
        proveedor_empresas = $('#proveedorMat').val();
        window.location.href = 'updateMatPrim?id=' + idMateriaPrimas + '&name=' + nombres
          + '&descripcion=' + descripcions + '&categoria=' + categorias + '&precio=' + precios + '&cantidad='
          + cantidads + '&unidad=' + unidads + '&proveedor_empresa=' + proveedor_empresas;
      } else {
      }
    });
  });
}

var confirmarEliminacionMatPrim = (idMateriaPrima, nombre, descripcion, categoria, precio, cantidad, proveedor_empresa, unidad) => {
  swal({
    title: "¿Quieres borrar " + nombre + " de la materia prima? ",
    text: "No se podrá deshacer esta acción",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      swal("Eliminada con éxito", {
        icon: "success",
      });
      window.location.href = 'deleteMatPrim?id=' + idMateriaPrima + '&name=' + nombre
        + '&descripcion=' + descripcion + '&categoria=' + categoria + '&precio=' + precio + '&cantidad='
        + cantidad + '&unidad=' + unidad + '&proveedor_empresa=' + proveedor_empresa;
    } else {
    }
  });
};
var confirmarActivacionMatPri = (idMateriaPrima, nombre, descripcion, categoria, precio, cantidad, proveedor_empresa, unidad) => {
  swal({
    title: "¿Quieres activar la materia prima " + nombre + "?",
    text: "No se podrá deshacer esta acción",
    icon: "info",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      swal("Activado con éxito", {
        icon: "success",
      });
      window.location.href = 'updateMatPrim?id=' + idMateriaPrima + '&name=' + nombre
        + '&descripcion=' + descripcion + '&categoria=' + categoria + '&precio=' + precio + '&cantidad='
        + cantidad + '&unidad=' + unidad + '&proveedor_empresa=' + proveedor_empresa;
    } else {
    }
  });
};

var confirmarInsercionMatPri = () => {

  swal({
    title: "¿Quieres activar la materia prima " + $('#nombreMateria1').val() + "?",
    text: "No se podrá deshacer esta acción",
    icon: "info",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      nombre = $('#nombreMateria1').val();
      descripcion = $('#descMatPrim1').val();
      categoria = $('#categoria11').val();
      precio = $('#precio11').val();
      cantidad = $('#cantidadMat1').val();
      unidad = $('#unidadM1').val();
      proveedor_empresa = $('#proveedorMat1').val();
      swal("Activado con éxito", {
        icon: "success",
      });
      window.location.href = 'insertMatPrim?name=' + nombre
        + '&descripcion=' + descripcion + '&categoria=' + categoria + '&precio=' + precio + '&cantidad='
        + cantidad + '&unidad=' + unidad + '&proveedor_empresa=' + proveedor_empresa;
    } else {
    }
  });
};

// ---------------------- FIN MAT PRIMA ------------------------------
function cargarFotoUsuario() {
  var fileChooser = document.getElementById("txtFoto");
  var foto = document.getElementById("imgFoto2");
  var base64 = document.getElementById("textarea");
  if (fileChooser.files.length > 0) {
    var fr = new FileReader();
    fr.onload = function () {
      foto.src = fr.result;
      base64.value = foto.src.replace(/^data:image\/(png|jpg|jpeg|gif);base64,/, '');
    }
    fr.readAsDataURL(fileChooser.files[0]);
  }
}

function cargarFoto1() {
  var fileChooser = document.getElementById("txtFoto2");
  var foto = document.getElementById("imgFoto2");
  var base64 = document.getElementById("textarea");
  if (fileChooser.files.length > 0) {
    var fr = new FileReader();
    fr.onload = function () {
      foto.src = fr.result;
      base64.value = foto.src.replace(/^data:image\/(png|jpg|jpeg|gif);base64,/, '');
    }
    fr.readAsDataURL(fileChooser.files[0]);
  }
}

function cargarFoto11() {
  var fileChooser = document.getElementById("txtFoto21");
  var foto = document.getElementById("imgFoto21");
  var base64 = document.getElementById("textareaModal");
  if (fileChooser.files.length > 0) {
    var fr = new FileReader();
    fr.onload = function () {
      foto.src = fr.result;
      base64.value = foto.src.replace(/^data:image\/(png|jpg|jpeg|gif);base64,/, '');
    }
    fr.readAsDataURL(fileChooser.files[0]);
  }
}


function modalRecetario(idRecetario, nombre, descripcion, costo, foto) {
  $("#idRecetario").val(idRecetario);
  $("#nombre").val(nombre);
  $("#desc").val(descripcion);
  $("#costo").val(costo);
  $("#imgFoto21").attr("src", "data:image/jpeg;base64," + foto).width(380).height(380);
  $("#textareaModal").val(foto);



  $("#updateBtn").click(function () {
    swal({
      title: "¿Quieres actualizar el Recetario?",
      text: "No se podrá deshacer esta acción",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then((willDelete) => {
      if (willDelete) { } else { }
    });
    $(".modal").removeClass("is-active");
  });
}
var confirmarEliminacionRecetario = (idRecetario, nombre) => {
  swal({
    title: "¿Quieres borrar " + nombre + " de la materia prima? ",
    text: "No se podrá deshacer esta acción ",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      swal("Eliminada con éxito ", {
        icon: "success",
      });
      window.location.href = 'desactivarPizza?id=' + idRecetario;
    } else { }
  });
};
var confirmarActivacionRecetario = (idRecetario, nombre) => {
  swal({
    title: "¿Quieres activar la materia prima " + nombre + "? ",
    text: "No se podrá deshacer esta acción ",
    icon: "info",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      swal("Activado con éxito ", {
        icon: "success",
      });
      window.location.href = 'activarPizza?id=' + idRecetario;
    } else { }
  });
};

// ---------------------- FIN FUNCIONES RECETARIO ------------------------

// ---------------------- FUNCIONES USUARIO ADMIN ------------------------

function modalUsuario(id, name, email, password, rol) {
  $("#id1").val(id);
  $("#txtNombre1").val(name);
  $("#txtCorreo1").val(email);
  $("#txtRol1").val(rol);

  $("#updateBtn").click(function () {
    swal({
      title: "¿Quieres actualizar al usuario?",
      text: "No se podrá deshacer esta acción",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then((willDelete) => {
      if (willDelete) {
        var id = $("#id1").val();
        console.log(id)
        var email = $("#txtCorreo1").val();
        var password = $("#txtContraseña1").val();
        var name = $("#txtNombre1").val();
        var r = $('select[id="cmbRol1"] option:selected').val();
        if (r != "") {
          var rol = r;
        } else {
          var rol = $("#txtRol1").val();
        }
        console.log(rol);
        window.location.href = 'modificarUsuario?id1=' + id + '&' + 'txtCorreo1=' + email + '&' + 'txtContraseña1=' + password + '&' + 'txtNombre1=' + name + '&' + 'cmbRol1=' + rol;
      } else {
      }
    });
    $(".modal").removeClass("is-active");
  });
}

var confirmarEliminacionUsuario = (id, name) => {
  swal({
    title: "¿Quieres borrar al usuario " + name + " ? ",
    text: "No se podrá deshacer esta acción",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      swal("Eliminada con éxito", {
        icon: "success",
      });
      window.location.href = 'eliminarUsuario?id=' + id;
    } else {
    }
  });
};
var confirmarActivacionUsuario = (id, name) => {
  swal({
    title: "¿Quieres activar al usuario " + name + "?",
    text: "No se podrá deshacer esta acción",
    icon: "info",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      swal("Activado con éxito", {
        icon: "success",
      });
      window.location.href = 'activarrUsuario?id=' + id;
    } else {
    }
  });
};

// -------------------- FIN FUNCIONES USUARIO ADMIN ---------------------------

// -------------------- FUNCIONES PROVEEDOR -----------------------------------


function modalProveedor(idProveedor, empresa, direccionPro, email, representante, telefono) {
  $("#idProveedor1").val(idProveedor);
  $("#txtEmpresa1").val(empresa);
  $("#txtDirección1").val(direccionPro);
  $("#txtEmail1").val(email);
  $("#txtTelefono1").val(telefono);
  $("#txtRepresentante1").val(representante);


  $("#updateBtn").click(function () {
    swal({
      title: "¿Quieres actualizar el proveedor?",
      text: "No se podrá deshacer esta acción",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then((willDelete) => {
      if (willDelete) {
        var idProveedor = $("#idProveedor1").val();
        var empresa = $("#txtEmpresa1").val();
        var direccionPro = $("#txtDirección1").val();
        var email = $("#txtEmail1").val();
        var telefono = $("#txtTelefono1").val();
        var representante = $("#txtRepresentante1").val();
        window.location.href = 'modificarProveedor?idProveedor1=' + idProveedor + '&' + 'txtEmpresa1=' + empresa + '&' + 'txtDirección1=' + direccionPro + '&' + 'txtEmail1=' + email + '&' + 'txtTelefono1=' + telefono + '&' + 'txtRepresentante1=' + representante;
      } else {
      }
    });
    $(".modal").removeClass("is-active");
  });
}

var confirmarEliminacionProveedor = (idProveedor, empresa) => {
  swal({
    title: "¿Quieres borrar " + empresa + " del proveedor? ",
    text: "No se podrá deshacer esta acción",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      swal("Eliminada con éxito", {
        icon: "success",
      });
      window.location.href = 'eliminarProveedor?idProveedor=' + idProveedor;
    } else {
    }
  });
};
var confirmarActivacionProveedor = (idProveedor, empresa) => {
  swal({
    title: "¿Quieres activar al proveedor " + empresa + "?",
    text: "No se podrá deshacer esta acción",
    icon: "info",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      swal("Activado con éxito", {
        icon: "success",
      });
      window.location.href = 'activarrProveedor?idProveedor=' + idProveedor;
    } else {
    }
  });
};

// --------------------------- FIN FUNCIONES PROVEEDOR ------------------------------

// --------------------------- FUNCIONES PERFIL, ETC --------------------------------
function doSearch() {
  const tableReg = document.getElementById('datos');
  const searchText = document.getElementById('searchTerm').value.toLowerCase();
  let total = 0;

  // Recorremos todas las filas con contenido de la tabla
  for (let i = 1; i < tableReg.rows.length; i++) {
    // Si el td tiene la clase "noSearch" no se busca en su cntenido
    if (tableReg.rows[i].classList.contains("noSearch")) {
      continue;
    }

    let found = false;
    const cellsOfRow = tableReg.rows[i].getElementsByTagName('td');
    // Recorremos todas las celdas
    for (let j = 0; j < cellsOfRow.length && !found; j++) {
      const compareWith = cellsOfRow[j].innerHTML.toLowerCase();
      // Buscamos el texto en el contenido de la celda
      if (searchText.length == 0 || compareWith.indexOf(searchText) > -1) {
        found = true;
        total++;
      }
    }
    if (found) {
      tableReg.rows[i].style.display = '';
    } else {
      // si no ha encontrado ninguna coincidencia, esconde la
      // fila de la tabla
      tableReg.rows[i].style.display = 'none';
    }
  }

  // mostramos las coincidencias
  const lastTR = tableReg.rows[tableReg.rows.length - 1];
  const td = lastTR.querySelector("td");
  lastTR.classList.remove("hide", "red");
  if (searchText == "") {
    lastTR.classList.add("hide");
  } else if (total) {
    td.innerHTML = "Se ha encontrado " + total + " coincidencia" + ((total > 1) ? "s" : "");
  } else {
    lastTR.classList.add("orange");
    td.innerHTML = "No se han encontrado coincidencias";
  }
}

var confirmarEliminacionPerfil = (idDireccion) => {
  swal({
    title: "¿Quieres borrar esta dirección?",
    text: "No se podrá deshacer esta acción",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      swal("Eliminada con éxito", {
        icon: "success",
      });
      window.location.href = 'eliminarDireccion?id=' + idDireccion;
    } else {
    }
  });
};

function modalPerfil(idDireccion, calle, colonia, numeroInt, numeroExt, cp, descripcion) {
  $("#txtCalle_").val(calle);
  $("#txtColonia_").val(colonia);
  $("#txtDescripcion_").val(descripcion);
  $("#txtNumInt_").val(numeroInt);
  $("#txtNumExt_").val(numeroExt);
  $("#txtCP_").val(cp);

  $("#updateBtn").click(function () {
    swal({
      title: "¿Quieres actualizar esta dirección?",
      text: "No se podrá deshacer esta acción",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then((willDelete) => {
      if (willDelete) {
        window.location.href = 'modificarDirección?id=' + idDireccion + '&calle=' + $("#txtCalle_").val()
          + '&colonia=' + $("#txtColonia_").val() + '&numeroInt=' + $("#txtNumInt_").val() + '&numeroExt=' + $("#txtNumExt_").val() + '&cp='
          + $("#txtCP_").val() + '&descripcion=' + $("#txtDescripcion_").val();
      } else {
      }
    });
  });
}

var img64 = null;
var elemento = document.createElement("iframe");
function base64(element) {
  var file = element.files[0];
  var reader = new FileReader();
  reader.onloadend = function () {
    img64 = reader.result;
    $("#textarea").val(img64);
  }
  reader.readAsDataURL(file);
}

function ponerValor() {
  img = $("#txtCalle_").val();
  $("#textarea").val(img);
}

// ---------------------------------- CARRITO -----------------------------
let listadoC = []

function carrito(idRecetario, nombre, descripcion, cantidad, precio) {

  var carritos = {
    idRecetario: idRecetario,
    nombre: nombre,
    descripcion: descripcion,
    cantidad: 1,
    precio: precio
  }
  listadoC.push(carritos)
  tamanio = listadoC.length;
  $('#txtTamnanio').html(tamanio);
  console.log(listadoC)
  var toastHTML = '<span>Agregado al carrito éxitosamente</span>';
  M.toast({ html: toastHTML });

  for (var i = 0; i <= listadoC.length; i++) {
    if (idRecetario == listadoC[i].idRecetario) {
      $('#btnCarritos' + idRecetario).hide()
      var desactivado = "Ya está en el carrito";
      $('#txtCarrito' + idRecetario).html(desactivado);
    }
  }
}

function detalleCarrito() {
  var str = '';
  var costoTotal = 0.0;
  var costoTotalProductos = 0.0;
  var cantidadSubt = 0;
  var cantidadTotal = 0;
  for (var i = 0; i < listadoC.length; i++) {
    var subtotal = (listadoC[i].cantidad * listadoC[i].precio);
    var subQ = 0
    subQ = subQ + listadoC[i].cantidad;
    console.log(subtotal)
    str += '<tr>' +
      '<td>' + listadoC[i].nombre + '</td>' +
      '<td>' + listadoC[i].descripcion + '</td>' +
      '<td>' + '<a href="#" class="waves-effect waves-light blue btn"\n\
      onclick="disminuirQ('  + i + ');">\n\
      <i class="material-icons">remove</i></a>' + '<a href="#" class="black-text grey lighten-2 btn"\n\
      ">'+ listadoC[i].cantidad + '</a>' + '<a href="#" class="waves-effect waves-light green btn"\n\
      onclick="aumentarQ('  + i + ');">\n\
      <i class="material-icons">add</i></a>' + '</td>' +
      '<td>' + subtotal + '</td>' +
      '<td><a href="#" class="waves-effect waves-light red btn"\n\
              onclick="removeItemFromArr('  + i + ');">\n\
              <i class="material-icons">delete</i></a>' + '</td></tr>';

    costoTotalProductos += subtotal;
    cantidadSubt += subQ;
  }
  costoTotal = "Total: $" + costoTotalProductos;
  cantidadTotal = cantidadSubt;
  $('#tbCarrito').html(str);
  $('#txtCantidad').val(cantidadTotal);
  $('#txtTotal').html(costoTotal);
  $('#txtTotalInput').val(costoTotalProductos);
}


function removeItemFromArr(item) {
  listadoC.splice(item, 1);
  var toastHTML = '<span>Removido del carrito</span>';
  M.toast({ html: toastHTML });
  tamanio = listadoC.length;
  $('#txtTamnanio').html(tamanio);
  detalleCarrito();
}

function disminuirQ(item) {
  if (listadoC[item].cantidad == 1) {
    var toastHTML = '<span>No puedes agregar cantidades negativas</span>';
    M.toast({ html: toastHTML });
  } else if (listadoC[item].cantidad == 0) {
    listadoC.splice(item, 1);
    var toastHTML = '<span>Removido del carrito</span>';
    M.toast({ html: toastHTML });
    detalleCarrito();
  } else {
    listadoC[item].cantidad = listadoC[item].cantidad - 1
    detalleCarrito();
  }

}

function aumentarQ(item) {
  listadoC[item].cantidad = listadoC[item].cantidad + 1
  detalleCarrito();
}

function enviarCarrito() {
  $("#updateBtnCarrito").click(function () {
    swal({
      title: "¿Seguro que deseas terminar tu compra?",
      text: "No se podrá deshacer esta acción",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then((willDelete) => {
      if (willDelete) {
        $.ajax({
          type: 'POST',
          url: 'http://localhost:5000/venta',
          dataType: "json",
          data: {
            'pizzas': JSON.stringify({ pizzas: listadoC }),
            'cantidad': $('#txtCantidad').val(),
            'total': $('#txtTotalInput').val(),
            'descripcion': $('#textareaDescripcion').val(),
            'direccion': $('#direccionVenta').val() // <-- the $ sign in the parameter name seems unusual, I would avoid it
          }

        });

        window.location.href = "/menu";
        var toastHTML23 = '<span class="white-text"> Venta terminada, consulta tus pedidos' + '</span><button class="btn-flat toast-action" href="{{ url_for("main.pedidos") }}">Pedidos</button>';
        var inDuration = 100;
        M.toast({ html: toastHTML23, inDuration });

      } else {
      }
    });
  });
}


// --------------------------- NORMALIZACION ----------------------------------


function checkDomicilio(e) {
  tecla = (document.all) ? e.keyCode : e.which;

  //Tecla de retroceso para borrar, siempre la permite
  if (tecla == 8) {
    return true;
  }

  // Patron de entrada, en este caso solo acepta numeros y letras
  patron = /[A-Za-z#.0-9 ]/;
  tecla_final = String.fromCharCode(tecla);
  return patron.test(tecla_final);
}

function checkNumeros(e) {
  tecla = (document.all) ? e.keyCode : e.which;

  //Tecla de retroceso para borrar, siempre la permite
  if (tecla == 8) {
    return true;
  }

  // Patron de entrada, en este caso solo acepta numeros y letras
  patron = /[0-9.]/;
  tecla_final = String.fromCodePoint(tecla);
  return patron.test(tecla_final);
}

function checkEmail(e) {
  // esta variable sería la tecla que voy haciendo

  tecla = (document.all) ? e.keyCode : e.which;

  //Tecla de retroceso para borrar, siempre la permite, permitimos la tecla de borrar por si se equivoca
  if (tecla == 8) {
    return true;
  }

  // Patron de entrada, en este caso solo acepta numeros y letras, sólo lo que se va a admitir en el teclado
  patron = /[A-Za-z@.]/;
  tecla_final = String.fromCharCode(tecla);
  //y se obtiene la tecla final que esta permitida en el patrón


  //ELIMINÓ LOS CARACTERES ESPCIALES EVITANDO ASÍ UNA "INYECCIÓN" DE CÓDIGO
  return patron.test(tecla_final);
}

function checkTelefono(e) {
  // esta variable sería la tecla que voy haciendo

  tecla = (document.all) ? e.keyCode : e.which;

  //Tecla de retroceso para borrar, siempre la permite, permitimos la tecla de borrar por si se equivoca
  if (tecla == 8) {
    return true;
  }

  // Patron de entrada, en este caso solo acepta numeros y letras, sólo lo que se va a admitir en el teclado
  patron = /[0-9-+()]/;
  tecla_final = String.fromCharCode(tecla);
  //y se obtiene la tecla final que esta permitida en el patrón


  //ELIMINÓ LOS CARACTERES ESPCIALES EVITANDO ASÍ UNA "INYECCIÓN" DE CÓDIGO
  return patron.test(tecla_final);
}

function check(e) {
  // esta variable sería la tecla que voy haciendo

  tecla = (document.all) ? e.keyCode : e.which;

  //Tecla de retroceso para borrar, siempre la permite, permitimos la tecla de borrar por si se equivoca
  if (tecla == 8) {
    return true;
  }

  // Patron de entrada, en este caso solo acepta numeros y letras, sólo lo que se va a admitir en el teclado
  patron = /[A-Za-z ]/;
  tecla_final = String.fromCharCode(tecla);
  //y se obtiene la tecla final que esta permitida en el patrón


  //ELIMINÓ LOS CARACTERES ESPCIALES EVITANDO ASÍ UNA "INYECCIÓN" DE CÓDIGO
  return patron.test(tecla_final);
}
