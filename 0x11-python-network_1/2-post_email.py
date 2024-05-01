#!/usr/bin/python3
"""
Module senda a POST request passing an email
"""


if __name__ == "__main__":
    from urllib import request, parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    encoded_email = parse.urlencode({'email': email}).encode('utf-8')
    req = request.Request(url=url, data=encoded_email, method='POST')
    with request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
