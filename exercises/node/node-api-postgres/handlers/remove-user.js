'use strict';

const db = require('../db');
const {deleteUser} = require('../db/queries');

const removeUser = (req, res, next) => {
  const userId = parseInt(req.params.id);

  db.query(deleteUser, [userId], (err, data) => {
    if (err) {
      return next(err);
    }

    res.status(200.).send(`User deleted with id: ${userId}`);
  });
};

module.exports = removeUser;