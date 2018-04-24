let requestGameOver = new XMLHttpRequest();
requestGameOver.responseType = 'json';
let url = `http://api.giphy.com/v1/gifs/MsWkfDR6kriyk?api_key=${process.env.API_KEY}`;

requestGameOver.onreadystatechange = function() {
  if (this.readyState === 4 && this.status === 200) {
    return requestGameOver.response;
  } else {
    console.log("Did not respond!");
  }
}

requestGameOver.open("GET", url, true);
requestGameOver.send();

export { requestGameOver };
