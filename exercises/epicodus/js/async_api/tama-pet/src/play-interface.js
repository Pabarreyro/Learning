let requestPlay = new XMLHttpRequest();
requestPlay.responseType = 'json';
let url = `http://api.giphy.com/v1/gifs/hc1jyTXYaiXy8?api_key=${process.env.API_KEY}`;

requestPlay.onreadystatechange = function() {
  if (this.readyState === 4 && this.status === 200) {
    return requestPlay.response;
  } else {
    console.log("Did not respond!");
  }
}

requestPlay.open("GET", url, true);
requestPlay.send();

export { requestPlay };
