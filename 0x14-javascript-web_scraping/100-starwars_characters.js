#!/usr/bin/node

/*
 * Script that takes film id as arg and prints all characters
 */
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const json = JSON.parse(body);
    for (const uri of json.characters) {
      request(uri, (err, resp, bod) => {
        if (err) console.log(err);
        else {
          const chardict = JSON.parse(bod);
          console.log(chardict.name);
        }
      });
    }
  }
});
