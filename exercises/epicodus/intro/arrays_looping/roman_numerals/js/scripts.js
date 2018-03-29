// Backend logic

var onesNumerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
var tensNumerals = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
var hundredsNumerals = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
var thousandsNumerals = ["M", "MM", "MMM"];

function convertOnes(number) {
  return onesNumerals[number-1];
};

function convertTens(number) {
  // var numberString = number.toString();
  var tenDigit = parseInt(number[0]);
  return tensNumerals[tenDigit-1];
};

function convertHundreds(number) {
  // var numberString = number.toString();
  var hundredDigit = parseInt(number[0]);
  return hundredsNumerals[hundredDigit-1];
}

function convertThousands(number) {
  // var numberString = number.toString();
  var thousandDigit = parseInt(number[0]);
  return thousandsNumerals[thousandDigit-1];
}

function romanNumeral(number) {
  var numberArray = number.toString().split("");
  var outputArray = [];
  reverseArray = numberArray.reverse();

  if (reverseArray.length === 4) {
    outputArray.push(convertOnes(reverseArray[0]), convertTens(reverseArray[1]), convertHundreds(reverseArray[2]), convertThousands(reverseArray[3]));
  } else if (reverseArray.length === 3) {
    outputArray.push(convertOnes(reverseArray[0]), convertTens(reverseArray[1]), convertHundreds(reverseArray[2]));
  } else if (reverseArray.length === 2) {
    outputArray.push(convertOnes(reverseArray[0]), convertTens(reverseArray[1]));
  } else {
    outputArray.push(convertOnes(reverseArray[0]));
  }

  var output = outputArray.reverse().join("");

  return output
  // for (var i = 0; i < reverseArray.length; i++) {
  //
  //   outputArray.push reserveArray[i]
  // }

}
