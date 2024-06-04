#!/usr/bin/node

/*
 * Script that prints number of movies featuring Wedge Antilles
 */

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const count = body.split('/people/18/').length - 1;
    console.log(count);
  }
});
