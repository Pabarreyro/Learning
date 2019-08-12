const express = require('express');
const routes = requires('./api/routes');

const port = process.env.PORT || 3000;

routes(app);

app.listen(port, function() {
  console.log('Server started on port: ' + port);
});
