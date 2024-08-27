    var infinite = new Waypoint.Infinite({
      element: $('.infinite-container')[0],
      onBeforePageLoad: function () {
        $('#message').animate({scrollTop:$('#message')[0].scrollHeight}, 1)
        $('.msg_card').animate({scrollTop:$('.msg_card')[0].scrollHeight}, 1);
        $('#message').animate({scrollTop:$('#message').prop('scrollHeight')});
        $('.loading').show();
      },
      onAfterPageLoad: function ($items) {
        $('.loading').hide();
        $('#message').animate({scrollTop:$('#message')[0].scrollHeight}, 1)
        $('.msg_card').animate({scrollTop:$('.msg_card')[0].scrollHeight}, 1);
        $('#message').animate({scrollTop:$('#message').prop('scrollHeight')});
        alert('hi hello')
      }
    });