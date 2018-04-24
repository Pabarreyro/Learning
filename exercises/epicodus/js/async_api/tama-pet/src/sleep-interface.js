let requestSleep = new XMLHttpRequest();
requestSleep.responseType = 'json';
let url = `http://api.giphy.com/v1/gifs/TrSqUougSkFO0?api_key=${process.env.API_KEY}`;

requestSleep.onreadystatechange = function() {
  if (this.readyState === 4 && this.status === 200) {
    return requestSleep.response;
  } else {
    console.log("Did not respond!");
  }
}

requestSleep.open("GET", url, true);
requestSleep.send();

export { requestSleep };
