function checkEnter(event) {
	if (event.which == 13) {
		submitFlight();
	}
}

function submitFlight() {
	var f_code = $("input").val();

	window.location.href = "http://localhost:8000/space/f_info/" + f_code;
}