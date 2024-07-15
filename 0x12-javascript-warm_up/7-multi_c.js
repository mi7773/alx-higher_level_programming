#!/usr/bin/node

const { argv } = require('node:process');

const val = Number(argv[2]);

if (val === Number(argv[2])) {
  for (let i = 0; i < val; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
