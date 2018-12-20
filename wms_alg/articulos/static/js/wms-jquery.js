$(document).ready(function() {
  // jQuery code to be added in here.
  $(form).on('submit', function(e) {
    // Prevent the page from getting refreshed
    e.preventDefault();

    $.ajax({
      type: 'POST',
      url: '/articulos/guarda/',
      data: {
        codigo:$('#codigo').val(),
        descripcion:$('#descripcion').val(),
        tarifa1:$('#tarifa1').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
      },
      success:function(){
        alert('Actualizado !');
      },
      error: function (ajaxContext) {
        alert(ajaxContext.responseText)
      }
    })
  })

});
