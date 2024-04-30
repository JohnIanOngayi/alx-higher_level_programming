#!/bin/bash
# Takes a URL, sends a GET reequest and displays the body
if curl -sI "$1" | head -n 1 | grep -q "200" ; then curl -s "$1" ; fi
