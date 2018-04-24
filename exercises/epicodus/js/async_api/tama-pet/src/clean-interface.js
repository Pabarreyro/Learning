let requestClean = new XMLHttpRequest();
requestClean.responseType = 'json';
let url = `http://api.giphy.com/v1/gifs/3oKIPCSX4UHmuS41TG?api_key=${process.env.API_KEY}`;

requestClean.onreadystatechange = function() {
  if (this.readyState === 4 && this.status === 200) {
    return requestClean.response;
  } else {
    console.log("Did not respond!");
  }
}

requestClean.open("GET", url, true);
requestClean.send();

export { requestClean };
