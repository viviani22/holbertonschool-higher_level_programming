#!/usr/bin/node
import process from 'node:process';
const myArgs = process.argv.slice(2);
const string = `${myArgs[0]} is ${myArgs[1]}`;
console.log(string);
