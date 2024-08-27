    $(document).on('click', '#like', function(e) {
        e.preventDefault();
        try{
        $.ajax({
            type: 'POST',
            url: "{% url 'like' %}",
            data:{
                post_id:$('#li').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            },
            dataType: "json",
            success: function (data) {
                if (data.msg === 'Liked'){
                    $('#like-section').load(window.location.href + " #like-section ");
                }
            }
        })}
        catch(err){
            console.log(err)
        }

    })