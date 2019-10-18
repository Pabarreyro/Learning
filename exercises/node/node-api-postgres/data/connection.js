'use strict';

const Pool = require('pg').Pool;

const pool = new Pool({
  user: 'me',
  host: 'localhost',
  database: 'api',
  password: 'loaner4pabloe',
  port: 5432
});

module.exports = pool;