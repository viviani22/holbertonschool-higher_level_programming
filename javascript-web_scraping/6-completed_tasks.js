#!/usr/bin/node

const request = require('request');
request('https://jsonplaceholder.typicode.com/todos', function(error, response, body) {
  const dict = JSON.parse(body);
  const nr_tasks = {};
  for (const user in dict) {
    if (dict[user].completed) {
      if (nr_tasks[dict[user].userId] === undefined) {
        nr_tasks[dict[user].userId] = 1;
      } else {
        nr_tasks[dict[user].userId] += 1;
      }
    }
  }
  console.log(nr_tasks);
});
