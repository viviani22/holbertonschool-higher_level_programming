#!/usr/bin/node

const request = require('request');
let i = 0;

request('https://swapi-api.hbtn.io/api/films/', function (error, response, body) {
  let number = 0;
  const dict = JSON.parse(body);
  for (const [key, value] of Object.entries(dict.results)) {
    for (let j = 0; j < (dict.results[i].characters).length; j++) {
      if (dict.results[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
	      number += 1;
      }
    }
    i += 1;
  }
console.log(number);
});
