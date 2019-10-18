'use strict';

const app = require('express')();
const bodyParser = require('body-parser');
const {
  createUser,
  getUsers,
  getUserById,
  updateUser
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
  .post(createUser); // curl --data "name={name}&email={email}" http://localhost:3000/users | json_pp

app.route('/users/:id')
  .get(getUserById)
  .put(updateUser); // curl -X PUT -d "name={name}" -d "email={email}" http://localhost:3000/users/{id} | json_pp

app.listen(port, () => {
  console.log(`App running on port ${port}.`)
});