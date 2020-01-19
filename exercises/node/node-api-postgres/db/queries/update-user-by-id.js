'use strict';

const selectUserById = `UPDATE users SET name = $1, email = $2 WHERE id = $3 RETURNING id, name, email`;

module.exports = selectUserById;