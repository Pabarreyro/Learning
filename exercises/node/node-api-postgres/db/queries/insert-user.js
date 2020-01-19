'use strict';

const insertUser = `INSERT INTO users (name, email) VALUES ($1,$2) RETURNING id, name, email`;

module.exports = insertUser;