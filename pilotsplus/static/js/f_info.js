$(document).ready(function() {
	$(".loader").html("<img src='/static/img/loader2.gif'>");
	f_code = $("#f_code").val();

	$.get("/space/calc/" + f_code, function(data) {
		var state = data[3]
		finalData = "<h1>Current Location</h1><br>" + state + "<br><br><h1>Places of Interest in " + state + "</h1><br><em>" + data[1] + "</em><br>" + data[2] + "<br><br>" + data[0];
		$(".loader").html("");
		$(".content").html(finalData);
		$(".content").css({
			"padding":"20px 20px 20px 20px"
		});
	});
});