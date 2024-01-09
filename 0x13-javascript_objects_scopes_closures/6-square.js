#!/usr/bin/node

const oldSquare = require('./5-square');

module.exports = class Square extends oldSquare {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.height; j++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    }
  }
};
