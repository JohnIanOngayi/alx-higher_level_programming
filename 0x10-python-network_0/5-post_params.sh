#!/bin/bash
# Script sends POST request
curl -X POST -H "Content-Type: application/json" -d '{"email": "test@gmail.com", "subject": "I will always be here for PLD"}' "$1"
