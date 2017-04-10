function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function() {
    $(".btn-field-to-change").click(btnFieldToChange);
});

$(document).ready(function() {
    $(".btn-field-change").click(btnFieldChange);
});

function btnFieldChange(){
    btn = $(this);
    input = btn.parent().parent().children('input:first');
    input.attr('disabled', true);
    btn.text(btn.val());
    btn.removeClass('btn-field-change');
    btn.addClass('btn-field-to-change');
    btn.unbind("click", btnFieldChange);
    btn.click(btnFieldToChange);
    $.ajax({
        type: "POST",
        data: {
            key: input.attr("name"),
            value: input.val(),
            xhr: true
        },
        success: function(result){
            alert(result.status);
        }
    });
}

function btnFieldToChange(){
    btn = $(this);
    input = btn.parent().parent().children('input:first');
    input.removeAttr('disabled');
    btn.val(btn.text());
    btn.text('Change');
    btn.addClass('btn-field-change');
    btn.removeClass('btn-field-to-change');
    btn.unbind("click", btnFieldToChange);
    btn.click(btnFieldChange);
}
var map;
function initMap() {
    var kiev = {lat: 50.548, lng: 30.226};
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: kiev
    });
    var marker;
    var markerInput_lat = $('#marker_lat');
    var markerInput_lng = $('#marker_lng');
    google.maps.event.addListener(map, 'click', function(event) {
        if (marker != null) {
            marker.setMap(null);
        }
        marker = new google.maps.Marker({
            position: event.latLng,
            map: map,
            draggable: true
        });
        markerInput_lat.val(marker.position.lat());
        markerInput_lng.val(marker.position.lng());
        google.maps.event.addListener(marker, 'drag', function(event) {
            markerInput_lat.val(this.position.lat());
            markerInput_lng.val(marker.position.lng());
        });
        google.maps.event.addListener(marker, 'dragend', function(event) {
            markerInput_lat.val(this.position.lat());
            markerInput_lng.val(this.position.lng());
        });
    });
}

function initMapToLocate(jobLocation, userLocation){
    var jobMarker;
    map.center = jobLocation;
    jobMarker = new google.maps.Marker({
            position: jobLocation,
            map: map
        });
    var userMarker = new google.maps.Marker({
            position: userLocation,
            map: map
        });
}

$(document).ready(function() {
    $(".btn-map-marker-set").click(function(){
        alert("go");
        var mapNode = map.getDiv();
        $('#mapHolder2').append(mapNode);
    });
});
