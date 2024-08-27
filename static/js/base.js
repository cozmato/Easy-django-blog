    $( function() {
    var availableTags = [
        '{% url 'search' %}'
    ];

$(document).ready(function() {
      $( "#q").autocomplete({
           source:"{% url 'search' %}",
           select: function(event,ui){
                   GetRedirectPage(ui.item.label,ui.item.value);
            }
       });
    });

    function GetRedirectPage(label, slug) {
          window.location.href = "/search?q="+slug;
    }

} );

                $(document).on('submit', '.form', function(event) {
          event.preventDefault();
          $.ajax({ // create an AJAX call...
              data: $(this).serialize(), // get the form data
              type: $(this).attr('method'), // GET or POST
              url: $(this).attr('action'), // the file to call
              success: function(data) {
                  if (data.msg === 'good'){
                      form.reset()
                      $('#moe').load(" #moe "); // update the DIV
                }
              }
          });
          return false;
        });



    $(document).ready(function (){
        setInterval(function () {
            $("#mmm").load(" #mmm > * ");
            $("#ccc").load(" #ccc ");
            $("#me").load(" #me ");
            $(".sho").load(" .sho ");
        }, 5000)
    })



 var mmm = document.getElementById('mmm')
  var se = document.getElementById('se')
 var he = document.getElementById('he')

  if (window.innerWidth < 601 ){
    se.addEventListener('input', () => {
        he.style.backgroundColor = 'none'
        mmm.style.display = 'none'
    })

    se.addEventListener('focusout', () => {
        he.style.backgroundColor = 'none'
        mmm.style.display = 'flex'
    })
  }

