function initMap() {
var myLatLng = {lat: 1.3071205, lng: 103.83304783333334};

var map = new google.maps.Map(document.getElementById('map'), {
zoom: 16,
center: myLatLng
});

var marker = new google.maps.Marker({
position: myLatLng,
map: map,
title: 'Hello World!'
});
}
