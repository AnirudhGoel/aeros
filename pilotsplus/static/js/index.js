function checkEnter(event) {
	if (event.which == 13) {
		submitFlight();
	}
}

function submitFlight() {
	var f_code = $("input").val();

	window.location.href = "http://localhost:8000/space/f_info/" + f_code;
}

$("#locate").click(function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(sendPosition);
    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
});

function sendPosition(position) {
	var lat = position.coords.latitude;
	var lon = position.coords.longitude;

	window.location.href = "http://localhost:8000/space/f_info2/" + lat + "/" + lon;
}