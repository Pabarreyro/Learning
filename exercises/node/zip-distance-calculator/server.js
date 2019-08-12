const express = require('express');
const routes = require('./server/routes');

const port = process.env.PORT || 3000;

const app = express();

routes(app);

app.listen(port, function() {
  console.log('Server started on port:' + port);
});
