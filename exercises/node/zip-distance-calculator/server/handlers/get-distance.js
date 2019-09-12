'use strict';

const calculateDistance = require('../lib/calculate-distance');

module.exports = (req, res) => {
  calculateDistance(req, res, (err, dist) => {
    if (err) {
      res.send(err);
    }
    res.json(dist);
  });
};