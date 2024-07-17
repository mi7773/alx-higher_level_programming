#!/usr/bin/node

const Square5 = require('./5-square');

module.exports = class Sqaure extends Square5 {
  charPrint (c) {
    this.print(c);
  }
};
