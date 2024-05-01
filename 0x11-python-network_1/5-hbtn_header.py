#!/usr/bin/python3
"""
Module sends GET request and prints the request Id
"""


if __name__ == "__main__":
    import requests
    import sys

    url = f"{sys.argv[1]}"
    resp = requests.get(url=url)
    print(resp.headers.get('X-Request-Id'))
