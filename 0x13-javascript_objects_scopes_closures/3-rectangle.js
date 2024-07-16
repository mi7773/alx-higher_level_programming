#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let shape = '';
    while (i < this.width) {
      shape += 'X';
      i++;
    }
    i = 0;
    while (i < this.height) {
      console.log(shape);
      i++;
    }
  }
};
