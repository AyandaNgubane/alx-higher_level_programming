#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (size) {
  let i = 0;
  let j = 0;
  while (j < size) {
    while (i < size) {
      process.stdout.write('X');
      i++;
    }
    j++;
    i = 0;
    console.log('');
  }
} else {
  console.log('Missing size');
}
