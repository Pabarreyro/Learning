let requestPlayful = new XMLHttpRequest();
requestPlayful.responseType = 'json';
let url = `http://api.giphy.com/v1/gifs/ZtB2l3jHiJsFa?api_key=${process.env.API_KEY}`;

requestPlayful.onreadystatechange = function() {
  if (this.readyState === 4 && this.status === 200) {
    return requestPlayful.response;
  } else {
    console.log("Did not respond!");
  }
}

requestPlayful.open("GET", url, true);
requestPlayful.send();

export { requestPlayful };
