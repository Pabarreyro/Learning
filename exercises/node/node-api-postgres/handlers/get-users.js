'use strict';

const db = require('../db');
const {selectAllUsers} = require('../db/queries');

const getUsers = (req, res, next) => {
  db.query(selectAllUsers, (err, data) => {
    if (err) {
      return next(err);
    }

    res.send(data.rows);
  });
};

module.exports = getUsers;