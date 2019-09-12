const request = require('request');

let apiKey = 'a7b8474154ce2639ffe7bb923a50a829';
let city = 'portland';
let url = `http://api.openweathermap.org/data/2.5/weather?q=${city}&units=imperial&appid=${apiKey}`;

request(url, function(err, response, body) {
    if (err) {
        console.log('error:', error);
    } else {
        let weather = JSON.parse(body);
        let output = `It's ${weather.main.temp} degrees in ${weather.name}`;
        console.log(output);
    }
});