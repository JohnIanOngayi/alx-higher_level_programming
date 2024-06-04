#!/usr/bin/node

/*
 * Script gets the contents of a webpage and stores it in a file
 */

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    try {
      fs.writeFileSync(file, body, 'utf-8');
    } catch (err) {
      console.log(err);
    }
  }
});
