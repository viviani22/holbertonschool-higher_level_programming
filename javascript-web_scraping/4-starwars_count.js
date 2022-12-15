#!/usr/bin/node

const request = require('request');
let i = 0;

request('https://swapi-api.hbtn.io/api/films/', function (error, response, body) {
  let number = 0;
  const films = JSON.parse(body).results;
  for (const film in films) {
    const characters = films[film].characters;
    for (const id in characters) {
      if (characters[id].includes(18)) {
        number++;
      }
    }
  }
  console.log(number);
});
