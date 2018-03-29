// Backend logic

var onesNumerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
var tensNumerals = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
var hundredsNumerals = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
var thousandsNumerals = ["M", "MM", "MMM"];

function convertOnes(number) {
  return onesNumerals[number-1];
};

function convertTens(number) {
  var numberString = number.toString();
  var tenDigit = parseInt(numberString[0]);
  return tensNumerals[tenDigit-1];
};

function convertHundreds(number) {
  var numberString = number.toString();
  var hundredDigit = parseInt(numberString[0]);
  return hundredsNumerals[hundredDigit-1];
}

function convertThousands(number) {
  var numberString = number.toString();
  var thousandDigit = parseInt(numberString[0]);
  return thousandsNumerals[thousandDigit-1];
}
