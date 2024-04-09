#!/usr/bin/node

const sortedArray = process.argv.slice(2).sort();

if (isNaN(sortedArray[sortedArray.length - 2])) console.log(0);
else console.log(sortedArray[sortedArray.length - 2]);
