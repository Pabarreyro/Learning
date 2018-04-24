// let unplayfulPromise =  new Promise(function(resolve, reject) {
//   let requestUnplayful = new XMLHttpRequest();
//   let url = `http://api.giphy.com/v1/gifs/qYcKovVHt3eE?api_key=${process.env.API_KEY}`;
//   requestUnplayful.responseType = 'json';
//
//   requestUnplayful.onload = function() {
//     if (this.status === 200) {
//       resolve(requestUnplayful.response);
//     } else {
//       reject(Error(requestUnplayful.statusText));
//     }
//   requestUnplayful.open("GET", url, true);
//   requestUnplayful.send();
// };
// export { unplayfulPromise };
