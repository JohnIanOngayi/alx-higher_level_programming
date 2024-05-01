#!/usr/bin/python3
"""
Module sends a GET request to said url
"""

if __name__ == "__main__":
    from urllib import request

    url = f"https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as resp:
        body = resp.read()
        print(f"Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
