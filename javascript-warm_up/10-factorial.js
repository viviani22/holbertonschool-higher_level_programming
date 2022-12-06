#!/usr/bin/node
import process from 'node:process';
const myArgs = process.argv.slice(2);
const myNum = parseInt(myArgs[0]);
if (isNaN(myNum)) {
  console.log(1);
} else {
  console.log(recursiveFact(myNum));
}

function recursiveFact (num) {
  if (num === 1) {
    return (1);
  }
  return (num * recursiveFact(num - 1));
}
