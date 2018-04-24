class Eat {
  eatingCall() {
    return new Promise(function(resolve, reject) {
      let requestEat = new XMLHttpRequest();
      let url = `http://api.giphy.com/v1/gifs/7oUdj7cAkXVfi?api_key=${process.env.API_KEY}`;
      requestEat.responseType = 'json';

      requestEat.onload = function() {
        if (this.status === 200) {
          resolve(requestEat.response);
        } else {
          reject(Error(requestEat.statusText));
        }
      }
      requestEat.open("GET", url, true);
      requestEat.send();
    });
  }
}
export { Eat };
