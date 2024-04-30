#!/bin/bash
# Script prints allowed HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f2- | tr -d '\r'
