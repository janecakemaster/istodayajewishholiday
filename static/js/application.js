$(function(){
	date = new Date();
	greg_year = date.getFullYear();
	greg_month = date.getMonth();
	greg_day = date.getDay();
	greg_date = date.getDate();
	// greg_month = 4;
	// greg_date = 27;
	isHoliday = false;
	time = date.getTime();
	$.ajax({
		url: '/',
		data: {greg_year: date.getFullYear()},
		success: function(data){
			d = JSON.parse(data);
			console.log(d);
			for(var key in d){
				if(d.hasOwnProperty(key)){
					currm = d[key][0][1];
					currd = d[key][0][2];
					dur = d[key][1];
					// add time check
					if (currm===greg_month && currd===greg_date && isHoliday===false) {
						isHoliday=true;
						$("#yesno").html("Yes");
						$("#extras").html("<a href=\"http://bit.ly/W3IPe6\">" + key + "</a>");
						// });
					}
				}
			}
			if(isHoliday===false){
				$("#yesno").html("No");
			}
		}
	});
});