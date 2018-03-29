// Backend logic

var onesNumerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
var tensNumerals = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];

function convertOnes(number) {
  return onesNumerals[number-1];
};

function convertTens(number) {
  var numberString = number.toString();
  var tenDigit = parseInt(numberString[0]);
  return tensNumerals[tenDigit-1];
};
