let searchParams = new URLSearchParams(window.location.search)
url = "https://arrivelah.herokuapp.com/?id="+searchParams.get('stop');



$.getJSON(url, function (json) {
    services = json["services"];


    for(i=0;i<services.length; i++){


      busno = services[i]["no"]
      arrtimems = services[i]["next"]["duration_ms"]
      arrtimemin = arrtimems/60000
      arrtime = Math.round( arrtimemin * 10 ) / 10;

      function initMap() {
    var myLatLng = {lat: services[i]["next"]["lat"], lng: services[i]["next"]["lng"]};

var map = new google.maps.Map(document.getElementById('map'+i), {
  zoom: 16,
  center: myLatLng
});

var marker = new google.maps.Marker({
  position: myLatLng,
  map: map,
  title: 'Hello World!'
});
}


      if(arrtime <= 0.5){
        arrtime="Arriving"
      }
      else{
        arrtime=arrtime+" minutes"
      };
      if(services[i]["next"]["load"] == "SDA"){
        load = '<i class="material-icons">directions_walk</i>'
      } else if(services[i]["next"]["load"] == "SEA"){
        load = '<i class="material-icons">airline_seat_recline_normal</i>'
      } else {
        load = '<i class="material-icons">wc</i>'
      }
      if(services[i]["next"]["type"] == "SD"){
        deck = '<i class="flaticon-056-bus-3">'
      } else {
        deck = '<i class="flaticon-101-double-decker-bus">'
      }
      $("table").append('<tr><td>'+busno+'</td><td><a href="#modal'+i+'">'+arrtime+'</a></td><td><i class="material-icons">accessible</i>'+load+deck+'</td></tr>');

      $("body").append('<div id="modal'+i+'" class="modal"><div class="modal-content" id="map'+i+'">  </div><div class="modal-footer"><a href="#!" class="modal-close waves-effect waves-green btn-flat">Close</a></div>')

    }
});
