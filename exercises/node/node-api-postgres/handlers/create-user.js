'use strict';

const db = require('../db');
const {insertUser} = require('../db/queries');

const createUser = (req, res, next) => {
  const {name, email} = req.body;

  db.query(insertUser, [name, email], (err, data) => {
    if (err) {
      return next(err);
    }

    res.status(201).send({
      users: data.rows[0]
    });
  });
};

module.exports = createUser;