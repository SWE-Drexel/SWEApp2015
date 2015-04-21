var main = function() {
	$('ul').sortable(); 
  $('#deletion').addClass('disabled');
  $('#submission').addClass('disabled');

  $('#submission').click(function() {
		
    	var post = $('.status-box').val();
      $('.posts').append('<li class="goallist">'+ post +'</li>');   	
    	$('.status-box').val('');
    	$('#submission').addClass('disabled'); 

      if ( $('ul').children().length > 0) {
        $('#deletion').removeClass('disabled');
        }
      else {
        $('#deletion').addClass('disabled');
      } 

  });
  
  $('.status-box').keyup(function() {
    var postLength = $(this).val().length;
    if(postLength === 0) {
      $('#submission').addClass('disabled'); 
    }
    else {
      $('#submission').removeClass('disabled');
    }
  });
  
  $(document).on('click','.goallist',function() {
        $(this).toggleClass('selected');
    });

  $('#deletion').click(function() {
    $('.selected').remove();
    if ( $('ul').children().length > 0) {
        $('#deletion').removeClass('disabled');
        }
      else {
        $('#deletion').addClass('disabled');
      }
  });

};
$(window).load(main)