var article_text = $('#text');
var old_top_of_text = article_text[0].getBoundingClientRect().y;

// scroll functions
$(window).scroll(function(e) {

	var top_of_text = article_text[0].getBoundingClientRect().y;
	var scrolling_down = (old_top_of_text > top_of_text);
	old_top_of_text = top_of_text;

    // add/remove class to navbar when scrolling to hide/show
    var scroll = $(window).scrollTop();
    if (scroll >= top_of_text) {
        $('.navbar').addClass("navbar-hide");
    } else {
        $('.navbar').removeClass("navbar-hide");
    }

	if(!scrolling_down){
		$('.navbar').removeClass("navbar-hide");

	}

});
