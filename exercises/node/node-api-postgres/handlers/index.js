'use strict';

const createUser = require('./create-user');
const getUsers = require('./get-users');
const getUserById = require('./get-user-by-id');

module.exports = {
  createUser,
  getUserById,
  getUsers
};