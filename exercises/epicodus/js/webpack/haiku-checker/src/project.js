export function checkLines(text) {
  let newlineCount = text.match(/.\n./g).length;
  return newlineCount;
}

export function splitSentences(text) {
  let sentenceArray = text.split(/\n/g);
  return sentenceArray;
}

export function countVowels(text) {
  let sentenceArray = splitSentences(text);
  let countArray = [];

  for (let i = 0; i < sentenceArray.length; i++) {
    countArray.push(sentenceArray[i].match(/[aeu]+|i|[cts]ia+|e[^o]\W|[ou]+/gi).length);
  }
  return countArray;
}


export function countWordsEndingE(text){
  let sentenceArray = splitSentences(text);
  let countArray = [];

  for (let i = 0; i < sentenceArray.length; i++) {
    if (sentenceArray[i].match(/[a-z]+e\s/gi) !== null) {
      countArray.push(sentenceArray[i].match(/ie|[a-z]+[^lh]e\W|\s[^rh]ele/gi).length);
    } else {
      countArray.push(0);
    }
  }
  return countArray;
}

export function updateVowelCount(text) {
  let sentenceArray = splitSentences(text);
  let vowelCount = countVowels(text);
  let endineCount = countWordsEndingE(text);
  let updatedVowels = [];

  for (var i = 0; i < sentenceArray.length; i++) {
    updatedVowels.push(vowelCount[i] - endineCount[i]);
  }
  return updatedVowels;
}
