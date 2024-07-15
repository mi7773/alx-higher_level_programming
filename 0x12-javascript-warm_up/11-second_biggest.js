#!/usr/bin/node

const { argv } = require('node:process');

let a = 0;
let b = 0;

for (let i of argv) {
  if (i === argv[0] || i === argv[1]) {
    continue;
  }
  i = Number(i);
  if (a < i) {
    b = a;
    a = i;
  } else if (b < i) {
    b = i;
  }
}

console.log(b);
