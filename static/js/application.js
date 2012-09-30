$(function(){
	date = new Date();
	greg_year = date.getFullYear();
	greg_month = date.getMonth();
	greg_day = date.getDay();
	greg_date = date.getDate();
	isHoliday = false;
	time = date.getTime();
	$.ajax({
		url: '/',
		data: {greg_year: date.getFullYear()},
		success: function(data){
			d = JSON.parse(data);
			for(var key in d){
				if(d.hasOwnProperty(key)){
					currm = d[key][1];
					currd = d[key][2];
					if (currm===greg_month && currd ===greg_date && isHoliday===false) {
						isHoliday=true;
						$("#yesno").html("Yes");
						$("#extras").html(key);
					};
					
					// console.log("obj " + d[key]);
					// console.log("month " + d[key][1]);
					// console.log("date " + d[key][2]);
				}
			}
			if(isHoliday===false){
				$("#yesno").html("No");
			}
			console.log(d);
		}
	});
});