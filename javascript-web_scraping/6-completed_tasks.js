#!/usr/bin/node

const request = require('request');
request('https://jsonplaceholder.typicode.com/todos', function(error, response, body) {
  let dict = JSON.parse(body);
  let userID = 1;
  let nr_tasks = {};
  for (let item of dict) {
    if (item.userId === userID) {
      if (userID in nr_tasks && item.completed) {
        nr_tasks[userID] += 1;
      }
      else {
	if (item.completed) {
          nr_tasks[userID] = 1;
	}
      }
    }
    else {
      userID += 1;
    }
  }
  console.log(nr_tasks);
});
