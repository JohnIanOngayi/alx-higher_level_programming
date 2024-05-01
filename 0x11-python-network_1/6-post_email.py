#!/usr/bin/python3
"""
Module sends POST request passing k:v email parameter
"""


if __name__ == "__main__":
    import requests
    import sys

    url = f"{sys.argv[1]}"
    data = {'email': f"{sys.argv[2]}"}
    resp = requests.post(url=url, data=data)
    print(resp.text)
