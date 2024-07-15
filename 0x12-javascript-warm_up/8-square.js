#!/usr/bin/node

const { argv } = require('node:process');

if (!(isNaN(Number(argv[2])))) {
  for (let i = 0; i < Number(argv[2]); i++) {
    let val = '';
    for (let j = 0; j < Number(argv[2]); j++) {
      val += 'x';
    }
    console.log(val);
  }
} else {
  console.log('Missing size');
}
