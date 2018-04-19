function checkLines(text) {
  let newlineCount = text.match(/.\n./g).length;
  return newlineCount;
}
function validateText(text) {
  if(text.match(/[^a-z-.,:;!?\s]/gi) !== null){
    return false;
  }
}
export {
  checkLines,
  validateText
}
