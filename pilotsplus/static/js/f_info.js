$(document).ready(function() {
	$(".box").html("<img src='/static/img/loader.gif' class='loader'>");
	f_code = $("#f_code").val();

	$.get("/space/calc/" + f_code, function(data) {
		console.log(data);
	});
});