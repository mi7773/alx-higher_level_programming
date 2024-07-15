#!/usr/bin/node

const { argv } = require('node:process');

const val = argv[2];

if (val == Number(val)) {
  console.log(Number(val));
} else {
  console.log('Not a number');
}
