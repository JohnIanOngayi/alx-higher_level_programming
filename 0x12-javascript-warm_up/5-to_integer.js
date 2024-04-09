#!/usr/bin/node

if (process.argv.length < 3) console.log('Not a number');
else if (isNaN(Number(process.argv[2]))) console.log('Not a number');
else console.log(`My number: ${Number(process.argv[2])}`);
