'use strict';

const app = require('express')();
const bodyParser = require('body-parser');
const {
  createUser,
  getUsers,
  getUserById
} = require('./handlers');

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
  .get(getUsers)
  .post(createUser);

app.route('/users/:id')
  .get(getUserById);

app.listen(port, () => {
  console.log(`App running on port ${port}.`)
});