#!/usr/bin/node
import process from 'node:process';
const myArgs = process.argv.slice(2);
if (myArgs.length === 0) {
  console.log(0);
} else {
  let largest = 0;
  let secondLargest = 0;
  for (let i = 0; i < myArgs.length; i++) {
    if (parseInt(myArgs[i]) > largest) {
      secondLargest = largest;
      largest = parseInt(myArgs[i]);
    }
  }
  console.log(secondLargest);
}
