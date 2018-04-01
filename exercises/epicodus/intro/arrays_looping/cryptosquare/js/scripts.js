let rows = 0;
let columns = 0;
let stringArray = [];
let stringLength = 0;
let stringArraySplit = [];
let outputArray = [];

function removeNonLetters(string) {
  return string.replace(/[^a-zA-Z]/g, '');
};

function setGrid(string) {
  stringLength = string.length;

  if (Math.sqrt(stringLength) % 1 === 0) {
    rows += Math.sqrt(stringLength);
    columns += Math.sqrt(stringLength);
  } else {
    rows += Math.ceil(Math.sqrt(stringLength));
    columns += Math.floor(Math.sqrt(stringLength));
  }
};

function splitString(string) {
  let leftovers = (columns*rows) - stringLength;
  let regexInsert = new RegExp("([a-z]{" + (columns - leftovers) + "," + columns + "})", "g");
  stringArray = string.match(regexInsert, rows);
};

function splitStringArray(array) {
  splitStringArray = array.map(function(string) {
    return string.split("");
  });
};

function pushLettersToOutput(array){

}
