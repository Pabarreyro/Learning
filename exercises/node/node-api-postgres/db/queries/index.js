'use strict';

const insertUser = require('./insert-user');
const selectAllUsers = require('./select-all-users');
const selectUserById = require('./select-all-user-by-id');

module.exports = {
  insertUser,
  selectUserById,
  selectAllUsers
};
