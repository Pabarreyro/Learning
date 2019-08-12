'use strict';

const calculateDistance = require('../lib/calculate-distance');

module.exports = (req, res) => {
  distance.find(req, res, (err, dist) => {
    if (err) {
      res.send(err);
    }
    res.json(dist);
  });
};