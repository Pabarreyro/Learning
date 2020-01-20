const pads = document.querySelectorAll('.pad'); 

const getSound = key => document.querySelector(`audio[data-key="${key}"]`);
const getPad = key => document.querySelector(`.pad[data-key="${key}"]`);

function playSound(file) {
  file.currentTime = 0;
  file.play();
}

function lightPad(pad) {
  pad.classList.add('playing');
} 

function respondToKey({keyCode}) {
  let sound = getSound(keyCode);
  let pad = getPad(keyCode);

  if (sound && pad) {
    playSound(sound);
    lightPad(pad);
  }
}

function removeTransition(e) {
  if (e.propertyName === 'transform') {
    this.classList.remove('playing');
  }
}

window.addEventListener('keydown', respondToKey);

pads.forEach(pad => pad.addEventListener('transitionend', removeTransition));