$(document).ready(function() {
  // jQuery code to be added in here.
  // $("#submit-yellow-btn").click( function(event) {
  //         alert("You clicked the button using JQuery!");
  // });

  $(document).on('submit', '#form1', function(e) {
    // Prevent the page from getting refreshed
    e.preventDefault();

    $.ajax({
      type: 'POST',
      url: '/articulo/'+$('form')+'/guarda/',
      data: {
        codigo:$('#codigo').val(),
        descripcion:$('#descripcion').val(),
        tarifa1:$('#tarifa1').val(),
        csrfmiddlewaretoken:$('input[name=csfrmiddlewaretoken]').val()
      },
      success:function(){
        alert('Updated Articulo');
      }
    })
  })

});
