autoResizeTextarea(document.querySelectorAll("textarea.form-control"), {maxHeight: 100})


function bot(){
    $('#message').animate({scrollTop:$('#message')[0].scrollHeight}, 3);
}

document.addEventListener("DOMContentLoaded", function() {

});



setInterval(function(){
    var h1 = $('#message')[0].scrollHeight;
    var t = $('#message').scrollTop();
    var h2 = $('#message').height();
    var offset = h1*0.075;
    if(h1-t-offset<h2){
        $('#bottom-button').hide();
    }
    else{
        $('#bottom-button').show();
    }
}, 100);


   function inni(){
       var body = document.getElementById("body")
       var file = document.getElementById("file")
       document.getElementById('send-btn').style.display = "block";
       document.getElementById('bi-send').style.display = "none";
       if (file.files.length == 0 && body.value.length == 0){
           document.getElementById("jjj").style.disabled = true;
           document.getElementById('send-btn').style.display = "none";
           document.getElementById('bi-send').style.display = "block";
           body.style.borderRadius = "10px";
           $('#message').animate({scrollTop:$('#message')[0].scrollHeight}, 3);

       }
   }


    function previewFile(input){
    $('.msg_card').animate({scrollTop:$('.msg_card')[0].scrollHeight}, 3000);
    document.getElementById("jjj").style.display = "block";
    document.getElementById('message').style.display = "none";
    document.getElementById('head').style.display = "none";
    document.getElementById('previewImg').style.display = "block";
    document.getElementById('pre').style.display = "flex";
    document.getElementById('jo').style.display = "flex";
    document.getElementById('bi-send').style.display = "none";

        var file = $("input[type=file]").get(0).files[0];

        if(file){
            var reader = new FileReader();

            reader.onload = function(){
                $("#previewImg").attr("src", reader.result);
            }
            reader.readAsDataURL(file);
        }
    }


   // async javascript request
    const progressBarFill = document.querySelector('#progressBar > .progress-bar-fill');
    const progressBarText = progressBarFill.querySelector('.progress-bar-text');
    const msgForm = document.getElementById("chatform")

    msgForm.addEventListener("submit", (event)=>{
        event.preventDefault()
        const targetData = event.target
        const formData = new FormData(targetData)
        const xhr = new XMLHttpRequest() // fetch
        const endpoint = msgForm.getAttribute("action")
        const method = msgForm.getAttribute("method")
        xhr.open(method, endpoint)
        //
        xhr.upload.addEventListener('progress', e => {
            const percent = e.lengthComputable ? (e.loaded / e.total) * 100: 0;

            progressBarFill.style.width = percent.toFixed(2) + "%";
            progressBarText.textContent = percent.toFixed(2) + "%";
        });
        xhr.responseType = 'json'
        xhr.dataType: "json",
        xhr.contentType: "text/xml",
        xhr.processData: false,
        xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
        xhr.onload = () => {
            // const myJsonResponse = JSON.parse(xhr.response)
            // console.log(xhr.status, xhr.response)
          //  if (xhr.status === 200) {
                msgForm.reset()
                $("#chatform").load(window.location.href + " #chatform ");
                document.getElementById("head").style.display = "block";
                document.getElementById("message").style.display = "block";
                document.getElementById("jo").style.display = "none";
                document.getElementById('progressBar').style.display = "none";
                $('.msg_card').load(window.location.href + " .msg_card ");
                // $('.msg_card').animate({scrollTop:$('.msg_card')[0].scrollHeight}, 3000);
                // $('#message').animate({scrollTop:$('#message')[0].scrollHeight}, 3000);
                $('#message').scrollIntoView()

            //}
            //else{
                //alert("An error occurred. Please try again later.")
            //}
        }
        xhr.send(formData)
    })

   function lo(){
      $('#message').animate({scrollTop:$('#message')[0].scrollHeight}, 1)
      //$('.msg_card').animate({scrollTop:$('.msg_card')[0].scrollHeight}, 1);
      //$('#message').scrollIntoView()
   }

                function check(){
                document.getElementById('progressBar').style.display = "flex";
                var body = document.getElementById("body")
                var file = document.getElementById("file")
                const send = document.getElementById("send")
                document.getElementById('jjj').style.display = "block";
                document.getElementById('bi-send').style.display = "block";
                document.getElementById('send-btn').style.display = "none";
                if(file.files.length == 0 && body.value.length == 0 ){
                    send.disabled = true
                    document.getElementById('bi-send').style.display = "block";
                    document.getElementById('send-btn').style.display = "none";
                    $('#jjj').load(window.location.href + " #jjj ");

                }
                else if(file.files.length > 0 && body.value.length > 0 ){
                    send.disabled = false
                    document.getElementById('send-btn').style.display = "block";
                    document.getElementById('bi-send').style.display = "none";
                }

            }

    $(document).ready(function (){
        setInterval(function () {
            $("#me").load(" #me > * ");
            $(".car").load(" .car > * ");
            $("#message").load(" #message ");
            $("#message").scrollIntoView();
        }, 3000)
    })


JavaScript

/*
	Load more content with jQuery - May 21, 2013
	(c) 2013 @ElmahdiMahmoud
*/

$(function () {
    $("div").slice(0, 4).show();
    $("#loadMore").on('click', function (e) {
        e.preventDefault();
        $("div:hidden").slice(0, 4).slideDown();
        if ($("div:hidden").length == 0) {
            $("#load").fadeOut('slow');
        }
        $('html,body').animate({
            scrollTop: $(this).offset().top
        }, 1500);
    });
});

$('a[href=#top]').click(function () {
    $('body,html').animate({
        scrollTop: 0
    }, 600);
    return false;
});

$(window).scroll(function () {
    if ($(this).scrollTop() > 50) {
        $('.totop a').fadeIn();
    } else {
        $('.totop a').fadeOut();
    }
});


Css

body {
    background-color: #f6f6f6;
    width: 400px;
    margin: 20px auto;
    font: normal 13px/100% sans-serif;
    color: #444;
}
div {
    display:none;
    padding: 10px;
    border-width: 0 1px 1px 0;
    border-style: solid;
    border-color: #fff;
    box-shadow: 0 1px 1px #ccc;
    margin-bottom: 5px;
    background-color: #f1f1f1;
}
.totop {
    position: fixed;
    bottom: 10px;
    right: 20px;
}

Html

<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>
<div>Content</div>

<div>Content</div>

 javascript:(function () {
    var script =  document.createElement('script');
    script.src="//cdn.jsdelivr.net/npm/eruda";
    document.body.appendChild(script);
    script.onload = function () {
        eruda.init()
    }
})();



