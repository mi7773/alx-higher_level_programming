#!/usr/bin/node

const { argv } = require('node:process');

const a = Number(argv[2]);

function factorial (a) {
  if (isNaN(a)) {
    return 1;
  }
  if (a === 1 || a === 0) {
    return 1;
  }
  if (a > 1) {
    return a * factorial(--a);
  }
}

console.log(factorial(a));
