#!/usr/bin/node

const { argv } = require('node:process');

let ind;

argv.forEach((arg, index) => {
  if (index === 2) {
    console.log(arg);
  }
  ind = index;
});

if (ind <= 1) {
  console.log('No argument');
}
