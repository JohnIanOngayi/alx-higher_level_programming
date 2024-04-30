#!/bin/bash
# Script tahes URl, sends a request and displays size of the response
curl -s "$1" | wc -c
