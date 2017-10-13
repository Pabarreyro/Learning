'use strict'
var map = new ol.Map({
  layers: [vector],
  target: document.getElementById('map'),
  view: new ol.View({
    center: [0, 0],
    zoom: 2
  })
});