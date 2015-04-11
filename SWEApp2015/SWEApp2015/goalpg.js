var main = function() {
	$('ul').sortable();
  $('.btn').click(function() {
		
    	var post = $('.status-box').val();
    	$('<li>').text(post).appendTo('.posts');
    	
    	$('.status-box').val('');
    	$('.btn').addClass('disabled'); 
  });
  
  $('.status-box').keyup(function() {
    var postLength = $(this).val().length;
    if(postLength === 0) {
      $('.btn').addClass('disabled'); 
    }
    else {
      $('.btn').removeClass('disabled');
    }
  });
  
  $('.btn').addClass('disabled');

  $('ul').click(function(){
    $(this).addClass('selected');
  });

};
$(document).ready(main)