#!/usr/bin/node
import process from 'node:process';
const myArgs = process.argv.slice(2);
const a = parseInt(myArgs[0]);
const b = parseInt(myArgs[1]);
if (isNaN(a) || isNaN(b)) {
  console.log(b);
} else {
  const sum = a + b;
  console.log(`${sum}`);
}
