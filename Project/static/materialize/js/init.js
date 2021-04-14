(function ($) {
  $(function () {
    $('.modal').modal();
    $('.parallax').parallax();
    $('.sidenav').sidenav();
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space

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


function cargarFoto1() {
  var fileChooser = document.getElementById("txtFoto2");
  var foto = document.getElementById("imgFoto2");
  var base64 = document.getElementById("textarea");
  if (fileChooser.files.length > 0) {
      var fr = new FileReader();
      fr.onload = function() {
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
      fr.onload = function() {
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
  $("#imgFoto21").attr("src", "data:image/jpeg;base64,"+foto).width(380).height(380);
  $("#textareaModal").val(foto);



  $("#updateBtn").click(function() {
      swal({
          title: "¿Quieres actualizar el Recetario?",
          text: "No se podrá deshacer esta acción",
          icon: "warning",
          buttons: true,
          dangerMode: true,
      }).then((willDelete) => {
          if (willDelete) {} else {}
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
      } else {}
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
      } else {}
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
              var r=$('select[id="cmbRol1"] option:selected').val();
              if (r!=""){
                  var rol = r;
              }else{
                  var rol= $("#txtRol1").val();
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

// --------------------------- FIN FUNCIONES PROVEEDOR --------------------------