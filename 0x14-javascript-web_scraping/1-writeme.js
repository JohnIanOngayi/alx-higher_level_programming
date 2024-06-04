#!/usr/bin/node

/*
 * Script that writes to a file
 */

const fs = require('fs');
const file = process.argv[2];
const text = process.argv[3];

try {
  fs.writeFileSync(file, text, 'utf-8');
} catch (err) {
  console.log(err);
}
