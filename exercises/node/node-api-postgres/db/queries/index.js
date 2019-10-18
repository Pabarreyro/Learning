'use strict';

const deleteUser = require('./delete-user');
const insertUser = require('./insert-user');
const selectAllUsers = require('./select-all-users');
const selectUserById = require('./select-user-by-id');
const updateUserById = require('./update-user-by-id');

module.exports = {
  deleteUser,
  insertUser,
  selectUserById,
  selectAllUsers,
  updateUserById
};
