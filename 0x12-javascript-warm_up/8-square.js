#!/usr/bin/node

const size = Number(process.argv[2]);

if (isNaN(size)) console.log('Missing size');
else {
  for (let i = 0; i < size; i++) {
    let side = '';
    for (let j = 0; j < size; j++) {
      side += 'X';
    }
    console.log(side);
  }
}
