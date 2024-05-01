#!/usr/bin/python3
"""
Module sends a GET request and fetchs the request ID
"""

if __name__ == "__main__":
    from urllib import request
    import sys

    url = f"{sys.argv[1]}"
    with request.urlopen(url) as resp:
        print(resp.info().get('X-Request-Id'))
