'use strict';

const selectUserById = `SELECT * FROM users WHERE id = $1`;

module.exports = selectUserById;