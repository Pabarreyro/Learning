'use strict';

const app = require('express')();
const bodyParser = require('body-parser');
const {getUsers} = require('./handlers');

const port = 3000;

app.use(bodyParser.json());

app.use(bodyParser.urlencoded({
  extended: true,
}));

app.route('/')
  .get((req, res) => {
    res.json({info: 'NodeJS, Express & Postgres API'})
  });

app.route('/users')
  .get(getUsers);

app.listen(port, () => {
  console.log(`App running on port ${port}.`)
});