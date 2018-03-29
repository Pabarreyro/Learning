'use strict';
/*

Make a 5x4 grid of hole images.
Every second, randomly pick _a hole_ in the grid and turn it's image into a mole.
If the user clicks on a mole image, turn it back into a hole.

Use the [setInterval](https://developer.mozilla.org/en-US/docs/Web/API/WindowTimers/setInterval) function to run a callback function periodically.

## Advanced

Keep score.

* Every mole that's hit is 100 points
* Every hole that's clicked is -50 points
* If the whole screen gets filled with moles, they lose, and the game stops.
* Every 10 seconds, increase the rate at which moles appear.
*/

var score = 0;
var timer;
var interval = 1000;
var clicks = 0;

function play() {
    var holeArray = $('.hole');
    console.log(holeArray)
    if (holeArray.length >0) {
        var random = Math.floor(Math.random()* holeArray.length);
        console.log(random);
        // $(holeArray[random]).attr('content', 'mole.jpg').removeClass('hole').addClass('mole');
        $(holeArray[random]).removeClass('hole').addClass('mole');
    } else {
        clearInterval(timer);
        alert('You Lose!');
    }
}

$('#resetButton').click(function (){
    timer = setInterval(play, interval);
});

$('div').click(function() {
    if ($(this).className === 'mole') {
        $(this).removeClass('mole').addClass('hole');
        score += 100;
        if(clicks === 9) {
            clicks = 0;
            interval -= 500;
            clearInterval(timer);
            timer = setInterval(play, interval);
        } else {
            clicks++
        }
    } else {
        score -= 50
    }
});

$('div').on('dragstart', function() {
    event.preventdefault();
;});

play();

