var header = $('#header-container');
var article_text = $('#text');

var bottom_of_header = header[0].getBoundingClientRect().height;
var old_top_of_text = article_text[0].getBoundingClientRect().y;

document.addEventListener('scroll', function () {

	var top_of_text = article_text[0].getBoundingClientRect().y;

	var scrolling_down = (old_top_of_text > top_of_text);
	old_top_of_text = top_of_text;

	if(bottom_of_header > top_of_text){
		header.css("margin-top", "-100px");
	}
	else{
		header.css("margin-top", "0");
	}

	if(!scrolling_down){
		header.css("margin-top", "0");
	}


	// console.log(bottom_of_header - top_of_text);
});

