'use strict';

const {Pool} = require('pg');

const pool = new Pool({
  user: 'me',
  host: 'localhost',
  database: 'api',
  password: 'loaner4pablo',
  port: 5432
});

const getClient = callback => pool.connect((err, client, done) => callback(err, client, done));

const query = (text, params, callback) => pool.query(text, params, callback);

module.exports = {
  getClient,
  query
};
