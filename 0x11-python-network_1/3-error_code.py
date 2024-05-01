#!/usr/bin/python3
"""
Module sends request and prints decoded response
"""


if __name__ == "__main__":
    from urllib import request, error
    import sys

    url = f"{sys.argv[1]}"
    try:
        with request.urlopen(url=url) as resp:
            print(resp.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
