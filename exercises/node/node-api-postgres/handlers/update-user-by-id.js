'use strict';

const db = require('../db');
const {updateUserById} = require('../db/queries');

const updateUser = (req, res, next) => {
  const userId = parseInt(req.params.id);
  const {name, email} = req.body;

  db.query(updateUserById, [name, email, userId], (err, data) => {
    if (err) {
      return next(err);
    }

    res.status(200).send({
      users: data.rows[0]
    });
  });
};

module.exports = updateUser;