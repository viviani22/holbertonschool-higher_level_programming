#!/usr/bin/node
import process from 'node:process';
const myArgs = process.argv.slice(2);
const myNum = parseInt(myArgs[0]);
if (isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myNum}`);
}
