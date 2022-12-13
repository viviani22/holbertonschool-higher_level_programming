#!/usr/bin/node

const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body) {
  const dict = JSON.parse(body);
  console.log(dict.title);
});
