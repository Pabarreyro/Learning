// Business logic
var myDestination  = {
  location: '',
  landmarks: '',
  season: '',
  notes: '',
};

function Destination(location, landmarks, season, notes) {
  this.location = location;
  this.landmarks = landmarks;
  this.season = season;
  this.notes = notes;
};

// user logic
$(document).ready(function() {
  $("#new-destination").submit(function(event) {
    event.preventDefault();
    let inputLocation = $("#new-location").val();
    let inputLandmark = $("#new-landmark").val();
    let inputSeason = $("#new-season").val();
    let inputNotes = $("#new-notes").val();


    let newDestination = new Destination(inputLocation, inputLandmark, inputSeason, inputNotes);

    $("#destinations").append("<li><span class='location-name'>" + newDestination.location + "</span></li>");

    $(".location-name").last().click(function() {
      $("#show-destination").show();
      $("#show-destination h2").text(newDestination.location);
      $(".landmark").text(newDestination.landmarks);
      $(".season").text(newDestination.season);
      $(".notes").text(newDestination.notes);
    });

    $("#new-location").val("");
    $("#new-landmark").val("");
    $("#new-season").val("");
    $("#new-notes").val("");
  });
});
