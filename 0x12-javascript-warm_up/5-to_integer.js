#!/usr/bin/node

const { argv } = require('node:process');

const val = argv[2];

if (Number(val) === Number(argv[2])) {
  console.log('My number:', Number(val));
} else {
  console.log('Not a number');
}
