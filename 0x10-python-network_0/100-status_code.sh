#!/bin/bash
# Script prints HTTPstatus code returned
curl -s -o /dev/null -w "%{http_code}" "$1"
