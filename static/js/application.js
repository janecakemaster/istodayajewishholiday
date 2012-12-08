$(function(){
	date = new Date();
	greg_year = date.getFullYear();
	greg_month = date.getMonth() + 1;
	greg_day = date.getDay();
	greg_date = date.getDate();
	$("#yesno").html(" ");

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
						$("#yesno").html("YES");
						hol = key;
						reg = /\se[a-z]*/;
						holidayname = hol.replace(reg, "");
						$("#extras").html("<a href=\"http://www.google.com/search?q=" + holidayname + "\">" + holidayname + "</a>");
						$("#footer").html("<p>Starts at sundown today</p>");
					}
					else if(isHoliday===false){
						$("#yesno").html("NO");
					}
				}
			}
		}
	});
});