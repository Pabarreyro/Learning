'use strict';

const handlers = require('../handlers');

module.exports = app => {
  app.route('/about')
    .get(handlers.about);

  app.route('/distance/:zipcode1/:zipcode2')
    .get(handlers.get_distance);
};
