'use strict';

const request = require('request');

const apiKey = process.env.ZIP_CODE_ENV || 
  'z3DlyD6dN6l1RF2G5gIByGivlwaJbS9MBywcvZg34bE61nAKyKpp8GAfyx1oYIaW';

const zipcodeBase = 'https://www.zipcodeapi.com/rest/';

const zipCodeURL = (zip1, zip2) => `${zipcodeBase}${apiKey}/distance.json/${zip1}/${zip2}/mile`;

const calculateDistance = (req, res, next) => {
  request(
    zipCodeURL(req.params.zipcode1, req.params.zipcode2),
    (error, response, body) => {
      if (!error && response.statusCode == 200) {
        response = JSON.parse(body);
        res.send(response);
      } else {
        console.log(response.body + response.error);
        res.send({distance: -1});
      }
    }
  )
};

module.exports = calculateDistance;
