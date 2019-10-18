'use strict';

const db = require('../db');
const {selectUserById} = require('../db/queries');

const getUsers = (req, res, next) => {
  const userId = parseInt(req.params.id);

  db.query(selectUserById, [userId], (err, data) => {
    if (err) {
      return next(err);
    }

    res.send(data.rows);
  });
};

module.exports = getUsers;