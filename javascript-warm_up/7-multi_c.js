#!/usr/bin/node
import process from 'node:process';
const myArgs = process.argv.slice(2);
if (isNaN(myArgs[0]) !== true) {
  const myNum = parseInt(myArgs[0]);
  for (let i = 0; i < myNum; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
