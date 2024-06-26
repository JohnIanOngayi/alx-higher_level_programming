#!/usr/bin/node

/*
 * Script that prints the title of a Star Wars movie where the episode number
 *    matches a given integer
 */

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
