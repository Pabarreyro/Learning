import {Triangle} from './triangle.js';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import $ from 'jquery';

$(function() {
  $("#check").submit(function(event){
    event.preventDefault();
    let sideA = parseInt($("#sideA").val());
    let sideB = parseInt($("#sideB").val());
    let sideC = parseInt($("#sideC").val());
    let triangle = new Triangle(sideA, sideB, sideC);
    if (triangle.checkTriangle() !== "not a triangle") {
      $("#triangletype").text(triangle.checkType());
    }
  });
});
