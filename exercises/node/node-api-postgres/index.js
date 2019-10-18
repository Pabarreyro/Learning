'use strict';

const app = require('express')();
const bodyParser = require('body-parser');

const port = 3000;

app.use(bodyParser.json());

app.use(bodyParser.urlencoded({
  extended: true,
}));

app.route('/')
  .get((req, res) => {
    res.json({info: 'NodeJS, Express & Postgres API'})
  });

app.listen(port, () => {
  console.log(`App running on port ${port}.`)
});