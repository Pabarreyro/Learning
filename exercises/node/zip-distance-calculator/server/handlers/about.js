'use strict';

const properties = require('../../package.json');

module.exports = (req, res) => {
  const appInfo = {
    name: properties.name,
    version: properties.version
  };

  res.send(appInfo);
};
