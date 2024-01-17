#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const links = JSON.parse(body);
    function chars (i) {
      if (i < links.characters.length) {
        request(links.characters[i], function (err, resp, bod) {
          if (err) {
            console.error(err);
          } else {
            console.log(JSON.parse(bod).name);
            chars(i + 1);
          }
        });
      }
    }
    chars(0);
  }
});

