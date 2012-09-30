$(function() {
	date = new Date();
	greg_year = date.getFullYear();
	$.ajax({
		    url: '/',
		    data: {greg_year: date.getFullYear()}, 
		    success: function(data) {
		    		console.log(data)
		    	}});
});