'use strict';

const deleteUser = `DELETE FROM users WHERE id = $1`;

module.exports = deleteUser;