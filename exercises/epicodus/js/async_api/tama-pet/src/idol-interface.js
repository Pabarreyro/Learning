let requestIdol = new XMLHttpRequest();
requestIdol.responseType = 'json';
let url = `http://api.giphy.com/v1/gifs/OFD5J5AO2czeg?api_key=${process.env.API_KEY}`;

requestIdol.onreadystatechange = function() {
  if (this.readyState === 4 && this.status === 200) {
    return requestIdol.response;
  } else {
    console.log("Did not respond!");
  }
}

requestIdol.open("GET", url, true);
requestIdol.send();

export { requestIdol };
