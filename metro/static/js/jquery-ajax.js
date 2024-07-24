$(document).ready(function($) {
	$('.popup-open').click(function() {
        var userfullname = $(this).attr('data-fullname');
        var useremail = $(this).attr('data-email');
        var useraddress = $(this).attr('data-address');
    
        $(".userfullname").empty();
        $(".useremail").empty();
        $(".useraddress").empty();
    
        $(".userfullname").append('<p>' + userfullname + '</p>');
        $(".useremail").append('<p>' + useremail + '</p>');
        $(".useraddress").append('<p> ' + useraddress + '</p>');
        $("#hide1").attr('value', userfullname);
        $("#hide2").attr('value', useremail);
        $("#hide3").attr('value', useraddress);

		$('.popup-fade').fadeIn();
		return false;
	});	
	
	$('.popup-close').click(function() {
		$(this).parents('.popup-fade').fadeOut();
		return false;
	});
    
    $('.save-btn').click(function() {
		$(this).parents('.popup-fade').fadeOut();
		return false;
	});	
 
	$(document).keydown(function(e) {
		if (e.keyCode === 27) {
			e.stopPropagation();
			$('.popup-fade').fadeOut();
		}
	});
	
	$('.popup-fade').click(function(e) {
		if ($(e.target).closest('.popup').length == 0) {
			$(this).fadeOut();					
		}
	});
});