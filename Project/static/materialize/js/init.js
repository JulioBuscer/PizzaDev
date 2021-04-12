(function($){
  $(function(){
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

// ---------------------- FIN MAT PRIMA ------------------------------