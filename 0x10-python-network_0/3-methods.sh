#!/bin/bash
# Script prints allowed HTTP methods
curl -sIX OPTIONS "$1" | grep -w Allow | awk '{print $2}'
