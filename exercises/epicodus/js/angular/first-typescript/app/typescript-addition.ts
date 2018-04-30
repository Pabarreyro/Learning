let findSum = function(firstValue: number, secondValue: number) {
  let sum: number = firstValue + secondValue;
  alert("The sum of your two numbers is: " + sum);
}

let firstNumber: number = parseInt(prompt("Please enter a  number."));
let secondNumber: number = parseInt(prompt("Please enter another number."));
findSum(firstNumber, secondNumber);
