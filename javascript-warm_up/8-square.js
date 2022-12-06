#!/usr/bin/node
import process from 'node:process';
const myArgs = process.argv.slice(2);
if (myArgs[0] !== undefined) {
  const myNum = parseInt(myArgs[0]);
  const row = '#'.repeat(myNum);
  for (let i = 0; i < myNum; i++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
