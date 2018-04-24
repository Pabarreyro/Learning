import { pet } from './tama-pet.js';
import { requestPlayful } from './playful-interface.js';
import { requestGameOver } from './gameover-interface.js';
// import { unplayfulPromise } from './unplayful-interface.js';
import { requestSleep } from './sleep-interface.js';
import { Eat } from './eat-interface.js';
import { requestIdol } from './idol-interface.js';
import { requestClean } from './clean-interface.js';
import $ from 'jquery';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles.css';

function progressBars() {
  const statusCheckInterval = setInterval(()=> {
    $("#playfullness").attr('src', `${requestPlayful.response.data.images.fixed_width_small.url}`);
    $("#health").css('width', (pet.health * 5) + '%');
    $("#clean").css('width', (pet.dirty * 10) + '%');
    $("#tummy").css('width', (pet.tummy * 10) + '%');
    $("#age span").text(pet.age);
    if (pet.petCemetery() === true) {
      clearInterval(statusCheckInterval);
      $("#health").css('width', 0 + '%');
      $(".pet-screen img").attr('src', `${requestGameOver.response.data.images.fixed_width.url}`)
    }
  }, 1000)
}

$(function() {
  let eating = new Eat();
  function idol() {
    setTimeout(() => {
      $(".pet-screen img").attr('src', `${requestIdol.response.data.images.fixed_width.url}` );
    }, 4000)
  }

  $("#startPet").submit(function(event) {
    event.preventDefault();
    $(this).hide();
    $(".pet-container").show();
    $("#feed").click(function() {
      if (pet.tummy < 10) {
        pet.tummy += 2;
      eating.eatingCall().then(function(response) {
        $(".pet-screen img").attr('src', response.data.images.fixed_width.url);
      })
        idol();
        if (pet.health < 20) {
          pet.health += 5;
        }
      }
    });
    $("#scoop").click(function() {
      if (pet.dirty > 0) {
        pet.dirty = 0;
        $(".pet-screen img").attr('src', `${requestClean.response.data.images.fixed_width.url}` );
        if (pet.health < 20) {
          pet.health += 5;
        }
      }
    });
    // $("#play").click(function() {
    //
    // });
    pet.hunger();
    pet.pooper();
    pet.birthday();
    progressBars();

  });
});
